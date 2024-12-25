from rest_framework import filters


class BaseOrderingFilter(filters.OrderingFilter):
    """Base ordering class"""

    ordering_param = "order_by"
