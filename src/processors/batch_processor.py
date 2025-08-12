import pandas as pd
from validation.schema_validator import SchemaValidator

class BatchProcessor:
    def __init__(self, lakehouse_client, validator: SchemaValidator):
        self.lakehouse_client = lakehouse_client
        self.validator = validator

    def process_and_store(self, data, target_path):
        # Convert bytes/records to DataFrame
        if isinstance(data, bytes):
            df = pd.read_csv(pd.io.common.BytesIO(data))
        elif isinstance(data, list):
            df = pd.DataFrame(data)
        else:
            raise ValueError("Unsupported batch data format")

        # Validate data
        self.validator.validate(df)

        # Upload
        data_bytes = df.to_csv(index=False).encode("utf-8")
        self.lakehouse_client.upload_file(target_path, data_bytes)
        print(f"✅ Batch data stored in Lakehouse at {target_path}")
