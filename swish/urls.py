from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("start-registration", views.start_registration, name="start_registration"),
    path("confirm-registration", views.confirm_registration, name="confirm_registration"),
    path(
        "complete-registration/<str:uidb64>/<str:token>", 
        views.complete_registration, 
        name="complete_registration"
    ),
    path("login", views.login_view, name="login_view"),
    path("reset-password", views.reset_password, name="reset_password"),
    path("logout", views.logout_view, name="logout_view"),
    path("contact-us", views.contact_us, name="contact_us"),
]