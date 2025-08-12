from connectors.blob_source import BlobSourceConnector
from connectors.sql_server_source import SQLServerSourceConnector
from connectors.eventhub_source import EventHubSourceConnector
from connectors.iothub_source import IoTHubSourceConnector

class IngestionFactory:
    @staticmethod
    def get_connector(source_type: str, **kwargs):
        connectors = {
            "blob": BlobSourceConnector,
            "sql": SQLServerSourceConnector,
            "eventhub": EventHubSourceConnector,
            "iothub": IoTHubSourceConnector
        }
        if source_type not in connectors:
            raise ValueError(f"Unsupported source type: {source_type}")
        return connectors[source_type](**kwargs)
