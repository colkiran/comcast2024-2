
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

def quot(x, y):
    return x / y

a = 20
b = 8

logging.debug(f'the difference of {a} and {b} is :{quot(a, b)}')
logging.info(f'the difference of {a} and {b} is :{quot(a, b)}')

a = 8
b = 20

logging.warning(f'the difference of {a} and {b} is :{quot(a, b)}')

a = 8
b = 0

try :
    quot(a, b)
except:
    logging.error(sys.exc_info()[0])
    logging.critical(sys.exc_info()[1])
