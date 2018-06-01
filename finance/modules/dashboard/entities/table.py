

class TableEntity(object):

    def __init__(self, months, incomes, expenses):
        self._months = months
        self._incomes = incomes
        self._expenses = expenses

    @property
    def months(self):
        return self._months

    @property
    def incomes(self):
        return self._incomes

    @property
    def expenses(self):
        return self._expenses
