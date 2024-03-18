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


class Tax(BaseModel):
    # Total Tax Amount of the Invoice
    amount: typing.Union[int, float] = Field(alias='amount')

    # Tax Details
    details: str = Field(alias='details')
    class Config:
        arbitrary_types_allowed = True
