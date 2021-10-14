from shopipy.exceptions import *


class ShopiPy:
    """
    SDK Class to interact with the Shopify API.
    Usage:
        shop_api = ShopifyAPI("shop_domain")
        shop_api.setup()
        orders = shop_api.get_request("/orders")
    """

    def __init__(
        self,
        shop_domain: str,
        version: str = "2021-04",
        api_key: str = None,
        api_password: str = None,
        token: str = None
    ):
        """
        Initial SDK Setup

        Args:
            shop_domain (str): [description]
            version (str, optional): [description]. Defaults to "2021-04".
            api_key (str, optional): [description]. Defaults to None.
            api_password (str, optional): [description]. Defaults to None.
            token (str, optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        self.config = dict(
            shop_domain=shop_domain,
            token=token,
            api_key=api_key,
            api_password=api_password,
            version=version
        )

    @property
    def OAuth(self, app_key: str, app_secret: str):
        from shopipy.resources.oauth import OAuth # type: ignore
        return OAuth(app_key=app_key, app_secret=app_secret, **self.config)

    @property
    def Orders(self):
        from shopipy.resources.orders import Orders # type: ignore
        return Orders(**self.config)

    @property
    def Products(self):
        from shopipy.resources.products import Products # type: ignore
        return Products(**self.config)

    @property
    def Customers(self):
        from shopipy.resources.customers import Customers # type: ignore
        return Customers(**self.config)

    @property
    def Collections(self):
        from shopipy.resources.collections import Collections # type: ignore
        return Collections(**self.config)

    @property
    def Inventory(self):
        from shopipy.resources.inventory import Inventory # type: ignore
        return Inventory(**self.config)

    @property
    def Fulfillment(self):
        from shopipy.resources.fulfillment import Fulfillment # type: ignore
        return Fulfillment(**self.config)

    @property
    def Shipping(self):
        from shopipy.resources.shipping import Shipping # type: ignore
        return Shipping(**self.config)
