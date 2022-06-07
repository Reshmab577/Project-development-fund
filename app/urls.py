from django.urls import path
from .import views


urlpatterns = [
    path('' ,views.function,name='function'),
    path('login/',views.app,name='app')

]