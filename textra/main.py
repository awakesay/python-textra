"""
Class module
"""

from typing import Final
from requests_oauthlib import OAuth2Session  # type: ignore
from oauthlib.oauth2 import BackendApplicationClient, OAuth2Token

BASE_URL: Final[str] = "https://mt-auto-minhon-mlt.ucri.jgn-x.jp"


class TextraToken(OAuth2Token):  # OAuth2Token の基底クラスは dict
    """
    Textra Web API の OAuth2 認証トークンを取得する。
    """

    OAUTH2_URL: Final[str] = BASE_URL + "/oauth2/token.php"

    def __init__(self, client_id: str, client_secret: str):
        """
        Description
        -----------
            Textra Web API の OAuth2 認証トークンを取得する。

        Parameters
        ----------
        `client_id`: `str`
            TexTra API key

        `client_secret`: `str`
            TexTra API secret

        Example
        -------
        >>> # APIキーとシークレットは事前に取得する。
        >>> api_key = "{your API key}"
        >>> api_secret = "{your API secret}"
        >>> token = TextraToken(api_key, api_secret)
        """

        # client_id と client_secret は後工程で利用するので、このクラスで保持する。
        self["client_id"] = client_id
        self["client_secret"] = client_secret

        super().__init__(
            OAuth2Session(
                client=BackendApplicationClient(client_id=client_id)
            ).fetch_token(
                token_url=self.OAUTH2_URL,
                client_id=client_id,
                client_secret=client_secret
            )
        )


class TextraRequestParameters(dict):
    """
    requests.post の引数に渡す Textra のリクエストパラメーターを生成します。
    """
    def __init__(
        self,
        token: TextraToken,
        name: str,
        api_name: str,
        api_param: str,
        **request_parameters
    ):
        """
        Description
        -----------
            requests.post の引数に渡す Textra のリクエストパラメーターを生成します。

        Parameters
        ----------
        `token`: `TextraToken`
        `name`: `str`
            ユーザー名
        `api_name`: `str`
        `api_param`: `str`
            リクエストURLの以下の値です。
            https://.../api/{`api_name`}/{`api_param`}

        Example
        -------
        >>> import requests
        >>> api_key = "{your API key}"
        >>> api_secret = "{your API secret}"
        >>> token = TextraToken(api_key, api_secret)
        >>> name = "{your user name}"
        >>> req_params = TextraRequestParameters(
        >>>     token,
        >>>     name,
        >>>     "mt",
        >>>     "generalNT_ja_en",  # 汎用NT 【日本語 - 英語】
        >>>     # 以降のパラメーターは利用するWeb API のリクエストパラメーターを参照してください。
        >>>     type="json"
        >>> )
        >>> response = requests.post(**req_params)
        >>> res_json = json.loads(response.text)
        >>> print(res_json)
        """
        self["url"] = f"{BASE_URL}/api/?"
        self["data"] = {
            "access_token": token["access_token"],
            "key": token["client_id"],
            "name": name,
            "api_name": api_name,
            "api_param": api_param,
        }
        self["data"] = self["data"] | request_parameters
