import logging
import employee

"""
# DEBUG : Detailed information ,typically of interest only when diagnosing problems
# INFO : Confirmation that things are working as expected.

#WARNING:An indication that something unexpected happened,
or indicative of some problem in the near future (e.g 'disk space low').
The software is still working as expected.

# ERROR :Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL : A serious error, indicating that the program itself may be unable to continue running
"""

# changing logging default configurations
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('basic.log')
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(name)s->%(asctime)s->%(levelname)s->%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.error("Tried to divide by zero")
    else:
        return result


num1 = 5
num2 = 0

add_result = add(num1, num2)
sub_result = subtract(num1, num2)
mul_result = multiply(num1, num2)
div_result = divide(num1, num2)

if add_result == 15:
    logger.debug("Addition works perfectly.")
elif add_result < 15:
    logger.warning("Its horrible add function.")
elif add_result < 0:
    logger.info("Gosh, you got to test your function.")
else:
    logger.critical("I have no idea what's going on.")
