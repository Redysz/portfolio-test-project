from django.urls import path
from django.urls import include

import blog.views

urlpatterns = [
    path('', blog.views.allblogs, name='allblogs'),
]
