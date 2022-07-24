__author___ = "Shakir Almasaari"
__version__ = "0.1"

from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential


class AzureKeyVaultError(BaseException):
    pass


class Keys(object):
    pass


class Certificates(object):
    pass


class Secrets(object):

    def __init__(self, az_tenant_id, az_client_id, az_client_secret, az_keyvault_name):
        self.az_tenant_id = az_tenant_id
        self.az_client_id = az_client_id
        self.az_client_secret = az_client_secret
        self.az_keyvault_uri = az_keyvault_name

        # Key-vault URL
        keyvault_uri = f"https://{self.az_keyvault_uri}.vault.azure.net/"

        self._credential = ClientSecretCredential(tenant_id=self.az_tenant_id,
                                                  client_id=self.az_client_id,
                                                  client_secret=az_client_secret)

        self._sc = SecretClient(vault_url=keyvault_uri, credential=self._credential)

    def get_secret(self, secret_key):
        secret_value = self._sc.get_secret(secret_key).value
        return secret_value

    def set_secret(self, secret_key, secret_value):
        self._sc.set_secret(secret_key, secret_value)

    def delete_secret(self, secret_key):
        """Deletes all versions of a secret"""
        self._sc.begin_delete_secret(secret_key)
  
