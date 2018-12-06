from finance.modules.dashboard.serializers import TableSerializer


class TableView(object):

    def __init__(self, interactor):
        self.interactor = interactor

    def get(self, **kwargs):

        user = kwargs.get('user')
        year = kwargs.get('year')
        month = kwargs.get('month')
        before = kwargs.get('before')
        after = kwargs.get('after')

        table = self.interactor.set_params(
                    user,
                    year,
                    month,
                    before,
                    after
                ).execute()

        body = TableSerializer.serialize(table)
        status = 200

        return body, status
