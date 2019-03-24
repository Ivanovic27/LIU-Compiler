
def get_variables(self):
    return self.functions[self.current_scope]["variables"]


def get_global_variables(self):
    return self.functions["global-function"]["variables"]


def get_parameters(self):
    return self.functions[self.current_scope]["parameters"]


def get_all_variables(self):
    scope_variables = get_variables(self)
    params_variables = get_parameters(self)
    global_variables = get_global_variables(self)
    return {**scope_variables, **params_variables, **global_variables}


def identification(self, ctx):
    id = str(ctx.Id())
    rest_ids = identification2(self, ctx.identification2())
    ids = [id] + rest_ids
    return ''.join(ids)


def identification2(self, ctx):
    if(ctx.Id() != None):
        id = str(ctx.Id())
        rest_ids = identification2(self, ctx.identification2())
        return [id] + rest_ids
    return []


def function(self, ctx):
    function_code(self, ctx.function_code())


def function_code(self, ctx):
    if(ctx.function_code() != None):
        instruction(self, ctx.instruction())
        function_code(self, ctx.function_code())


def instruction(self, ctx):
    if(ctx.definition() != None):
        definition(self, ctx.definition())
    elif(ctx.execution() != None):
        execution(self, ctx.execution())
    elif(ctx.return_statement() != None):
        return_statement(self, ctx.return_statement())


def return_statement(self, ctx):
    if(ctx.group()):
        literal = group(self, ctx.group())
    else:
        literal = basic_literal(self, ctx.basic_literal())
    function = self.functions[self.current_scope]
    if(function["type"] != None and function["type"] != literal["type"]):
        raise ValueError("Return type of function '" +
                         self.current_scope + "' is of type " + function["type"])
    function["type"] = literal["type"]


def definition(self, ctx):
    if(ctx.definition_function_name()):
        definition_function(self, ctx)
    else:
        definition_variable(self, ctx)


def definition_function(self, ctx):
    (function_name, table_parameters) = definition_function_name(
        self, ctx.definition_function_name())
    # Check if the new function is already defined
    if(function_name in self.functions):
        raise ValueError("The function '" + function_name +
                         "' is already defined")
    # Add a function to the functions table
    self.functions[function_name] = {
        "type": None,
        "variables": {},
        "parameters": table_parameters
    }
    # Change scope inside of the new function
    self.current_scope = function_name
    function(self, ctx.function())
    self.current_scope = "global-function"


def definition_variable(self, ctx):
    variable_name = identification(self, ctx.identification())
    # Check if variable is declared globally
    if(variable_name in get_global_variables(self)):
        raise ValueError("Definition '" + variable_name +
                         "' is already globally declared.")
    literal = extended_literal(self, ctx.extended_literal())
    # Check if the new variable type is different from the one already defined
    if(variable_name in get_all_variables(self)):
        if(get_all_variables(self)[variable_name]["type"] != literal["type"]):
            raise ValueError("Type of definition '" + variable_name +
                             "' is not compatible with type " + literal["type"])
    # Add if is not already defined in other part
    if(variable_name not in get_all_variables(self)):
        get_variables(self)[variable_name] = {**literal, "name": variable_name}


def defintion_parameter(self, ctx):
    variable_name = identification(self, ctx.identification())
    literal = extended_literal(self, ctx.extended_literal())
    return (variable_name, literal)


def extended_literal(self, ctx):
    if(ctx.literal() != None):
        info = literal(self, ctx.literal())
    elif(ctx.group() != None):
        info = group(self, ctx.group())
    return info


def group(self, ctx):
    variables = group2(self, ctx.group2())
    return {"type": "GROUP", "variables": variables}


def group2(self, ctx):
    return group3(self, ctx, 0)


def group3(self, ctx, current_position):
    if ctx.literal() != None:
        first_item = literal(self, ctx.literal())
        first_item["pos"] = current_position
        rest_items = group3(self, ctx.group3(), current_position + 1)
        return [first_item] + rest_items
    return []


def literal(self, ctx):
    if(ctx.basic_literal() != None):
        info = basic_literal(self, ctx.basic_literal())
    elif(ctx.terminal_definition() != None):
        info = terminal_definition(self, ctx.terminal_definition())
    return info


def terminal_definition(self, ctx):
    id = identification(self, ctx.identification())
    info = basic_literal(self, ctx.basic_literal())
    return {"id": id, "type": info["type"]}


def basic_literal(self, ctx):
    if(ctx.identification() != None):
        id = identification(self, ctx.identification())
        # Check if the accessed variable exists
        if(id not in get_all_variables(self)):
            raise ValueError("'" + id + "' is not declared as a definition.")
        return get_all_variables(self)[id]
    elif(ctx.execution() != None):
        (function_name, a) = execution(self, ctx.execution())
        exection_type = self.functions[function_name]["type"]
        return { "type": exection_type, "name": a }
    elif(ctx.String() != None):
        return {"type": 'STRING' }
    elif(ctx.Boolean() != None):
        return {"type": 'BOOLEAN'}
    elif(ctx.Number() != None):
        return {"type": 'NUMBER'}


