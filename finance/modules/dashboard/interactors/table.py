

class GetTableInteractor(object):

    def __init__(self, repo):
        self.repo = repo


    def set_params(self, user, year, month, before, after):
        self.user = user
        self.year = year
        self.month = month
        self.before = before
        self.after = after

        return self

    def execute(self):
        return self.repo.get_table(
                                    self.user,
                                    self.year,
                                    self.month,
                                    self.before,
                                    self.after
                                )