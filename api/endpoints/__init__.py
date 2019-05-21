from .HelloWorld import HelloWorld
from .protected import init_protected
from .login import init_login
from .signup import init_signup

uninitialzed_endpoints = [
    (HelloWorld, '/')
]

uninitialized_jwt_endpoints = [
    (init_login, '/login'),
    (init_protected, '/protected'),
    (init_signup, '/signup')
]