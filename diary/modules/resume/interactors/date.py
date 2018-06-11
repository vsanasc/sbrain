

class GetDateInteractor(object):

    def __init__(self, repo):
        self.repo = repo

    def set_params(self, user, year, month, day):
        self.user = user
        self.year = year
        self.month = month
        self.day = day

        return self

    def execute(self):
        return self.repo.get_date(
                                    self.user,
                                    self.year,
                                    self.month,
                                    self.day
                                )