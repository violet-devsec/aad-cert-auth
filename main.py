import os
from dotenv import load_dotenv
from azure.identity import CertificateCredential
from azure.keyvault.secrets import SecretClient

load_dotenv()

TenantId = os.environ["AZURE_TENANT_ID"]
ClientId = os.environ["AZURE_CLIENT_ID"]
KVUri = os.environ["KEY_VAULT_URI"]
CertPath = "./kv-prv.pfx"

credential = CertificateCredential(tenant_id=TenantId, client_id=ClientId, certificate_path=CertPath, password="")
kvClient = SecretClient(vault_url=KVUri, credential=credential)
secret = kvClient.get_secret(os.environ["SECRET_NAME"]).value

print(secret)
