# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from helcim_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CONNECTIONTEST = "/connection-test"
    PAYMENT_PURCHASE = "/payment/purchase"
    PAYMENT_PREAUTH = "/payment/preauth"
    PAYMENT_CAPTURE = "/payment/capture"
    PAYMENT_VERIFY = "/payment/verify"
    PAYMENT_REFUND = "/payment/refund"
    PAYMENT_REVERSE = "/payment/reverse"
    PAYMENT_WITHDRAW = "/payment/withdraw"
    CARDBATCHES_CARD_BATCH_ID = "/card-batches/{cardBatchId}"
    CARDBATCHES_CARD_BATCH_ID_SETTLE = "/card-batches/{cardBatchId}/settle"
    CARDTRANSACTIONS_CARD_TRANSACTION_ID = "/card-transactions/{cardTransactionId}"
    CUSTOMERS_CUSTOMER_ID = "/customers/{customerId}"
    CUSTOMERS_CUSTOMER_ID_CARDS = "/customers/{customerId}/cards"
    CUSTOMERS_CUSTOMER_ID_CARDS_CARD_ID = "/customers/{customerId}/cards/{cardId}"
    CUSTOMERS_CUSTOMER_ID_BANKACCOUNTS = "/customers/{customerId}/bank-accounts"
    CUSTOMERS_CUSTOMER_ID_BANKACCOUNTS_BANK_ACCOUNT_ID = "/customers/{customerId}/bank-accounts/{bankAccountId}"
    CUSTOMERS_CUSTOMER_ID_BANKACCOUNTS_BANK_ACCOUNT_ID_DEFAULT = "/customers/{customerId}/bank-accounts/{bankAccountId}/default"
    INVOICES_INVOICE_ID = "/invoices/{invoiceId}"
    HELCIMPAY_INITIALIZE = "/helcim-pay/initialize"
    CARDBATCHES = "/card-batches"
    CARDTRANSACTIONS = "/card-transactions"
    CUSTOMERS = "/customers"
    INVOICES = "/invoices"
    CARDTERMINALS = "/card-terminals"
