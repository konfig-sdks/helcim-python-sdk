<div align="center">

[![Visit Helcim](./header.png)](https://www.helcim.com&#x2F;)

# Helcim<a id="helcim"></a>

This API covers publicly accessible merchant actions


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`helcim.card_batch.get_all`](#helcimcard_batchget_all)
  * [`helcim.card_batch.get_details`](#helcimcard_batchget_details)
  * [`helcim.card_batch.settle_batch`](#helcimcard_batchsettle_batch)
  * [`helcim.card_terminal.get_all`](#helcimcard_terminalget_all)
  * [`helcim.card_transaction.collect_transactions`](#helcimcard_transactioncollect_transactions)
  * [`helcim.card_transaction.get_by_id`](#helcimcard_transactionget_by_id)
  * [`helcim.customer.create_new_customer`](#helcimcustomercreate_new_customer)
  * [`helcim.customer.get_bank_account`](#helcimcustomerget_bank_account)
  * [`helcim.customer.get_bank_accounts`](#helcimcustomerget_bank_accounts)
  * [`helcim.customer.get_card_details`](#helcimcustomerget_card_details)
  * [`helcim.customer.get_cards`](#helcimcustomerget_cards)
  * [`helcim.customer.get_customer`](#helcimcustomerget_customer)
  * [`helcim.customer.list`](#helcimcustomerlist)
  * [`helcim.customer.set_bank_account_default`](#helcimcustomerset_bank_account_default)
  * [`helcim.customer.update_details`](#helcimcustomerupdate_details)
  * [`helcim.general.test_connectivity_to_helcim_api`](#helcimgeneraltest_connectivity_to_helcim_api)
  * [`helcim.helcim_pay.create_checkout_session`](#helcimhelcim_paycreate_checkout_session)
  * [`helcim.invoice.create_new`](#helciminvoicecreate_new)
  * [`helcim.invoice.get_by_id`](#helciminvoiceget_by_id)
  * [`helcim.invoice.list`](#helciminvoicelist)
  * [`helcim.invoice.update_details`](#helciminvoiceupdate_details)
  * [`helcim.payment.process_capture_transaction`](#helcimpaymentprocess_capture_transaction)
  * [`helcim.payment.process_preauth_transaction`](#helcimpaymentprocess_preauth_transaction)
  * [`helcim.payment.process_purchase_transaction`](#helcimpaymentprocess_purchase_transaction)
  * [`helcim.payment.process_refund_transaction`](#helcimpaymentprocess_refund_transaction)
  * [`helcim.payment.process_withdrawal_transaction`](#helcimpaymentprocess_withdrawal_transaction)
  * [`helcim.payment.reverse_transaction`](#helcimpaymentreverse_transaction)
  * [`helcim.payment.verify_transaction`](#helcimpaymentverify_transaction)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Helcim&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from helcim_python_sdk import Helcim, ApiException

helcim = Helcim(
    api_access_auth="YOUR_API_KEY",
)

try:
    # Get Card Batches
    get_all_response = helcim.card_batch.get_all(
        batch_number=18900,
        terminal_id=180000,
        collect_stats="true",
    )
    print(get_all_response)
except ApiException as e:
    print("Exception when calling CardBatchApi.get_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from helcim_python_sdk import Helcim, ApiException

helcim = Helcim(
    api_access_auth="YOUR_API_KEY",
)


async def main():
    try:
        # Get Card Batches
        get_all_response = await helcim.card_batch.aget_all(
            batch_number=18900,
            terminal_id=180000,
            collect_stats="true",
        )
        print(get_all_response)
    except ApiException as e:
        print("Exception when calling CardBatchApi.get_all: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from helcim_python_sdk import Helcim, ApiException

helcim = Helcim(
    api_access_auth="YOUR_API_KEY",
)

try:
    # Get Card Batches
    get_all_response = helcim.card_batch.raw.get_all(
        batch_number=18900,
        terminal_id=180000,
        collect_stats="true",
    )
    pprint(get_all_response.body)
    pprint(get_all_response.headers)
    pprint(get_all_response.status)
    pprint(get_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling CardBatchApi.get_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `helcim.card_batch.get_all`<a id="helcimcard_batchget_all"></a>

Get Card Batches

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = helcim.card_batch.get_all(
    batch_number=18900,
    terminal_id=180000,
    collect_stats="true",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch_number: `Union[int, float]`<a id="batch_number-unionint-float"></a>

The number of the batch to retrieve. Note that this is the batch number, not batch ID.

##### terminal_id: `Union[int, float]`<a id="terminal_id-unionint-float"></a>

The terminalId of the requested batch

##### collect_stats: `str`<a id="collect_stats-str"></a>

Includes transaction statistics for the batch

#### 🔄 Return<a id="🔄-return"></a>

[`CardBatchGetAllResponse`](./helcim_python_sdk/pydantic/card_batch_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/card-batches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.card_batch.get_details`<a id="helcimcard_batchget_details"></a>

Get Card Batch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = helcim.card_batch.get_details(
    card_batch_id=1,
    collect_stats="true",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_batch_id: `int`<a id="card_batch_id-int"></a>

The Card Batch Id of the Card Batch you want to get

##### collect_stats: `str`<a id="collect_stats-str"></a>

Includes transaction statistics for the batch

#### 🔄 Return<a id="🔄-return"></a>

[`CardBatch`](./helcim_python_sdk/pydantic/card_batch.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/card-batches/{cardBatchId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.card_batch.settle_batch`<a id="helcimcard_batchsettle_batch"></a>

Settles an Open Card Batch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
settle_batch_response = helcim.card_batch.settle_batch(
    card_batch_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_batch_id: `int`<a id="card_batch_id-int"></a>

The Card Batch Id of the Card Batch you want to settle

#### 🔄 Return<a id="🔄-return"></a>

[`CardBatch`](./helcim_python_sdk/pydantic/card_batch.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/card-batches/{cardBatchId}/settle` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.card_terminal.get_all`<a id="helcimcard_terminalget_all"></a>

Get card terminals

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = helcim.card_terminal.get_all(
    currency="CAD",
    status="ACTIVE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

The abbreviation of card terminal's currency. Possible values are CAD | USD

##### status: `str`<a id="status-str"></a>

The card terminal's status. possible values are ACTIVE | INACTIVE

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardTerminalsRequest`](./helcim_python_sdk/type/card_terminals_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CardTerminalGetAllResponse`](./helcim_python_sdk/pydantic/card_terminal_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/card-terminals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.card_transaction.collect_transactions`<a id="helcimcard_transactioncollect_transactions"></a>

Collects up to 1000 Card Transactions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
collect_transactions_response = helcim.card_transaction.collect_transactions(
    date_from="2020-01-01",
    date_to="2021-01-01",
    search="500",
    customer_code="CST1000",
    invoice_number="INV1000",
    card_token="5454JK97UU1F5454",
    card_batch_id=3,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### date_from: `str`<a id="date_from-str"></a>

Filters transactions created from 2020-01-01 (Mountain Time)

##### date_to: `str`<a id="date_to-str"></a>

Filters transactions created until 2021-01-01 (Mountain Time)

##### search: `str`<a id="search-str"></a>

Searches amount, card number(F4L4 only), cardholder name, & approval codes

##### customer_code: `str`<a id="customer_code-str"></a>

The code of the customer associated with the transaction

##### invoice_number: `str`<a id="invoice_number-str"></a>

The number of the invoice associated with the transaction

##### card_token: `str`<a id="card_token-str"></a>

The token of the card associated with the transaction

##### card_batch_id: `int`<a id="card_batch_id-int"></a>

The id of the batch associated with the transaction

#### 🔄 Return<a id="🔄-return"></a>

[`CardTransactionCollectTransactionsResponse`](./helcim_python_sdk/pydantic/card_transaction_collect_transactions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/card-transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.card_transaction.get_by_id`<a id="helcimcard_transactionget_by_id"></a>

Get Card Transaction by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = helcim.card_transaction.get_by_id(
    card_transaction_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_transaction_id: `int`<a id="card_transaction_id-int"></a>

The Card Transaction Id of the Card Transaction you want to get

#### 🔄 Return<a id="🔄-return"></a>

[`SuccessfulPaymentResponse`](./helcim_python_sdk/pydantic/successful_payment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/card-transactions/{cardTransactionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.customer.create_new_customer`<a id="helcimcustomercreate_new_customer"></a>

Create customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_customer_response = helcim.customer.create_new_customer(
    customer_code="CST1000",
    contact_name="John Smith",
    business_name="Best Company",
    cell_phone="908-295-4902",
    billing_address={
        "name": "John Smith / Helcim",
        "street1": "Jump Street 21",
        "city": "Calgary",
        "province": "AB",
        "country": "CAN",
        "postal_code": "H0H0H0",
        "phone": "4031231234",
        "email": "john@example.com",
    },
    shipping_address={
        "name": "John Smith / Helcim",
        "street1": "Jump Street 21",
        "city": "Calgary",
        "province": "AB",
        "country": "CAN",
        "postal_code": "H0H0H0",
        "phone": "4031231234",
        "email": "john@example.com",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_code: `str`<a id="customer_code-str"></a>

The unique customer code. If blank, it will be automatically generated.

##### contact_name: `str`<a id="contact_name-str"></a>

The primary contact name (full name) of the customer.

##### business_name: `str`<a id="business_name-str"></a>

The business name of the customer. There must be either a contact name or business name present.

##### cell_phone: `str`<a id="cell_phone-str"></a>

The cell phone number of the customer.

##### billing_address: [`Address`](./helcim_python_sdk/type/address.py)<a id="billing_address-addresshelcim_python_sdktypeaddresspy"></a>


##### shipping_address: [`Address`](./helcim_python_sdk/type/address.py)<a id="shipping_address-addresshelcim_python_sdktypeaddresspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomerRequest`](./helcim_python_sdk/type/customer_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Customer`](./helcim_python_sdk/pydantic/customer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.customer.get_bank_account`<a id="helcimcustomerget_bank_account"></a>

Get customer bank account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bank_account_response = helcim.customer.get_bank_account(
    customer_id=1,
    bank_account_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `int`<a id="customer_id-int"></a>

The Id of the customer

##### bank_account_id: `int`<a id="bank_account_id-int"></a>

The Id of the bank account

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerGetBankAccountResponse`](./helcim_python_sdk/pydantic/customer_get_bank_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customers/{customerId}/bank-accounts/{bankAccountId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.customer.get_bank_accounts`<a id="helcimcustomerget_bank_accounts"></a>

Get customer bank accounts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_bank_accounts_response = helcim.customer.get_bank_accounts(
    customer_id=1,
    bank_token="string_example",
    verified=3.14,
    ready=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `int`<a id="customer_id-int"></a>

The Id of the customer

##### bank_token: `str`<a id="bank_token-str"></a>

The bank account token.

##### verified: `Union[int, float]`<a id="verified-unionint-float"></a>

Check if bank account is verified or not. use 1 or 0.

##### ready: `Union[int, float]`<a id="ready-unionint-float"></a>

Check if bank account is ready or not. use 1 or 0.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerGetBankAccountsResponse`](./helcim_python_sdk/pydantic/customer_get_bank_accounts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customers/{customerId}/bank-accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.customer.get_card_details`<a id="helcimcustomerget_card_details"></a>

Get customer card

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_card_details_response = helcim.customer.get_card_details(
    customer_id=1,
    card_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `int`<a id="customer_id-int"></a>

The Id of the customer

##### card_id: `int`<a id="card_id-int"></a>

The Id of the card

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerGetCardDetailsResponse`](./helcim_python_sdk/pydantic/customer_get_card_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customers/{customerId}/cards/{cardId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.customer.get_cards`<a id="helcimcustomerget_cards"></a>

Get customer cards

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cards_response = helcim.customer.get_cards(
    customer_id=1,
    card_token="907af81acc0224e0134949",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `int`<a id="customer_id-int"></a>

The Id of the customer

##### card_token: `str`<a id="card_token-str"></a>

The card token.

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerGetCardsResponse`](./helcim_python_sdk/pydantic/customer_get_cards_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customers/{customerId}/cards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.customer.get_customer`<a id="helcimcustomerget_customer"></a>

Get customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_customer_response = helcim.customer.get_customer(
    customer_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `int`<a id="customer_id-int"></a>

The Id of the customer

#### 🔄 Return<a id="🔄-return"></a>

[`Customer`](./helcim_python_sdk/pydantic/customer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customers/{customerId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.customer.list`<a id="helcimcustomerlist"></a>

Get customers

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = helcim.customer.list(
    search="john",
    customer_code="CST1000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### search: `str`<a id="search-str"></a>

The search term to be used for partial matching on contactName, businessName, customerCode, city, phone and email (Only use one query field per request).

##### customer_code: `str`<a id="customer_code-str"></a>

Existing customer code (Only use one query field per request).

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerListResponse`](./helcim_python_sdk/pydantic/customer_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.customer.set_bank_account_default`<a id="helcimcustomerset_bank_account_default"></a>

Set customer bank account as default

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_bank_account_default_response = helcim.customer.set_bank_account_default(
    customer_id=1,
    bank_account_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `int`<a id="customer_id-int"></a>

The Id of the customer

##### bank_account_id: `int`<a id="bank_account_id-int"></a>

The Id of the bank account

#### 🔄 Return<a id="🔄-return"></a>

[`CustomerSetBankAccountDefaultResponse`](./helcim_python_sdk/pydantic/customer_set_bank_account_default_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customers/{customerId}/bank-accounts/{bankAccountId}/default` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.customer.update_details`<a id="helcimcustomerupdate_details"></a>

Update customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_details_response = helcim.customer.update_details(
    customer_id="customerId_example",
    customer_code="CST1000",
    contact_name="John Smith",
    business_name="Best Company",
    cell_phone="908-295-4902",
    billing_address={
        "name": "John Smith / Helcim",
        "street1": "Jump Street 21",
        "city": "Calgary",
        "province": "AB",
        "country": "CAN",
        "postal_code": "H0H0H0",
        "phone": "4031231234",
        "email": "john@example.com",
    },
    shipping_address={
        "name": "John Smith / Helcim",
        "street1": "Jump Street 21",
        "city": "Calgary",
        "province": "AB",
        "country": "CAN",
        "postal_code": "H0H0H0",
        "phone": "4031231234",
        "email": "john@example.com",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

The Id of the customer

##### customer_code: `str`<a id="customer_code-str"></a>

The unique customer code.

##### contact_name: `str`<a id="contact_name-str"></a>

The primary contact name (full name) of the customer.

##### business_name: `str`<a id="business_name-str"></a>

The business name of the customer. There must be either a contact name or business name present.

##### cell_phone: `str`<a id="cell_phone-str"></a>

The cell phone number of the customer.

##### billing_address: [`Address`](./helcim_python_sdk/type/address.py)<a id="billing_address-addresshelcim_python_sdktypeaddresspy"></a>


##### shipping_address: [`Address`](./helcim_python_sdk/type/address.py)<a id="shipping_address-addresshelcim_python_sdktypeaddresspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CustomerUpdateRequest`](./helcim_python_sdk/type/customer_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Customer`](./helcim_python_sdk/pydantic/customer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/customers/{customerId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.general.test_connectivity_to_helcim_api`<a id="helcimgeneraltest_connectivity_to_helcim_api"></a>

Tests connectivity to the Helcim API

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
test_connectivity_to_helcim_api_response = (
    helcim.general.test_connectivity_to_helcim_api()
)
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/connection-test` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.helcim_pay.create_checkout_session`<a id="helcimhelcim_paycreate_checkout_session"></a>

Creates a HelcimPay.js Checkout Session

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_checkout_session_response = helcim.helcim_pay.create_checkout_session(
    payment_type="purchase",
    amount=100,
    currency="CAD",
    customer_code="CST1000",
    invoice_number="INV1000",
    payment_method="cc-ach",
    allow_partial=1,
    has_convenience_fee=1,
    tax_amount=3.67,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_type: `str`<a id="payment_type-str"></a>

Payment Type. Valid payment types are purchase | preauth | verify

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The amount of the transaction to be processed

##### currency: `str`<a id="currency-str"></a>

Currency abbreviation. CAD | USD

##### customer_code: `str`<a id="customer_code-str"></a>

This is the code of an existing customer in Helcim associated with this checkout

##### invoice_number: `str`<a id="invoice_number-str"></a>

This is the number of an existing invoice in Helcim associated with this checkout

##### payment_method: `str`<a id="payment_method-str"></a>

This is the payment method (credit card, ACH) that customer can use to pay the amount. cc | ach | cc-ach

##### allow_partial: `Union[int, float]`<a id="allow_partial-unionint-float"></a>

This is used to determine whether the partial payment UI will be displayed to the customer

##### has_convenience_fee: `Union[int, float]`<a id="has_convenience_fee-unionint-float"></a>

This is used to apply the convenience fee rate to credit card transaction should customer chooses this payment method

##### tax_amount: `Union[int, float]`<a id="tax_amount-unionint-float"></a>

This is used to enable level 2 processing lower rates. The value should be the dollar amount of the tax to 2 decimal places.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HelcimPayInitializeRequest`](./helcim_python_sdk/type/helcim_pay_initialize_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckoutInit200Response`](./helcim_python_sdk/pydantic/checkout_init200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/helcim-pay/initialize` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.invoice.create_new`<a id="helciminvoicecreate_new"></a>

Create invoice

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_response = helcim.invoice.create_new(
    body=None,
    invoice_number="",
    tip_amount=0.99,
    deposit_amount=1,
    notes="No vegetables please",
    customer_id=123123,
    currency="CAD",
    type="INVOICE",
    status="DUE",
    billing_address={
        "name": "John Smith / Helcim",
        "street1": "Jump Street 21",
        "city": "Calgary",
        "province": "AB",
        "country": "CAN",
        "postal_code": "H0H0H0",
        "phone": "4031231234",
        "email": "john@example.com",
    },
    shipping={
        "amount": 10.99,
        "details": "Canada Post 1 day shipping",
        "address": {
            "name": "John Smith / Helcim",
            "street1": "Jump Street 21",
            "city": "Calgary",
            "province": "AB",
            "country": "CAN",
            "postal_code": "H0H0H0",
            "phone": "4031231234",
            "email": "john@example.com",
        },
    },
    pickup={
        "date": "2022-01-25 13:55:55",
        "name": "Jane Smith",
    },
    tax={
        "amount": 5.99,
        "details": "GST 5%",
    },
    discount={
        "amount": 10.99,
        "details": "DISC100",
    },
    line_items=[
        {
            "description": "Red Hat",
            "sku": "ITM1434",
            "quantity": 10.5,
            "price": 10.55,
            "total": 110.78,
            "tax_amount": 0,
            "discount_amount": 0,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_number: `str`<a id="invoice_number-str"></a>

Invoice number of invoice to be created. Will be generated if blank

##### tip_amount: `Union[int, float]`<a id="tip_amount-unionint-float"></a>

Tip amount

##### deposit_amount: `Union[int, float]`<a id="deposit_amount-unionint-float"></a>

Deposit amount

##### notes: `str`<a id="notes-str"></a>

Comment to appear at the bottom of the invoice, visible to the customer.

##### customer_id: `int`<a id="customer_id-int"></a>

Unique customer Id.

##### currency: `str`<a id="currency-str"></a>

The currency abbreviation of the invoice, such as CAD or USD. This should match currency of existing invoice.

##### type: `str`<a id="type-str"></a>

The type of the invoice, such as ESTIMATE | INVOICE | QUOTE | ORDER | PURCHASE_ORDER | STATEMENT | REGISTRATION | CREDIT.

##### status: `str`<a id="status-str"></a>

The status of invoice, such as DUE | SHIPPED | COMPLETED | CANCELLED

##### billing_address: [`Address`](./helcim_python_sdk/type/address.py)<a id="billing_address-addresshelcim_python_sdktypeaddresspy"></a>


##### shipping: [`Shipping`](./helcim_python_sdk/type/shipping.py)<a id="shipping-shippinghelcim_python_sdktypeshippingpy"></a>


##### pickup: [`Pickup`](./helcim_python_sdk/type/pickup.py)<a id="pickup-pickuphelcim_python_sdktypepickuppy"></a>


##### tax: [`Tax`](./helcim_python_sdk/type/tax.py)<a id="tax-taxhelcim_python_sdktypetaxpy"></a>


##### discount: [`Discount`](./helcim_python_sdk/type/discount.py)<a id="discount-discounthelcim_python_sdktypediscountpy"></a>


##### line_items: List[`LineItem`]<a id="line_items-listlineitem"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateInvoiceRequest`](./helcim_python_sdk/type/create_invoice_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateInvoice200Response`](./helcim_python_sdk/pydantic/create_invoice200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invoices` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.invoice.get_by_id`<a id="helciminvoiceget_by_id"></a>

Get invoice

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = helcim.invoice.get_by_id(
    invoice_id="invoiceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_id: `str`<a id="invoice_id-str"></a>

The unique invoice Id

#### 🔄 Return<a id="🔄-return"></a>

[`GetInvoice200Response`](./helcim_python_sdk/pydantic/get_invoice200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invoices/{invoiceId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.invoice.list`<a id="helciminvoicelist"></a>

Get invoices

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = helcim.invoice.list(
    invoice_number="INV1000",
    date_start="2020-01-01",
    date_end="2021-01-01",
    with_convenience_fee=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_number: `str`<a id="invoice_number-str"></a>

The number of the invoice associated with the transaction

##### date_start: `str`<a id="date_start-str"></a>

Filters transactions created from 2020-01-01 (Mountain Time)

##### date_end: `str`<a id="date_end-str"></a>

Filters transactions created until 2021-01-01 (Mountain Time)

##### with_convenience_fee: `int`<a id="with_convenience_fee-int"></a>

Include convenience fee of each invoice 0 | 1

#### 🔄 Return<a id="🔄-return"></a>

[`InvoiceListResponse`](./helcim_python_sdk/pydantic/invoice_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invoices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.invoice.update_details`<a id="helciminvoiceupdate_details"></a>

Update invoice

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_details_response = helcim.invoice.update_details(
    body=None,
    invoice_id="invoiceId_example",
    invoice_number="",
    tip_amount=0.99,
    deposit_amount=1,
    notes="No vegetables please",
    currency="CAD",
    type="INVOICE",
    status="DUE",
    billing_address={
        "name": "John Smith / Helcim",
        "street1": "Jump Street 21",
        "city": "Calgary",
        "province": "AB",
        "country": "CAN",
        "postal_code": "H0H0H0",
        "phone": "4031231234",
        "email": "john@example.com",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_id: `str`<a id="invoice_id-str"></a>

The unique invoice Id

##### invoice_number: `str`<a id="invoice_number-str"></a>

Invoice number of invoice to be created. Will be generated if blank

##### tip_amount: `Union[int, float]`<a id="tip_amount-unionint-float"></a>

Tip amount

##### deposit_amount: `Union[int, float]`<a id="deposit_amount-unionint-float"></a>

Deposit amount

##### notes: `str`<a id="notes-str"></a>

Comment to appear at the bottom of the invoice, visible to the customer.

##### currency: `str`<a id="currency-str"></a>

The currency abbreviation of the invoice, such as CAD or USD. This should match currency of existing invoice.

##### type: `str`<a id="type-str"></a>

The type of the invoice, such as ESTIMATE | INVOICE | QUOTE | ORDER | PURCHASE_ORDER | STATEMENT | REGISTRATION | CREDIT.

##### status: `str`<a id="status-str"></a>

The status of invoice, such as DUE | SHIPPED | COMPLETED | CANCELLED

##### billing_address: [`Address`](./helcim_python_sdk/type/address.py)<a id="billing_address-addresshelcim_python_sdktypeaddresspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateInvoiceRequest`](./helcim_python_sdk/type/update_invoice_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GetInvoice200Response`](./helcim_python_sdk/pydantic/get_invoice200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/invoices/{invoiceId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.payment.process_capture_transaction`<a id="helcimpaymentprocess_capture_transaction"></a>

Process Capture Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
process_capture_transaction_response = helcim.payment.process_capture_transaction(
    pre_auth_transaction_id=198763,
    amount=100.99,
    ip_address="192.168.1.1",
    idempotency_key="idempotency-key_example",
    ecommerce=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pre_auth_transaction_id: `int`<a id="pre_auth_transaction_id-int"></a>

The transaction ID of the original pre-authorization transaction.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The amount to capture. Must be less or equal to the original pre-authorization amount.

##### ip_address: `str`<a id="ip_address-str"></a>

IP address of the customer making the transaction, used as part of fraud detection.

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

Idempotency Key. Alphanumeric 25-characters

##### ecommerce: `bool`<a id="ecommerce-bool"></a>

Set to indicate that the transaction is e-commerce. When set, the Helcim Fraud Defender will provide further analysis.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CaptureRequest`](./helcim_python_sdk/type/capture_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SuccessfulPaymentResponse`](./helcim_python_sdk/pydantic/successful_payment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/capture` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.payment.process_preauth_transaction`<a id="helcimpaymentprocess_preauth_transaction"></a>

Process Preauth Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
process_preauth_transaction_response = helcim.payment.process_preauth_transaction(
    body=None,
    idempotency_key="idempotency-key_example",
    ip_address="192.168.1.1",
    ecommerce=True,
    terminal_id=3215,
    currency="CAD",
    amount=100.99,
    customer_code="",
    invoice_number="",
    invoice=None,
    billing_address={
        "name": "John Smith / Helcim",
        "street1": "Jump Street 21",
        "city": "Calgary",
        "province": "AB",
        "country": "CAN",
        "postal_code": "H0H0H0",
        "phone": "4031231234",
        "email": "john@example.com",
    },
    card_data=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

Idempotency Key. Alphanumeric 25-characters

##### ip_address: `str`<a id="ip_address-str"></a>

IP address of the customer making the transaction, used as part of fraud detection.

##### ecommerce: `bool`<a id="ecommerce-bool"></a>

Set to indicate that the transaction is e-commerce. When set, the Helcim Fraud Defender will provide further analysis.

##### terminal_id: `int`<a id="terminal_id-int"></a>

For card transactions only. Id of the terminal you would want to use. Default terminal for of the currency will be used if you dont send this.

##### currency: `str`<a id="currency-str"></a>

The currency abbreviation of the invoice, such as CAD or USD. This should match currency of existing invoice.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount to be processed

##### customer_code: `str`<a id="customer_code-str"></a>

Existing customer code associated with the transaction

##### invoice_number: `str`<a id="invoice_number-str"></a>

To be filled when associating transaction to existing invoice. Invoice should be associated to the same customer linked to the card

##### invoice: [`PaymentRequestInvoice`](./helcim_python_sdk/type/payment_request_invoice.py)<a id="invoice-paymentrequestinvoicehelcim_python_sdktypepayment_request_invoicepy"></a>


##### billing_address: [`Address`](./helcim_python_sdk/type/address.py)<a id="billing_address-addresshelcim_python_sdktypeaddresspy"></a>


##### card_data: `CardDataCardData`<a id="card_data-carddatacarddata"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PurchaseRequest`](./helcim_python_sdk/type/purchase_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SuccessfulPaymentResponse`](./helcim_python_sdk/pydantic/successful_payment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/preauth` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.payment.process_purchase_transaction`<a id="helcimpaymentprocess_purchase_transaction"></a>

Process Purchase Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
process_purchase_transaction_response = helcim.payment.process_purchase_transaction(
    body=None,
    idempotency_key="idempotency-key_example",
    ip_address="192.168.1.1",
    ecommerce=True,
    terminal_id=3215,
    currency="CAD",
    amount=100.99,
    customer_code="",
    invoice_number="",
    invoice=None,
    billing_address={
        "name": "John Smith / Helcim",
        "street1": "Jump Street 21",
        "city": "Calgary",
        "province": "AB",
        "country": "CAN",
        "postal_code": "H0H0H0",
        "phone": "4031231234",
        "email": "john@example.com",
    },
    card_data=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

Idempotency Key. Alphanumeric 25-characters

##### ip_address: `str`<a id="ip_address-str"></a>

IP address of the customer making the transaction, used as part of fraud detection.

##### ecommerce: `bool`<a id="ecommerce-bool"></a>

Set to indicate that the transaction is e-commerce. When set, the Helcim Fraud Defender will provide further analysis.

##### terminal_id: `int`<a id="terminal_id-int"></a>

For card transactions only. Id of the terminal you would want to use. Default terminal for of the currency will be used if you dont send this.

##### currency: `str`<a id="currency-str"></a>

The currency abbreviation of the invoice, such as CAD or USD. This should match currency of existing invoice.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount to be processed

##### customer_code: `str`<a id="customer_code-str"></a>

Existing customer code associated with the transaction

##### invoice_number: `str`<a id="invoice_number-str"></a>

To be filled when associating transaction to existing invoice. Invoice should be associated to the same customer linked to the card

##### invoice: [`PaymentRequestInvoice`](./helcim_python_sdk/type/payment_request_invoice.py)<a id="invoice-paymentrequestinvoicehelcim_python_sdktypepayment_request_invoicepy"></a>


##### billing_address: [`Address`](./helcim_python_sdk/type/address.py)<a id="billing_address-addresshelcim_python_sdktypeaddresspy"></a>


##### card_data: `CardDataCardData`<a id="card_data-carddatacarddata"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PurchaseRequest`](./helcim_python_sdk/type/purchase_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SuccessfulPaymentResponse`](./helcim_python_sdk/pydantic/successful_payment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/purchase` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.payment.process_refund_transaction`<a id="helcimpaymentprocess_refund_transaction"></a>

Process Refund Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
process_refund_transaction_response = helcim.payment.process_refund_transaction(
    original_transaction_id=198763,
    amount=100.99,
    ip_address="192.168.1.1",
    idempotency_key="idempotency-key_example",
    ecommerce=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### original_transaction_id: `int`<a id="original_transaction_id-int"></a>

The transaction ID of the purchase/capture transaction.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The amount to refund. Must be less or equal to the original purchase/capture amount.

##### ip_address: `str`<a id="ip_address-str"></a>

IP address of the customer making the transaction, used as part of fraud detection.

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

Idempotency Key. Alphanumeric 25-characters

##### ecommerce: `bool`<a id="ecommerce-bool"></a>

Set to indicate that the transaction is e-commerce. When set, the Helcim Fraud Defender will provide further analysis.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RefundRequest`](./helcim_python_sdk/type/refund_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SuccessfulPaymentResponse`](./helcim_python_sdk/pydantic/successful_payment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/refund` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.payment.process_withdrawal_transaction`<a id="helcimpaymentprocess_withdrawal_transaction"></a>

Process Withdraw Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
process_withdrawal_transaction_response = helcim.payment.process_withdrawal_transaction(
    body=None,
    idempotency_key="idempotency-key_example",
    ip_address="192.168.1.1",
    ecommerce=True,
    terminal_id=3215,
    currency="CAD",
    amount=100.99,
    customer_code="",
    invoice_number="",
    invoice=None,
    billing_address={
        "name": "John Smith / Helcim",
        "street1": "Jump Street 21",
        "city": "Calgary",
        "province": "AB",
        "country": "CAN",
        "postal_code": "H0H0H0",
        "phone": "4031231234",
        "email": "john@example.com",
    },
    bank_data=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

Idempotency Key. Alphanumeric 25-characters

##### ip_address: `str`<a id="ip_address-str"></a>

IP address of the customer making the transaction, used as part of fraud detection.

##### ecommerce: `bool`<a id="ecommerce-bool"></a>

Set to indicate that the transaction is e-commerce. When set, the Helcim Fraud Defender will provide further analysis.

##### terminal_id: `int`<a id="terminal_id-int"></a>

For card transactions only. Id of the terminal you would want to use. Default terminal for of the currency will be used if you dont send this.

##### currency: `str`<a id="currency-str"></a>

The currency abbreviation of the invoice, such as CAD or USD. This should match currency of existing invoice.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

Amount to be processed

##### customer_code: `str`<a id="customer_code-str"></a>

Existing customer code associated with the transaction

##### invoice_number: `str`<a id="invoice_number-str"></a>

To be filled when associating transaction to existing invoice. Invoice should be associated to the same customer linked to the card

##### invoice: [`PaymentRequestInvoice`](./helcim_python_sdk/type/payment_request_invoice.py)<a id="invoice-paymentrequestinvoicehelcim_python_sdktypepayment_request_invoicepy"></a>


##### billing_address: [`Address`](./helcim_python_sdk/type/address.py)<a id="billing_address-addresshelcim_python_sdktypeaddresspy"></a>


##### bank_data: `BankDataBankData`<a id="bank_data-bankdatabankdata"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WithdrawRequest`](./helcim_python_sdk/type/withdraw_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SuccessfulAchTransactionResponse`](./helcim_python_sdk/pydantic/successful_ach_transaction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/withdraw` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.payment.reverse_transaction`<a id="helcimpaymentreverse_transaction"></a>

Process Reverse Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
reverse_transaction_response = helcim.payment.reverse_transaction(
    card_transaction_id=198763,
    ip_address="192.168.1.1",
    idempotency_key="idempotency-key_example",
    ecommerce=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_transaction_id: `int`<a id="card_transaction_id-int"></a>

The transaction ID of the original transaction.

##### ip_address: `str`<a id="ip_address-str"></a>

IP address of the customer making the transaction, used as part of fraud detection.

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

Idempotency Key. Alphanumeric 25-characters

##### ecommerce: `bool`<a id="ecommerce-bool"></a>

Set to indicate that the transaction is e-commerce. When set, the Helcim Fraud Defender will provide further analysis.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RefundRequest1`](./helcim_python_sdk/type/refund_request1.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/reverse` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `helcim.payment.verify_transaction`<a id="helcimpaymentverify_transaction"></a>

Process Verify Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_transaction_response = helcim.payment.verify_transaction(
    ip_address="192.168.1.1",
    currency="CAD",
    card_data={
        "card_number": "5454545454545454",
        "card_expiry": "1257",
        "card_cvv": "100",
    },
    billing_address={
        "name": "John Smith / Helcim",
        "street1": "Jump Street 21",
        "city": "Calgary",
        "province": "AB",
        "country": "CAN",
        "postal_code": "H0H0H0",
        "phone": "4031231234",
        "email": "john@example.com",
    },
    idempotency_key="idempotency-key_example",
    ecommerce=True,
    customer_code="",
    invoice_number="",
    invoice=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ip_address: `str`<a id="ip_address-str"></a>

IP address of the customer making the transaction, used as part of fraud detection.

##### currency: `str`<a id="currency-str"></a>

The currency abbreviation of the transaction.

##### card_data: [`Card`](./helcim_python_sdk/type/card.py)<a id="card_data-cardhelcim_python_sdktypecardpy"></a>


##### billing_address: [`Address`](./helcim_python_sdk/type/address.py)<a id="billing_address-addresshelcim_python_sdktypeaddresspy"></a>


##### idempotency_key: `str`<a id="idempotency_key-str"></a>

Idempotency Key. Alphanumeric 25-characters

##### ecommerce: `bool`<a id="ecommerce-bool"></a>

Set to indicate that the transaction is e-commerce. When set, the Helcim Fraud Defender will provide further analysis.

##### customer_code: `str`<a id="customer_code-str"></a>

Existing customer code associated with the transaction

##### invoice_number: `str`<a id="invoice_number-str"></a>

To be filled when associating transaction to existing invoice. Invoice should be associated to the same customer linked to the card

##### invoice: [`VerifyRequestInvoice`](./helcim_python_sdk/type/verify_request_invoice.py)<a id="invoice-verifyrequestinvoicehelcim_python_sdktypeverify_request_invoicepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`VerifyRequest`](./helcim_python_sdk/type/verify_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SuccessfulPaymentResponse`](./helcim_python_sdk/pydantic/successful_payment_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payment/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
