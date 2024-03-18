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

from helcim_python_sdk.pydantic.invoice import Invoice
from helcim_python_sdk.pydantic.invoice_create import InvoiceCreate
from helcim_python_sdk.pydantic.invoice_create_after_processing import InvoiceCreateAfterProcessing
from helcim_python_sdk.pydantic.invoice_response_base import InvoiceResponseBase

GetInvoice200Response = typing.Union[InvoiceResponseBase,InvoiceCreate,InvoiceCreateAfterProcessing,Invoice]
