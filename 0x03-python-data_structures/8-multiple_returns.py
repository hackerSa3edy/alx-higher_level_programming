#!/usr/bin/python3


def multiple_returns(sentence):
    if isinstance(sentence, str):
        s_len = len(sentence)
        return (s_len, sentence[0] if sentence else None)
