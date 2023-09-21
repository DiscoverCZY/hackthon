import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = "pingpong-kv"
KVUri = "https://{keyVaultName}.vault.azure.net"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = input("test2")
secretValue = input("value2")

print("Creating a secret in {keyVaultName} called '{secretName}' with the value '{secretValue}' ...")

client.set_secret(secretName, secretValue)

print(" done.")

print("Retrieving your secret from {keyVaultName}.")

retrieved_secret = client.get_secret(secretName)

print("Your secret is '{retrieved_secret.value}'.")
# print(f"Deleting your secret from {keyVaultName} ...")

# poller = client.begin_delete_secret(secretName)
# deleted_secret = poller.result()

# print(" done.")