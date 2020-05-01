# ots
[onetimesecret](https://onetimesecret.com/) API client and cli with [Fire](https://github.com/google/python-fire)

Create an account at onetimesecret.com, then generate an API key.

Store your user and key in `~/.ots` as `user:api_key` and set read-only permissions on the file.

Email a random secret.

```bash
otscli.py generate_secret --email="foo@example.com"
```

Email a secret to someone.

```bash
otscli.py create_secret "I enjoyed the movie cats!" --email="foo@example.com"
```

The secret_key can be used to retrieve a secret from the cli.

```bash
otscli.py retrieve_secret nhoe1zdl1bvyhp8oj5utsx8mc8t451t
```
