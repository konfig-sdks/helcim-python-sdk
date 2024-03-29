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


class CheckoutInit200Response(BaseModel):
    # The checkout token is used to initialize Helcim Pay
    checkout_token: typing.Optional[str] = Field(None, alias='checkoutToken')

    # The secret token is used to validate the transaction response
    secret_token: typing.Optional[str] = Field(None, alias='secretToken')
    class Config:
        arbitrary_types_allowed = True
