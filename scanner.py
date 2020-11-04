from symbols_table_hash import SymbolsTable
from validate_token import Token
from pif import PIF


class Scanner:
    def __init__(self, file):
        self.__symbols_table = SymbolsTable()
        self.__types = ['int', 'real', 'char', 'string', 'bool', 'array', 'none']
        self.__operators = ['<', '>', '<=', '>=', '=', '!=', '+', '-', '/', '%', '*', ':=', '&', '|']
        self.__reserved_words = self.__types + ['if', 'else', 'while', 'then', 'do', 'print', 'read', 'return', 'main']
        self.__separators = ['[', ']', '(', ')', ' ', '.', '{', '}', ';', ':']
        self.__pif = PIF()
        self.__file = file
        self.__set_files()
        self.__errors = []

    def __contains_operator(self, tok):
        for c in tok:
            if c in self.__operators:
                return True

    def __check_token(self, tok, line):
        tok = tok.strip()
        token = Token(tok)
        if token in self.__reserved_words:
            self.__pif.add(0, token.token)
        elif token.is_identifier() or token.is_constant():
            key = self.__symbols_table.add_symbol(token.token)
            self.__pif.add(key, token.token)
        else:
            self.__errors.append('Line ' + str(line) + ': Lexical error: unknown token ' + token.token)

    def get_tokens(self):
        with open(self.__file, 'r') as file:
            for i, line in enumerate(file):
                statement = line.strip()

                tokens = statement.split(' ')
                for tok in tokens:
                    if tok == '':
                        continue
                    tok = tok.strip()
                    if tok in self.__reserved_words or tok in self.__operators or tok in self.__separators:
                        self.__pif.add(0, tok)
                    elif not self.__contains_operator(tok):
                        self.__check_token(tok, i)
                    else:
                        symbol = ''
                        operands = []
                        for char in tok:
                            if char in self.__separators or char in self.__operators:
                                if symbol != '':
                                    operands.append(symbol)
                                symbol = ''
                                self.__pif.add(0, char)
                            else:
                                symbol += char
                        if symbol != '' and symbol not in operands:
                            operands.append(symbol)
                        for operand in operands:
                            self.__check_token(operand, i)

    def __set_files(self):
        problem = self.__file.split('.')[0]
        self.__st_file = problem + '_st.out'
        self.__pif_file = problem + '_pif.out'

    def write_files(self):
        with open(self.__st_file, 'w') as st:
            st.write(str(self.__symbols_table))
        with open(self.__pif_file, 'w') as pif:
            pif.write(str(self.__pif))
            for err in self.__errors:
                pif.write(err)

