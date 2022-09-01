from woocommerce import API

wcapi = API(
    url="http://localhost/noamazon",
    consumer_key="ck_xxx",
    consumer_secret="cs_xxx",
    version="wc/v3"
)

r = wcapi.get("orders")

import pprint
pprint.pprint(r.json())