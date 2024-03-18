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

from helcim_python_sdk.model.customer_get_card_details_response import CustomerGetCardDetailsResponse as CustomerGetCardDetailsResponseSchema
from helcim_python_sdk.model.failed_payment_response import FailedPaymentResponse as FailedPaymentResponseSchema

from helcim_python_sdk.type.failed_payment_response import FailedPaymentResponse
from helcim_python_sdk.type.customer_get_card_details_response import CustomerGetCardDetailsResponse

from ...api_client import Dictionary
from helcim_python_sdk.pydantic.customer_get_card_details_response import CustomerGetCardDetailsResponse as CustomerGetCardDetailsResponsePydantic
from helcim_python_sdk.pydantic.failed_payment_response import FailedPaymentResponse as FailedPaymentResponsePydantic

from . import path

# Path params
CustomerIdSchema = schemas.IntSchema
CardIdSchema = schemas.IntSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'customerId': typing.Union[CustomerIdSchema, decimal.Decimal, int, ],
        'cardId': typing.Union[CardIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_customer_id = api_client.PathParameter(
    name="customerId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CustomerIdSchema,
    required=True,
)
request_path_card_id = api_client.PathParameter(
    name="cardId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CardIdSchema,
    required=True,
)
_auth = [
    'ApiAccessAuth',
]
SchemaFor200ResponseBodyApplicationJson = CustomerGetCardDetailsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CustomerGetCardDetailsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CustomerGetCardDetailsResponse


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

    def _get_card_details_mapped_args(
        self,
        customer_id: int,
        card_id: int,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if customer_id is not None:
            _path_params["customerId"] = customer_id
        if card_id is not None:
            _path_params["cardId"] = card_id
        args.path = _path_params
        return args

    async def _aget_card_details_oapg(
        self,
            path_params: typing.Optional[dict] = {},
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
        Get customer card
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_customer_id,
            request_path_card_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/customers/{customerId}/cards/{cardId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


    def _get_card_details_oapg(
        self,
            path_params: typing.Optional[dict] = {},
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
        Get customer card
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_customer_id,
            request_path_card_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/customers/{customerId}/cards/{cardId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
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


class GetCardDetailsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_card_details(
        self,
        customer_id: int,
        card_id: int,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_card_details_mapped_args(
            customer_id=customer_id,
            card_id=card_id,
        )
        return await self._aget_card_details_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_card_details(
        self,
        customer_id: int,
        card_id: int,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_card_details_mapped_args(
            customer_id=customer_id,
            card_id=card_id,
        )
        return self._get_card_details_oapg(
            path_params=args.path,
        )

class GetCardDetails(BaseApi):

    async def aget_card_details(
        self,
        customer_id: int,
        card_id: int,
        validate: bool = False,
        **kwargs,
    ) -> CustomerGetCardDetailsResponsePydantic:
        raw_response = await self.raw.aget_card_details(
            customer_id=customer_id,
            card_id=card_id,
            **kwargs,
        )
        if validate:
            return RootModel[CustomerGetCardDetailsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(CustomerGetCardDetailsResponsePydantic, raw_response.body)
    
    
    def get_card_details(
        self,
        customer_id: int,
        card_id: int,
        validate: bool = False,
    ) -> CustomerGetCardDetailsResponsePydantic:
        raw_response = self.raw.get_card_details(
            customer_id=customer_id,
            card_id=card_id,
        )
        if validate:
            return RootModel[CustomerGetCardDetailsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(CustomerGetCardDetailsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        customer_id: int,
        card_id: int,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_card_details_mapped_args(
            customer_id=customer_id,
            card_id=card_id,
        )
        return await self._aget_card_details_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        customer_id: int,
        card_id: int,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_card_details_mapped_args(
            customer_id=customer_id,
            card_id=card_id,
        )
        return self._get_card_details_oapg(
            path_params=args.path,
        )

