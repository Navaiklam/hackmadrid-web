from django.urls import path
from .views import  eventos, cfpblack, home, objetivos, flaghunters, hackerspace, colaboracion, conferencias, login, world_party
urlpatterns = [
    path('', home, name="home"),
    path('world_party/', world_party, name="world_party"),
    path('actividades/', eventos, name="eventos"),
    path('objetivos/', objetivos, name="objetivos"),
    path('flaghunters/', flaghunters, name="flaghunters"),
    path('hackerspace/', hackerspace, name="hackerspace"),
    path('colaboracion/', colaboracion, name="colaboracion"),
    path('conferencias/', conferencias, name="conferencias"),
    path('cfp-black/', cfpblack, name="cfp-black"),

    path('login/', login, name="login"),

]

