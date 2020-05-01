import json
import requests
from requests.auth import HTTPBasicAuth


class Ots(object):

    def __init__(
            self,
            user,
            api_key,
            base_uri='https://onetimesecret.com/api/v1'):
        self.user = user
        self.api_key = api_key
        self.base_uri = base_uri
        
    def _post(self, path, params={}):
        try:
            r = requests.post(
                f"{self.base_uri}/{path}",
                params=params,
                auth=HTTPBasicAuth(
                    username=self.user,
                    password=self.api_key
                )
            )
        except:
            raise
        return json.loads(r.text)

    def create_secret(self, secret, email=None, ttl='3600', passphrase=None):
        """
        Args:
            secret (str): the secret value
            passphrase (str, optional): a passphrase the recipient must know to view the secret
        """
        params = {
            "secret": secret,
            "recipient": email,
            "ttl": ttl,
            "passphrase": passphrase,
        }
        return self._post('share', params)

    def generate_secret(self, email=None, ttl='3600', passphrase=None):
        """
        Args:
            ttl (str, optional): time, in seconds, the secret will live for
            passphrase (str, optional): a passphrase the recipient must know to view the secret
            recipient (str, optional): email address to recieve secret
        """
        params = {
            "recipient": email,
            "ttl": ttl,
            "passphrase": passphrase,
        }
        return self._post('generate', params)

    def retrieve_secret(self, secret_key, passphrase=None):
        """
        Args:
            secret_key (str): unique key to retrieve secret
            passphrase (str, optional): a passphrase the recipient must know to view the secret
        """
        params = {
            "passphrase": passphrase
        }
        return self._post(f"secret/{secret_key}", params)

    def retieve_metdata(self, metadata_key):
        """
        Args:
            metadata_key (str): the unique key to retrieve metadata
        """
        return self._post(f"private/{metadata_key}")

    def burn_secret(self, metadata_key):
        """
        Args:
            metadata_key (str): the unique key to burn secret
        """
        return self._post(f"private/{metadata_key}/burn")

    def retrieve_recent_metadata(self):
        """
        """
        return self._post(f"private/recent")
