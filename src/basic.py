import logging

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

logging.basicConfig(filename='python.log', level=logging.DEBUG, format='%(asctime)s^%(levelname)s^%(message)s')


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


num1 = 5
num2 = 10

add_result = add(num1, num2)
sub_result = subtract(num1, num2)
mul_result = multiply(num1, num2)
div_result = divide(num1, num2)

if add_result == 15:
    logging.info("Addition works perfectly.")
elif add_result < 15:
    logging.warning("Its horrible add function.")
elif add_result < 0:
    logging.debug("Gosh, you got to test your function.")
else:
    logging.critical("I have no idea what's going on.")
