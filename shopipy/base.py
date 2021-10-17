from typing import Any, Dict
import requests # type: ignore
from shopipy.exceptions import *

class BaseClient:

    def __init__(
        self,
        shop_domain: str = None,
        version: str = "2021-04",
        api_key: str = None,
        api_secret: str = None,
        app_key: str = None,
        app_password: str = None,
        app_shared_secret: str = None,
        access_token: str = None,
        timeout: int = 5
    ):
        """
        Base class to interact with Shopify API.

        Args:
            shop_domain (str): The shopDomain (without 'myshopify')
            version (str): API Version, defaults to "2021-04"
            access_token (str, optional): access_token, used for public apps.
            api_key (str, optional): API Key, for private apps.
            api_password (str, optional): API Password for private apps.
        """
        super(BaseClient, self).__init__()
        self.shop_domain = shop_domain
        self.version = version
        self.api_key = api_key
        self.api_secret = api_secret
        self.app_key = app_key
        self.app_password = app_password
        self.app_shared_secret = app_shared_secret
        self.access_token = access_token
        self.timeout = timeout
        
        # Calculated fields
        self.base_url = f"https://{shop_domain}.myshopify.com/admin/api/{version}"
        self.header = dict() # type: ignore
        self.private = False
        self.setup()

    def setup(self):
        """
        Main setup function, used to set the API version.
        If the application is private, uses the app_password as the access_token.
        """
        if self.app_password:
            self.private = True
            self.access_token = self.app_password

        # Has to have one or the other (public or private app)        
        if not (self.app_key or self.api_key):
            raise CredentialsError("Can't use API Key when defining the token.")
            
        # App is private but no password was set
        if self.app_key and not self.app_password:
            raise CredentialsError("No password set for private app.")

        # Sets the header for authorized requests
        self.header = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": self.access_token
        }


    def _clean_params(self, data: dict):
        """Receives a dictionary of data, and excludes unset.

        Args:
            data (dict): The data dictionary

        Returns:
            data (dict): The cleaned up dictionary
        """
        return dict(filter(lambda item: item[1] is not None, data.items()))

    def _get(self, path: str, **params):
        """
        GET Request to the provided endpoint

        Args:
            path (str): The Shopify endpoint.

        Returns:
            Response: Request's JSON Response object.
        """
        full_path = self.base_url + path
        r = requests.get(url=full_path, headers=self.header, timeout=self.timeout, params=dict(**params))
        response = r.json()
        return response

    def _post(self, path: str, payload: Dict[Any, Any]):
        """
        POST Request to the provided endpoint

        Args:
            path (str): The Shopify endpoint.
            payload (dict): A Payload to send Shopify.

        Returns:
            Response: Request's JSON Response object.
        """    
        full_path = self.base_url + path
        response = requests.post(url=full_path, headers=self.header, json=payload, timeout=self.timeout)
        return response

    def _put(self, path: str, payload: Dict[Any, Any]):
        """
        PUT Request to the provided endpoint

        Args:
            path (str): The Shopify endpoint.
            payload (dict): A Payload to send Shopify.

        Returns:
            Response: Request's JSON Response object.
        """    
        full_path = self.base_url + path
        response = requests.put(url=full_path, headers=self.header, json=payload, timeout=self.timeout)
        return response

    def _delete(self, path: str, **params):
        """
        DELETE Request to the provided endpoint

        Args:
            path (str): The Shopify endpoint.
            payload (dict): A Payload to send Shopify.

        Returns:
            Response: Request's JSON Response object.
        """    
        full_path = self.base_url + path
        response = requests.delete(url=full_path, headers=self.header, timeout=self.timeout, params=dict(**params))
        return response
