from .HelloWorld import HelloWorld
from .protected import init_protected
from .login import init_login
from .signup import init_signup
from .create_owner import init_create_owner
from .create_manager import init_create_manager
from .create_tenant import init_create_tenant
from .get_roles import init_get_roles

uninitialzed_endpoints = [
    (HelloWorld, '/')
]

uninitialized_jwt_endpoints = [
    (init_login, '/login'),
    (init_protected, '/protected'),
    (init_signup, '/signup'),
    (init_create_owner, '/create_owner'),
    (init_create_manager, '/create_manager'),
    (init_create_tenant, '/create_tenant'),
    (init_get_roles, '/get_roles')
]