from django.conf.urls import url, include

import adminpage.views as view

urlpatterns = [
    url(r'^$', view.index),
]