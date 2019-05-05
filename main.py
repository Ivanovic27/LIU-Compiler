import sys
from virtualMachine import *
from antlr4 import *
from grammar.LiuLexer import LiuLexer
from grammar.LiuParser import LiuParser
from SemanticAnalyzer import SemanticAnalyzer
from globals import (global_data as gl, memory)
from preloaded_data import global_function
from antlr4.error.ErrorListener import ErrorListener

# TODO: Merge get_execution_data and get_definition_data
# TODO: Move create_variable to another file.
# TODO: Print remove extra memory added.
# TODO: Add negative numbers.

class MyErrorListener( ErrorListener ):
    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        message = 'ERROR in line {0}, column {1}: {2}'.format(line, column, msg)
        raise Exception(message)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        # raise Exception("Oh no!!")
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        # raise Exception("Oh no!!")
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        # raise Exception("Oh no!!")
        pass

def main(argv):
    try:
        file_name = argv[1]
        input = FileStream(file_name)
        lexer = LiuLexer(input)
        lexer._listeners = [MyErrorListener()]
        stream = CommonTokenStream(lexer)
        parser = LiuParser(stream)
        parser._listeners = [MyErrorListener()]
        tree = parser.program()
        semantic = SemanticAnalyzer()
        walker = ParseTreeWalker()
        walker.walk(semantic, tree)
        execute_program()
        # gl.print_function(global_function)
        # gl.print_globals()
        # gl.print_constants()
        # gl.print_quadruples()
    except BaseException as e:
        print(e)
        sys.exit()
    except:
        sys.exit()


if __name__ == "__main__":
    main(sys.argv)
