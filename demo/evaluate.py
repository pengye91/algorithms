#!/usr/bin/env python
# encoding: utf-8

import sys
import re
import ast
import operator

input_expression = str(sys.argv[1])

numbers_stack = []
operators_stack = []
operators_dict = {"+": operator.add, "-": operator.sub,
                  "/": operator.truediv, "*": operator.mul, }

exp_lists = re.findall(r"[()-/\*\+]|\d+\.\d+|\d+", input_expression)
print(input_expression)

for e in exp_lists:
    if e == '(':
        pass
    elif e in ['+', '-', '*', '/']:
        operators_stack.append(operators_dict[e])
    elif e != ')':
        numbers_stack.append(ast.literal_eval(e))
    elif e == ')':
        latter = numbers_stack.pop()
        first = numbers_stack.pop()
        numbers_stack.append(operators_stack.pop()(first, latter))

print(numbers_stack.pop())
