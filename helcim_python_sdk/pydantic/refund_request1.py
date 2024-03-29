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


class RefundRequest1(BaseModel):
    # The transaction ID of the original transaction.
    card_transaction_id: int = Field(alias='cardTransactionId')

    # IP address of the customer making the transaction, used as part of fraud detection.
    ip_address: str = Field(alias='ipAddress')

    # Set to indicate that the transaction is e-commerce. When set, the Helcim Fraud Defender will provide further analysis.
    ecommerce: typing.Optional[bool] = Field(None, alias='ecommerce')
    class Config:
        arbitrary_types_allowed = True
