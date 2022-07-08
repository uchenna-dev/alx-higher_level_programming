#!/usr/bin/python3
# 2-uniq_add .py[D[D[[[C[C[.py
# Yovo Koffi Vianney


def uniq_add(my_list=[]):
"""Add all unique integers in a list (once for eac integers)."""
result = 0
for x in set(my_list):
result += x
return (result)
