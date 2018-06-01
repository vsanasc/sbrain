from django.http import JsonResponse
from django.views.generic import View


class WrapperView(View):

    view_factory = None

    def get(self, request, *args, **kwargs):
        kwargs.update(request.GET)
        body, status = self.view_factory.create().get(**kwargs)

        return JsonResponse(body, status=status)


    def post(self, request, *args, **kwargs):
        kwargs.update(request.GET)
        kwargs.update(request.POST)
        body, status = self.view_factory.create().get(**kwargs)

        return JsonResponse(body, status=status)