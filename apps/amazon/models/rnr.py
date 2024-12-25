from django.db import models

from core.models import BaseModel
from amazon.models import Marketplace


class Rnr(BaseModel):
    asin = models.CharField(max_length=255, blank=True, null=True)
    marketplace = models.ForeignKey(
        Marketplace, on_delete=models.PROTECT, blank=True, null=True
    )
    child_one_star_reviews_count = models.IntegerField(blank=True, null=True)
    child_one_star_rating_count = models.IntegerField(blank=True, null=True)
    child_two_star_reviews_count = models.IntegerField(blank=True, null=True)
    child_two_star_rating_count = models.IntegerField(blank=True, null=True)
    child_three_star_reviews_count = models.IntegerField(blank=True, null=True)
    child_three_star_rating_count = models.IntegerField(blank=True, null=True)
    child_four_star_reviews_count = models.IntegerField(blank=True, null=True)
    child_four_star_rating_count = models.IntegerField(blank=True, null=True)
    child_five_star_reviews_count = models.IntegerField(blank=True, null=True)
    child_five_star_rating_count = models.IntegerField(blank=True, null=True)
    child_total_rating = models.IntegerField(blank=True, null=True)
    child_total_reviews = models.IntegerField(blank=True, null=True)
    
    child_verified_total_rating = models.IntegerField(blank=True, null=True)
    child_verified_total_reviews = models.IntegerField(blank=True, null=True)
    child_verified_one_star_reviews_count = models.IntegerField(blank=True, null=True)
    child_verified_one_star_rating_count = models.IntegerField(blank=True, null=True)
    child_verified_two_star_reviews_count = models.IntegerField(blank=True, null=True)
    child_verified_two_star_rating_count = models.IntegerField(blank=True, null=True)
    child_verified_three_star_reviews_count = models.IntegerField(blank=True, null=True)
    child_verified_three_star_rating_count = models.IntegerField(blank=True, null=True)
    child_verified_four_star_reviews_count = models.IntegerField(blank=True, null=True)
    child_verified_four_star_rating_count = models.IntegerField(blank=True, null=True)
    child_verified_five_star_reviews_count = models.IntegerField(blank=True, null=True)
    child_verified_five_star_rating_count = models.IntegerField(blank=True, null=True)
    
    parent_verified_total_rating = models.IntegerField(blank=True, null=True)
    parent_verified_total_reviews = models.IntegerField(blank=True, null=True)
    parent_verified_one_star_reviews_count = models.IntegerField(blank=True, null=True)
    parent_verified_one_star_rating_count = models.IntegerField(blank=True, null=True)
    parent_verified_two_star_reviews_count = models.IntegerField(blank=True, null=True)
    parent_verified_two_star_rating_count = models.IntegerField(blank=True, null=True)
    parent_verified_three_star_reviews_count = models.IntegerField(blank=True, null=True)
    parent_verified_three_star_rating_count = models.IntegerField(blank=True, null=True)
    parent_verified_four_star_reviews_count = models.IntegerField(blank=True, null=True)
    parent_verified_four_star_rating_count = models.IntegerField(blank=True, null=True)
    parent_verified_five_star_reviews_count = models.IntegerField(blank=True, null=True)
    parent_verified_five_star_rating_count = models.IntegerField(blank=True, null=True)
    
    parent_total_rating = models.IntegerField(blank=True, null=True)
    parent_total_reviews = models.IntegerField(blank=True, null=True)
    parent_one_star_reviews_count = models.IntegerField(blank=True, null=True)
    parent_one_star_rating_count = models.IntegerField(blank=True, null=True)
    parent_two_star_reviews_count = models.IntegerField(blank=True, null=True)
    parent_two_star_rating_count = models.IntegerField(blank=True, null=True)
    parent_three_star_reviews_count = models.IntegerField(blank=True, null=True)
    parent_three_star_rating_count = models.IntegerField(blank=True, null=True)
    parent_four_star_reviews_count = models.IntegerField(blank=True, null=True)
    parent_four_star_rating_count = models.IntegerField(blank=True, null=True)
    parent_five_star_reviews_count = models.IntegerField(blank=True, null=True)
    parent_five_star_rating_count = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = '"amazon"."rnr"'
        verbose_name = "Rating And Reviews"
        verbose_name_plural = "Rating And Reviews"
