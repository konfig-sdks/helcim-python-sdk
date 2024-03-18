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


class CardToken(BaseModel):
    # The token for the card on file. If Customer Code is filled, The card should must be owned by a passed customer code
    card_token: str = Field(alias='cardToken')
    class Config:
        arbitrary_types_allowed = True
