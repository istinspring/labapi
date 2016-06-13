import os
from eve import Eve

print os.getcwd()

api = Eve(settings='settings.py')

if __name__ == '__main__':
    api.run()
