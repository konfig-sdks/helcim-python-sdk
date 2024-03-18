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


class RequiredDiscount(TypedDict):
    # Total Discount Amount of the Invoice
    amount: typing.Union[int, float]

    # Discount Details/Code
    details: str

class OptionalDiscount(TypedDict, total=False):
    pass

class Discount(RequiredDiscount, OptionalDiscount):
    pass