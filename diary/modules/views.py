from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class WrapperView(LoginRequiredMixin, View):

    view_factory = None

    def get(self, request, *args, **kwargs):
        kwargs.update(request.GET)
        kwargs.update({'user': request.user.pk})
        body, status = self.view_factory.create().get(**kwargs)

        return JsonResponse(body, status=status)

    def post(self, request, *args, **kwargs):
        kwargs.update(request.GET)
        kwargs.update(request.POST)
        kwargs.update({'user': request.user.pk})
        body, status = self.view_factory.create().get(**kwargs)

        return JsonResponse(body, status=status)
