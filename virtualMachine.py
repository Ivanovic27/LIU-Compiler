from globals import (memory)
from Operator import Operator
import sys
import math

global_data = []
constant_data = []
on_function = False
segments = []
quadruples = [0]
map_info = None

# Operations


def add_operator(left, right, virtual_direction):
    """
    Name: add_operator
    Description: Executes an addition operation in the virtual machine
    Parameters: 
        - left: direction of the first value to add
        - right: direction of the second value to add
    Returns: The sum of the values on directions on left and right
    Important methods where its called: Called with Operator.SUM
    """
    return float(get_value_direction(left)) + float(get_value_direction(right))


def subtract_operator(left, right, virtual_direction):
    """
    Name: subtract_operator
    Description: Executes a subtraction operation in the virtual machine
    Parameters: 
        - left: direction of the first value to subtract
        - right: direction of the second value to subtract
    Returns: The subtraction of the values on directions on left and right
    Important methods where its called: Called with Operator.SUBTRACT
    """
    return float(get_value_direction(left)) - float(get_value_direction(right))


def multiply_operator(left, right, virtual_direction):
    """
    Name: multiply_operator
    Description: Executes a multiplication operation in the virtual machine
    Parameters: 
        - left: direction of the first value to subtract
        - right: direction of the second value to subtract
    Returns: The multiplication of the values on directions on left and right
    Important methods where its called: Called with Operator.MULTIPLY
    """
    return float(get_value_direction(left)) * float(get_value_direction(right))


def divide_operator(left, right, virtual_direction):
    """
    Name: divide_operator
    Description: Executes a divition operation in the virtual machine
    Parameters: 
        - left: direction of the first value to subtract
        - right: direction of the second value to subtract
    Returns: The divition of the values on directions on left and right
    Important methods where its called: Called with Operator.DIVIDE
    """
    return float(get_value_direction(left)) / float(get_value_direction(right))


def assign_operator(left, right, virtual_direction):
    """
    Name: assign_operator
    Description: Executes an assignation operation in the virtual machine
    Parameters: 
        - left: direction of the first value to subtract
    Returns: The value of the left operator
    Important methods where its called: Called with Operator.ASSIGN
    """
    return get_value_direction(left)


def and_operator(left, right, virtual_direction):
    """
    Name: and_operator
    Description: Executes an and operation in the virtual machine
    Parameters: 
        - left: direction of the first value to 
        - right: direction of the second value to 
    Returns: The result of and operation between values of left and right
    Important methods where its called: Called with Operator.AND
    """
    return bool(get_value_direction(left)) and bool(get_value_direction(right))


def or_operator(left, right, virtual_direction):
    """
    Name: or_operator
    Description: Executes an or operation in the virtual machine
    Parameters: 
        - left: direction of the first value to 
        - right: direction of the second value to 
    Returns: The result of a or operation of the value on the left and right virtual direction values
    Important methods where its called: Called with Operator.OR
    """
    return bool(get_value_direction(left)) or bool(get_value_direction(right))


def not_operator(left, right, virtual_direction):
    """
    Name: not_operator
    Description: Executes a not operation in the virtual machine
    Parameters: 
        - left: direction of the first value to 
        - right: direction of the second value to 
    Returns: The result of not operation of the left value
    Important methods where its called: Called with Operator.NOT
    """
    return not bool(get_value_direction(left))


def equal_operator(left, right, virtual_direction):
    """
    Name: equal_operator
    Description: Executes an equal operation in the virtual machine
    Parameters: 
        - left: direction of the first value to 
        - right: direction of the second value to 
    Returns: The result of a equal operation of the value on the left and right virtual direction values
    Important methods where its called: Called with Operator.EQUAL
    """
    return (get_value_direction(left) == get_value_direction(right))


def greater_operator(left, right, virtual_direction):
    """
    Name: greater_operator
    Description: Executes a greater operation in the virtual machine
    Parameters: 
        - left: direction of the first value to 
        - right: direction of the second value to 
    Returns: The result of a greater operation of the value on the left and right virtual direction values
    Important methods where its called: Called with Operator.GREATER
    """
    return (float(get_value_direction(left)) > float(get_value_direction(right)))


