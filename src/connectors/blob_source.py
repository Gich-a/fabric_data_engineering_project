import os
from azure.storage.blob import BlobServiceClient

class BlobSourceConnector:
    def __init__(self, connection_string, container_name, file_path):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_name = container_name
        self.file_path = file_path

    def fetch_data(self):
        blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=self.file_path)
        data = blob_client.download_blob().readall()
        return data
