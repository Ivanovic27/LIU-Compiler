from globals import (memory)
from Operator import Operator
import sys

global_data = []
constant_data = []
on_function = False
segments = []
quadruples = [0]


# Operations
def add_operator(left, right, virtual_direction):
    return float(get_value_direction(left)) + float(get_value_direction(right))


def subtract_operator(left, right, virtual_direction):
    return float(get_value_direction(left)) - float(get_value_direction(right))


def multiply_operator(left, right, virtual_direction):
    return float(get_value_direction(left)) * float(get_value_direction(right))


def divide_operator(left, right, virtual_direction):
    return float(get_value_direction(left)) / float(get_value_direction(right))


def assign_operator(left, right, virtual_direction):
    return get_value_direction(left)


def and_operator(left, right, virtual_direction):
    return bool(get_value_direction(left)) and bool(get_value_direction(right))


def or_operator(left, right, virtual_direction):
    return bool(get_value_direction(left)) or bool(get_value_direction(right))


def not_operator(left, right, virtual_direction):
    return not bool(get_value_direction(left))


def equal_operator(left, right, virtual_direction):
    return (get_value_direction(left) == get_value_direction(right))


def greater_operator(left, right, virtual_direction):
    return (float(get_value_direction(left)) > float(get_value_direction(right)))


def less_operator(left, right, virtual_direction):
    return (float(get_value_direction(left)) < float(get_value_direction(right)))


def read_operator(left, right, virtual_direction):
    return input()


def print_operator(left, right, virtual_direction):
    value = str(get_value_direction(left))
    print(value.replace("\\n", "\n"), end="")


def gotoF_operator(left, right, virtual_direction):
    value = get_value_direction(left)
    if not bool(value):
        set_quadruple(virtual_direction - memory.start_code)
    else:
        next_quadruple()


def goto_operator(left, right, virtual_direction):
    set_quadruple(virtual_direction - memory.start_code)


def era_operator(left, right, virtual_direction):
    next_quadruple()
    segments.append([])
    quadruples.append(left - memory.start_code)


def gosub_operator(left, right, virtual_direction):
    next_quadruple()
    quadruples.append(left - memory.start_code)


def paramend_operator(left, right, virtual_direction):
    quadruples.pop()


def param_operator(left, right, virtual_direction):
    return get_value_direction(left, -2)

def paramarr_operator(left, right, virtual_direction):
    size = get_value_direction(right)
    for i in range(0, size):
        assign_result(Operator.ASSIGN, virtual_direction + i, get_value_direction(left + i))


def return_operator(left, right, virtual_direction):
    return get_value_direction(left)


def endproc_operator(left, right, virtual_direction):
    segments.pop()
    quadruples.pop()


def ver_operator(left, right, virtual_direction):
    a = get_value_direction(left)
    if a < right or a > virtual_direction:
        raise ValueError("Array off limits")


goto_operators = [Operator.GOTOF, Operator.GOTO, Operator.ERA,
                  Operator.GOSUB, Operator.PARAMEND, Operator.ENDPROC]
not_assign_operations = {
    Operator.PRINT: print_operator,
    Operator.GOTOF: gotoF_operator,
    Operator.GOTO: goto_operator,
    Operator.ERA: era_operator,
    Operator.GOSUB: gosub_operator,
    Operator.PARAMEND: paramend_operator,
    Operator.ENDPROC: endproc_operator,
    Operator.VER: ver_operator,
    Operator.PARAMARR: paramarr_operator
}
assign_operations = {
    Operator.SUM: add_operator,
    Operator.SUBTRACT: subtract_operator,
    Operator.ASSIGN: assign_operator,
    Operator.MULTIPLY: multiply_operator,
    Operator.DIVIDE: divide_operator,
    Operator.AND: and_operator,
    Operator.OR: or_operator,
    Operator.EQUAL: equal_operator,
    Operator.GREATER: greater_operator,
    Operator.LESS: less_operator,
    Operator.NOT: not_operator,
    Operator.READ: read_operator,
    Operator.PARAM: param_operator,
    Operator.RETURN: return_operator
}


def execute_program():
    global on_function
    while True:
        current_quadruple = memory.code_segment[get_quadruple()]
        operator = current_quadruple.operator
        left = current_quadruple.left
        right = current_quadruple.right
        virtual_direction = current_quadruple.virtual_direction
        # Finish executing when found an end of line
        if operator == Operator.EOF:
            break
        # Skip all the code from STARTPROC to ENDPROC
        if operator == Operator.STARTPROC:
            on_function = True
        if on_function:
            if operator == Operator.ENDPROC:
                on_function = False
            next_quadruple()
            continue

        if operator in assign_operations:
            result = assign_operations[operator](left, right, virtual_direction)
        elif operator in not_assign_operations:
            not_assign_operations[operator](left, right, virtual_direction)

        # Execute ANYTHING that requires an assignation
        if operator not in not_assign_operations:
            assign_result(operator, virtual_direction, result)
        # Remove memory from return and return to previous quadruple
        if operator == Operator.RETURN:
            segments.pop()
            quadruples.pop()
            continue
        # Jump to next quadruple
        if operator not in goto_operators:
            next_quadruple()

# Get Values from Directions


def set_quadruple(value):
    quadruples[-1] = value


def get_quadruple():
    return quadruples[-1]


def next_quadruple():
    set_quadruple(get_quadruple() + 1)


def get_real_direction(direction):
    if isinstance(direction, str):
        direction = int(direction[1:-1])
        new_direction = get_value_direction(direction)
        return get_real_direction(int(new_direction))
    elif direction >= memory.start_global and direction < memory.start_constant:
        return ('global', direction - memory.start_global)
    elif direction >= memory.start_constant and direction < memory.start_code:
        return ('constant', direction - memory.start_constant)
    elif direction >= memory.start_code and direction < memory.start_local:
        return ('code', direction - memory.start_code)
    elif direction >= memory.start_local:
        return ('local', direction - memory.start_local)


def get_value_direction(direction, dir=-1):
    dir_type, direction = get_real_direction(direction)
    if dir_type == 'global':
        return global_data[direction]
    elif dir_type == 'constant':
        return memory.constant_data[direction]
    elif dir_type == 'local':
        return segments[dir][direction]


def assign_memory(data, direction):
    extra_ammount = direction - len(data) + 1
    if extra_ammount > 0:
        for _ in range(0, extra_ammount):
            data.append(None)


def assign_result(operator, direction, value):
    """
    Assign results to Directions
    """
    dir_type, direction = get_real_direction(direction)
    if dir_type == 'global':
        assign_memory(global_data, direction)
        global_data[direction] = value
    elif dir_type == 'constant':
        assign_memory(memory.constant_data, direction)
        memory.constant_data[direction] = value
    elif dir_type == 'local':
        assign_memory(segments[-1], direction)
        segments[-1][direction] = value
