INFO keystone.common.wsgi [req-b28d7cf9-8591-4629-99a1-bdcd85b046b4 - - - - -] POST http://controller:5000/v3/auth/tokens`
WARNING keystone.common.wsgi [req-b28d7cf9-8591-4629-99a1-bdcd85b046b4 - - - - -] Authorization failed. The request you have made requires authentication. from 172.16.1.5`
INFO keystone.common.wsgi [req-ef70efb4-0b60-4738-b8ba-204c657aebcc - - - - -] GET http://controller:5000/v3/`
INFO keystone.common.wsgi [req-2a491a01-a525-46e6-ba26-b2d53ab02567 - - - - -] POST http://controller:5000/v3/auth/tokens`
INFO keystone.token.providers.fernet.utils [req-2a491a01-a525-46e6-ba26-b2d53ab02567 - - - - -] Loaded 2 encryption keys (max_active_keys=3) from: /etc/keystone/fernet-keys/`
INFO keystone.common.wsgi [req-e34f17f4-4957-4117-a174-73fb8de19d29 - - - - -] POST http://controller:5000/v3/auth/tokens`
WARNING keystone.common.wsgi [req-e34f17f4-4957-4117-a174-73fb8de19d29 - - - - -] Authorization failed. The request you have made requires authentication. from 172.16.1.5`
INFO keystone.common.wsgi [req-98982a97-90ca-411f-843d-c4dd5186fe5a - - - - -] POST http://controller:5000/v3/auth/tokens`
ERROR keystone.auth.plugins.core [req-98982a97-90ca-411f-843d-c4dd5186fe5a - - - - -] Could not find user: root`
ERROR keystone.auth.plugins.core Traceback (most recent call last):`
ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/keystone/auth/plugins/core.py", line 173, in _validate_and_normalize_auth_data`
ERROR keystone.auth.plugins.core     user_name, domain_ref["id"])`
ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/keystone/common/manager.py", line 124, in wrapped`
ERROR keystone.auth.plugins.core     __ret_val = __f(*args, **kwargs)
ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/keystone/identity/core.py", line 433, in wrapper
ERROR keystone.auth.plugins.core     return f(self, *args, **kwargs)`
ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/keystone/identity/core.py", line 443, in wrapper
ERROR keystone.auth.plugins.core     return f(self, *args, **kwargs)`
ERROR keystone.auth.plugins.core   File "/usr/lib/python2.7/dist-packages/dogpile/cache/region.py", line 1053, in decorate`
INFO keystone.common.wsgi [req-409620fb-dd6b-493a-9b9f-259943f1564b 63dee1ed626b4040bcd43b3492997a8c - - 19b6c35443a340c5a8648c97c46fdff7 -] GET http://controller:5000/v3/users/63dee1ed626b4040bcd43b3492997a8c/projects`

