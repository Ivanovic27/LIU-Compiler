import sys
from antlr4 import *
from grammar.LiuLexer import LiuLexer
from grammar.LiuParser import LiuParser
from semantic_analyzer import SemanticAnalyzer


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
