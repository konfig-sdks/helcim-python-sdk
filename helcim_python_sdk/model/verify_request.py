# coding: utf-8

"""
    The Helcim API

    This API covers publicly accessible merchant actions

    The version of the OpenAPI document: 2.0.0
    Generated by: https://konfigthis.com
"""

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


class VerifyRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "cardData",
            "amount",
            "ipAddress",
            "currency",
            "billingAddress",
        }
        
        class properties:
            ipAddress = schemas.StrSchema
            currency = schemas.StrSchema
        
            @staticmethod
            def cardData() -> typing.Type['Card']:
                return Card
        
            @staticmethod
            def billingAddress() -> typing.Type['Address']:
                return Address
            ecommerce = schemas.BoolSchema
            customerCode = schemas.StrSchema
            invoiceNumber = schemas.StrSchema
        
            @staticmethod
            def invoice() -> typing.Type['VerifyRequestInvoice']:
                return VerifyRequestInvoice
            __annotations__ = {
                "ipAddress": ipAddress,
                "currency": currency,
                "cardData": cardData,
                "billingAddress": billingAddress,
                "ecommerce": ecommerce,
                "customerCode": customerCode,
                "invoiceNumber": invoiceNumber,
                "invoice": invoice,
            }
    
    cardData: 'Card'
    amount: schemas.AnyTypeSchema
    ipAddress: MetaOapg.properties.ipAddress
    currency: MetaOapg.properties.currency
    billingAddress: 'Address'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipAddress"]) -> MetaOapg.properties.ipAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardData"]) -> 'Card': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billingAddress"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ecommerce"]) -> MetaOapg.properties.ecommerce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerCode"]) -> MetaOapg.properties.customerCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoiceNumber"]) -> MetaOapg.properties.invoiceNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoice"]) -> 'VerifyRequestInvoice': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ipAddress", "currency", "cardData", "billingAddress", "ecommerce", "customerCode", "invoiceNumber", "invoice", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipAddress"]) -> MetaOapg.properties.ipAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardData"]) -> 'Card': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billingAddress"]) -> 'Address': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ecommerce"]) -> typing.Union[MetaOapg.properties.ecommerce, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerCode"]) -> typing.Union[MetaOapg.properties.customerCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoiceNumber"]) -> typing.Union[MetaOapg.properties.invoiceNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoice"]) -> typing.Union['VerifyRequestInvoice', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ipAddress", "currency", "cardData", "billingAddress", "ecommerce", "customerCode", "invoiceNumber", "invoice", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cardData: 'Card',
        amount: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        ipAddress: typing.Union[MetaOapg.properties.ipAddress, str, ],
        currency: typing.Union[MetaOapg.properties.currency, str, ],
        billingAddress: 'Address',
        ecommerce: typing.Union[MetaOapg.properties.ecommerce, bool, schemas.Unset] = schemas.unset,
        customerCode: typing.Union[MetaOapg.properties.customerCode, str, schemas.Unset] = schemas.unset,
        invoiceNumber: typing.Union[MetaOapg.properties.invoiceNumber, str, schemas.Unset] = schemas.unset,
        invoice: typing.Union['VerifyRequestInvoice', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VerifyRequest':
        return super().__new__(
            cls,
            *args,
            cardData=cardData,
            amount=amount,
            ipAddress=ipAddress,
            currency=currency,
            billingAddress=billingAddress,
            ecommerce=ecommerce,
            customerCode=customerCode,
            invoiceNumber=invoiceNumber,
            invoice=invoice,
            _configuration=_configuration,
            **kwargs,
        )

from helcim_python_sdk.model.address import Address
from helcim_python_sdk.model.card import Card
from helcim_python_sdk.model.verify_request_invoice import VerifyRequestInvoice
