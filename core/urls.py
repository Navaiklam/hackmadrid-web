from django.urls import path
from .views import eventos, cfpblack, home
urlpatterns = [
    path('', home, name="home"),
    path('actividades/', eventos, name="eventos"),
    path('cfp-black/', cfpblack, name="cfp-black"),

]

