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

from helcim_python_sdk.type.invoice_base import InvoiceBase
from helcim_python_sdk.type.invoice_create import InvoiceCreate
from helcim_python_sdk.type.invoice_create_after_processing import InvoiceCreateAfterProcessing

CreateInvoiceRequest = typing.Union[InvoiceBase,InvoiceCreate,InvoiceCreateAfterProcessing]
