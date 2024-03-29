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

from helcim_python_sdk.type.address import Address
from helcim_python_sdk.type.payment_request_invoice import PaymentRequestInvoice

class RequiredPaymentRequest(TypedDict):
    # IP address of the customer making the transaction, used as part of fraud detection.
    ipAddress: str

    # The currency abbreviation of the invoice, such as CAD or USD. This should match currency of existing invoice.
    currency: str

    # Amount to be processed
    amount: typing.Union[int, float]

class OptionalPaymentRequest(TypedDict, total=False):
    # Set to indicate that the transaction is e-commerce. When set, the Helcim Fraud Defender will provide further analysis.
    ecommerce: bool

    # For card transactions only. Id of the terminal you would want to use. Default terminal for of the currency will be used if you dont send this.
    terminalId: int

    # Existing customer code associated with the transaction
    customerCode: str

    # To be filled when associating transaction to existing invoice. Invoice should be associated to the same customer linked to the card
    invoiceNumber: str

    invoice: PaymentRequestInvoice

    billingAddress: Address

class PaymentRequest(RequiredPaymentRequest, OptionalPaymentRequest):
    pass
