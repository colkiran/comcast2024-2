

import logging
import sys
import time

logging.basicConfig(filename="myfile.log", filemode="a",
                    level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

logging.debug(str(time.perf_counter()).center(60, "-"))
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
