
class TableView(object):

    def __init__(self, interactor):
        self.interactor = interactor

    def get(self, **kwargs):

        user = kwargs.get('user')
        year = kwargs.get('year')
        month = kwargs.get('month')
        before = kwargs.get('before')
        after = kwargs.get('after')

        body = self.interactor.set_params(
                    user,
                    year,
                    month,
                    before,
                    after
                ).execute()
        status = 200

        return body, status
