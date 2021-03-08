from django.contrib.auth.models import AbstractUser
from django.db import models

from swish.models import User, Product

class FashionProduct(models.Model, Product):
    image = models.ImageField(upload_to="fashion-product-image/", blank=False, null=False)
    size = models.PositiveIntegerField(default=0)


class UserFashionProduct():
    timestamp = models.DateTimeField(auto_now_add=True)


class FashionProductWishList(models.Model, UserFashionProduct):
    is_wishlisted = models.BooleanField()
    product = models.ForeignKey(FashionProduct, on_delete=models.CASCADE, related_name="on_wishlist_fashion")
    user = models.ManyToManyField(User, related_name="wishlisted_fashion")


class FashionProductCart(models.Model, UserFashionProduct):
    is_in_cart = models.BooleanField()
    product = models.ForeignKey(FashionProduct, on_delete=models.CASCADE, related_name="on_cart_fashion")
    user = models.ManyToManyField(User, related_name="carted_fashion")


class FashionProductRating(models.Model, UserFashionProduct):
    number_of_stars = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(FashionProduct, on_delete=models.CASCADE, related_name="on_rating_fashion")
    user = models.ManyToManyField(User, related_name="rated_fashion")

class FashionProductReview(models.Model, UserFashionProduct):
    content = models.TextField(blank=False)
    product = models.ForeignKey(FashionProduct, on_delete=models.CASCADE, related_name="on_review_fashion")
    user = models.ManyToManyField(User, related_name="reviewed_fashion")

class FashionProductOrder(models.Model, UserFashionProduct):
    is_cancelled = models.BooleanField()
    is_completed = models.BooleanField()
    product = models.ForeignKey(FashionProduct, on_delete=models.CASCADE, related_name="on_order_fashion")
    user = models.ManyToManyField(User, related_name="ordered_fashion")