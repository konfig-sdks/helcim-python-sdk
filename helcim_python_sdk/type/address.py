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


class RequiredAddress(TypedDict):
    # Contact Name or Business Name
    name: str

    street1: str

    postalCode: str

class OptionalAddress(TypedDict, total=False):
    street2: str

    city: str

    # 2 letter abbreviation of the province(AB, BC, CA). Required field if country is CAN or USA.
    province: str

    # 3-letter abbreviation of the country(CAN, USA)
    country: str

    # 10 to 15 digits phone number.
    phone: str

    email: str

class Address(RequiredAddress, OptionalAddress):
    pass
