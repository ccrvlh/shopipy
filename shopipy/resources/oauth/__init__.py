from shopipy.base import BaseClient
from typing import Any, Dict, List
import hmac, urllib, json, sha256, re, six, time # type: ignore

class OAuth(BaseClient):

    api_key: str = ""
    secret: str = ""
    protocol: str = "https"
    myshopify_domain: str = "myshopify.com"
    port: str = ""

    def __init__(self, shop_url: str, version: str = None, token: str = None, access_scopes: List[str] = None, *args, **kwargs):
        self.url = self.__prepare_url(shop_url)
        self.token = token
        self.version = version
        self.access_scopes = access_scopes
        super(OAuth, self).__init__(*args, **kwargs)

    def create_permission_url(self, scope: List[str], redirect_uri: str, state: str = None):
        query_params = dict(
            client_id=self.api_key,
            scope=",".join(scope),
            redirect_uri=redirect_uri
        )
        if state:
            query_params["state"] = state
        return f"https://{self.url}/admin/oauth/authorize?{urllib.parse.urlencode(query_params)}"

    def request_token(self, params: Dict[Any, Any]):
        if self.token:
            return self.token
        
        if not self.validate_params(params):
            raise Exception("Invalid HMAC: Possibly malicious login")
        
        code = params["code"]
        url = f"https://{self.url}/admin/oauth/access_token?"
        
        query_params = dict(
            client_id=self.api_key,
            client_secret=self.secret,
            code=code
        )
        
        request = urllib.request.Request(url, urllib.parse.urlencode(query_params).encode("utf-8"))
        response = urllib.request.urlopen(request)

        if response.code == 200:
            json_payload = json.loads(response.read().decode("utf-8"))
            self.token = json_payload["access_token"]
            self.access_scopes = json_payload["scope"]
            return self.token
        else:
            raise Exception(response.msg)

    @classmethod
    def validate_params(cls, params: Dict[Any, Any]):
        # Avoid replay attacks by making sure the request
        # isn't more than a day old.
        one_day = 24 * 60 * 60
        if int(params.get("timestamp", 0)) < time.time() - one_day:
            return False

        return cls.validate_hmac(params)

    @classmethod
    def validate_hmac(cls, params: Dict[Any, Any]):
        if "hmac" not in params:
            return False

        hmac_calculated = cls.calculate_hmac(params).encode("utf-8")
        hmac_to_verify = params["hmac"].encode("utf-8")

        # Try to use compare_digest() to reduce vulnerability to timing attacks.
        # If it's not available, just fall back to regular string comparison.
        try:
            return hmac.compare_digest(hmac_calculated, hmac_to_verify)
        except AttributeError:
            return hmac_calculated == hmac_to_verify

    @classmethod
    def calculate_hmac(cls, params: Dict[Any, Any]):
        """
        Calculate the HMAC of the given parameters in line with Shopify's rules for OAuth authentication.
        See http://docs.shopify.com/api/authentication/oauth#verification.
        """
        encoded_params = cls.__encoded_params_for_signature(params)
        return hmac.new(cls.secret.encode(), encoded_params.encode(), sha256).hexdigest()

    @classmethod
    def __prepare_url(cls, url: str):
        if not url or (url.strip() == ""):
            return None
        url = re.sub("^https?://", "", url)
        shop = urllib.parse.urlparse("https://" + url).hostname
        if shop is None:
            return None
        idx = shop.find(".")
        if idx != -1:
            shop = shop[0:idx]
        if len(shop) == 0:
            return None
        shop += "." + cls.myshopify_domain
        if cls.port:
            shop += ":" + str(cls.port)
        return shop

    @classmethod
    def __encoded_params_for_signature(cls, params: Dict[Any, Any]):
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
