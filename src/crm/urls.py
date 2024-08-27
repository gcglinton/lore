from django.urls import path

from . import views

app_name = "crm"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # ex: /crm/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
