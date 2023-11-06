#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if not (isinstance(tuple_a, tuple) and isinstance(tuple_b, tuple)):
        return

    t_a_len = len(tuple_a)
    t_b_len = len(tuple_b)

    if t_a_len < 2:
        tuple_a = tuple_a + (0, 0)

    if t_b_len < 2:
        tuple_b = tuple_b + (0, 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
