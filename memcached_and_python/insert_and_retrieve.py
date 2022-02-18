#!/usr/bin/env python3

from pymemcache.client.base import Client

client = Client('localhost')
client.set('some_key', 'some_value')
# The decode on the next line is to convert the type of the result from
# 'bytes' to 'str'
result = client.get('some_key').decode()
print(type(result))
print(result)
