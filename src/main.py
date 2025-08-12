from factories.ingestion_factory import IngestionFactory
from processors.batch_processor import BatchProcessor
from processors.streaming_processor import StreamingProcessor
from utils.fabric_clients import FabricLakehouseClient, FabricEventhouseClient
from security.key_vault_client import KeyVaultClient
from validation.schema_validator import SchemaValidator
import os
from utils.powerbi_client import PowerBIClient

# Load secrets
kv_client = KeyVaultClient(vault_url=os.getenv("KEY_VAULT_URL"))
fabric_token = kv_client.get_secret("fabric-api-token")
workspace_id = kv_client.get_secret("fabric-workspace-id")
tenant_id = kv_client.get_secret("pbi-tenant-id")
client_id = kv_client.get_secret("pbi-client-id")
client_secret = kv_client.get_secret("pbi-client-secret")
group_id = kv_client.get_secret("pbi-workspace-id")
dataset_id = kv_client.get_secret("pbi-dataset-id")

# Clients
pbi_client = PowerBIClient(tenant_id, client_id, client_secret)
pbi_client.refresh_dataset(group_id, dataset_id)
lakehouse_client = FabricLakehouseClient(workspace_id, kv_client.get_secret("fabric-lakehouse-id"), fabric_token)
eventhouse_client = FabricEventhouseClient(workspace_id, kv_client.get_secret("fabric-eventhouse-id"), fabric_token)

# Validators
batch_validator = SchemaValidator("great_expectations/expectations/batch_expectations.json")
streaming_validator = SchemaValidator("great_expectations/expectations/streaming_expectations.json")

# Batch example
blob_connector = IngestionFactory.get_connector(
    source_type="blob",
    connection_string=kv_client.get_secret("blob-connection-string"),
    container_name="input-data",
    file_path="data.csv"
)
batch_data = blob_connector.fetch_data()
batch_processor = BatchProcessor(lakehouse_client, batch_validator)
batch_processor.process_and_store(batch_data, "raw/data.csv")

# Streaming example
def handle_event(partition_context, event):
    streaming_processor = StreamingProcessor(eventhouse_client, streaming_validator)
    streaming_processor.process_event(event.body_as_json())
    partition_context.update_checkpoint(event)

eventhub_connector = IngestionFactory.get_connector(
    source_type="eventhub",
    connection_str=kv_client.get_secret("eventhub-connection-string"),
    eventhub_name="mystream"
)
eventhub_connector.receive_events(handle_event)
