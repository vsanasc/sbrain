from django.contrib.auth.models import User
from finance.models import (
    ExpenseType,
    ExpenseCategory,
    Expense,
    IncomeType,
    Income
)

from dateutil.relativedelta import relativedelta
from core.utils import list_months
from enum import Enum

import datetime


class TypeCell(str, Enum):
    month = 'month'
    value = 'value'
    name = 'name'
    totalRow = 'total_row'
    totalColumn = 'total_column'
    averageRow = 'average_row'
    title = 'title'
    blank = 'blank'


class TableDatabaseRepo(object):

    def __init__(self):
        self.incomesMonthValue = {}
        self.expenseMonthValue = {}
        self.table = []
        self.user = None
        self.date = None
        self.start = None
        self.end = None
        self.months = []

    def get_table(self, user, year, month, before, after):
        
        self.user = User.objects.all().first()
        self.date = datetime.date(year, month, 1)

        self.start = self.date - relativedelta(months=before)
        self.end = self.date + relativedelta(months=after)
        
        self.months = list_months(self.start, self.end)

        self._get_months()
        self._get_incomes()
        self._get_expenses()
        self._get_totals()


        return self.table

    def _get_months(self):

        row = []
        row.append(
            {
                'text': '',
                'type': TypeCell.blank
            }
        )
        for m in self.months:
            self.incomesMonthValue[m.strftime('%Y-%m')] = 0
            self.expenseMonthValue[m.strftime('%Y-%m')] = 0
            row.append(
                {
                    'text': m.strftime('%b %Y'),
                    'date': m,
                    'type': TypeCell.month
                }
            )
        row.append(
            {
                'text': "Totals",
                'type': TypeCell.totalRow
            }
        )
        row.append(
            {
                'text': "Avg",
                'type': TypeCell.averageRow
            }
        )

        self.table.append(row)

    def _get_incomes(self):

        self.table.append(
            [
            {
                'text': 'Income',
                'type': TypeCell.title,
                'merge': len(self.table[0])
            }
            ]
        )
        
        incomeTypes = IncomeType.objects.filter(
                                            user=self.user,
                                            status=1 
                                        )
        for item in incomeTypes:
            row = []
            totals = 0
            for (index, date) in enumerate(self.table[0]):
                if date['type'] == TypeCell.blank:
                    row.append(
                        {
                            'text': item.name,
                            'type': TypeCell.name,
                            'note': item.note
                        }
                    )
                        
                elif date['type'] == TypeCell.month:
                    incomes = Income.objects.filter(
                                            type=item,
                                            date__year=date['date'].year,
                                            date__month=date['date'].month
                                        ).values_list(
                                            'value',
                                            flat=True
                                        )
                    subtotal = sum(incomes)
                    keyTotalMonth = date['date'].strftime('%Y-%m')
                    self.incomesMonthValue[keyTotalMonth] += subtotal
                    totals += subtotal
                    subtotalStr = '{:0,.2f}'.format(subtotal)
                    row.append(
                        {
                            'text': '{} {}'.format(item.currency, subtotalStr),
                            'type': TypeCell.value,
                            'value': subtotal
                        }
                    )
                elif date['type'] == TypeCell.totalRow:
                    totalStr = '{:0,.2f}'.format(totals)
                    row.append(
                        {
                            'text': '{} {}'.format(item.currency, totalStr),
                            'type': TypeCell.value,
                            'value': totals
                        }
                    )
                else:
                    average = round(totals/len(self.months), 2)
                    row.append(
                        {
                            'text': '{} {}'.format(item.currency, average),
                            'type': TypeCell.averageRow,
                            'value': average
                        }
                    )

            self.table.append(row)

        # total Income
        totalsRow = []
        for date in self.table[0]:

            if date['type'] == TypeCell.blank:
                totalsRow.append(
                    {
                        'text': 'Total income:',
                        'type': TypeCell.totalColumn
                    }
                )
            elif date['type'] == TypeCell.month:
                keyTotalMonth = date['date'].strftime('%Y-%m')
                value = self.incomesMonthValue[keyTotalMonth]
                totalsRow.append(
                    {
                        'text': '{}'.format(value),
                        'value': value
                    }
                )

        self.table.append(totalsRow)


    def _get_expenses(self):

        self.table.append(
            [
            {
                'text': 'Expenses',
                'type': TypeCell.title,
                'merge': len(self.table[0])
            }
            ]
        )

        categories = ExpenseCategory.objects.filter(
                                            user=self.user,
                                            status=1
                                        ).order_by(
                                            'order'
                                        )


        for cat in categories:

            self.table.append(
                [
                    {
                        'text': cat.name,
                        'type': TypeCell.name,
                    }  
                ]
            )

            types = ExpenseType.objects.filter(
                                            category=cat
                                        ).order_by('-importance')

            for item in types:
                row = []
                totals = 0
                for (index, date) in enumerate(self.table[0]):

                    if date['type'] == TypeCell.blank:
                        row.append(
                            {
                                'text': item.name,
                                'type': TypeCell.name,
                            }
                        )
                    elif date['type'] == TypeCell.month:

                        values = Expense.objects.filter(
                                            type=item,
                                            date__year=date['date'].year,
                                            date__month=date['date'].month
                                        ).values_list(
                                            'value',
                                            flat=True
                                        )
                        subtotal = sum(values)
                        keyTotalMonth = date['date'].strftime('%Y-%m')
                        self.expenseMonthValue[keyTotalMonth] += subtotal
                        totals += subtotal
                        subtotalStr = '{:0,.2f}'.format(subtotal)
                        row.append(
                            {
                                'text': '{} {}'.format(item.currency, subtotalStr),
                                'type': TypeCell.value,
                                'value': subtotal
                            }
                        )
                    elif date['type'] == TypeCell.totalRow:
                        totalStr = '{:0,.2f}'.format(totals)
                        row.append(
                            {
                                'text': '{} {}'.format(item.currency, totalStr),
                                'type': TypeCell.value,
                                'value': totals
                            }
                        )
                    else:
                        
                        average = round(totals/len(self.months), 2)
                        row.append(
                            {
                                'text': '{} {}'.format(item.currency, average),
                                'type': TypeCell.averageRow,
                                'value': average
                            }
                        )

                self.table.append(row)

    def _get_totals(self):
        print(self.expenseMonthValue, self.incomesMonthValue)



class TableCacheRepo(object):

    def get_table(self, user, year, month, before, after):
        return None

    def save_table(self, table):
        pass


class TableRepo(object):

    def __init__(self, db_repo, cache_repo):
        self.db_repo = db_repo
        self.cache_repo = cache_repo

    def get_table(self, user, year, month, before, after):

        table = self.cache_repo \
                    .get_table(
                        user,
                        year,
                        month,
                        before,
                        after
                    )

        if table is None:
            table = self.db_repo \
                        .get_table(
                            user,
                            year,
                            month,
                            before,
                            after
                        )
            self.cache_repo.save_table(table)

        return table
