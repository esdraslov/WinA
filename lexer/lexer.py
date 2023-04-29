from until.error import languageError
from .token import token

class lexerError(languageError):
    pass

class lexer:
    def __init__(self):
        self.line = None

    def new_token(self, kind):
        return token(kind, self.line)

    def make_tokens(self, line):
        self.line = line
        tokens = []

        while not self.line.finished():
            self.ignore_spaces()
            if self.line.finished(): break

            tokens += [self.new_token("Punctuator")]

        return tokens

    def ignore_spaces(self):
        while self.line.next().isspace():
            self.line.take()
            self.line.ignore()

    def make_token(self):
        if self.line.next() in '()|_^':
            return self.make_punctuator()
        if self.line.next() in '~+=*/%':
            return self.make_operator()
        if self.line.next() in '1234567890.':
            return self.make_number()

        self.line.take()
        raise lexerError(self.new_token('?'), 'unrecogzed symbol')

    def make_punctuator(self):
        pass

    def make_operator(self):
        pass

    def make_number(self):
        pass