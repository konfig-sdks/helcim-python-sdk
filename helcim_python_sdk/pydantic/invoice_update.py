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

class InvoiceUpdate(BaseModel):
    # The currency abbreviation of the invoice, such as CAD or USD. This should match currency of existing invoice.
    currency: typing.Optional[str] = Field(None, alias='currency')

    # The type of the invoice, such as ESTIMATE | INVOICE | QUOTE | ORDER | PURCHASE_ORDER | STATEMENT | REGISTRATION | CREDIT.
    type: typing.Optional[str] = Field(None, alias='type')

    # The status of invoice, such as DUE | SHIPPED | COMPLETED | CANCELLED
    status: typing.Optional[str] = Field(None, alias='status')

    billing_address: typing.Optional[Address] = Field(None, alias='billingAddress')
    class Config:
        arbitrary_types_allowed = True
