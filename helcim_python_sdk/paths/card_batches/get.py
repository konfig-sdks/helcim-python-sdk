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

from helcim_python_sdk.model.card_batch_get_all_response import CardBatchGetAllResponse as CardBatchGetAllResponseSchema
from helcim_python_sdk.model.failed_payment_response import FailedPaymentResponse as FailedPaymentResponseSchema

from helcim_python_sdk.type.failed_payment_response import FailedPaymentResponse
from helcim_python_sdk.type.card_batch_get_all_response import CardBatchGetAllResponse

from ...api_client import Dictionary
from helcim_python_sdk.pydantic.failed_payment_response import FailedPaymentResponse as FailedPaymentResponsePydantic
from helcim_python_sdk.pydantic.card_batch_get_all_response import CardBatchGetAllResponse as CardBatchGetAllResponsePydantic

from . import path

# Query params
BatchNumberSchema = schemas.NumberSchema
TerminalIdSchema = schemas.NumberSchema


class CollectStatsSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "true": "TRUE",
            "false": "FALSE",
        }
    
    @schemas.classproperty
    def TRUE(cls):
        return cls("true")
    
    @schemas.classproperty
    def FALSE(cls):
        return cls("false")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'batchNumber': typing.Union[BatchNumberSchema, decimal.Decimal, int, float, ],
        'terminalId': typing.Union[TerminalIdSchema, decimal.Decimal, int, float, ],
        'collect-stats': typing.Union[CollectStatsSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_batch_number = api_client.QueryParameter(
    name="batchNumber",
    style=api_client.ParameterStyle.FORM,
    schema=BatchNumberSchema,
    explode=True,
)
request_query_terminal_id = api_client.QueryParameter(
    name="terminalId",
    style=api_client.ParameterStyle.FORM,
    schema=TerminalIdSchema,
    explode=True,
)
request_query_collect_stats = api_client.QueryParameter(
    name="collect-stats",
    style=api_client.ParameterStyle.FORM,
    schema=CollectStatsSchema,
    explode=True,
)
_auth = [
    'ApiAccessAuth',
]
SchemaFor200ResponseBodyApplicationJson = CardBatchGetAllResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CardBatchGetAllResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CardBatchGetAllResponse


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

    def _get_all_mapped_args(
        self,
        batch_number: typing.Optional[typing.Union[int, float]] = None,
        terminal_id: typing.Optional[typing.Union[int, float]] = None,
        collect_stats: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if batch_number is not None:
            _query_params["batchNumber"] = batch_number
        if terminal_id is not None:
            _query_params["terminalId"] = terminal_id
        if collect_stats is not None:
            _query_params["collect-stats"] = collect_stats
        args.query = _query_params
        return args

    async def _aget_all_oapg(
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
        Get Card Batches
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_batch_number,
            request_query_terminal_id,
            request_query_collect_stats,
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
            path_template='/card-batches',
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


    def _get_all_oapg(
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
        Get Card Batches
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_batch_number,
            request_query_terminal_id,
            request_query_collect_stats,
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
            path_template='/card-batches',
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


class GetAllRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_all(
        self,
        batch_number: typing.Optional[typing.Union[int, float]] = None,
        terminal_id: typing.Optional[typing.Union[int, float]] = None,
        collect_stats: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_mapped_args(
            batch_number=batch_number,
            terminal_id=terminal_id,
            collect_stats=collect_stats,
        )
        return await self._aget_all_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_all(
        self,
        batch_number: typing.Optional[typing.Union[int, float]] = None,
        terminal_id: typing.Optional[typing.Union[int, float]] = None,
        collect_stats: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_mapped_args(
            batch_number=batch_number,
            terminal_id=terminal_id,
            collect_stats=collect_stats,
        )
        return self._get_all_oapg(
            query_params=args.query,
        )

class GetAll(BaseApi):

    async def aget_all(
        self,
        batch_number: typing.Optional[typing.Union[int, float]] = None,
        terminal_id: typing.Optional[typing.Union[int, float]] = None,
        collect_stats: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CardBatchGetAllResponsePydantic:
        raw_response = await self.raw.aget_all(
            batch_number=batch_number,
            terminal_id=terminal_id,
            collect_stats=collect_stats,
            **kwargs,
        )
        if validate:
            return RootModel[CardBatchGetAllResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(CardBatchGetAllResponsePydantic, raw_response.body)
    
    
    def get_all(
        self,
        batch_number: typing.Optional[typing.Union[int, float]] = None,
        terminal_id: typing.Optional[typing.Union[int, float]] = None,
        collect_stats: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CardBatchGetAllResponsePydantic:
        raw_response = self.raw.get_all(
            batch_number=batch_number,
            terminal_id=terminal_id,
            collect_stats=collect_stats,
        )
        if validate:
            return RootModel[CardBatchGetAllResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(CardBatchGetAllResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        batch_number: typing.Optional[typing.Union[int, float]] = None,
        terminal_id: typing.Optional[typing.Union[int, float]] = None,
        collect_stats: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_mapped_args(
            batch_number=batch_number,
            terminal_id=terminal_id,
            collect_stats=collect_stats,
        )
        return await self._aget_all_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        batch_number: typing.Optional[typing.Union[int, float]] = None,
        terminal_id: typing.Optional[typing.Union[int, float]] = None,
        collect_stats: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_mapped_args(
            batch_number=batch_number,
            terminal_id=terminal_id,
            collect_stats=collect_stats,
        )
        return self._get_all_oapg(
            query_params=args.query,
        )

