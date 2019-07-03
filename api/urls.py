from rest_framework import routers
from rest_framework.response import Response
from rest_framework.authtoken import views as auth_token_views
from django.urls import path
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from djoser.views import UserCreateView
from . import views


router = routers.SimpleRouter()
router.register(r'todos', views.TodoViewSet, basename='todo')

schema_view = get_swagger_view(title='ToDo API')

urlpatterns = [
    path('auth/token', auth_token_views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/create', UserCreateView.as_view()),
    url(r'^$', schema_view),
    *router.urls,
]
