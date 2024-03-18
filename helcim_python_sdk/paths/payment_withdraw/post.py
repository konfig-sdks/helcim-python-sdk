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

from helcim_python_sdk.model.payment_request_invoice import PaymentRequestInvoice as PaymentRequestInvoiceSchema
from helcim_python_sdk.model.withdraw_request import WithdrawRequest as WithdrawRequestSchema
from helcim_python_sdk.model.successful_ach_transaction_response import SuccessfulAchTransactionResponse as SuccessfulAchTransactionResponseSchema
from helcim_python_sdk.model.bank_data_bank_data import BankDataBankData as BankDataBankDataSchema
from helcim_python_sdk.model.address import Address as AddressSchema
from helcim_python_sdk.model.failed_payment_response import FailedPaymentResponse as FailedPaymentResponseSchema

from helcim_python_sdk.type.address import Address
from helcim_python_sdk.type.successful_ach_transaction_response import SuccessfulAchTransactionResponse
from helcim_python_sdk.type.failed_payment_response import FailedPaymentResponse
from helcim_python_sdk.type.withdraw_request import WithdrawRequest
from helcim_python_sdk.type.payment_request_invoice import PaymentRequestInvoice
from helcim_python_sdk.type.bank_data_bank_data import BankDataBankData

from ...api_client import Dictionary
from helcim_python_sdk.pydantic.bank_data_bank_data import BankDataBankData as BankDataBankDataPydantic
from helcim_python_sdk.pydantic.withdraw_request import WithdrawRequest as WithdrawRequestPydantic
from helcim_python_sdk.pydantic.failed_payment_response import FailedPaymentResponse as FailedPaymentResponsePydantic
from helcim_python_sdk.pydantic.address import Address as AddressPydantic
from helcim_python_sdk.pydantic.payment_request_invoice import PaymentRequestInvoice as PaymentRequestInvoicePydantic
from helcim_python_sdk.pydantic.successful_ach_transaction_response import SuccessfulAchTransactionResponse as SuccessfulAchTransactionResponsePydantic

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
SchemaForRequestBodyApplicationJson = WithdrawRequestSchema


