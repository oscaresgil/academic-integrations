# -*- coding: utf-8 -*-
from django.conf.urls import url

import views

urlpatterns = [
    url(
        r'^student/(?P<student_code>[-A-Za-z0-9_]+)/enroll/$',
        views.enroll_student,
        name='enroll_student'
    ),
    url(
        r'^(?P<student_id>[\w.@+-]+)/registration/$',
        views.registration,
        name='odoo-registration'
    ),
    url(
        r'^(?P<student_id>[\w.@+-]+)/client-edition/$',
        views.client_edition,
        name='odoo-client-edition'
    ),
    url(
        r'^search/clients/$',
        views.search_clients,
        name='odoo-search-clients'
    ),
    url(
        r'^ajax/tutor-invoice/$',
        views.tutor_invoice,
        name='odoo-tutor-invoice'
    )
]
