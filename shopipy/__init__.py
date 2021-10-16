from shopipy.exceptions import *


class ShopiPy:
    """ SDK Class to interact with the Shopify API. """

    def __init__(
        self,
        shop_domain: str,
        version: str = "2021-04",
        api_key: str = None,
        api_secret: str = None,
        app_key: str = None,
        app_password: str = None,
        app_shared_secret: str = None,
        token: str = None
    ):
        """
        Initial SDK Setup

        Args:
            shop_domain (str): [description]
            version (str, optional): [description]. Defaults to "2021-04".
            api_key (str, optional): The App API Key. Defaults to None.
            api_secret (str, optional): The App API Secret. Defaults to None.
            app_key (str, optional): The Private App App Key. Defaults to None.
            app_password (str, optional): The Private App Password. Defaults to None.
            token (str, optional): [description]. Defaults to None.
        """
        self.config = dict(
            shop_domain=shop_domain,
            token=token,
            api_key=api_key,
            api_secret=api_secret,
            app_key=app_key,
            app_password=app_password,
            app_shared_secret=app_shared_secret,
            version=version
        )

    @property
    def OAuth(self):
        from shopipy.resources.oauth import OAuth
        return OAuth

    @property
    def Orders(self):
        from shopipy.resources.orders import Orders
        return Orders(**self.config)

    @property
    def Products(self):
        from shopipy.resources.products import Products
        return Products(**self.config)

    @property
    def Customers(self):
        from shopipy.resources.customers import Customers
        return Customers(**self.config)

    @property
    def Collections(self):
        from shopipy.resources.collections import Collections
        return Collections(**self.config)

    @property
    def Inventory(self):
        from shopipy.resources.inventory import Inventory
        return Inventory(**self.config)

    @property
    def Fulfillment(self):
        from shopipy.resources.fulfillment import Fulfillment
        return Fulfillment(**self.config)

    @property
    def Shipping(self):
        from shopipy.resources.shipping import Shipping
        return Shipping(**self.config)