def execution(self, ctx):
    if(ctx.execution_function_name() != None):
        (function_name, table) = execution_function_name(
            self, ctx.execution_function_name())
        check(self, table, function_name)
        return function_name
    elif (ctx.add_execution() != None):
        return do_execution(self, ctx.add_execution(), 'sum')
    elif (ctx.subtract_execution() != None):
        return do_execution(self, ctx.subtract_execution(), 'subtract')
    elif (ctx.divide_execution() != None):
        return do_execution(self, ctx.divide_execution(), 'divide')
    elif (ctx.multiply_execution() != None):
        return do_execution(self, ctx.multiply_execution(), 'multiply')
    elif (ctx.not_execution() != None):
        return do_execution(self, ctx.not_execution(), 'not')
    elif (ctx.equal_execution() != None):
        return do_execution(self, ctx.equal_execution(), 'equal')
    elif (ctx.or_execution() != None):
        return do_execution(self, ctx.or_execution(), 'or')
    elif (ctx.and_execution() != None):
        return do_execution(self, ctx.and_execution(), 'and')
    elif (ctx.print_execution() != None):
        return do_execution(self, ctx.print_execution(), 'print')
    elif (ctx.read_execution() != None):
        return do_execution(self, ctx.read_execution(), 'read')

def check(self, table, function_name):
    for row in table:
        parameters = self.functions[function_name]["parameters"]
        a = False
        if "infiniteParams" in self.functions[function_name]:
            id = next(iter(parameters))
            a = parameters[id]["type"] == row["type"]
        else:
            for key, parameter in parameters.items():
                if(parameter["pos"] == row["pos"] and parameter["type"] == row["type"] and parameter["param"] == row["param"]):
                    a = True
                    break
        if(a == False):
            raise ValueError("Parameters of function '" + function_name + "' do not match")
    # Check that function does not exist
    if(function_name not in self.functions):
        raise ValueError("Function " + function_name + "does not exist.")

def do_execution(self, ctx, id):
    table = group(self, ctx.group())
    for row in table["variables"]:
        row["param"] = 0
    check(self, table["variables"], id + '(param)')
    return (id + '(param)', add_cuadruple_infinite(self, id, table))

def add_cuadruple_infinite(self, id, table):
    temp = table["variables"][0]['name']
    
    if(len(table["variables"]) == 1):
        registry = 't' + str(self.register)
        self.cuadruples.append((id, temp, None, registry))
        temp = registry
        self.register += 1
    for row in table["variables"][1:]:
        registry = 't' + str(self.register)
        self.cuadruples.append((id, temp, row['name'], registry))
        temp = registry
        self.register += 1
    return temp

def execution_function_name(self, ctx):
    parameters_counter = 0
    table = group(self, ctx.group())
    table = table["variables"]
    for row in table:
        row["param"] = parameters_counter
    (rest_name, rest_table) = execution_function_name2(
        self, ctx.execution_function_name2(), parameters_counter + 1)
    table = table + rest_table
    id = identification(self, ctx.identification())
    if(ctx.children[0] == ctx.identification()):
        return (id + '(param)' + rest_name, table)
    else:
        return ('(param)' + id + rest_name, table)


def execution_function_name2(self, ctx, parameters_counter):
    if(ctx.identification and ctx.identification() != None):
        (rest_name, table) = execution_function_name2(
            self, ctx.execution_function_name2(), parameters_counter)
        id = identification(self, ctx.identification())
        return (id + rest_name, table)
    elif(ctx.group() != None):
        new_table = group(self, ctx.group())
        new_table = new_table["variables"]
        for row in new_table:
            row["param"] = parameters_counter
        (rest_name, table) = execution_function_name2(
            self, ctx.execution_function_name2(), parameters_counter + 1)
        return ("(param)" + rest_name, table + new_table)
    return ("", [])


# TODO: Clean code
def definition_function_name(self, ctx):
    parameters_counter = 0
    if(self.current_scope != "global-function"):
        raise ValueError('Function cannot be declared inside another function')
    a = identification(self, ctx.identification())
    table = parameters(self, ctx.parameters())
    for key, value in table.items():
        value["param"] = parameters_counter
    if(ctx.children[0] == ctx.identification()):
        b = a + '(param)' + definition_function_name2(self,
                                                      ctx.definition_function_name2(), parameters_counter + 1, table)
    else:
        b = '(param)' + a + definition_function_name2(self,
                                                      ctx.definition_function_name2(), parameters_counter + 1, table)
    return (b, table)

# TODO: Clean code


def definition_function_name2(self, ctx, parameters_counter, table):
    if(ctx.parameters() != None):
        table_params = parameters(self, ctx.parameters())
        for key, value in table_params.items():
            value["param"] = parameters_counter
            table[key] = value
        return '(param)' + definition_function_name2(self, ctx.definition_function_name2(), parameters_counter + 1, table)
    elif(ctx.identification() != None):
        return identification(self, ctx.identification()) + definition_function_name2(self, ctx.definition_function_name2(), parameters_counter, table)
    return ''


def parameters(self, ctx):
    return parameters3(self, ctx.parameters3())


def parameters2(self, ctx, params_table, current_param_position):
    if(ctx.definition() != None):
        (name, type) = defintion_parameter(self, ctx.definition())
        params_table[name] = {
            "type": type["type"],
            "pos": current_param_position
        }
        parameters2(self, ctx.parameters2(), params_table,
                    current_param_position + 1)


def parameters3(self, ctx):
    params_table = {}
    parameters2(self, ctx, params_table, 0)
    return params_table
