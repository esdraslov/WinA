import keyboard

def main():
    print('WinA 1.0.0, x64, null:')
    while True:
        line = input(">")
        if line == 'quit()' or keyboard.is_pressed('ctrl+c'): break

if __name__ == '__main__':
    main()