import sys
from antlr4 import (FileStream, CommonTokenStream, ParseTreeWalker)
from grammar.LiuLexer import LiuLexer
from grammar.LiuParser import LiuParser
from SemanticAnalyzer import SemanticAnalyzer
import globals as gl

# TODO: Change Variables and Functions to Classes.
# TODO: Change equal for only 2 parameters.
# TODO: Change print cuadruples to have only left.
# TODO: Merge get_execution_data and get_definition_data
# TODO: Move add_cuadruple_infinite and create_variable to another file.


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

    gl.print_function("(param)do(param)")
    gl.print_function("(param)do(param)")
    gl.print_cuadruples()


if __name__ == '__main__':
    main(sys.argv)
