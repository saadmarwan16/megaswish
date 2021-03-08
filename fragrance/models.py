from django.contrib.auth.models import AbstractUser
from django.db import models

from swish.models import User, Product

class FragranceProduct(models.Model, Product):
    image = models.ImageField(upload_to="fragrance-product-image/", blank=False, null=False)
    volume = models.PositiveIntegerField(default=0)


class UserFragranceProduct():
    timestamp = models.DateTimeField(auto_now_add=True)


class FragranceProductWishList(models.Model, UserFragranceProduct):
    is_wishlisted = models.BooleanField()
    product = models.ForeignKey(FragranceProduct, on_delete=models.CASCADE, related_name="on_wishlist_fragrance")
    user = models.ManyToManyField(User, related_name="wishlisted_fragrance")


class FragranceProductCart(models.Model, UserFragranceProduct):
    is_in_cart = models.BooleanField()
    product = models.ForeignKey(FragranceProduct, on_delete=models.CASCADE, related_name="on_cart_fragrance")
    user = models.ManyToManyField(User, related_name="carted_fragrance")


class FragranceProductRating(models.Model, UserFragranceProduct):
    number_of_stars = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(FragranceProduct, on_delete=models.CASCADE, related_name="on_rating_fragrance")
    user = models.ManyToManyField(User, related_name="rated_fragrance")

class FragranceProductReview(models.Model, UserFragranceProduct):
    content = models.TextField(blank=False)
    product = models.ForeignKey(FragranceProduct, on_delete=models.CASCADE, related_name="on_review_fragrance")
    user = models.ManyToManyField(User, related_name="reviewed_fragrance")

class FragranceProductOrder(models.Model, UserFragranceProduct):
    is_cancelled = models.BooleanField()
    is_completed = models.BooleanField()
    product = models.ForeignKey(FragranceProduct, on_delete=models.CASCADE, related_name="on_order_fragrance")
    user = models.ManyToManyField(User, related_name="ordered_fragrance")