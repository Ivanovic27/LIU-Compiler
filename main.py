import sys
from antlr4 import *
from grammar.LiuLexer import LiuLexer
from grammar.LiuParser import LiuParser
from semantic_analyzer import SemanticAnalyzer

# TODO: Change Variables and Functions to Classes.
# TODO: Change equal for only 2 parameters.
# TODO: Change print cuadruples to have only left.


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


if __name__ == '__main__':
    main(sys.argv)
