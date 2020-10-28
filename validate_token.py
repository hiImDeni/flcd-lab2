import re

def is_valid_name(name):
    for char in name:
        if not (char.isalpha() or char.isnumeric() or char == '-' or char == '_'):
            return False
    return True


class Token:
    def __init__(self, token):
        self.token = token

    def is_identifier(self):
        return re.match('[a-zA-Z][a-zA-Z0-9]{0,}', self.token) is not None

    def is_numeric_constant(self):
        if len(self.token) > 1 and self.token[0] == '0':
            return False

        return self.token.isnumeric()

    def is_char_constant(self):
        return ((len(self.token) == 2) or len(self.token) == 3) and self.token[0] == "'" and self.token[-1] == "'"

    def is_string_constant(self):
        return len(self.token) >= 2 and self.token[0] == '"' and self.token[-1] == '"'

    def is_boolean_constant(self):
        return self.token == 'false' or self.token == 'true'

    def is_real_constant(self):
        realConstant = self.token.split(',')
        return len(realConstant) == 2 and realConstant[0].isnumeric() and realConstant[1].isnumeric()

    def is_constant(self):
        return self.is_boolean_constant() or self.is_char_constant() or \
               self.is_numeric_constant() or self.is_real_constant() or self.is_string_constant()
