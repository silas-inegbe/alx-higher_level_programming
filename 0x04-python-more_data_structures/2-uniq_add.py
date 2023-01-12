#!/usr/bin/python3

def uniq_add(my_list=[]):
    return sum(set(filter(lambda x: type(x) == int,my_list)))
