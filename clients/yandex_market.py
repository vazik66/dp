import aiohttp
from typing import TypedDict, Literal, TypeVar, Generic

_T = TypeVar("_T", bound=dict)


class BaseResponse(TypedDict, Generic[_T]):
    data: _T
    error: bool
    errorText: str
    additionalErrors: list[str] | None
    requestId: str | None


class Client:
    API_URL = ""

    def __init__(self, http_client: aiohttp.ClientSession, api_key: str):
        self.http_client = http_client
        self.api_key = api_key

    async def _request(
            self,
            method: Literal["get", "post", "patch", "put", "delete"],
            url: str,
            params: dict | None = None,
            data: dict | None = None,
            headers: dict | None = None,
    ) -> dict:
        _headers = {"Authorization": self.api_key}
        if headers:
            _headers = {**_headers, **headers}

        async with self.http_client as session:
            async with session.request(
                    method, url, params=params, json=data, headers=headers
            ) as resp:
                resp.raise_for_status()
                return await resp.json()


raise NotImplementedError()
