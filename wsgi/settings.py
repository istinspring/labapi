import os


DEBUG = True
PROPAGATE_EXCEPTIONS = True
SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']
HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS', 'localhost')
APP_NAME = os.environ.get('OPENSHIFT_APP_NAME', 'labapi')
IP = os.environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1')
PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 5000))

MONGO_URI = os.environ['OPENSHIFT_MONGODB_URL']

DOMAIN = {
    'leads': {
        'datasource': {
            'default_sort': [('_created', 1)]
        },
        'resource_methods': ['GET', 'POST'],
        'schema': {
            'name': {
                'type': 'string',
                'minlength': 4,
                'maxlength': 32,
                'required': True,
            },
            'email': {
                'type': 'string',
                'minlength': 4,
                'maxlength': 32,
                'required': True,
            },
            'content': {
                'type': 'string',
            },
            'source_url': {
                'type': 'string',
                'required': True,
            }
        }
    }
}
