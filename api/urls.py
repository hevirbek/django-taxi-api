from django.urls import path
from . import views

urlpatterns = [
    path('taxi/<int:pk>', views.taxi_detail),
    path('taxi/request_list/<int:tid>', views.request_list),
    path('request/<int:pk>', views.request_detail),
    path('request', views.create_request),
    path('taxi', views.create_taxi),
]