def less_operator(left, right, virtual_direction):
    """
    Name: less_operator
    Description: Executes a less operation in the virtual machine
    Parameters: 
        - left: direction of the first value to 
        - right: direction of the second value to 
    Returns: The result of a less operation of the value on the left and right virtual direction values
    Important methods where its called: Called with Operator.LESS
    """
    return (float(get_value_direction(left)) < float(get_value_direction(right)))


def sqrt_operator(left, right, virtual_direction):
    """
    Name: sqrt_operator
    Description: Executes a sqrt operation in the virtual machine
    Parameters: 
        - left: direction of the first value to 
        - right: direction of the second value to 
    Returns: The result of a sqrt operation of the value on the left direction
    Important methods where its called: Called with Operator.SQRT
    """
    return (math.sqrt(float(get_value_direction(left))))


def power_operator(left, right, virtual_direction):
    """
    Name: power_operator
    Description: Executes a power operation in the virtual machine
    Parameters: 
        - left: direction of the first value to 
        - right: direction of the second value to 
    Returns: The result of a powert operation between the value on the left direction elevated to the value on the right direction
    Important methods where its called: Called with Operator.POWER
    """
    return (float(get_value_direction(left)) ** float(get_value_direction(right)))


def max_operator(left, right, virtual_direction):
    """
    Name: max_operator
    Description: Executes a max operation of an array in the virtual machine
    Parameters: 
        - left: direction of the first value on the array
        - right: size of the array to check
    Returns: The maximum value on an array
    Important methods where its called: Called with Operator.MAX
    """
    size = get_value_direction(right)
    result = None
    for i in range(0, size):
        temp = get_value_direction(left + i)
        if result == None or temp > result:
            result = temp
    return result


def min_operator(left, right, virtual_direction):
    """
    Name: min_operator
    Description: Executes a min operation of an array in the virtual machine
    Parameters: 
        - left: direction of the first value on the array
        - right: size of the array to check
    Returns: The minimum value on an array
    Important methods where its called: Called with Operator.MIN
    """
    size = get_value_direction(right)
    result = None
    for i in range(0, size):
        temp = get_value_direction(left + i)
        if result == None or temp < result:
            result = temp
    return result


def multiply_all_operator(left, right, virtual_direction):
    """
    Name: multiply_all_operator
    Description: Multiplies all the values in an array
    Parameters: 
        - left: direction of the first value on the array
        - right: size of the array to check
    Returns: The value of all the array values being multiplicated
    Important methods where its called: Called with Operator.MULTIPLYALL
    """
    size = get_value_direction(right)
    result = 1
    for i in range(0, size):
        value = float(get_value_direction(left + i))
        result *= value
    return result


def subtract_all_operator(left, right, virtual_direction):
    """
    Name: subtract_all_operator
    Description: Substracts all the values in an array
    Parameters: 
        - left: direction of the first value on the array
        - right: size of the array to check
    Returns: The value of all the array values being subtracted
    Important methods where its called: Called with Operator.SUBTRACTALL
    """
    size = get_value_direction(right)
    result = 0
    for i in range(0, size):
        value = float(get_value_direction(left + i))
        result -= value
    return result


def add_all_operator(left, right, virtual_direction):
    """
    Name: add_all_operator
    Description: Add all the values in an array
    Parameters: 
        - left: direction of the first value on the array
        - right: size of the array to check
    Returns: The value of all the array values being added
    Important methods where its called: Called with Operator.ADDALL
    """
    size = get_value_direction(right)
    result = 0
    for i in range(0, size):
        value = float(get_value_direction(left + i))
        result += value
    return result


def first_operator(left, right, virtual_direction):
    """
    Name: first_operator
    Description: Gets the value of the first element on an array
    Parameters: 
        - left: direction of the first value on the array
    Returns: The value of the first value on an array
    Important methods where its called: Called with Operator.FIRST
    """
    return get_value_direction(left)


