#!/usr/bin/env python3

import etcd3

etcd = etcd3.client(host='<server-ip>', port=<stream-port>)

etcd.put('test_1', 'hey test_1')

keys = etcd.get_prefix('test_1')

for key in keys:
    print(key[0].decode("utf-8"))

