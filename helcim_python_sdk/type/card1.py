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


class RequiredCard1(TypedDict):
    pass

class OptionalCard1(TypedDict, total=False):
    # The card holder name.
    cardHolderName: str

    # The F6L4 of card.
    cardF6L4: str

    # Card token
    cardToken: str

class Card1(RequiredCard1, OptionalCard1):
    pass