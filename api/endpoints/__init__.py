from .HelloWorld import HelloWorld
from .protected import init_protected
from .login import init_login

uninitialzed_endpoints = [
    (HelloWorld, '/')
]

uninitialized_jwt_endpoints = [
    (init_login, '/login'),
    (init_protected, '/protected')
]