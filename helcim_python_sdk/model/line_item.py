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


class LineItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "total",
            "quantity",
            "price",
            "description",
        }
        
        class properties:
            description = schemas.StrSchema
            quantity = schemas.NumberSchema
            price = schemas.NumberSchema
            total = schemas.NumberSchema
            sku = schemas.StrSchema
            taxAmount = schemas.NumberSchema
            discountAmount = schemas.NumberSchema
            __annotations__ = {
                "description": description,
                "quantity": quantity,
                "price": price,
                "total": total,
                "sku": sku,
                "taxAmount": taxAmount,
                "discountAmount": discountAmount,
            }
    
    total: MetaOapg.properties.total
    quantity: MetaOapg.properties.quantity
    price: MetaOapg.properties.price
    description: MetaOapg.properties.description
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sku"]) -> MetaOapg.properties.sku: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxAmount"]) -> MetaOapg.properties.taxAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discountAmount"]) -> MetaOapg.properties.discountAmount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "quantity", "price", "total", "sku", "taxAmount", "discountAmount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantity"]) -> MetaOapg.properties.quantity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sku"]) -> typing.Union[MetaOapg.properties.sku, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxAmount"]) -> typing.Union[MetaOapg.properties.taxAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discountAmount"]) -> typing.Union[MetaOapg.properties.discountAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "quantity", "price", "total", "sku", "taxAmount", "discountAmount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, float, ],
        quantity: typing.Union[MetaOapg.properties.quantity, decimal.Decimal, int, float, ],
        price: typing.Union[MetaOapg.properties.price, decimal.Decimal, int, float, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        sku: typing.Union[MetaOapg.properties.sku, str, schemas.Unset] = schemas.unset,
        taxAmount: typing.Union[MetaOapg.properties.taxAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        discountAmount: typing.Union[MetaOapg.properties.discountAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LineItem':
        return super().__new__(
            cls,
            *args,
            total=total,
            quantity=quantity,
            price=price,
            description=description,
            sku=sku,
            taxAmount=taxAmount,
            discountAmount=discountAmount,
            _configuration=_configuration,
            **kwargs,
        )
