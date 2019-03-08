import sys
from antlr4 import *
from grammar.LiuLexer import LiuLexer
from grammar.LiuParser import LiuParser


def main(argv):
    input = FileStream(argv[1])
    lexer = LiuLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LiuParser(stream)
    tree = parser.programa()


if __name__ == '__main__':
    main(sys.argv)
