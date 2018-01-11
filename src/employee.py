import logging

# changing logging default configurations
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('employee.log')

formatter = logging.Formatter('%(name)s->%(asctime)s->%(levelname)s->%(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Employee created: {}'.format(self.fullname))

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('John', 'Doe')
emp2 = Employee('Jane', 'Doe')
