output "key_vault_id" {
  value = azurerm_key_vault.kv.id
}

output "lakehouse_id" {
  value = azapi_resource.fabric_lakehouse.id
}
