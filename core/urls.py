from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login as user_login
from django.conf import settings

from core.views import (
    permission_denied_view,
    page_not_found,
    server_error,
    gateway_timeout
)
from core.views import user_logout

handler403 = permission_denied_view
handler404 = page_not_found
handler500 = server_error
handler504 = gateway_timeout

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^user-login/$', user_login, {
            'template_name': 'login_form.html',
            'redirect_field_name': 'next'
        }, name='user-login-form'),

    url(r'^logout/$', user_logout, {
            'login_url': '/'
        }, name='logout'),

    url(r'^', include('inventory.urls'),
        name="home"),
    ]

if settings.DEBUG:
    urlpatterns += [
        # test error pages urls
        url(r'^404/', handler404),
        url(r'^403/', handler403),
        url(r'^500/', handler500),
        url(r'^504/', handler504),
    ]
