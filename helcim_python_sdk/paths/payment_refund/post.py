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

from helcim_python_sdk.model.refund_request import RefundRequest as RefundRequestSchema
from helcim_python_sdk.model.successful_payment_response import SuccessfulPaymentResponse as SuccessfulPaymentResponseSchema
from helcim_python_sdk.model.failed_payment_response import FailedPaymentResponse as FailedPaymentResponseSchema

from helcim_python_sdk.type.refund_request import RefundRequest
from helcim_python_sdk.type.failed_payment_response import FailedPaymentResponse
from helcim_python_sdk.type.successful_payment_response import SuccessfulPaymentResponse

from ...api_client import Dictionary
from helcim_python_sdk.pydantic.failed_payment_response import FailedPaymentResponse as FailedPaymentResponsePydantic
from helcim_python_sdk.pydantic.successful_payment_response import SuccessfulPaymentResponse as SuccessfulPaymentResponsePydantic
from helcim_python_sdk.pydantic.refund_request import RefundRequest as RefundRequestPydantic

from . import path

# Header params
IdempotencyKeySchema = schemas.UUIDSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'idempotency-key': typing.Union[IdempotencyKeySchema, str, uuid.UUID, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_idempotency_key = api_client.HeaderParameter(
    name="idempotency-key",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdempotencyKeySchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = RefundRequestSchema


request_body_refund_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'ApiAccessAuth',
]
SchemaFor200ResponseBodyApplicationJson = SuccessfulPaymentResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SuccessfulPaymentResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SuccessfulPaymentResponse


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

    def _process_refund_transaction_mapped_args(
        self,
        original_transaction_id: int,
        amount: typing.Union[int, float],
        ip_address: str,
        idempotency_key: str,
        ecommerce: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if original_transaction_id is not None:
            _body["originalTransactionId"] = original_transaction_id
        if amount is not None:
            _body["amount"] = amount
        if ip_address is not None:
            _body["ipAddress"] = ip_address
        if ecommerce is not None:
            _body["ecommerce"] = ecommerce
        args.body = _body
        if idempotency_key is not None:
            _header_params["idempotency-key"] = idempotency_key
        args.header = _header_params
        return args

    async def _aprocess_refund_transaction_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Process Refund Transaction
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_idempotency_key,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/payment/refund',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_refund_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _process_refund_transaction_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Process Refund Transaction
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_idempotency_key,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/payment/refund',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_refund_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class ProcessRefundTransactionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aprocess_refund_transaction(
        self,
        original_transaction_id: int,
        amount: typing.Union[int, float],
        ip_address: str,
        idempotency_key: str,
        ecommerce: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._process_refund_transaction_mapped_args(
            original_transaction_id=original_transaction_id,
            amount=amount,
            ip_address=ip_address,
            idempotency_key=idempotency_key,
            ecommerce=ecommerce,
        )
        return await self._aprocess_refund_transaction_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def process_refund_transaction(
        self,
        original_transaction_id: int,
        amount: typing.Union[int, float],
        ip_address: str,
        idempotency_key: str,
        ecommerce: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._process_refund_transaction_mapped_args(
            original_transaction_id=original_transaction_id,
            amount=amount,
            ip_address=ip_address,
            idempotency_key=idempotency_key,
            ecommerce=ecommerce,
        )
        return self._process_refund_transaction_oapg(
            body=args.body,
            header_params=args.header,
        )

class ProcessRefundTransaction(BaseApi):

    async def aprocess_refund_transaction(
        self,
        original_transaction_id: int,
        amount: typing.Union[int, float],
        ip_address: str,
        idempotency_key: str,
        ecommerce: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> SuccessfulPaymentResponsePydantic:
        raw_response = await self.raw.aprocess_refund_transaction(
            original_transaction_id=original_transaction_id,
            amount=amount,
            ip_address=ip_address,
            idempotency_key=idempotency_key,
            ecommerce=ecommerce,
            **kwargs,
        )
        if validate:
            return SuccessfulPaymentResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SuccessfulPaymentResponsePydantic, raw_response.body)
    
    
    def process_refund_transaction(
        self,
        original_transaction_id: int,
        amount: typing.Union[int, float],
        ip_address: str,
        idempotency_key: str,
        ecommerce: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> SuccessfulPaymentResponsePydantic:
        raw_response = self.raw.process_refund_transaction(
            original_transaction_id=original_transaction_id,
            amount=amount,
            ip_address=ip_address,
            idempotency_key=idempotency_key,
            ecommerce=ecommerce,
        )
        if validate:
            return SuccessfulPaymentResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SuccessfulPaymentResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        original_transaction_id: int,
        amount: typing.Union[int, float],
        ip_address: str,
        idempotency_key: str,
        ecommerce: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._process_refund_transaction_mapped_args(
            original_transaction_id=original_transaction_id,
            amount=amount,
            ip_address=ip_address,
            idempotency_key=idempotency_key,
            ecommerce=ecommerce,
        )
        return await self._aprocess_refund_transaction_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        original_transaction_id: int,
        amount: typing.Union[int, float],
        ip_address: str,
        idempotency_key: str,
        ecommerce: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._process_refund_transaction_mapped_args(
            original_transaction_id=original_transaction_id,
            amount=amount,
            ip_address=ip_address,
            idempotency_key=idempotency_key,
            ecommerce=ecommerce,
        )
        return self._process_refund_transaction_oapg(
            body=args.body,
            header_params=args.header,
        )
