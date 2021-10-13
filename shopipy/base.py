from typing import Any, Dict
import requests # type: ignore
from shopipy.exceptions import *

class BaseClient:

    def __init__(
        self,
        shop_domain: str,
        version: str = "2021-04",
        token: str = None,
        api_key: str = None,
        api_password: str = None
    ):
        """
        Base class to interact with Shopify API.

        Args:
            shop_domain (str): The shopDomain (without 'myshopify')
            version (str): API Version, defaults to "2021-04"
            token (str, optional): Token, used for public apps.
            api_key (str, optional): API Key, for private apps.
            api_password (str, optional): API Password for private apps.
        """
        super(BaseClient, self).__init__()
        self.shop_domain = shop_domain
        self.token = token
        self.api_key = api_key
        self.api_password = api_password
        self.version = version

        self.base_url = f"https://{shop_domain}.myshopify.com/admin/api/{version}"
        self.header = dict() # type: ignore
        self.private = True
        self.setup()


            # time.sleep(1)
            # r = requests.get(str(url), timeout=10)
            # retry_after = r.headers.get('Retry-After', 0)
            # retry_after = int(retry_after)
            # time.sleep(retry_after)

            # json_object = r.json()
            # customers = json_object['customers']

            # if len(customers) == 0:
            #     break



    def setup(self):
        """
        Main setup function, used to set the API version,
        token (after a database query) and header for the requests.
        """
        if self.token:
            if self.api_key:
                raise CredentialsError("Can't use API Key when defining the token.")
            
            self.private = False
            self.header = {
                "Content-Type": "application/json",
                "X-Shopify-Access-Token": self.token
            }

        elif self.api_key:
            if not self.api_password:
                raise CredentialsError("No password set for private app.")
            self.header = {"Content-Type": "application/json"}

    def _clean_params(self, data: dict):
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
        if self.private:
            r = requests.get(url=full_path, headers=self.header, timeout=5, params=dict(**params), auth=(self.api_key, self.api_password))
            response = r.json()
        else:
            r = requests.get(url=full_path, headers=self.header, timeout=5, params=dict(**params))
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
        if self.private:
            r = requests.post(url=full_path, headers=self.header, data=payload, timeout=5, auth=(self.api_key, self.api_password))
            response = r.json()
        else:
            r = requests.post(url=full_path, headers=self.header, data=payload, timeout=5)
            response = r.json()
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
        if self.private:
            r = requests.put(url=full_path, headers=self.header, data=payload, timeout=5, auth=(self.api_key, self.api_password))
            response = r.json()
        else:
            r = requests.put(url=full_path, headers=self.header, data=payload, timeout=5)
            response = r.json()
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
        if self.private:
            r = requests.delete(url=full_path, headers=self.header, timeout=5, params=dict(**params), auth=(self.api_key, self.api_password))
            response = r.json()
        else:
            r = requests.delete(url=full_path, headers=self.header, timeout=5, params=dict(**params))
            response = r.json()
        return response