def last_operator(left, right, virtual_direction):
    """
    Name: last_operator
    Description: Gets the value of the last element on an array
    Parameters: 
        - left: direction of the first value on the array
        - right: size of the array to check
    Returns: The value of the last value on an array
    Important methods where its called: Called with Operator.LAST
    """
    size = get_value_direction(right)
    return get_value_direction(left + size - 1)


def is_text_operator(left, right, virtual_direction):
    """
    Name: is_text_operator
    Description: Checks if the value on a direction is text or not
    Parameters: 
        - left: direction of the value to be checked
    Returns: Returns True if the value on the direction is text false if it's not
    Important methods where its called: Called with Operator.ISTEXT
    """
    value = get_value_direction(left)
    return type(value) is str


def is_number_operator(left, right, virtual_direction):
    """
    Name: is_number_operator
    Description: Checks if the value on a direction is a number or not
    Parameters: 
        - left: direction of the value to be checked
    Returns: Returns True if the value on the direction is a number false if it's not
    Important methods where its called: Called with Operator.ISNUMBER
    """
    value = get_value_direction(left)
    return type(value) is float or type(value) is int


def is_even_operator(left, right, virtual_direction):
    """
    Name: is_even_operator
    Description: Checks if the value on a direction is a number and is even
    Parameters: 
        - left: direction of the value to be checked
    Returns: Returns True if the value on the direction is an even number false if it's not
    Important methods where its called: Called with Operator.ISEVEN
    """
    value = float(get_value_direction(left))
    return (value % 2) <= 0


def is_odd_operator(left, right, virtual_direction):
    """
    Name: is_odd_operator
    Description: Checks if the value on a direction is a number and is odd
    Parameters: 
        - left: direction of the value to be checked
    Returns: Returns True if the value on the direction is an odd number false if it's not
    Important methods where its called: Called with Operator.ISODD
    """
    value = float(get_value_direction(left))
    return (value % 2) > 0


def is_empty_operator(left, right, virtual_direction):
    """
    Name: is_empty_operator
    Description: Checks if the value on a direction is empty
    Parameters: 
        - left: direction of the value to be checked
    Returns: Returns True if the value on the direction is empty, false if it's not
    Important methods where its called: Called with Operator.ISEMPTY
    """
    value = get_value_direction(left)
    return value == None


def map_operator(left, right, virtual_direction):
    """
    Name: map_operator
    Description: Executes a map function to change the content of the array.
    Parameters: 
        - left: The direction of the array or the operator.
        - right: The size of the array or the number to operate with.
    Returns: NA
    Important methods where its called: Called with Operator.MAP
    """
    global map_info
    if map_info == None:
        size = get_value_direction(right)
        dir = left
        map_info = (left, size)
    else:
        (dir, size) = map_info
        operator = str(get_value_direction(left))
        num = float(get_value_direction(right))
        for i in range(0, size):
            try:
                previous_value = float(get_value_direction(dir + i))
            except ValueError:
                continue
            new_value = previous_value
            if operator == 'multiply':
                new_value *= num
            elif operator == 'divide':
                new_value /= num
            elif operator == 'add':
                new_value += num
            elif operator == 'subtract':
                new_value -= num
            assign_result(Operator.ASSIGN, dir + i, new_value)
        map_info = None


def filter_operator(left, right, virtual_direction):
    """
    Name: filter_operator
    Description: Executes a filter function to remove elements of the array that not match.
    Parameters:
        - left: The direction of the array or the operator.
        - right: The size of the array or the number to operate with.
    Returns: NA
    Important methods where its called: Called with Operator.FILTER
    """
    global map_info
    if map_info == None:
        size = get_value_direction(right)
        dir = left
        map_info = (left, size)
    else:
        (dir, size) = map_info
        operator = str(get_value_direction(left))
        num = float(get_value_direction(right))
        new_results = []
        for i in range(0, size):
            try:
                value = float(get_value_direction(dir + i))
            except ValueError:
                new_results.append(get_value_direction(dir + i))
                continue
            if (operator == 'greater' and value > num) or (operator == 'less' and value < num) or (operator == 'equal' and value == num) or (operator == 'not equal' and value != num):
                new_results.append(value)
        for i in range(0, size):
            value = None
            if i < len(new_results):
                value = new_results[i]
            assign_result(Operator.ASSIGN, dir + i, value)
        map_info = None


