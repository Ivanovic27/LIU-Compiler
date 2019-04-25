import sys
from virtualMachine import *
from antlr4 import (FileStream, CommonTokenStream, ParseTreeWalker)
from grammar.LiuLexer import LiuLexer
from grammar.LiuParser import LiuParser
from SemanticAnalyzer import SemanticAnalyzer
from globals import (global_data as gl, memory)
from preloaded_data import global_function

# TODO: Merge get_execution_data and get_definition_data
# TODO: Move create_variable to another file.
# TODO: Print remove extra memory added.


def main(argv):
    file_name = argv[1]
    input = FileStream(file_name)
    lexer = LiuLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LiuParser(stream)
    tree = parser.program()
    semantic = SemanticAnalyzer()
    walker = ParseTreeWalker()
    walker.walk(semantic, tree)
    
    execute_next_cuadruple()
    gl.print_function(global_function)
    gl.print_globals()
    gl.print_constants()
    gl.print_quadruples()


if __name__ == "__main__":
    main(sys.argv)
