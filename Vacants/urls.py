from django.urls import path

from . import views

urlpatterns = [
    path("", views.insert_vacant),
    path("verify/", views.verify_vacant),
    path("analyzed/", views.analyzed_vacant),
    path("reported/", views.report_vacant),
    path("admin/", views.admin_page),
]