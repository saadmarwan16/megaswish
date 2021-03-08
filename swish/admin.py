from django.contrib import admin

# Register your models here.
from .models import User

# Register the User, AuctionListing, Bid and Comment models
admin.site.register(User)