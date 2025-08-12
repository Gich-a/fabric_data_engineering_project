import requests
import os

class FabricLakehouseClient:
    def __init__(self, workspace_id, lakehouse_id, token):
        self.workspace_id = workspace_id
        self.lakehouse_id = lakehouse_id
        self.token = token

    def upload_file(self, path, data_bytes):
        url = f"https://api.fabric.microsoft.com/workspaces/{self.workspace_id}/lakehouses/{self.lakehouse_id}/files/{path}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.put(url, headers=headers, data=data_bytes)
        response.raise_for_status()

class FabricEventhouseClient:
    def __init__(self, workspace_id, eventhouse_id, token):
        self.workspace_id = workspace_id
        self.eventhouse_id = eventhouse_id
        self.token = token

    def append_event(self, event_data):
        url = f"https://api.fabric.microsoft.com/workspaces/{self.workspace_id}/eventhouses/{self.eventhouse_id}/events"
        headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
        response = requests.post(url, headers=headers, json=event_data)
        response.raise_for_status()
