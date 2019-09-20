
from dateutil.relativedelta import relativedelta

def list_months(start, end):
    final = end + relativedelta(months=1)
    values = []
    current = start
    while current < final:
        values.append(current)
        current = current + relativedelta(months=1)

    return values
    
