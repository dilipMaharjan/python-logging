from logger_config import logger

logger = logger('basics.log', __file__,'console')

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
