from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import (
    HttpResponseNotFound,
    HttpResponseServerError,
    HttpResponseForbidden,
    HttpResponseRedirect
)
from django.template.loader import render_to_string
from django.template import RequestContext
from django.views.generic.base import RedirectView


def page_not_found(request):
    """View for Error 404

    :param request: HttpRequest
    :return: HttpResponse
    """
    return HttpResponseNotFound(
        render_to_string("404.html", RequestContext(request)))


def permission_denied_view(request):
    """View for Error 403

    :param request: HttpRequest
    :return: HttpResponse
    """
    return HttpResponseForbidden(
        render_to_string('403.html', RequestContext(request)))


def server_error(request):
    """View for Error 500

    :param request: HttpRequest
    :return: HttpResponse
    """
    return HttpResponseServerError(
        render_to_string("500.html", RequestContext(request)))


def gateway_timeout(request):
    """View for Error 504

    :param request: HttpRequest
    :return: HttpResponse
    """
    return HttpResponseServerError(
        render_to_string("500.html", RequestContext(request)))


def user_logout(request, login_url=False):
    """Override logout view.

    :param request: HttpRequest
    :return: HttpResponse
    """
    logout(request)
    if login_url:
        return HttpResponseRedirect('%s?next=%s' % (reverse('user-login-form'),
                                                    login_url))
    else:
        return HttpResponseRedirect(reverse('home'))
