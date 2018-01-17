from logger_config import logger

logger = logger('employee.log', __file__, 'file')


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

if emp1.first != 'Dilip':
    logger.error("Invalid first name")
