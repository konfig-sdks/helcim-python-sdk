# coding: utf-8

"""
    The Helcim API

    This API covers publicly accessible merchant actions

    The version of the OpenAPI document: 2.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from helcim_python_sdk.pydantic.discount import Discount
from helcim_python_sdk.pydantic.line_item import LineItem
from helcim_python_sdk.pydantic.pickup import Pickup
from helcim_python_sdk.pydantic.shipping import Shipping
from helcim_python_sdk.pydantic.tax import Tax

class InvoiceCreateAfterProcessing(BaseModel):
    shipping: typing.Optional[Shipping] = Field(None, alias='shipping')

    pickup: typing.Optional[Pickup] = Field(None, alias='pickup')

    tax: typing.Optional[Tax] = Field(None, alias='tax')

    discount: typing.Optional[Discount] = Field(None, alias='discount')

    line_items: typing.Optional[typing.List[LineItem]] = Field(None, alias='lineItems')
    class Config:
        arbitrary_types_allowed = True
