from pyshopify.exceptions import *


class PyShopify:
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
        self.auth = dict(
            shop_domain=shop_domain,
            token=token,
            api_key=api_key,
            api_password=api_password,
            version=version
        )

    @property
    def Orders(self):
        from pyshopify.resources.orders import Orders # type: ignore
        return Orders(**self.auth)

    @property
    def Products(self):
        from pyshopify.resources.products import Products # type: ignore
        return Products(**self.auth)

    @property
    def Customers(self):
        from pyshopify.resources.customers import Customers # type: ignore
        return Customers(**self.auth)

    @property
    def Collections(self):
        from pyshopify.resources.collections import Collections # type: ignore
        return Collections(**self.auth)

    @property
    def Inventory(self):
        from pyshopify.resources.inventory import Inventory # type: ignore
        return Inventory(**self.auth)

    @property
    def Fulfillment(self):
        from pyshopify.resources.fulfillment import Fulfillment # type: ignore
        return Fulfillment(**self.auth)

    @property
    def Shipping(self):
        from pyshopify.resources.shipping import Shipping # type: ignore
        return Shipping(**self.auth)
