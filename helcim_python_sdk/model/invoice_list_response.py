# coding: utf-8

"""
    The Helcim API

    This API covers publicly accessible merchant actions

    The version of the OpenAPI document: 2.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from helcim_python_sdk import schemas  # noqa: F401


class InvoiceListResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['GetInvoices200ResponseInner']:
            return GetInvoices200ResponseInner

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['GetInvoices200ResponseInner'], typing.List['GetInvoices200ResponseInner']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'InvoiceListResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'GetInvoices200ResponseInner':
        return super().__getitem__(i)

from helcim_python_sdk.model.get_invoices200_response_inner import GetInvoices200ResponseInner
