from apps.core.views import FightViewSet
from django.urls import path

urlpatterns = [
    path("fight/", FightViewSet.as_view()),
]
