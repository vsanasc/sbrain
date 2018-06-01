from finance.modules.dashboard.repositories import (
    TableDatabaseRepo,
    TableCacheRepo,
    TableRepo
)

from finance.modules.dashboard.views import (
    TableView
)

from finance.modules.dashboard.interactors import (
    GetTableInteractor
)

class TableDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return TableDatabaseRepo()

class TableCacheRepoFactory(object):

    @staticmethod
    def get():
        return TableCacheRepo()

class TableRepoFactory(object):

    @staticmethod
    def get():
        db_repo = TableDatabaseRepoFactory.get()
        cache_repo = TableCacheRepoFactory.get()
        return TableRepo(db_repo, cache_repo)

class GetTableInteractorFactory(object):

    @staticmethod
    def get():
        repo = TableRepoFactory.get()
        return GetTableInteractor(repo)


class TableViewFactory(object):

    @staticmethod
    def create():
        interactor = GetTableInteractorFactory.get()
        return TableView(interactor)