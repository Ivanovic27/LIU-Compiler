import sys
from virtualMachine import *
from antlr4 import *
from grammar.LiuLexer import LiuLexer
from grammar.LiuParser import LiuParser
from SemanticAnalyzer import SemanticAnalyzer
from globals import (global_data as gl, memory)
from preloaded_data import global_function
from antlr4.error.ErrorListener import ErrorListener


class GrammarErrorListener(ErrorListener):
    """
    Name: GrammarErrorListener
    Description: Displays the errors of the executing program
    Parameters: 
        ErrorListener, contains the error arrayener of ANTLR4
    Returns: NA
    Important methods where its called: 
        - main, to send the errors and display them
    """

    def __init__(self):
        super(GrammarErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Formats the error to show the message, line and column.
        """
        message = 'ERROR in line {0}, column {1}: {2}'.format(
            line, column, msg)
        raise Exception(message)


def main(argv):
    """
    Name: main
    Description: Compiles and exectues the generated code from a file.
    Parameters:
        argv[1]: Contains the name of the file to compile and execute.
    Returns: NA
    Important methods where its called: NA
    """
    try:
        file_name = argv[1]
        input = FileStream(file_name)
        lexer = LiuLexer(input)
        lexer._listeners = [GrammarErrorListener()]
        stream = CommonTokenStream(lexer)
        parser = LiuParser(stream)
        parser._listeners = [GrammarErrorListener()]
        tree = parser.program()
        semantic = SemanticAnalyzer()
        walker = ParseTreeWalker()
        walker.walk(semantic, tree)
        # execute_program()
        # gl.print_function(global_function)
        # gl.print_globals()
        # gl.print_constants()
        gl.print_quadruples()
    except BaseException as e:
        print(e)
        sys.exit()
    except:
        sys.exit()


if __name__ == "__main__":
    main(sys.argv)
