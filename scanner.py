from symbols_table_hash import SymbolsTable
from validate_token import Token
from pif import PIF
import re


class Scanner:
    def __init__(self, file):
        self.__symbols_table = SymbolsTable()
        self.__types = ['int', 'real', 'char', 'string', 'bool', 'array', 'none']
        self.__operators = ['<', '>', '<=', '>=', '=', '!=', '+', '-', '/', '//', '%', '*', ':=', '&', '|']
        self.__reserved_words = self.__types + ['if', 'while', 'then', 'do', 'print', 'read', 'return', 'main']
        self.__separators = ['[', ']', '(', ')', '$', ' ', '.', '{', '}']  # $ -> is for comments
        self.__pif = PIF()
        self.__file = file

    def parse(self):
        with open(self.__file, 'r') as file:
            for i, line in enumerate(file):
                l = line.strip()
                statements = l.split('.')

                for statement in statements:
                    tokens = statement.split(' ')
                    for tok in tokens:
                        if tok == '':
                            continue
                        if tok in self.__reserved_words or tok in self.__operators or tok in self.__separators:
                            self.__pif.add(0, tok)
                        else:
                            token = Token(tok)

                            if token.is_identifier() or token.is_constant():
                                key = self.__symbols_table.add_symbol(token.token)
                                self.__pif.add(key, token.token)
                            else:
                                raise ValueError('Lexical error at line ' + str(i) + ': ' + token.token)

    def write_files(self):
        problem = self.__file.split('.')[0]
        st_file = problem + '_st.out'
        pif_file = problem + '_pif.out'
        with open(st_file, 'w') as st:
            st.write(str(self.__symbols_table))
        with open(pif_file, 'w') as pif:
            pif.write(str(self.__pif))

