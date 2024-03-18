# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from helcim_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    CUSTOMER = "Customer"
    PAYMENT = "Payment"
    INVOICE = "Invoice"
    CARD_BATCH = "Card Batch"
    CARD_TRANSACTION = "Card Transaction"
    GENERAL = "General"
    CARD_TERMINAL = "Card Terminal"
    HELCIM_PAY = "Helcim Pay"
    TODO = "TODO"
