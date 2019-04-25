from globals import (global_data as gl, memory)
from Operator import Operator

class Segment():
    current_cuadruple = None
    memory = []
    def __init__(self, current_cuadruple):
        self.current_cuadruple = current_cuadruple

segments = []
not_assign_operators = [Operator.PRINT, Operator.EOF, Operator.GOTOF, Operator.GOTO, Operator.ERA, Operator.GOSUB, Operator.PARAMEND, Operator.RETURN, Operator.PARAM]
goto_operators = [Operator.GOTOF, Operator.GOTO]

def execute_next_cuadruple():
    cuadruple = memory.code_segment[gl.current_cuadruple]
    print(cuadruple.operator)
    recognize_Operation(cuadruple.operator, cuadruple.left,cuadruple.right, cuadruple.virtual_direction)

def recognize_Operation(operator, left, right, virtual_direction):
    if operator == Operator.STARTPROC:
        gl.on_function = True
    if operator == Operator.ENDPROC:
        gl.on_function = False

    if operator == Operator.ENDPROC or gl.on_function:
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
        elif operator == Operator.NOT:
            result = notOperator(left, right, virtual_direction)
        elif operator == Operator.READ:
            result = readOperator(left, right, virtual_direction)
        elif operator == Operator.PRINT:
            printOperator(left, right, virtual_direction)
        elif operator == Operator.GOTOF:
            gotoFOperator(left,right,virtual_direction)
        elif operator == Operator.GOTO:
            gotoOperator(left,right,virtual_direction)
        elif operator == Operator.ERA:
            # eraOperator(left,right,virtual_direction)
            print("asd")
        elif operator == Operator.GOSUB:
            print("Go sub")
        elif operator == Operator.PARAMEND:
            print("Paramend")
        elif operator == Operator.PARAM:
            print("Param")

        # Execute ANYTHING that requires an assignation
        if operator not in not_assign_operators:
            assignResult(virtual_direction, result)
        if operator != Operator.EOF:
            if operator in goto_operators:
                # Jump to quadruple
                execute_next_cuadruple()
            else:
                # Go to next quadruple
                setCuadruple(getCuadruple() + 1)
                execute_next_cuadruple()
                

#Operations
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

def readOperator(left, right, virtual_direction):
    return input('Enter your input:')

def printOperator(left, right, virtual_direction):
    value = getValueDirection(left)
    print(value,end="")

def gotoFOperator(left,right,virtual_direction):
    value = getValueDirection(left)
    if(False == bool(value)):
        setCuadruple(virtual_direction - memory.start_code)
    else:
        setCuadruple(gl.current_cuadruple + 1)
 
def gotoOperator(left,right,virtual_direction):
    setCuadruple(virtual_direction - memory.start_code)

def eraOperator(left,right,virtual_direction):
    setCuadruple(virtual_direction - memory.start_code)

#Get Values from Directions

def setCuadruple(value):
    if len(segments) == 0:
        gl.current_cuadruple = value
    else:
        segments[-1].current_cuadruple = value

def getCuadruple():
    if len(segments) == 0:
        return gl.current_cuadruple
    else:
        return segments[-1].current_cuadruple


def getValueDirection(direction):
    # Constant Values
    if(float(direction) >= memory.start_constant):
        direction = direction - memory.start_constant
        for index, value in enumerate(memory.constant_data):
            if(direction == index):
                return value
    # Local Values
    elif(float(direction) >= memory.start_local):
        direction = direction - memory.start_local
        for index, value in enumerate(segments[-1].segment):
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
    if(float(direction) >= memory.start_constant):
        direction = direction - memory.start_constant
        for index, stuff in enumerate(memory.constant_data):
            if(index == direction):
                memory.global_data[index] = value
    # Local Values
    elif(float(direction) >= memory.start_local):
        direction = direction - memory.start_local
        for index, stuff in enumerate(segments[-1].segment):
            if(index == direction):
                memory.global_data[index] = value
    # Global Values
    else:
        for index, stuff in enumerate(memory.global_data):
            if(index == direction):
                memory.global_data[index] = value
