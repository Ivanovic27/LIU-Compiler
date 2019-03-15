import sys
from antlr4 import *
from grammar.LiuLexer import LiuLexer
from grammar.LiuParser import LiuParser


class LiuGrammarListener(ParseTreeListener):
    def enterDefinition(self, ctx):
        pass

    def enterIdentification(self, ctx):
        pass

    def exitIdentification2(self, ctx):
        pass


def identification(self, ctx):
    a = []
    a.append(str(ctx.Id()))
    algo = ctx.identification2()
    while(algo.Id() != None):
        a.append(str(algo.Id()))
        algo = algo.identification2()
    return ''.join(a)

# TODO: Make directory for functions.
# TODO: Define scope for functions.
# TODO: Check types for groups.
# TODO: Check types inside groups.


def definition(self, ctx):
    if(not ctx.definition_function_name()):
        variable_name = identification(self, ctx.identification())
        b = extended_literal(self, ctx.extended_literal())
        if(variable_name in self.variables):
            print(self.variables[variable_name])
            if(self.variables[variable_name]["type"] != b["type"]):
                raise ValueError('errroorrr')

        self.variables[variable_name] = b
        print(self.variables)


def extended_literal(self, ctx):
    if(ctx.literal() != None):
        a = literal(self, ctx.literal())
    return a


def literal(self, ctx):
    if(ctx.basic_literal() != None):
        a = basic_literal(self, ctx.basic_literal())
    return a


def basic_literal(self, ctx):
    if(ctx.identification() != None):
        # TODO: Check if the identification exists in the table
        id = identification(self, ctx.identification())
        if(id not in self.variables):
            raise ValueError('errroorrr')
        return self.variables[id]
    elif(ctx.execution() != None):
        # TODO: Check execution value type
        return {"type": "STRING"}
    elif(ctx.String() != None):
        return {"type": 'STRING'}
    elif(ctx.Boolean() != None):
        return {"type": 'BOOLEAN'}
    elif(ctx.Number() != None):
        return {"type": 'NUMBER'}


class KeyPrinter(LiuGrammarListener):
    def __init__(self):
        self.variables = {}

    def enterDefinition(self, ctx):
        definition(self, ctx)


def main(argv):
    input = FileStream(argv[1])
    lexer = LiuLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LiuParser(stream)
    tree = parser.program()
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main(sys.argv)
