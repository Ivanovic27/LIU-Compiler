from enum import Enum


class Operator(Enum):
    ASSIGN = 0
    GOTO = 1
    GOTOF = 2
    GOTOT = 3
    ERA = 4
    PARAM = 5
    GOSUB = 6
    RETURN = 7
    PARAMEND = 8
    ENDPROC = 9
    MEM = 10
    SUM = 11
    SUBTRACT = 12
    DIVIDE = 13
    MULTIPLY = 14
    NOT = 15
    EQUAL = 16
    OR = 17
    AND = 18
    PRINT = 19
    READ = 20
    NEXT = 21
    EOF = 22
    STARTPROC = 23
    GREATER = 24
    LESS = 25
    VER = 26
    PARAMARR = 27
    SQRT = 28
    POWER = 29
    MAX = 30
    MIN = 31
