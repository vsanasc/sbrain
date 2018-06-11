from diary.modules.resume.repositories import (
    DateDatabaseRepo,
    DateCacheRepo,
    DateRepo
)

from diary.modules.resume.views import (
    DateView
)

from diary.modules.resume.interactors import (
    GetDateInteractor
)


class DateDatabaseRepoFactory(object):

    @staticmethod
    def get():
        return DateDatabaseRepo()


class DateCacheRepoFactory(object):

    @staticmethod
    def get():
        return DateCacheRepo()


class DateRepoFactory(object):

    @staticmethod
    def get():
        db_repo = DateDatabaseRepoFactory.get()
        cache_repo = DateCacheRepoFactory.get()
        return DateRepo(db_repo, cache_repo)


class GetDateInteractorFactory(object):

    @staticmethod
    def get():
        repo = DateRepoFactory.get()
        return GetDateInteractor(repo)


class DateViewFactory(object):

    @staticmethod
    def create():
        interactor = GetDateInteractorFactory.get()
        return DateView(interactor)
