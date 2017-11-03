#!/usr/bin/env python3

"""
Token and Token types
"""
__author__ = 'Aollio Hou'
__email__ = 'aollio@outlook.com'


class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))

    __repr__ = __str__


# operators. integer div is integer div.
PLUS, MINUS, MUL, DIV = 'PLUS', 'MINUS', 'MUL', 'DIV'
DOT, COMMA, SEIM, LPAREN, RPAREN, COLON = 'DOT', 'COMMA', 'SEIM', 'LPAREN', 'RPAREN', 'COLON'
SPACE, NEWLINE = 'SPACE', 'NEWLINE'
ASSIGN = 'ASSIGN'
EOF = 'EOF'
# identity, variable type token
ID = 'ID'
REAL_CONST = 'REAL'
INTEGER_CONST = 'INTEGER'
# 单个符号标记
SINGLE_MARK_DICT = {
    '+': Token(type=PLUS, value='+'),
    '-': Token(type=MINUS, value='-'),
    '*': Token(type=MUL, value='*'),
    '/': Token(type=DIV, value='/'),
    '.': Token(type=DOT, value='.'),
    ';': Token(type=SEIM, value=';'),
    '(': Token(type=LPAREN, value='('),
    ')': Token(type=RPAREN, value=')'),
    ',': Token(type=COMMA, value=','),
    ':': Token(type=COLON, value=':'),
    # '\n': Token(type=NEWLINE, value='\n'),
    # ' ': Token(type=SPACE, value=' '),
    '=': Token(type=ASSIGN, value='='),
}

INDENT = 'INDENT'

IF, ELIF, ELSE = 'if', 'elif', 'else'
PRESERVE_DICT = {
    IF: Token(type=IF, value=IF),
    ELIF: Token(type=ELIF, value=ELIF),
    ELSE: Token(type=ELSE, value=ELSE)
}
