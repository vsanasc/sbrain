

class ExpenseEntity(object):

    def __init__(self, name, value, date, currency):
        self._name = name
        self._value = value
        self._date = date
        self._currency = currency

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    @property
    def date(self):
        return self._date

    @property
    def currency(self):
        return self._currency
