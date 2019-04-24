from globals import (global_data as gl, memory)
from Operator import Operator


def execute_next_cuadruple():
    cuadruple = memory.code_segment[gl.current_cuadruple]
    recognize_Operation(cuadruple.operator, cuadruple.left,cuadruple.right, cuadruple.virtual_direction)

def recognize_Operation(operator, left, right, virtual_direction):
    if operator == Operator.SUM:
        result = addOperator(left, right, virtual_direction)
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
    elif operator == Operator.NOT:
        result = notOperator(left, right, virtual_direction)
    elif operator == Operator.READ:
        result = readOperator(left, right, virtual_direction)
    elif operator == Operator.PRINT:
        printOperator(left, right, virtual_direction)
    if operator != Operator.PRINT and operator != Operator.EOF:
        assignResult(virtual_direction, result)
    if operator != Operator.EOF:
        gl.current_cuadruple = gl.current_cuadruple + 1
        execute_next_cuadruple()

#Operations
def addOperator(left, right, virtual_direction):
    return float(getValueDirection(left)) + float(getValueDirection(right))


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


def readOperator(left, right, virtual_direction):
    return input('Enter your input:')


def printOperator(left, right, virtual_direction):
    print("This is where you print")

#Get Values from Directions


def getValueDirection(direction):
    # Constant Values
    if(float(direction) >= 200):
        direction = direction - 200
        for index, value in enumerate(memory.constant_data):
            if(direction == index):
                return value
    # Local Values
    elif(float(direction) >= 600):
        direction = direction - 600
        for index, value in enumerate(memory.local_segment):
            if(direction == index):
                return value
    # Global Values
    else:
        for index, value in enumerate(memory.global_data):
            if(direction == index):
                return value
    return 0

#Assign results to Directions


def assignResult(direction, value):
    # Constant Values
    if(float(direction) >= 200):
        direction = direction - 200
        for index, stuff in enumerate(memory.constant_data):
            if(index == direction):
                memory.global_data[index] = value
    # Local Values
    elif(float(direction) >= 600):
        direction = direction - 600
        for index, stuff in enumerate(memory.local_segment):
            if(index == direction):
                memory.global_data[index] = value
    # Global Values
    else:
        for index, stuff in enumerate(memory.global_data):
            if(index == direction):
                memory.global_data[index] = value
