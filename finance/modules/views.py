from django.http import JsonResponse

# Create your views here.

class ViewWrapper(View):

    view_factory = None

    def get(self, request, *args, **kwargs):
        body, status = self.view_factory.create().get(**kwargs)

        return JsonResponse(body, status=status)