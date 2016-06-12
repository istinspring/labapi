from eve import Eve
from wsgi import settings


api = Eve(settings=settings)

if __name__ == '__main__':
    api.run()
