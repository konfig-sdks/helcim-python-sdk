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


class RequiredRefundRequest1(TypedDict):
    # The transaction ID of the original transaction.
    cardTransactionId: int

    # IP address of the customer making the transaction, used as part of fraud detection.
    ipAddress: str

class OptionalRefundRequest1(TypedDict, total=False):
    # Set to indicate that the transaction is e-commerce. When set, the Helcim Fraud Defender will provide further analysis.
    ecommerce: bool

class RefundRequest1(RequiredRefundRequest1, OptionalRefundRequest1):
    pass
