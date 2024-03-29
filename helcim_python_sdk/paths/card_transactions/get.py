# coding: utf-8

"""
    The Helcim API

    This API covers publicly accessible merchant actions

    The version of the OpenAPI document: 2.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from helcim_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from helcim_python_sdk.api_response import AsyncGeneratorResponse
from helcim_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from helcim_python_sdk import schemas  # noqa: F401

from helcim_python_sdk.model.card_transaction_collect_transactions_response import CardTransactionCollectTransactionsResponse as CardTransactionCollectTransactionsResponseSchema
from helcim_python_sdk.model.failed_payment_response import FailedPaymentResponse as FailedPaymentResponseSchema

from helcim_python_sdk.type.failed_payment_response import FailedPaymentResponse
from helcim_python_sdk.type.card_transaction_collect_transactions_response import CardTransactionCollectTransactionsResponse

from ...api_client import Dictionary
from helcim_python_sdk.pydantic.failed_payment_response import FailedPaymentResponse as FailedPaymentResponsePydantic
from helcim_python_sdk.pydantic.card_transaction_collect_transactions_response import CardTransactionCollectTransactionsResponse as CardTransactionCollectTransactionsResponsePydantic

from . import path

# Query params
DateFromSchema = schemas.StrSchema
DateToSchema = schemas.StrSchema
SearchSchema = schemas.StrSchema
CustomerCodeSchema = schemas.StrSchema
InvoiceNumberSchema = schemas.StrSchema
CardTokenSchema = schemas.StrSchema
CardBatchIdSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'dateFrom': typing.Union[DateFromSchema, str, ],
        'dateTo': typing.Union[DateToSchema, str, ],
        'search': typing.Union[SearchSchema, str, ],
        'customerCode': typing.Union[CustomerCodeSchema, str, ],
        'invoiceNumber': typing.Union[InvoiceNumberSchema, str, ],
        'cardToken': typing.Union[CardTokenSchema, str, ],
        'cardBatchId': typing.Union[CardBatchIdSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_date_from = api_client.QueryParameter(
    name="dateFrom",
    style=api_client.ParameterStyle.FORM,
    schema=DateFromSchema,
    explode=True,
)
request_query_date_to = api_client.QueryParameter(
    name="dateTo",
    style=api_client.ParameterStyle.FORM,
    schema=DateToSchema,
    explode=True,
)
request_query_search = api_client.QueryParameter(
    name="search",
    style=api_client.ParameterStyle.FORM,
    schema=SearchSchema,
    explode=True,
)
request_query_customer_code = api_client.QueryParameter(
    name="customerCode",
    style=api_client.ParameterStyle.FORM,
    schema=CustomerCodeSchema,
    explode=True,
)
request_query_invoice_number = api_client.QueryParameter(
    name="invoiceNumber",
    style=api_client.ParameterStyle.FORM,
    schema=InvoiceNumberSchema,
    explode=True,
)
request_query_card_token = api_client.QueryParameter(
    name="cardToken",
    style=api_client.ParameterStyle.FORM,
    schema=CardTokenSchema,
    explode=True,
)
request_query_card_batch_id = api_client.QueryParameter(
    name="cardBatchId",
    style=api_client.ParameterStyle.FORM,
    schema=CardBatchIdSchema,
    explode=True,
)
_auth = [
    'ApiAccessAuth',
]
SchemaFor200ResponseBodyApplicationJson = CardTransactionCollectTransactionsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CardTransactionCollectTransactionsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CardTransactionCollectTransactionsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = FailedPaymentResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: FailedPaymentResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: FailedPaymentResponse


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _collect_transactions_mapped_args(
        self,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        card_token: typing.Optional[str] = None,
        card_batch_id: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if date_from is not None:
            _query_params["dateFrom"] = date_from
        if date_to is not None:
            _query_params["dateTo"] = date_to
        if search is not None:
            _query_params["search"] = search
        if customer_code is not None:
            _query_params["customerCode"] = customer_code
        if invoice_number is not None:
            _query_params["invoiceNumber"] = invoice_number
        if card_token is not None:
            _query_params["cardToken"] = card_token
        if card_batch_id is not None:
            _query_params["cardBatchId"] = card_batch_id
        args.query = _query_params
        return args

    async def _acollect_transactions_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Collects up to 1000 Card Transactions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_date_from,
            request_query_date_to,
            request_query_search,
            request_query_customer_code,
            request_query_invoice_number,
            request_query_card_token,
            request_query_card_batch_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/card-transactions',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _collect_transactions_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Collects up to 1000 Card Transactions
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_date_from,
            request_query_date_to,
            request_query_search,
            request_query_customer_code,
            request_query_invoice_number,
            request_query_card_token,
            request_query_card_batch_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/card-transactions',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CollectTransactionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acollect_transactions(
        self,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        card_token: typing.Optional[str] = None,
        card_batch_id: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._collect_transactions_mapped_args(
            date_from=date_from,
            date_to=date_to,
            search=search,
            customer_code=customer_code,
            invoice_number=invoice_number,
            card_token=card_token,
            card_batch_id=card_batch_id,
        )
        return await self._acollect_transactions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def collect_transactions(
        self,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        card_token: typing.Optional[str] = None,
        card_batch_id: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._collect_transactions_mapped_args(
            date_from=date_from,
            date_to=date_to,
            search=search,
            customer_code=customer_code,
            invoice_number=invoice_number,
            card_token=card_token,
            card_batch_id=card_batch_id,
        )
        return self._collect_transactions_oapg(
            query_params=args.query,
        )

class CollectTransactions(BaseApi):

    async def acollect_transactions(
        self,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        card_token: typing.Optional[str] = None,
        card_batch_id: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> CardTransactionCollectTransactionsResponsePydantic:
        raw_response = await self.raw.acollect_transactions(
            date_from=date_from,
            date_to=date_to,
            search=search,
            customer_code=customer_code,
            invoice_number=invoice_number,
            card_token=card_token,
            card_batch_id=card_batch_id,
            **kwargs,
        )
        if validate:
            return RootModel[CardTransactionCollectTransactionsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(CardTransactionCollectTransactionsResponsePydantic, raw_response.body)
    
    
    def collect_transactions(
        self,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        card_token: typing.Optional[str] = None,
        card_batch_id: typing.Optional[int] = None,
        validate: bool = False,
    ) -> CardTransactionCollectTransactionsResponsePydantic:
        raw_response = self.raw.collect_transactions(
            date_from=date_from,
            date_to=date_to,
            search=search,
            customer_code=customer_code,
            invoice_number=invoice_number,
            card_token=card_token,
            card_batch_id=card_batch_id,
        )
        if validate:
            return RootModel[CardTransactionCollectTransactionsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(CardTransactionCollectTransactionsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        card_token: typing.Optional[str] = None,
        card_batch_id: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._collect_transactions_mapped_args(
            date_from=date_from,
            date_to=date_to,
            search=search,
            customer_code=customer_code,
            invoice_number=invoice_number,
            card_token=card_token,
            card_batch_id=card_batch_id,
        )
        return await self._acollect_transactions_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        date_from: typing.Optional[str] = None,
        date_to: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        card_token: typing.Optional[str] = None,
        card_batch_id: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._collect_transactions_mapped_args(
            date_from=date_from,
            date_to=date_to,
            search=search,
            customer_code=customer_code,
            invoice_number=invoice_number,
            card_token=card_token,
            card_batch_id=card_batch_id,
        )
        return self._collect_transactions_oapg(
            query_params=args.query,
        )

