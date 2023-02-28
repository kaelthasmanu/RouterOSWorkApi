#!/usr/bin/python
from librouteros import connect

api = connect(
    username='admin',
    password='112233',
    host='152.206.118.189',
    )
interfaces = api.path('interface')
tuple(interfaces)
for item in interfaces:
    print(item)
