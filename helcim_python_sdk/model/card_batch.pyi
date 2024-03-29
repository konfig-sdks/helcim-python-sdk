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


class CardBatch(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            dateCreated = schemas.StrSchema
            dateUpdated = schemas.StrSchema
            dateClosed = schemas.StrSchema
            closed = schemas.BoolSchema
            terminalId = schemas.IntSchema
            batchNumber = schemas.IntSchema
            netSales = schemas.NumberSchema
            totalSales = schemas.NumberSchema
            totalRefunds = schemas.NumberSchema
            totalReversed = schemas.NumberSchema
            totalRefundsReversed = schemas.NumberSchema
            countTotal = schemas.NumberSchema
            countApproved = schemas.NumberSchema
            countDeclined = schemas.NumberSchema
            __annotations__ = {
                "id": id,
                "dateCreated": dateCreated,
                "dateUpdated": dateUpdated,
                "dateClosed": dateClosed,
                "closed": closed,
                "terminalId": terminalId,
                "batchNumber": batchNumber,
                "netSales": netSales,
                "totalSales": totalSales,
                "totalRefunds": totalRefunds,
                "totalReversed": totalReversed,
                "totalRefundsReversed": totalRefundsReversed,
                "countTotal": countTotal,
                "countApproved": countApproved,
                "countDeclined": countDeclined,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateCreated"]) -> MetaOapg.properties.dateCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateUpdated"]) -> MetaOapg.properties.dateUpdated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateClosed"]) -> MetaOapg.properties.dateClosed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["closed"]) -> MetaOapg.properties.closed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminalId"]) -> MetaOapg.properties.terminalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["batchNumber"]) -> MetaOapg.properties.batchNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["netSales"]) -> MetaOapg.properties.netSales: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalSales"]) -> MetaOapg.properties.totalSales: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalRefunds"]) -> MetaOapg.properties.totalRefunds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalReversed"]) -> MetaOapg.properties.totalReversed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalRefundsReversed"]) -> MetaOapg.properties.totalRefundsReversed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countTotal"]) -> MetaOapg.properties.countTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countApproved"]) -> MetaOapg.properties.countApproved: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countDeclined"]) -> MetaOapg.properties.countDeclined: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "dateCreated", "dateUpdated", "dateClosed", "closed", "terminalId", "batchNumber", "netSales", "totalSales", "totalRefunds", "totalReversed", "totalRefundsReversed", "countTotal", "countApproved", "countDeclined", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateCreated"]) -> typing.Union[MetaOapg.properties.dateCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateUpdated"]) -> typing.Union[MetaOapg.properties.dateUpdated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateClosed"]) -> typing.Union[MetaOapg.properties.dateClosed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["closed"]) -> typing.Union[MetaOapg.properties.closed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminalId"]) -> typing.Union[MetaOapg.properties.terminalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["batchNumber"]) -> typing.Union[MetaOapg.properties.batchNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["netSales"]) -> typing.Union[MetaOapg.properties.netSales, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalSales"]) -> typing.Union[MetaOapg.properties.totalSales, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalRefunds"]) -> typing.Union[MetaOapg.properties.totalRefunds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalReversed"]) -> typing.Union[MetaOapg.properties.totalReversed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalRefundsReversed"]) -> typing.Union[MetaOapg.properties.totalRefundsReversed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countTotal"]) -> typing.Union[MetaOapg.properties.countTotal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countApproved"]) -> typing.Union[MetaOapg.properties.countApproved, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countDeclined"]) -> typing.Union[MetaOapg.properties.countDeclined, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "dateCreated", "dateUpdated", "dateClosed", "closed", "terminalId", "batchNumber", "netSales", "totalSales", "totalRefunds", "totalReversed", "totalRefundsReversed", "countTotal", "countApproved", "countDeclined", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dateCreated: typing.Union[MetaOapg.properties.dateCreated, str, schemas.Unset] = schemas.unset,
        dateUpdated: typing.Union[MetaOapg.properties.dateUpdated, str, schemas.Unset] = schemas.unset,
        dateClosed: typing.Union[MetaOapg.properties.dateClosed, str, schemas.Unset] = schemas.unset,
        closed: typing.Union[MetaOapg.properties.closed, bool, schemas.Unset] = schemas.unset,
        terminalId: typing.Union[MetaOapg.properties.terminalId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        batchNumber: typing.Union[MetaOapg.properties.batchNumber, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        netSales: typing.Union[MetaOapg.properties.netSales, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalSales: typing.Union[MetaOapg.properties.totalSales, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalRefunds: typing.Union[MetaOapg.properties.totalRefunds, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalReversed: typing.Union[MetaOapg.properties.totalReversed, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalRefundsReversed: typing.Union[MetaOapg.properties.totalRefundsReversed, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        countTotal: typing.Union[MetaOapg.properties.countTotal, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        countApproved: typing.Union[MetaOapg.properties.countApproved, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        countDeclined: typing.Union[MetaOapg.properties.countDeclined, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CardBatch':
        return super().__new__(
            cls,
            *args,
            id=id,
            dateCreated=dateCreated,
            dateUpdated=dateUpdated,
            dateClosed=dateClosed,
            closed=closed,
            terminalId=terminalId,
            batchNumber=batchNumber,
            netSales=netSales,
            totalSales=totalSales,
            totalRefunds=totalRefunds,
            totalReversed=totalReversed,
            totalRefundsReversed=totalRefundsReversed,
            countTotal=countTotal,
            countApproved=countApproved,
            countDeclined=countDeclined,
            _configuration=_configuration,
            **kwargs,
        )
