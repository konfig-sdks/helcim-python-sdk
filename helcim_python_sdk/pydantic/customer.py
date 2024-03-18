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

from helcim_python_sdk.pydantic.address import Address
from helcim_python_sdk.pydantic.card1 import Card1

class Customer(BaseModel):
    # Id of Customer
    id: typing.Optional[int] = Field(None, alias='id')

    # Customer code of the customer
    customer_code: typing.Optional[str] = Field(None, alias='customerCode')

    # Name of the business
    business_name: typing.Optional[str] = Field(None, alias='businessName')

    # Contact Name
    contact_name: typing.Optional[str] = Field(None, alias='contactName')

    # Cell phone number of customer
    cell_phone: typing.Optional[str] = Field(None, alias='cellPhone')

    billing_address: typing.Optional[Address] = Field(None, alias='billingAddress')

    shipping_address: typing.Optional[Address] = Field(None, alias='shippingAddress')

    # Array of cards stored in the vault associated with this customer.
    cards: typing.Optional[typing.List[Card1]] = Field(None, alias='cards')
    class Config:
        arbitrary_types_allowed = True