request_body_withdraw_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'ApiAccessAuth',
]
SchemaFor200ResponseBodyApplicationJson = SuccessfulAchTransactionResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SuccessfulAchTransactionResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SuccessfulAchTransactionResponse


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

    def _process_withdrawal_transaction_mapped_args(
        self,
        idempotency_key: str,
        ip_address: typing.Optional[str] = None,
        ecommerce: typing.Optional[bool] = None,
        terminal_id: typing.Optional[int] = None,
        currency: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        invoice: typing.Optional[PaymentRequestInvoice] = None,
        billing_address: typing.Optional[Address] = None,
        bank_data: typing.Optional[BankDataBankData] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if ip_address is not None:
            _body["ipAddress"] = ip_address
        if ecommerce is not None:
            _body["ecommerce"] = ecommerce
        if terminal_id is not None:
            _body["terminalId"] = terminal_id
        if currency is not None:
            _body["currency"] = currency
        if amount is not None:
            _body["amount"] = amount
        if customer_code is not None:
            _body["customerCode"] = customer_code
        if invoice_number is not None:
            _body["invoiceNumber"] = invoice_number
        if invoice is not None:
            _body["invoice"] = invoice
        if billing_address is not None:
            _body["billingAddress"] = billing_address
        if bank_data is not None:
            _body["bankData"] = bank_data
        args.body = _body
        if idempotency_key is not None:
            _header_params["idempotency-key"] = idempotency_key
        args.header = _header_params
        return args

    async def _aprocess_withdrawal_transaction_oapg(
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
        Process Withdraw Transaction
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
            path_template='/payment/withdraw',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_withdraw_request.serialize(body, content_type)
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


    def _process_withdrawal_transaction_oapg(
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
        Process Withdraw Transaction
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
            path_template='/payment/withdraw',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_withdraw_request.serialize(body, content_type)
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


class ProcessWithdrawalTransactionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aprocess_withdrawal_transaction(
        self,
        idempotency_key: str,
        ip_address: typing.Optional[str] = None,
        ecommerce: typing.Optional[bool] = None,
        terminal_id: typing.Optional[int] = None,
        currency: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        invoice: typing.Optional[PaymentRequestInvoice] = None,
        billing_address: typing.Optional[Address] = None,
        bank_data: typing.Optional[BankDataBankData] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._process_withdrawal_transaction_mapped_args(
            body=body,
            idempotency_key=idempotency_key,
            ip_address=ip_address,
            ecommerce=ecommerce,
            terminal_id=terminal_id,
            currency=currency,
            amount=amount,
            customer_code=customer_code,
            invoice_number=invoice_number,
            invoice=invoice,
            billing_address=billing_address,
            bank_data=bank_data,
        )
        return await self._aprocess_withdrawal_transaction_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def process_withdrawal_transaction(
        self,
        idempotency_key: str,
        ip_address: typing.Optional[str] = None,
        ecommerce: typing.Optional[bool] = None,
        terminal_id: typing.Optional[int] = None,
        currency: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        invoice: typing.Optional[PaymentRequestInvoice] = None,
        billing_address: typing.Optional[Address] = None,
        bank_data: typing.Optional[BankDataBankData] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._process_withdrawal_transaction_mapped_args(
            body=body,
            idempotency_key=idempotency_key,
            ip_address=ip_address,
            ecommerce=ecommerce,
            terminal_id=terminal_id,
            currency=currency,
            amount=amount,
            customer_code=customer_code,
            invoice_number=invoice_number,
            invoice=invoice,
            billing_address=billing_address,
            bank_data=bank_data,
        )
        return self._process_withdrawal_transaction_oapg(
            body=args.body,
            header_params=args.header,
        )

class ProcessWithdrawalTransaction(BaseApi):

    async def aprocess_withdrawal_transaction(
        self,
        idempotency_key: str,
        ip_address: typing.Optional[str] = None,
        ecommerce: typing.Optional[bool] = None,
        terminal_id: typing.Optional[int] = None,
        currency: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        invoice: typing.Optional[PaymentRequestInvoice] = None,
        billing_address: typing.Optional[Address] = None,
        bank_data: typing.Optional[BankDataBankData] = None,
        validate: bool = False,
        **kwargs,
    ) -> SuccessfulAchTransactionResponsePydantic:
        raw_response = await self.raw.aprocess_withdrawal_transaction(
            body=body,
            idempotency_key=idempotency_key,
            ip_address=ip_address,
            ecommerce=ecommerce,
            terminal_id=terminal_id,
            currency=currency,
            amount=amount,
            customer_code=customer_code,
            invoice_number=invoice_number,
            invoice=invoice,
            billing_address=billing_address,
            bank_data=bank_data,
            **kwargs,
        )
        if validate:
            return SuccessfulAchTransactionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SuccessfulAchTransactionResponsePydantic, raw_response.body)
    
    
    def process_withdrawal_transaction(
        self,
        idempotency_key: str,
        ip_address: typing.Optional[str] = None,
        ecommerce: typing.Optional[bool] = None,
        terminal_id: typing.Optional[int] = None,
        currency: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        invoice: typing.Optional[PaymentRequestInvoice] = None,
        billing_address: typing.Optional[Address] = None,
        bank_data: typing.Optional[BankDataBankData] = None,
        validate: bool = False,
    ) -> SuccessfulAchTransactionResponsePydantic:
        raw_response = self.raw.process_withdrawal_transaction(
            body=body,
            idempotency_key=idempotency_key,
            ip_address=ip_address,
            ecommerce=ecommerce,
            terminal_id=terminal_id,
            currency=currency,
            amount=amount,
            customer_code=customer_code,
            invoice_number=invoice_number,
            invoice=invoice,
            billing_address=billing_address,
            bank_data=bank_data,
        )
        if validate:
            return SuccessfulAchTransactionResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SuccessfulAchTransactionResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        idempotency_key: str,
        ip_address: typing.Optional[str] = None,
        ecommerce: typing.Optional[bool] = None,
        terminal_id: typing.Optional[int] = None,
        currency: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        invoice: typing.Optional[PaymentRequestInvoice] = None,
        billing_address: typing.Optional[Address] = None,
        bank_data: typing.Optional[BankDataBankData] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._process_withdrawal_transaction_mapped_args(
            body=body,
            idempotency_key=idempotency_key,
            ip_address=ip_address,
            ecommerce=ecommerce,
            terminal_id=terminal_id,
            currency=currency,
            amount=amount,
            customer_code=customer_code,
            invoice_number=invoice_number,
            invoice=invoice,
            billing_address=billing_address,
            bank_data=bank_data,
        )
        return await self._aprocess_withdrawal_transaction_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        idempotency_key: str,
        ip_address: typing.Optional[str] = None,
        ecommerce: typing.Optional[bool] = None,
        terminal_id: typing.Optional[int] = None,
        currency: typing.Optional[str] = None,
        amount: typing.Optional[typing.Union[int, float]] = None,
        customer_code: typing.Optional[str] = None,
        invoice_number: typing.Optional[str] = None,
        invoice: typing.Optional[PaymentRequestInvoice] = None,
        billing_address: typing.Optional[Address] = None,
        bank_data: typing.Optional[BankDataBankData] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._process_withdrawal_transaction_mapped_args(
            body=body,
            idempotency_key=idempotency_key,
            ip_address=ip_address,
            ecommerce=ecommerce,
            terminal_id=terminal_id,
            currency=currency,
            amount=amount,
            customer_code=customer_code,
            invoice_number=invoice_number,
            invoice=invoice,
            billing_address=billing_address,
            bank_data=bank_data,
        )
        return self._process_withdrawal_transaction_oapg(
            body=args.body,
            header_params=args.header,
        )

