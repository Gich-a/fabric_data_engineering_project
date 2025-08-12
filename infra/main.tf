resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_key_vault" "kv" {
  name                        = var.key_vault_name
  location                    = azurerm_resource_group.rg.location
  resource_group_name         = azurerm_resource_group.rg.name
  tenant_id                   = var.tenant_id
  sku_name                    = "standard"
}

# Eventhouse
resource "azapi_resource" "fabric_eventhouse" {
  type      = "Microsoft.Fabric/eventhouses@2023-01-01"
  name      = var.eventhouse_name
  parent_id = azurerm_resource_group.rg.id
  location  = azurerm_resource_group.rg.location
  body = jsonencode({
    properties = {
      description = "Production Eventhouse"
    }
  })
}

# Eventstream
resource "azapi_resource" "fabric_eventstream" {
  type      = "Microsoft.Fabric/eventstreams@2023-01-01"
  name      = var.eventstream_name
  parent_id = azurerm_resource_group.rg.id
  location  = azurerm_resource_group.rg.location
  body = jsonencode({
    properties = {
      description = "Streaming ingestion"
    }
  })
}

# Lakehouse
resource "azapi_resource" "fabric_lakehouse" {
  type      = "Microsoft.Fabric/lakehouses@2023-01-01"
  name      = var.lakehouse_name
  parent_id = azurerm_resource_group.rg.id
  location  = azurerm_resource_group.rg.location
  body = jsonencode({
    properties = {
      storage = "OneLake"
    }
  })
}

# Warehouse
resource "azapi_resource" "fabric_warehouse" {
  type      = "Microsoft.Fabric/warehouses@2023-01-01"
  name      = var.warehouse_name
  parent_id = azurerm_resource_group.rg.id
  location  = azurerm_resource_group.rg.location
  body = jsonencode({
    properties = {
      description = "Fabric Warehouse for analytics"
    }
  })
}
