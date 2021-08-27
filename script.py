import sys
from io import StringIO
import curses

UPLINE = '\033[A'

def handler(text):
    '''
    RUSH BANANA NO STOP GRANADA
    '''
    print('\n' + '-' * 75)
    print(f'\033[1m\033[96mAlright folk I obviously see you typed \033[91m{text}\033[96m so chill bruh')



if __name__ == '__main__':
    if (len(sys.argv) >= 2):
        input_text = " ".join(sys.argv[1:])
        sys.stdout.write('\033[s')
        handler(input_text)
        sys.stdout.write(f'\033[u')
