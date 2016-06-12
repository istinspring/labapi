from eve import Eve
from wsgi import settings

api = Eve()

if __name__ == '__main__':
    api.run(settings=settings)
