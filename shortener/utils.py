from random import choice
import string

from django.conf import settings


def get_unique_short_url(
    alphabet=string.ascii_lowercase+string.digits,
    short_url_length=settings.SHORT_URL_LENGTH
):
    # result = ""
    # for _ in range(short_url_length):
    #     result += choice(alphabet)
    # return result
    return "".join([
        choice(alphabet) for _ in range(short_url_length)
    ])

