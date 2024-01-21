import aiohttp
from typing import TypedDict, Literal


class ProductResponse(TypedDict):
    result: TypedDict(
        "result",
        {
            "items": list[
                TypedDict(
                    "Item",
                    {
                        "offer_id": str,
                        "product_id": int,
                    },
                )
            ],
            "last_id": str,
            "total": int,
        },
    )


class ChatResponse(TypedDict):
    chats: TypedDict(
        "Chat",
        {
            "chat_id": str,
            "chat_status": Literal["All", "Opened", "Closed"],
            "chat_type": Literal["Seller_Support", "Buyer_Seller"],
            "created_at": str,
            "first_unread_message_id": int,
            "last_message_id": int,
            "unread_count": int,
        },
    )

    total_chats_count: int
    total_unread_count: int


class ChatSendMessageResponse(TypedDict):
    result: str


class ProductFilter(TypedDict):
    offer_id: list[str]
    product_id: list[int]
    visibility: Literal[
        "ALL", "VISIBLE", "INVISIBLE", "EMPTY_STOCK", "NOT_MODERATED", "MODERATED"
    ]


class ChatFilter(TypedDict):
    chat_status: Literal["All", "Opened", "Closed"]
    unread_only: bool


class OzonErrorResponse(TypedDict):
    code: int
    details: list[TypedDict("Detail", {"typeUrl": str, "value": str})]
    message: str


class Client:
    API_URL = "https://api-seller.ozon.ru/"

    def __init__(
        self, http_client: aiohttp.ClientSession, client_id: str, api_key: str
    ):
        self.http_client = http_client
        self.client_id = client_id
        self.api_key = api_key

    async def _post(self, url: str, data: dict) -> dict:
        headers = {"Client-Id": self.client_id, "Api-Key": self.api_key}
        async with self.http_client as session:
            async with session.post(url, json=data, headers=headers) as resp:
                resp.raise_for_status()
                return await resp.json()

    async def product_list(
        self, filter_: ProductFilter | None = None, last_id: str = "", limit: int = 1000
    ) -> ProductResponse | OzonErrorResponse:
        url = f"{self.API_URL}v2/product/list"
        data = {"filter": filter_, "last_id": last_id, "limit": limit}
        return await self._post(url, data)

    async def chat_list(
        self, filter_: ChatFilter | None = None, offset: int = 0, limit: int = 30
    ) -> ChatResponse | OzonErrorResponse:
        url = f"{self.API_URL}v1/chat/list"
        data = {"filter": filter_, "offset": offset, "limit": limit}
        return await self._post(url, data)

    async def chat_send_message(
        self, chat_id: str, text: str
    ) -> ChatSendMessageResponse | OzonErrorResponse:
        url = f"{self.API_URL}v1/chat/send/message"
        data = {"chat_id": chat_id, "text": text}
        return await self._post(url, data)

    async def chat_send_file(
        self, chat_id: str, base64_content: str, name: str
    ) -> ChatSendMessageResponse | OzonErrorResponse:
        url = f"{self.API_URL}v1/chat/send/message"
        data = {"chat_id": chat_id, "base64_content": base64_content, "name": name}
        return await self._post(url, data)
