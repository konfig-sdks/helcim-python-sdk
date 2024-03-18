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


class RequiredHelcimPayInitializeRequest(TypedDict):
    # Payment Type. Valid payment types are purchase | preauth | verify
    paymentType: str

    # The amount of the transaction to be processed
    amount: typing.Union[int, float]

    # Currency abbreviation. CAD | USD
    currency: str

class OptionalHelcimPayInitializeRequest(TypedDict, total=False):
    # This is the code of an existing customer in Helcim associated with this checkout
    customerCode: str

    # This is the number of an existing invoice in Helcim associated with this checkout
    invoiceNumber: str

    # This is the payment method (credit card, ACH) that customer can use to pay the amount. cc | ach | cc-ach
    paymentMethod: str

    # This is used to determine whether the partial payment UI will be displayed to the customer
    allowPartial: typing.Union[int, float]

    # This is used to apply the convenience fee rate to credit card transaction should customer chooses this payment method
    hasConvenienceFee: typing.Union[int, float]

    # This is used to enable level 2 processing lower rates. The value should be the dollar amount of the tax to 2 decimal places.
    taxAmount: typing.Union[int, float]

class HelcimPayInitializeRequest(RequiredHelcimPayInitializeRequest, OptionalHelcimPayInitializeRequest):
    pass
