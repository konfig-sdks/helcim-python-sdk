# coding: utf-8

"""
    The Helcim API

    This API covers publicly accessible merchant actions

    The version of the OpenAPI document: 2.0.0
    Generated by: https://konfigthis.com
"""

from helcim_python_sdk.paths.card_transactions.get import CollectTransactions
from helcim_python_sdk.paths.card_transactions_card_transaction_id.get import GetById
from helcim_python_sdk.apis.tags.card_transaction_api_raw import CardTransactionApiRaw


class CardTransactionApi(
    CollectTransactions,
    GetById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CardTransactionApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CardTransactionApiRaw(api_client)
