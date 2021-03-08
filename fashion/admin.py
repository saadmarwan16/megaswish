from django.contrib import admin

# Register your models here.
from .models import FashionProduct, FashionProductWishList, FashionProductCart, FashionProductRating, FashionProductReview, FashionProductOrder

# Register the User, AuctionListing, Bid and Comment models
admin.site.register(FashionProduct)
admin.site.register(FashionProductWishList)
admin.site.register(FashionProductCart)
admin.site.register(FashionProductRating)
admin.site.register(FashionProductReview)
admin.site.register(FashionProductOrder)