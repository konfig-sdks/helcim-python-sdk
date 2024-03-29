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


class RequiredInvoiceBase(TypedDict):
    pass

class OptionalInvoiceBase(TypedDict, total=False):
    # Invoice number of invoice to be created. Will be generated if blank
    invoiceNumber: str

    # Tip amount
    tipAmount: typing.Union[int, float]

    # Deposit amount
    depositAmount: typing.Union[int, float]

    # Comment to appear at the bottom of the invoice, visible to the customer.
    notes: str

class InvoiceBase(RequiredInvoiceBase, OptionalInvoiceBase):
    pass
