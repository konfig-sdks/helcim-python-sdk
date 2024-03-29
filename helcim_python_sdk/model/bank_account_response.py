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


class BankAccountResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            customerId = schemas.IntSchema
            dateCreated = schemas.StrSchema
            dateUpdated = schemas.StrSchema
            dateLastUsed = schemas.StrSchema
            dateVerified = schemas.StrSchema
            bankToken = schemas.StrSchema
            accountType = schemas.StrSchema
            accountCorporate = schemas.StrSchema
            verified = schemas.StrSchema
            ready = schemas.StrSchema
            bankIdNumber = schemas.StrSchema
            transitNumber = schemas.StrSchema
            routingNumber = schemas.StrSchema
            bankAccountNumberL4 = schemas.StrSchema
        
            @staticmethod
            def address() -> typing.Type['Address']:
                return Address
            __annotations__ = {
                "id": id,
                "customerId": customerId,
                "dateCreated": dateCreated,
                "dateUpdated": dateUpdated,
                "dateLastUsed": dateLastUsed,
                "dateVerified": dateVerified,
                "bankToken": bankToken,
                "accountType": accountType,
                "accountCorporate": accountCorporate,
                "verified": verified,
                "ready": ready,
                "bankIdNumber": bankIdNumber,
                "transitNumber": transitNumber,
                "routingNumber": routingNumber,
                "bankAccountNumberL4": bankAccountNumberL4,
                "address": address,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customerId"]) -> MetaOapg.properties.customerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateCreated"]) -> MetaOapg.properties.dateCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateUpdated"]) -> MetaOapg.properties.dateUpdated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateLastUsed"]) -> MetaOapg.properties.dateLastUsed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateVerified"]) -> MetaOapg.properties.dateVerified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bankToken"]) -> MetaOapg.properties.bankToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountType"]) -> MetaOapg.properties.accountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountCorporate"]) -> MetaOapg.properties.accountCorporate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verified"]) -> MetaOapg.properties.verified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ready"]) -> MetaOapg.properties.ready: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bankIdNumber"]) -> MetaOapg.properties.bankIdNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transitNumber"]) -> MetaOapg.properties.transitNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["routingNumber"]) -> MetaOapg.properties.routingNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bankAccountNumberL4"]) -> MetaOapg.properties.bankAccountNumberL4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'Address': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "customerId", "dateCreated", "dateUpdated", "dateLastUsed", "dateVerified", "bankToken", "accountType", "accountCorporate", "verified", "ready", "bankIdNumber", "transitNumber", "routingNumber", "bankAccountNumberL4", "address", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customerId"]) -> typing.Union[MetaOapg.properties.customerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateCreated"]) -> typing.Union[MetaOapg.properties.dateCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateUpdated"]) -> typing.Union[MetaOapg.properties.dateUpdated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateLastUsed"]) -> typing.Union[MetaOapg.properties.dateLastUsed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateVerified"]) -> typing.Union[MetaOapg.properties.dateVerified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bankToken"]) -> typing.Union[MetaOapg.properties.bankToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountType"]) -> typing.Union[MetaOapg.properties.accountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountCorporate"]) -> typing.Union[MetaOapg.properties.accountCorporate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verified"]) -> typing.Union[MetaOapg.properties.verified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ready"]) -> typing.Union[MetaOapg.properties.ready, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bankIdNumber"]) -> typing.Union[MetaOapg.properties.bankIdNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transitNumber"]) -> typing.Union[MetaOapg.properties.transitNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["routingNumber"]) -> typing.Union[MetaOapg.properties.routingNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bankAccountNumberL4"]) -> typing.Union[MetaOapg.properties.bankAccountNumberL4, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['Address', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "customerId", "dateCreated", "dateUpdated", "dateLastUsed", "dateVerified", "bankToken", "accountType", "accountCorporate", "verified", "ready", "bankIdNumber", "transitNumber", "routingNumber", "bankAccountNumberL4", "address", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        customerId: typing.Union[MetaOapg.properties.customerId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dateCreated: typing.Union[MetaOapg.properties.dateCreated, str, schemas.Unset] = schemas.unset,
        dateUpdated: typing.Union[MetaOapg.properties.dateUpdated, str, schemas.Unset] = schemas.unset,
        dateLastUsed: typing.Union[MetaOapg.properties.dateLastUsed, str, schemas.Unset] = schemas.unset,
        dateVerified: typing.Union[MetaOapg.properties.dateVerified, str, schemas.Unset] = schemas.unset,
        bankToken: typing.Union[MetaOapg.properties.bankToken, str, schemas.Unset] = schemas.unset,
        accountType: typing.Union[MetaOapg.properties.accountType, str, schemas.Unset] = schemas.unset,
        accountCorporate: typing.Union[MetaOapg.properties.accountCorporate, str, schemas.Unset] = schemas.unset,
        verified: typing.Union[MetaOapg.properties.verified, str, schemas.Unset] = schemas.unset,
        ready: typing.Union[MetaOapg.properties.ready, str, schemas.Unset] = schemas.unset,
        bankIdNumber: typing.Union[MetaOapg.properties.bankIdNumber, str, schemas.Unset] = schemas.unset,
        transitNumber: typing.Union[MetaOapg.properties.transitNumber, str, schemas.Unset] = schemas.unset,
        routingNumber: typing.Union[MetaOapg.properties.routingNumber, str, schemas.Unset] = schemas.unset,
        bankAccountNumberL4: typing.Union[MetaOapg.properties.bankAccountNumberL4, str, schemas.Unset] = schemas.unset,
        address: typing.Union['Address', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BankAccountResponse':
        return super().__new__(
            cls,
            *args,
            id=id,
            customerId=customerId,
            dateCreated=dateCreated,
            dateUpdated=dateUpdated,
            dateLastUsed=dateLastUsed,
            dateVerified=dateVerified,
            bankToken=bankToken,
            accountType=accountType,
            accountCorporate=accountCorporate,
            verified=verified,
            ready=ready,
            bankIdNumber=bankIdNumber,
            transitNumber=transitNumber,
            routingNumber=routingNumber,
            bankAccountNumberL4=bankAccountNumberL4,
            address=address,
            _configuration=_configuration,
            **kwargs,
        )

from helcim_python_sdk.model.address import Address
