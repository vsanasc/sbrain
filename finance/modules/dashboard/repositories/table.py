from finance.modules.dashboard.entities import TableEntity


class TableDatabaseRepo(object):

    def get_table(self, user, year, month, before, after):
        return TableEntity('', '', '')


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
