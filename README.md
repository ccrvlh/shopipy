# Usage

NOT PRODUCTION READY

### For public apps:

```python
from shopipy import ShopiPy

api_key = "MY_API_KEY"
api_secret = "MY_API_SECRET"

shopify = ShopiPy(api_key=api_key, api_secret=api_secret)

# OAuth Flow
shop_domain = "MY_SHOP_DOMAIN"
state = "my_super_secret_key"
redirect_uri = "https://myapp.com/callback"
scopes = ['read_products', 'read_orders']

auth_url = shopify.OAuth.create_permission_url(
    shop_domain=shop_domain,
    scopes=scopes,
    redirect_uri=redirect_uri,
    state=state
)

# Request Token from the Shopify request to the callback URL
request_params = {}
shopify = ShopiPy(shop_domain=shop_domain, api_key=api_key, api_secret=api_secret)
access_token = shopify.OAuth.request_token(request_params)

# Make an authenticated request
# access_token = ShopifyAppDB.query.first_by(shop_domain=shop_domain).first()
shopify = ShopiPy(shop_domain=shop_domain, access_token=access_token)
product_list = shopify.Products.list_products()
orders_count = shopify.Orders.count(status="open")
```

### For private apps:

```python

from shopipy import ShopiPy

# Set Credentials
private_key = "MY_APP_KEY"
private_password = "MY_APP_PASSWORD"
shop_domain = "MY_SHOP_DOMAIN"

# Instanciates client
shopify = ShopiPy(shop_domain=shop_domain, app_key=private_key, app_password=private_password)

# Retrieve information
product = shopify.Products.get("432432432432")
orders = shopify.Orders.count()
```
