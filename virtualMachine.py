from globals import (global_data as gl, memory)
from Operator import Operator
import sys

sys.setrecursionlimit(7000)


class Segment():
    def __init__(self):
        self.memory = []


segments = []
goto_operators = [Operator.GOTOF, Operator.GOTO, Operator.ERA,
                  Operator.GOSUB, Operator.PARAMEND, Operator.ENDPROC]
not_assign_operators = goto_operators + \
    [Operator.STARTPROC, Operator.PRINT, Operator.EOF]
cuadruples = [0]


def execute_next_cuadruple():
    cuadruple = memory.code_segment[getCuadruple()]
    recognize_Operation(cuadruple.operator, cuadruple.left,
                        cuadruple.right, cuadruple.virtual_direction)


def recognize_Operation(operator, left, right, virtual_direction):
    if operator == Operator.STARTPROC:
        gl.on_function = True

    if gl.on_function and operator != Operator.ENDPROC:
        setCuadruple(getCuadruple() + 1)
        execute_next_cuadruple()
    elif gl.on_function and operator == Operator.ENDPROC:
        gl.on_function = False
        setCuadruple(getCuadruple() + 1)
        execute_next_cuadruple()
    else:
        if operator == Operator.SUM:
            result = addOperator(left, right, virtual_direction)
        elif operator == Operator.SUBTRACT:
            result = substractOperator(left, right, virtual_direction)
        elif operator == Operator.ASSIGN:
            result = assignOperator(left, virtual_direction)
        elif operator == Operator.MULTIPLY:
            result = multiplyOperator(left, right, virtual_direction)
        elif operator == Operator.DIVIDE:
            result = divideOperator(left, right, virtual_direction)
        elif operator == Operator.AND:
            result = andOperator(left, right, virtual_direction)
        elif operator == Operator.OR:
            result = orOperator(left, right, virtual_direction)
        elif operator == Operator.EQUAL:
            result = equalOperator(left, right, virtual_direction)
        elif operator == Operator.GREATER:
            result = greaterOperator(left, right, virtual_direction)
        elif operator == Operator.LESS:
            result = lessOperator(left, right, virtual_direction)
        elif operator == Operator.NOT:
            result = notOperator(left, right, virtual_direction)
        elif operator == Operator.READ:
            result = readOperator(left, right, virtual_direction)
        elif operator == Operator.PRINT:
            printOperator(left, right, virtual_direction)
        elif operator == Operator.GOTOF:
            gotoFOperator(left, right, virtual_direction)
        elif operator == Operator.GOTO:
            gotoOperator(left, right, virtual_direction)
        elif operator == Operator.ERA:
            eraOperator(left, right, virtual_direction)
        elif operator == Operator.GOSUB:
            gosubOperator(left, right, virtual_direction)
        elif operator == Operator.PARAMEND:
            paramendOperator(left, right, virtual_direction)
        elif operator == Operator.PARAM:
            result = paramOperator(left, right, virtual_direction)
        elif operator == Operator.RETURN:
            result = returnOperator(left, right, virtual_direction)
        elif operator == Operator.ENDPROC:
            endprocOperator(left, right, virtual_direction)

        # Execute ANYTHING that requires an assignation
        if operator not in not_assign_operators:
            assignResult(operator, virtual_direction, result)
            if operator == Operator.RETURN:
                segments.pop()
                cuadruples.pop()
        if operator != Operator.EOF:
            if operator in goto_operators or operator == Operator.RETURN:
                # Jump to quadruple
                execute_next_cuadruple()
            else:
                # Go to next quadruple
                setCuadruple(getCuadruple() + 1)
                execute_next_cuadruple()


# Operations
def addOperator(left, right, virtual_direction):
    return float(getValueDirection(left)) + float(getValueDirection(right))


def substractOperator(left, right, virtual_direction):
    return float(getValueDirection(left)) - float(getValueDirection(right))


def multiplyOperator(left, right, virtual_direction):
    return float(getValueDirection(left)) * float(getValueDirection(right))


