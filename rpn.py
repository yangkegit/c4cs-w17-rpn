#!/usr/bin/env python3
import operator

Operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(arg):
    stack = []
    for operand in arg.split():
        try:
            operand = float(operand)
            stack.append(operand)
        except:
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.append(Operators[operand](arg1, arg2))
    return stack.pop()

def main():
    while True:
        result = calculate(input('rpn calc> '))
        print("Result:", result)

if __name__ == '__main__':
    main()
