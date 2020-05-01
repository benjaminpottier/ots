# ots
onetimesecret API client and cli with [Fire](https://github.com/google/python-fire)

Email a random secret.

```bash
otscli.py generate_secret "foo@example.com"
```

Email a secret to someone.

```bash
otscli.py create_secret "foo@example.com" "I enjoyed the movie cats!"
```

The secret_key can be used to retrieve a secret from the cli.

```bash
otscli.py retrieve_secret nhoe1zdl1bvyhp8oj5utsx8mc8t451t
```
