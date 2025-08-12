import requests
from azure.identity import ClientSecretCredential

class PowerBIClient:
    def __init__(self, tenant_id, client_id, client_secret):
        self.credential = ClientSecretCredential(tenant_id, client_id, client_secret)
        self.token = self.credential.get_token("https://analysis.windows.net/powerbi/api/.default").token

    def refresh_dataset(self, group_id, dataset_id):
        url = f"https://api.powerbi.com/v1.0/myorg/groups/{group_id}/datasets/{dataset_id}/refreshes"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(url, headers=headers)
        if response.status_code == 202:
            print(f"✅ Power BI dataset {dataset_id} refresh triggered successfully.")
        else:
            raise Exception(f"❌ Failed to refresh Power BI dataset: {response.text}")
