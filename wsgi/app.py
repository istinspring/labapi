import os
from eve import Eve
from wsgi import settings
from honcho.environ import parse

d = parse('../.env')
for k, v in d.items():
    os.environ[k] = v

api = Eve()

if __name__ == '__main__':
    api.run(settings=settings)
