from diary.modules.resume.serializers import DateSerializer

class DateView(object):

    def __init__(self, interactor):
        self.interactor = interactor

    def get(self, **kwargs):

        user = kwargs.get('user')
        year = kwargs.get('year')
        month = kwargs.get('month')
        day = kwargs.get('day')

        date = self.interactor \
                .set_params(
                    user,
                    year,
                    month,
                    day
                ).execute()

        body = DateSerializer.serialize(date)
        status = 200

        return body, status