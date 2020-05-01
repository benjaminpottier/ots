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
        attrs = json.loads(r.text)
        return attrs

    def create_secret(self, secret, email=None, ttl='3600', passphrase=None):
        """
        secret: the secret value which is encrypted before being stored.
        passphrase: a string that the recipient must know to view the secret.
        ttl: the maximum amount of time, in seconds, that the secret should survive.
        recipient: an email address.
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
        passphrase: a string that the recipient must know to view the secret.
        ttl: the maximum amount of time, in seconds, that the secret should survive.
        recipient: an email address.
        """
        params = {
            "recipient": email,
            "ttl": ttl,
            "passphrase": passphrase,
        }
        return self._post('generate', params)

    def retrieve_secret(self, secret_key, passphrase=None):
        """
        secret_key: the unique key for this secret.
        passphrase (if required): the passphrase is required only if the secret was create with one.
        """
        params = {
            "passphrase": passphrase
        }
        return self._post(f"secret/{secret_key}", params)

    def retieve_metdata(self, metadata_key):
        """
        metadata_key: the unique key for this metadata.
        """
        return self._post(f"private/{metadata_key}")

    def burn_secret(self, metadata_key):
        """
        metadata_key: the unique key for this metadata.
        """
        return self._post(f"private/{metadata_key}/burn")

    def retrieve_recent_metadata(self):
        """
        retreive a list of recent metadata.
        """
        return self._post(f"private/recent")
