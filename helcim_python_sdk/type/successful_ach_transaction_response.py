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


class RequiredSuccessfulAchTransactionResponse(TypedDict):
    pass

class OptionalSuccessfulAchTransactionResponse(TypedDict, total=False):
    # The transaction id
    transactionId: typing.Union[int, float]

    # The id of associated card batch
    batchId: typing.Union[int, float]

    # The date(Mountain Time) when the transaction is created.
    dateCreated: str

    # The status of the transaction. possible values are APPROVED | DECLINED | IN_PROGRESS | CANCELLED | PENDING
    statusAuth: str

    # The status of the transaction. possible values are OPENED | CLEARED | REJECTED | CONTESTED | RETURNED
    statusClearing: str

    # The type of the transaction. possible values are WITHDRAWAL | DEPOSIT | SETTLE | REVERSE | REFUND
    type: str

    # The amount of processed transaction
    amount: typing.Union[int, float]

    # The abbreviation of the transaction's currency
    currency: str

    # Approval Code
    approvalCode: str

    # Bank account number
    bankAccountNumber: str

    # Bank Token associated with bankAccount
    bankToken: str

    # Invoice number associated to the transaction
    invoiceNumber: str

class SuccessfulAchTransactionResponse(RequiredSuccessfulAchTransactionResponse, OptionalSuccessfulAchTransactionResponse):
    pass