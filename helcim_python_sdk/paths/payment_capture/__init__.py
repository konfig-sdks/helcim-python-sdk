# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from helcim_python_sdk.paths.payment_capture import Api

from helcim_python_sdk.paths import PathValues

path = PathValues.PAYMENT_CAPTURE