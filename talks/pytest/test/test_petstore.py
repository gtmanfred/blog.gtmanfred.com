import json

import urllib3

def test_inventory():
    http = urllib3.PoolManager()
    url = 'https://petstore.swagger.io/v2/store/inventory'
    ret = http.request('GET', url)
    assert json.loads(ret.data)[' not available'] == 1
