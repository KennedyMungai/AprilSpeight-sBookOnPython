#!/usr/bin/python3

from pexpect import ExceptionPexpect
from chatbot import Chat, register_call
import wikipedia
import os
import warnings
warnings.filterwarnings("ignore")

@register_call("whoIs")
def who_is(session, query):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.summary(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "I don't know about "+query
