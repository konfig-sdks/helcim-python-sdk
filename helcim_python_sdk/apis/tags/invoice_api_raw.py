# coding: utf-8

"""
    The Helcim API

    This API covers publicly accessible merchant actions

    The version of the OpenAPI document: 2.0.0
    Generated by: https://konfigthis.com
"""

from helcim_python_sdk.paths.invoices.post import CreateNewRaw
from helcim_python_sdk.paths.invoices_invoice_id.get import GetByIdRaw
from helcim_python_sdk.paths.invoices.get import ListRaw
from helcim_python_sdk.paths.invoices_invoice_id.put import UpdateDetailsRaw


class InvoiceApiRaw(
    CreateNewRaw,
    GetByIdRaw,
    ListRaw,
    UpdateDetailsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