def length_operator(left, right, virtual_direction):
    """
    Name: length_operator
    Description: Gets the size of an array
    Parameters: 
        - right: direction of the value with the size of the array
    Returns: The value of the length of the array
    Important methods where its called: Called with Operator.LENGTH
    """
    return get_value_direction(right)


def read_operator(left, right, virtual_direction):
    """
    Name: read_operator
    Description: Returns the value of an input
    Parameters: NA
    Returns: The input of the user
    Important methods where its called: Called with Operator.READ
    """
    return input()


def print_operator(left, right, virtual_direction):
    """
    Name: print_operator
    Description: Prints the value on the left direction
    Parameters:
        - left: The direction to be printed
    Returns: NA
    Important methods where its called: Called with Operator.PRINT
    """
    value = str(get_value_direction(left))
    print(value.replace("\\n", "\n"), end="")


def gotoF_operator(left, right, virtual_direction):
    """
    Name: gotoF_operator
    Description: Sets the quadruple to be executed to the value on the left direction if a value is false
    Parameters:
        - left: The direction to be executed next
    Returns: NA
    Important methods where its called: Called with Operator.GOTOF
    """
    value = get_value_direction(left)
    if not bool(value):
        set_quadruple(virtual_direction - memory.start_code)
    else:
        next_quadruple()


def goto_operator(left, right, virtual_direction):
    """
    Name: gotoF_operator
    Description: Sets the quadruple to be executed to the value on the left direction
    Parameters:
        - left: The direction to be executed next
    Returns: NA
    Important methods where its called: Called with Operator.GOTOF
    """
    set_quadruple(virtual_direction - memory.start_code)


def era_operator(left, right, virtual_direction):
    """
    Name: era_operator
    Description: Sets the next segment to be executed and pushes to queue where it was before era
    Parameters:
        - left: The direction of the last exectued quadruple
    Returns: NA
    Important methods where its called: Called with Operator.ERA
    """
    next_quadruple()
    segments.append([])
    quadruples.append(left - memory.start_code)


def gosub_operator(left, right, virtual_direction):
    """
    Name: gosub_operator
    Description: Sets the next segment to be executed and pushes to queue where it was before gosun
    Parameters:
        - left: The direction of the last exectued quadruple
    Returns: NA
    Important methods where its called: Called with Operator.GOSUB
    """
    next_quadruple()
    quadruples.append(left - memory.start_code)


def paramend_operator(left, right, virtual_direction):
    """
    Name: paramend_operator
    Description: Returns to the last place it jumped before PARAM section
    Parameters: na
    Returns: NA
    Important methods where its called: Called with Operator.PARAMEND
    """
    quadruples.pop()


def param_operator(left, right, virtual_direction):
    """
    Name: param_operator
    Description: Gets value for params on the segment before the recently initialized
    Parameters: Left: direction to be retrieved
    Returns: The Value of the direction of left for the segment before the actual one
    Important methods where its called: Called with Operator.PARAM
    """
    return get_value_direction(left, -2)


def paramarr_operator(left, right, virtual_direction):
    """
    Name: paramarr_operator
    Description: Gets value for arrays on the segment before the recently initialized
    Parameters: right: size of array
                left: direction of the start of the array
    Returns: NA
    Important methods where its called: Called with Operator.PARAMARR
    """
    size = get_value_direction(right)
    for i in range(0, size):
        assign_result(Operator.ASSIGN, virtual_direction +
                      i, get_value_direction(left + i))


def return_operator(left, right, virtual_direction):
    """
    Name: return_operator
    Description: Returns the value on the left memory section
    Parameters: 
                left: direction of the value to be retrieved
    Returns: value of the direction on left
    Important methods where its called: Called with Operator.RETURN
    """
    return get_value_direction(left)


def endproc_operator(left, right, virtual_direction):
    """
    Name: endproc_operator
    Description: Kills the memory of the last created segment and returns to last executed quadruple before the call
    Parameters: NA
    Returns: NA
    Important methods where its called: Called with Operator.ENDPROC
    """
    segments.pop()
    quadruples.pop()


