from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from social_django.views import complete
from django.shortcuts import render_to_response
from django.template import RequestContext,Context,loader



class AuthComplete(View):
    def get(self, request, *args, **kwargs):
        backend = kwargs.pop('backend')

        return complete(request, backend, *args, **kwargs)


class LoginError(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=401)


def error404(request):
    response = render_to_response(
        '400.html',
        context_instance=RequestContext(request)
    )

    response.status_code = 404

    return response