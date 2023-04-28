class token:
    def __init__(self, kind, line):
        self.kind = kind
        self.line = line
        self.locale, self.string = line.new_locale()

        self.string = self.string or 'EOF'

    def __repr__(self):
        return f'{self.kind[0]}"{self.string}"'

    def mark(self):
        self.line.mark(self)