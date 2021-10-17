from shopipy.base import BaseClient
import requests
from typing import Any, Dict, List
import hmac, urllib, json, six, time
from hashlib import sha256

class OAuth(BaseClient):

    def __init__(self, shop_domain: str = None, version: str = "2021-04", api_key: str = None, api_secret: str = None, app_key: str = None, app_password: str = None, app_shared_secret: str = None, access_token: str = None, timeout: int = 5):
        super().__init__(shop_domain=shop_domain, version=version, api_key=api_key, api_secret=api_secret, app_key=app_key, app_password=app_password, app_shared_secret=app_shared_secret, access_token=access_token, timeout=timeout)

    def create_permission_url(self, shop_domain: str, scopes: List[str], redirect_uri: str, state: str = None):
        """ Creates the URL that will be used for the OAuth flow """
        query_params = dict(
            client_id=self.api_key,
            scope=",".join(scopes),
            redirect_uri=redirect_uri,
            state=state
        )
        clened_params = self._clean_params(query_params)
        return f"https://{shop_domain}.myshopify.com/admin/oauth/authorize?{urllib.parse.urlencode(clened_params)}"

    def request_token(self, request_params: Dict[Any, Any]):
        """ Parses the callback from Shopify to get the token after the OAuth Flow is complete """
        if self.access_token:
            return self.access_token
        
        if not self.validate_params(request_params):
            raise Exception("Invalid HMAC: Possibly malicious login")

        url = f"https://{self.shop_domain}.myshopify.com/admin/oauth/access_token?"
        
        query_params = dict(
            client_id=self.api_key,
            client_secret=self.api_secret,
            code=request_params["code"]
        )
        
        response = requests.get(url, params=query_params)
        if response.status_code == 200:
            json_payload = response.json()
            self.token = json_payload["access_token"]
            self.scopes = json_payload["scope"]
            return self.token
        else:
            raise Exception(response.text)

    def validate_params(self, params: Dict[Any, Any]):
        """ Avoid replay attacks by making sure the request isn't more than a day old. """
        one_day = 24 * 60 * 60
        if int(params.get("timestamp", 0)) < time.time() - one_day:
            return False

        return self.validate_hmac(params)

    def validate_hmac(self, params: Dict[Any, Any]):
        """ Validates that the request is from Shopify through HMAC validation """
        if "hmac" not in params:
            return False

        hmac_calculated = self.calculate_hmac(params).encode("utf-8")
        hmac_to_verify = params["hmac"].encode("utf-8")

        # Try to use compare_digest() to reduce vulnerability to timing attacks.
        # If it's not available, just fall back to regular string comparison.
        try:
            return hmac.compare_digest(hmac_calculated, hmac_to_verify)
        except AttributeError:
            return hmac_calculated == hmac_to_verify

    def calculate_hmac(self, params: Dict[Any, Any]):
        """
        Calculate the HMAC of the given parameters in line with Shopify's rules for OAuth authentication.
        See http://docs.shopify.com/api/authentication/oauth#verification.
        """
        encoded_params = self.__encoded_params_for_signature(params)
        return hmac.new(self.api_secret.encode(), encoded_params.encode(), sha256).hexdigest()

    def __encoded_params_for_signature(self, params: Dict[Any, Any]):
        """
        Sort and combine query parameters into a single string, excluding those that should be removed and joining with '&'
        """

        def encoded_pairs(params):
            for k, v in six.iteritems(params):
                if k == "hmac":
                    continue

                if k.endswith("[]"):
                    # foo[]=1&foo[]=2 has to be transformed as foo=["1", "2"] note the whitespace after comma
                    k = k.rstrip("[]")
                    v = json.dumps(list(map(str, v)))

                # escape delimiters to avoid tampering
                k = str(k).replace("%", "%25").replace("=", "%3D")
                v = str(v).replace("%", "%25")
                yield "{0}={1}".format(k, v).replace("&", "%26")

        return "&".join(sorted(encoded_pairs(params)))
