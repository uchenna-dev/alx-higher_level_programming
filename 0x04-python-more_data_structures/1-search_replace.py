#!/usr/bin/python3
# 1-search_replace.py
# Yovo Koffi Vianney

def search_replace(my_list, search, replace):
"""Replace all occurences of an element by another in a new list."""
new_list = my_list[:]
for i in range(len(new_list)):
if new_list[i] == search:
new_list[i] = replace
return (new_list)
