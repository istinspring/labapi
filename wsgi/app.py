from eve import Eve


api = Eve(settings='wsgi/settings.py')

if __name__ == '__main__':
    api.run()
