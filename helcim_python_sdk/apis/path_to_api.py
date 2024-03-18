import typing_extensions

from helcim_python_sdk.paths import PathValues
from helcim_python_sdk.apis.paths.connection_test import ConnectionTest
from helcim_python_sdk.apis.paths.payment_purchase import PaymentPurchase
from helcim_python_sdk.apis.paths.payment_preauth import PaymentPreauth
from helcim_python_sdk.apis.paths.payment_capture import PaymentCapture
from helcim_python_sdk.apis.paths.payment_verify import PaymentVerify
from helcim_python_sdk.apis.paths.payment_refund import PaymentRefund
from helcim_python_sdk.apis.paths.payment_reverse import PaymentReverse
from helcim_python_sdk.apis.paths.payment_withdraw import PaymentWithdraw
from helcim_python_sdk.apis.paths.card_batches_card_batch_id import CardBatchesCardBatchId
from helcim_python_sdk.apis.paths.card_batches_card_batch_id_settle import CardBatchesCardBatchIdSettle
from helcim_python_sdk.apis.paths.card_transactions_card_transaction_id import CardTransactionsCardTransactionId
from helcim_python_sdk.apis.paths.customers_customer_id import CustomersCustomerId
from helcim_python_sdk.apis.paths.customers_customer_id_cards import CustomersCustomerIdCards
from helcim_python_sdk.apis.paths.customers_customer_id_cards_card_id import CustomersCustomerIdCardsCardId
from helcim_python_sdk.apis.paths.customers_customer_id_bank_accounts import CustomersCustomerIdBankAccounts
from helcim_python_sdk.apis.paths.customers_customer_id_bank_accounts_bank_account_id import CustomersCustomerIdBankAccountsBankAccountId
from helcim_python_sdk.apis.paths.customers_customer_id_bank_accounts_bank_account_id_default import CustomersCustomerIdBankAccountsBankAccountIdDefault
from helcim_python_sdk.apis.paths.invoices_invoice_id import InvoicesInvoiceId
from helcim_python_sdk.apis.paths.helcim_pay_initialize import HelcimPayInitialize
from helcim_python_sdk.apis.paths.card_batches import CardBatches
from helcim_python_sdk.apis.paths.card_transactions import CardTransactions
from helcim_python_sdk.apis.paths.customers import Customers
from helcim_python_sdk.apis.paths.invoices import Invoices
from helcim_python_sdk.apis.paths.card_terminals import CardTerminals

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CONNECTIONTEST: ConnectionTest,
        PathValues.PAYMENT_PURCHASE: PaymentPurchase,
        PathValues.PAYMENT_PREAUTH: PaymentPreauth,
        PathValues.PAYMENT_CAPTURE: PaymentCapture,
        PathValues.PAYMENT_VERIFY: PaymentVerify,
        PathValues.PAYMENT_REFUND: PaymentRefund,
        PathValues.PAYMENT_REVERSE: PaymentReverse,
        PathValues.PAYMENT_WITHDRAW: PaymentWithdraw,
        PathValues.CARDBATCHES_CARD_BATCH_ID: CardBatchesCardBatchId,
        PathValues.CARDBATCHES_CARD_BATCH_ID_SETTLE: CardBatchesCardBatchIdSettle,
        PathValues.CARDTRANSACTIONS_CARD_TRANSACTION_ID: CardTransactionsCardTransactionId,
        PathValues.CUSTOMERS_CUSTOMER_ID: CustomersCustomerId,
        PathValues.CUSTOMERS_CUSTOMER_ID_CARDS: CustomersCustomerIdCards,
        PathValues.CUSTOMERS_CUSTOMER_ID_CARDS_CARD_ID: CustomersCustomerIdCardsCardId,
        PathValues.CUSTOMERS_CUSTOMER_ID_BANKACCOUNTS: CustomersCustomerIdBankAccounts,
        PathValues.CUSTOMERS_CUSTOMER_ID_BANKACCOUNTS_BANK_ACCOUNT_ID: CustomersCustomerIdBankAccountsBankAccountId,
        PathValues.CUSTOMERS_CUSTOMER_ID_BANKACCOUNTS_BANK_ACCOUNT_ID_DEFAULT: CustomersCustomerIdBankAccountsBankAccountIdDefault,
        PathValues.INVOICES_INVOICE_ID: InvoicesInvoiceId,
        PathValues.HELCIMPAY_INITIALIZE: HelcimPayInitialize,
        PathValues.CARDBATCHES: CardBatches,
        PathValues.CARDTRANSACTIONS: CardTransactions,
        PathValues.CUSTOMERS: Customers,
        PathValues.INVOICES: Invoices,
        PathValues.CARDTERMINALS: CardTerminals,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CONNECTIONTEST: ConnectionTest,
        PathValues.PAYMENT_PURCHASE: PaymentPurchase,
        PathValues.PAYMENT_PREAUTH: PaymentPreauth,
        PathValues.PAYMENT_CAPTURE: PaymentCapture,
        PathValues.PAYMENT_VERIFY: PaymentVerify,
        PathValues.PAYMENT_REFUND: PaymentRefund,
        PathValues.PAYMENT_REVERSE: PaymentReverse,
        PathValues.PAYMENT_WITHDRAW: PaymentWithdraw,
        PathValues.CARDBATCHES_CARD_BATCH_ID: CardBatchesCardBatchId,
        PathValues.CARDBATCHES_CARD_BATCH_ID_SETTLE: CardBatchesCardBatchIdSettle,
        PathValues.CARDTRANSACTIONS_CARD_TRANSACTION_ID: CardTransactionsCardTransactionId,
        PathValues.CUSTOMERS_CUSTOMER_ID: CustomersCustomerId,
        PathValues.CUSTOMERS_CUSTOMER_ID_CARDS: CustomersCustomerIdCards,
        PathValues.CUSTOMERS_CUSTOMER_ID_CARDS_CARD_ID: CustomersCustomerIdCardsCardId,
        PathValues.CUSTOMERS_CUSTOMER_ID_BANKACCOUNTS: CustomersCustomerIdBankAccounts,
        PathValues.CUSTOMERS_CUSTOMER_ID_BANKACCOUNTS_BANK_ACCOUNT_ID: CustomersCustomerIdBankAccountsBankAccountId,
        PathValues.CUSTOMERS_CUSTOMER_ID_BANKACCOUNTS_BANK_ACCOUNT_ID_DEFAULT: CustomersCustomerIdBankAccountsBankAccountIdDefault,
        PathValues.INVOICES_INVOICE_ID: InvoicesInvoiceId,
        PathValues.HELCIMPAY_INITIALIZE: HelcimPayInitialize,
        PathValues.CARDBATCHES: CardBatches,
        PathValues.CARDTRANSACTIONS: CardTransactions,
        PathValues.CUSTOMERS: Customers,
        PathValues.INVOICES: Invoices,
        PathValues.CARDTERMINALS: CardTerminals,
    }
)
