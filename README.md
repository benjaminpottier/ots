# ots
[onetimesecret](https://onetimesecret.com/) API client and cli with [Fire](https://github.com/google/python-fire)

## Install

```bash
git clone https://github.com/benjaminpottier/ots.git
cd ots
sudo python3 setup.py install
```

## Setup

Create an account at onetimesecret.com and generate an API key.

Store your user and key in `~/.ots` as `user:api_key` and set read-only permissions on the file.

## Examples

Email a random secret.

```bash
otscli.py generate_secret --email="foo@example.com"
```

Email a secret to someone.

```bash
otscli.py create_secret "I enjoyed the movie Cats!" --email="foo@example.com"
```

The above is just an example of something you may want to keep secret. I didn't see Cats.
