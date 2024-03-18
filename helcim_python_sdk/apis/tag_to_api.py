import typing_extensions

from helcim_python_sdk.apis.tags import TagValues
from helcim_python_sdk.apis.tags.customer_api import CustomerApi
from helcim_python_sdk.apis.tags.payment_api import PaymentApi
from helcim_python_sdk.apis.tags.invoice_api import InvoiceApi
from helcim_python_sdk.apis.tags.card_batch_api import CardBatchApi
from helcim_python_sdk.apis.tags.card_transaction_api import CardTransactionApi
from helcim_python_sdk.apis.tags.general_api import GeneralApi
from helcim_python_sdk.apis.tags.card_terminal_api import CardTerminalApi
from helcim_python_sdk.apis.tags.helcim_pay_api import HelcimPayApi
from helcim_python_sdk.apis.tags.todo_api import TODOApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CUSTOMER: CustomerApi,
        TagValues.PAYMENT: PaymentApi,
        TagValues.INVOICE: InvoiceApi,
        TagValues.CARD_BATCH: CardBatchApi,
        TagValues.CARD_TRANSACTION: CardTransactionApi,
        TagValues.GENERAL: GeneralApi,
        TagValues.CARD_TERMINAL: CardTerminalApi,
        TagValues.HELCIM_PAY: HelcimPayApi,
        TagValues.TODO: TODOApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CUSTOMER: CustomerApi,
        TagValues.PAYMENT: PaymentApi,
        TagValues.INVOICE: InvoiceApi,
        TagValues.CARD_BATCH: CardBatchApi,
        TagValues.CARD_TRANSACTION: CardTransactionApi,
        TagValues.GENERAL: GeneralApi,
        TagValues.CARD_TERMINAL: CardTerminalApi,
        TagValues.HELCIM_PAY: HelcimPayApi,
        TagValues.TODO: TODOApi,
    }
)
