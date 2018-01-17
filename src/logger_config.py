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


def logger(logfile, loggername,handler):
    logger = logging.getLogger(loggername.split('/')[-1])
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(name)s->%(asctime)s->%(levelname)s->%(message)s')
    file_handler.setFormatter(formatter)
    if handler == 'file':
        stream_handler = logging.FileHandler(logfile)
    else:
        stream_handler = logging.StreamHandler()

    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
