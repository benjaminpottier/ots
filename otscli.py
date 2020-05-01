import fire
from ots import Ots

user = ''
api_key = ''

if __name__ == '__main__':
  fire.Fire(Ots(user, api_key))
