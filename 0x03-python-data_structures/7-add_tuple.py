#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)
# checking for tuple_a we have that:
    if lenA < 1:
        tuple_a = (0, 0)
    elif lenA < 2:
        tuple_a = (tuple_a[0], 0)

# checking for tuple_b, we have:
    if lenB < 1:
        tuple_b = (0, 0)
    elif lenB < 2:
        tuple_b = (tuple_b[0], 0)

add_result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
return add_result