def ver_operator(left, right, virtual_direction):
    """
    Name: ver_operator
    Description: Verifies if the memory to be accessed is between the ranges of an array
    Parameters: left: memory to be accessed:
                right: memory start for the array
                virtual_direction: size of the array
    Returns: NA
    Important methods where its called: Called with Operator.VER
    """
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
    Operator.PARAMARR: paramarr_operator,
    Operator.MAP: map_operator,
    Operator.FILTER: filter_operator
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
    Operator.RETURN: return_operator,
    Operator.SQRT: sqrt_operator,
    Operator.POWER: power_operator,
    Operator.MAX: max_operator,
    Operator.MIN: min_operator,
    Operator.MULTIPLYALL: multiply_all_operator,
    Operator.SUBTRACTALL: subtract_all_operator,
    Operator.ADDALL: add_all_operator,
    Operator.FIRST: first_operator,
    Operator.LAST: last_operator,
    Operator.ISTEXT: is_text_operator,
    Operator.ISNUMBER: is_number_operator,
    Operator.ISEVEN: is_even_operator,
    Operator.ISODD: is_odd_operator,
    Operator.ISEMPTY: is_empty_operator,
    Operator.LENGTH: length_operator
}


def execute_program():
    """
    Name: execute_program
    Description: Executes de program on the virtual machine quadruple by quadruple
    Parameters: NA
    Returns: NA
    Important methods where its called: NA
    """
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
            result = assign_operations[operator](
                left, right, virtual_direction)
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
    """
    Name: set_quadruple
    Description: Sets the next quadruple to be executed
    Parameters: value: number of the next quadruple to be executed
    Returns: NA
    Important methods where its called: GOTO Operators and next_quadruple
    """
    quadruples[-1] = value


def get_quadruple():
    """
    Name: get_quadruple
    Description: Returns the qudruple that is being executed
    Parameters: NA
    Returns: NA
    Important methods where its called: 
        - execute_program: To get the quadruple to exectue
        - next_quadruple: To execute the next quadruple
    """
    return quadruples[-1]


def next_quadruple():
    """
    Name: next_quadruple
    Description: Sets the current quadruple to the next one
    Parameters: NA
    Returns: NA
    Important methods where its called: 
        - GOTOF
        - ERA
        - GOSUB
        - next_quadruple
    """
    set_quadruple(get_quadruple() + 1)


def get_real_direction(direction):
    """
    Name: get_real_direction
    Description: Gets the real direction without the offset of memory
    Parameters: direction: direction to be accessed with offset
    Returns: The real direction and which memory it belongs to
    Important methods where its called:
        - get_real_direction
        - get_value_direction
        - assign_results 
    """
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
    """
    Name: get_value_direction
    Description: Gets the value of a direction depending on the segment it wants
    Parameters: direction: direction in which they want the value from
                dir: Segment in which the direction belongs
    Returns: The value of the direction according to the segment and its direction type
    Important methods where its called:
        - Every operation the virtual machine does
    """
    dir_type, direction = get_real_direction(direction)
    if dir_type == 'global':
        return global_data[direction]
    elif dir_type == 'constant':
        return memory.constant_data[direction]
    elif dir_type == 'local':
        return segments[dir][direction]


def assign_memory(data, direction):
    """
    Name: assign_memory
    Description: Asigns memory according to a ceratin direction if it doesn't have enough appended
    Parameters: direction: direction needed to execute a quadruple
                data: Memory in which the space is needed 
    Returns: NA
    Important methods where its called:
        - assign_result: When there needs to be an assignation to expand the memory size
    """
    extra_ammount = direction - len(data) + 1
    if extra_ammount > 0:
        for _ in range(0, extra_ammount):
            data.append(None)


def assign_result(operator, direction, value):
    """
    Name: assign_result
    Description: Asigns results to memory depending on its direction type
    Parameters: direction: direction where the assignation will be done
                value: Value that has to be assigned to the direction
    Returns: NA
    Important methods where its called:
        - execute_program
        - map_operator
        - filter_operator
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
