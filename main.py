from lexer.lexer import lexer
from lexer.source_line import sourceLine
from until.error import languageError

def main():
    print('WinA 1.0.0, x64, null:')
    while True:
        line = input(">")
        if line == 'quit()': break

        try:
            line = sourceLine(line)
            tokens = lexer.make_tokens(line)
            print(tokens)
        except languageError as error:
            print(error)

if __name__ == '__main__':
    main()