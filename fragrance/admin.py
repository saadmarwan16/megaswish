from django.contrib import admin

# Register your models here.
from .models import FragranceProduct, FragranceProductWishList, FragranceProductCart, FragranceProductRating, FragranceProductReview, FragranceProductOrder

# Register the User, AuctionListing, Bid and Comment models
admin.site.register(FragranceProduct)
admin.site.register(FragranceProductWishList)
admin.site.register(FragranceProductCart)
admin.site.register(FragranceProductRating)
admin.site.register(FragranceProductReview)
admin.site.register(FragranceProductOrder)