from symbols_table_hash import SymbolsTable
from validate_token import Token
import re

class Scanner:
    def __init__(self, _program=''):
        self.__symbols_table = SymbolsTable()
        self.__program = _program
        self.__types = ['int', 'real', 'char', 'string', 'bool', 'array', 'none']
        self.__operators = ['<', '>', '<=', '>=', '=', '!=', '+', '-', '/', '//', '%', '*', ':=', '&', '|']
        self.__reserved_words = self.__types + ['if', 'while', 'then', 'do', 'print', 'read', 'return', 'main']
        self.__separators = ['[', ']', '(', ')', '$', ' ', '.']  # $ -> is for comments
        self.__pif = []
        self.statements = []
        # self.__read_program()

    def __read_program(self):
        file = open('p1.txt', 'r')
        for line in file:
            self.__statements.appens(line)

    def parse(self):
        statements = self.__program.split('.')
        for statement in statements:
            tokens = statement.split(' ')
            for tok in tokens:
                if tok in self.__reserved_words or tok in self.__operators or tok in self.__separators:
                    self.__pif.append([tok, 0])
                else:
                    token = Token(tok)

                    if token.is_identifier() or token.is_constant():
                        key = self.__symbols_table.add_symbol(token.token)
                        self.__pif.append([token.token, key])
                    else:
                        raise ValueError('Lexical error: ' + token.token)


if __name__ == '__main__':
    p1 = "int divisorsSum: int nr.[.int sum.sum := 0.int i.i = 1.while i <= nr do.[.if nr % i = 0 then.[.sum := sum + i.].i := i + 1.].return sum.]"
    scanner = Scanner(p1)
    scanner.parse()

    perr = "real sum: real 1nr, real 2nr. #. return 1nr + 2nr."
    scanner = Scanner(perr)
    scanner.parse()
