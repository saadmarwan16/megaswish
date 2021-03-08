from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_subscriber = models.BooleanField(default=False)

    # Ensure password is valid
#     if not user.is_password_valid():
#         return render(request, "network/register.html", {
#             "message": "Password must be at least 8 characters long, contain one uppercase, one lower case, one digit"
#         })

#     # Ensure password matches confirmation
#     elif not user.do_passwords_match:
#         return render(request, "network/register.html", {
#             "message": "Passwords must match."
#         })

    # def __str__(self):
        #     return f"{self.username}"

        # def is_password_valid(self):
        #     """
        #     Returns true password has at least one uppercase, at least one lower case, at least one digit and
        #     is at least eight character long
        #     """

        #     return (any(c.isupper() for c in self.password) and any(c.islower() for c in self.password)
        #         and any(c.isdigit() for c in self.password) and len(self.password) >= 8)

        # def do_passwords_match(self, confirmation):
        #     return self.password == confirmation

        #     return render(request, "swish/complete-registration.html", {
        #         "firstname": firstname,
        #         "lastname": lastname,
        #         "email": email
        #     })


class Product():
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=64, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=64)
    num_left_in_stock = models.PositiveIntegerField(default=0)
    time_posted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)