def divideOperator(left, right, virtual_direction):
    return float(getValueDirection(left)) / float(getValueDirection(right))


def assignOperator(left, virtual_direction):
    return getValueDirection(left)


def andOperator(left, right, virtual_direction):
    return bool(getValueDirection(left)) and bool(getValueDirection(right))


def orOperator(left, right, virtual_direction):
    return bool(getValueDirection(left)) or bool(getValueDirection(right))


def notOperator(left, right, virtual_direction):
    return not getValueDirection(left)


def equalOperator(left, right, virtual_direction):
    return (getValueDirection(left) == getValueDirection(right))


def greaterOperator(left, right, virtual_direction):
    return (getValueDirection(left) > getValueDirection(right))


def lessOperator(left, right, virtual_direction):
    return (getValueDirection(left) < getValueDirection(right))


def readOperator(left, right, virtual_direction):
    return input('Enter your input:')


def printOperator(left, right, virtual_direction):
    value = str(getValueDirection(left))
    print(value.replace("\\n", "\n"), end="")


def gotoFOperator(left, right, virtual_direction):
    value = getValueDirection(left)
    if(False == bool(value)):
        setCuadruple(virtual_direction - memory.start_code)
    else:
        setCuadruple(getCuadruple() + 1)


def gotoOperator(left, right, virtual_direction):
    setCuadruple(virtual_direction - memory.start_code)


def eraOperator(left, right, virtual_direction):
    setCuadruple(getCuadruple() + 1)
    segments.append(Segment())
    cuadruples.append(left - memory.start_code)


def gosubOperator(left, right, virtual_direction):
    setCuadruple(getCuadruple() + 1)
    cuadruples.append(left - memory.start_code)


def paramendOperator(left, right, virtual_direction):
    cuadruples.pop()


def paramOperator(left, right, virtual_direction):
    return getValueDirection(left, -2)


def returnOperator(left, right, virtual_direction):
    value = getValueDirection(left)
    return value


def endprocOperator(left, right, virtual_direction):
    segments.pop()
    cuadruples.pop()

# Get Values from Directions


def setCuadruple(value):
    cuadruples[-1] = value
    # if len(segments) == 0:
    #    gl.current_cuadruple = value
    # else:
    #    segments[-1].current_cuadruple = value


def getCuadruple():
    return cuadruples[-1]
    # if len(segments) == 0:
    #    return gl.current_cuadruple
    # else:
    #    return segments[-1].current_cuadruple


def getValueDirection(direction, dir=-1):
    # Constant Values
    if(float(direction) >= memory.start_constant and float(direction) < memory.start_local):
        direction = direction - memory.start_constant
        for index, value in enumerate(memory.constant_data):
            if(direction == index):
                return value
    # Local Values
    elif(float(direction) >= memory.start_local):
        direction = direction - memory.start_local
        for index, value in enumerate(segments[dir].memory):
            if(direction == index):
                return value
    # Global Values
    else:
        for index, value in enumerate(memory.global_data):
            if(direction == index):
                return value
    return 0

# Assign results to Directions


def assignResult(operator, direction, value):
    # Constant Values
    if(float(direction) >= memory.start_constant and float(direction) < memory.start_local):
        direction = direction - memory.start_constant
        num = direction - len(memory.constant_data) + 1
        if num > 0:
            for _ in range(0, num):
                memory.constant_data.append(None)
        memory.constant_data[direction] = value
    # Local Values
    elif(float(direction) >= memory.start_local):
        direction = direction - memory.start_local
        num = direction - len(segments[-1].memory) + 1
        if num > 0:
            for _ in range(0, num):
                segments[-1].memory.append(None)
        segments[-1].memory[direction] = value
    # Global Values
    else:
        direction = direction - memory.start_global
        num = direction - len(memory.global_data) + 1
        if num > 0:
            for _ in range(0, num):
                memory.global_data.append(None)
        memory.global_data[direction] = value
