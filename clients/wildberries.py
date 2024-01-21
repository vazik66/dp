import aiohttp
from typing import TypedDict, Literal, TypeVar, Generic

_T = TypeVar("_T", bound=dict)


class BaseResponse(TypedDict, Generic[_T]):
    data: _T
    error: bool
    errorText: str
    additionalErrors: list[str] | None
    requestId: str | None


class CountUnseenResponse(TypedDict):
    countUnanswered: int
    countUnansweredToday: int


class HasNewResponse(TypedDict):
    hasNewQuestions: bool
    hasNewFeedbacks: bool


class ListQuestionsParams(TypedDict):
    isAnswered: bool
    nmId: int | None  # Артикул WB
    take: int  # Max: 10.000
    skip: int  # Max: 10.000
    order: Literal["dateAsc", "dateDesc"] | None
    dateFrom: int | None  # UnixTimestamp
    dateTo: int | None  # UnixTimestamp


class Question(TypedDict):
    id: int
    text: str
    createdDate: str
    state: Literal["none", "wbRu", "suppliersPortalSynch"]
    # Отклонен продавцом, Ответ предоставлен, Новый вопрос
    answer: TypedDict("Answer", {"text": str, "editable": bool, "createDate": str})
    productDetails: TypedDict(
        "ProductDetails",
        {
            "nmId": int,
            "umtId": int,
            "productName": str,
            "supplierArticle": str,
            "supplierName": str,
            "brandName": str,
        },
    )
    wasViewed: bool


class ListQuestionsResponse(TypedDict, Generic[_T]):
    countUnanswered: int
    countArchive: int
    questions: list[Question]


class QuestionAnswerParams(TypedDict):
    id: str
    answer: TypedDict("Answer", {"text": str})
    # none: вопрос отклонен
    # wbRu: ответ предоставлен, вопрос отображается на сайте
    state: Literal["none", "wbRu"]


class Client:
    API_URL = "https://feedbacks-api.wb.ru/api/"

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

    async def get_unseen_count(self) -> BaseResponse[CountUnseenResponse]:
        url = f"{self.API_URL}v1/questions/count-unanswered"
        response = await self._request("get", url)
        return response

    async def has_new(self) -> BaseResponse[HasNewResponse]:
        """
        Returns booleans if it has new questions on has new feedbacks
        """
        url = f"{self.API_URL}v1/new-feedbacks-questions"
        response = await self._request("get", url)
        return response

    async def list_questions(
        self, params: ListQuestionsParams
    ) -> BaseResponse[ListQuestionsResponse]:
        url = f"{self.API_URL}v1/questions"
        response = await self._request("get", url, params=params)
        return response

    async def update_question(
        self, params: QuestionAnswerParams
    ) -> BaseResponse[dict | None]:
        url = f"{self.API_URL}v1/questions"
        response = await self._request("patch", url, data=params)
        return response

    async def get_question_by_id(self, id_: str) -> BaseResponse[Question]:
        url = f"{self.API_URL}v1/questions"
        params = {"id": id_}
        response = await self._request("get", url, params=params)
        return response
