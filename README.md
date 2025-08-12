## Data Engineering on Microsoft Fabric

This project demonstrates a complete, end-to-end data engineering solution built on Microsoft Fabric. It uses Terraform for infrastructure as code, Python for data ingestion and processing logic, Great Expectations for data quality, and Azure DevOps for CI/CD automation.

The solution is designed to handle both batch and streaming data, process it through a validation pipeline, store it in a Fabric Lakehouse and Warehouse, and automatically trigger Power BI refreshes.

Architecture
The project follows a modern data platform architecture, automated from start to finish:

CI/CD Pipeline (Azure DevOps): The central orchestrator that triggers and manages all stages of deployment and execution.

Infrastructure Provisioning (Terraform): Automatically deploys and configures all necessary resources in Azure and Microsoft Fabric, including the Lakehouse, Warehouse, Eventhouse, and Key Vault.

Secure Credentials (Azure Key Vault): All secrets (API keys, connection strings, etc.) are securely stored and managed in Azure Key Vault. The Python application uses a caching client to minimize API calls and improve performance.

Data Ingestion (Python): A flexible factory pattern handles ingesting data from multiple sources:

Batch: Azure Blob Storage, SQL Server.

Streaming: Azure Event Hubs, IoT Hub.

Data Validation (Great Expectations): Before data is loaded, it's passed through a validation gate using Great Expectations to ensure schema and data quality. This prevents bad data from corrupting the analytics environment.

Data Loading (Python): Validated data is loaded into the Fabric Lakehouse for storage and the Fabric Warehouse for analytics.

BI Refresh (Power BI REST API): Once the data is loaded, the pipeline automatically triggers a refresh of a specified Power BI dataset, ensuring dashboards are always up-to-date.

Directory structure
```
fabric_data_engineering_project/
│
├── src/
│   ├── main.py
│   ├── config/settings.py
│   ├── factories/ingestion_factory.py
│   ├── connectors/blob_source.py
│   ├── connectors/sql_server_source.py
│   ├── connectors/eventhub_source.py
│   ├── connectors/iothub_source.py
│   ├── processors/batch_processor.py
│   ├── processors/streaming_processor.py
│   ├── security/key_vault_client.py
│   ├── validation/schema_validator.py
│   ├── utils/logger.py
│
├── infra/
│   ├── provider.tf
│   ├── variables.tf
│   ├── main.tf
│   ├── outputs.tf
│
├── tests/
│   ├── test_connectors.py
│   ├── test_factory.py
│   ├── test_validation.py
│
├── azure-pipelines.yml
├── requirements.txt
└── README.md
```