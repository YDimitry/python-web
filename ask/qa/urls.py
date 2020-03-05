from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    re_path(r'question/(?P<id>\d+)/?', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('popular/', views.popular, name='popular'),
    path('new/', views.new, name='new'),
    # path('filldb/', views.filldb, name='filldb'),
]