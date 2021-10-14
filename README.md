# Usage

NOT PRODUCTION READY

### For public apps:

```python

from shopipy import ShopiPy

my_token = "MY_APP_TOKEN"
my_shop = "MY_SHOP_NAME"

client = ShopiPy(shop_domain=my_shop, token=my_token)

# Clients
orders = client.Orders.get_all(created_at_min="2021-05-01")
customers = client.Customers.get_all(created_at_min="2021-05-01")
products = client.Producyts.get_all(created_at_min="2021-05-01")
```

### For private apps:

```python

from shopipy import ShopiPy

my_shop = "MY_SHOP_NAME"
my_api_key = "MY_API_KEY"
my_api_password = "MY_API_PASSWORD"

client = ShopiPy(shop_domain=my_shop, api_key=my_api_key, api_password=my_api_password)

# Clients
orders = client.Orders.get_all(created_at_min="2021-05-01")
customers = client.Customers.get_all(created_at_min="2021-05-01")
products = client.Producyts.get_all(created_at_min="2021-05-01")
```
