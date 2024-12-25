from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class BaseLimitOffsetPagination(pagination.LimitOffsetPagination):
    """Limit/Offset pagination"""

    default_limit = 100

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                {
                    "meta": {
                        "limit": self.limit,
                        "next": self.get_next_link(),
                        "offset": self.offset,
                        "previous": self.get_previous_link(),
                        "total_count": self.count,
                    },
                    "objects": data,
                }
            )
        )
