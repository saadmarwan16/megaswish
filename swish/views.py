from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib import messages
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string, get_template
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

from .utils.promotion_register import ProductsPromotionalSignUp
from .utils.registration_token_generator import token_generator
from .utils.email_thread import EmailThread
from .models import User


def index(request):
    return render(request, "swish/index.html", {
        "categories": ["Belts", "Business Wear", "Fila T-shirts", "Parfume Oils", "Plain T-shirts", 
                        "Shoes", "Socks", "Suits", "Ties"],
        "carousel_images": ["swish/images/perfect.png", "perfect.png", "perfect.png"],
        "numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    })


def start_registration(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        subject = 'Confirm Registration'

        # Firstname, lastname, username and email are all valid
        if firstname and lastname and username and email:

            # Attempt to create new user
            try:
                user = User.objects.create_user(
                    first_name=firstname, 
                    last_name=lastname,
                    username=username,
                    email=email, 
                    password="",
                    is_active=False
                )
                user.save()

            # Another user already exists with the same username or email
            except IntegrityError:
                messages.error(request, "Username or Email already taken.")
                return render(request, "swish/start-registration.html")

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse("complete_registration", kwargs={
                "uidb64": uidb64, 
                "token": token_generator.make_token(user)
            })
            complete_registration_url = "http://"+domain+link

            # Attempt to send a message to user's email address
            try:
                template = render_to_string("swish/confirm-registration-message.html", {
                    "firstname": firstname,
                    "url": complete_registration_url
                })

                email_message = EmailMessage(subject, template, settings.EMAIL_HOST_USER, [email])
                EmailThread(email_message).start()

            # User entered a bad email address
            except BadHeaderError:
                messages.error(request, "Bad email.")
                return render(request, "swish/start-registration.html")

            return HttpResponseRedirect(reverse("confirm_registration"))

        else:
            messages.error(request, "An error occured, please try again.")
            return render(request, "swish/start-registration.html")

    return render(request, "swish/start-registration.html")


def confirm_registration(request):
    return render(request, "swish/confirm-registration.html")


def complete_registration(request, uidb64, token):
    if request.method == "POST":
        password = request.POST.get("password")
        confirmation = request.POST.get("confirm-password")
        opted_out = request.POST.get("opted-out")

        # Make sure passwords are the same
        if password != confirmation:
            return render(request, "swish/complete-registration.html", {
                "uidb64": uidb64,
                "token": token,
                "message": "Passwords must match."
            })

        id = int(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)
        user.set_password(password)
        user.is_active = True

        # # The user has not opted out from mailing list subscription
        # if not opted_out:

        #     # The user has not already subscribed to the mailing list
        #     if not User.objects.filter(id=id, is_subscriber=True).exists():
        #         promotions = ProductsPromotionalSignUp(
        #             settings.MAILCHIMP_API_KEY,
        #             settings.MAILCHIMP_DATA_CENTER,
        #             settings.MAILCHIMP_EMAIL_LIST_ID
        #         )

        #         promotions.subscribe(user.email)
        #         user.is_subscriber = True

        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    return render(request, "swish/complete-registration.html", {
        "uidb64": uidb64,
        "token": token
    })


def login_view(request):

    # User submits a login form
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Invalid username or password")
            return render(request, "swish/login.html")

    # User tries to get the login page
    return render(request, "swish/login.html")


def reset_password(request):
    return render(request, "swish/reset-password.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def contact_us(request):

    name = request.POST.get("name", "")
    from_email = request.POST.get("email", "")
    subject = request.POST.get("subject", "")
    message = request.POST.get("message", "")

    if subject and message and from_email:
        try:
            email_message = EmailMessage(subject, message, from_email, [settings.EMAIL_HOST_USER])
            EmailThread(email_message).start()

        except BadHeaderError:
            print("Bad email")

        return HttpResponseRedirect(reverse("index"))