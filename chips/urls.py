from django.urls import path
from . import views

app_name = 'chips'

urlpatterns = [
    path("", views.year_view), 
    path("year/", views.year_view, name="year_view"),
    path("day/<int:year>/<int:month>/<int:day>/", views.day_detail, name="day_detail"),
]