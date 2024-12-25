from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit

from core.utils import BaseViewSet
from amazon.models import Rnr
from .filters import RnrFilterSet
from .permission import RnrPermission
from .serializer import RnrSerializer, RnrListSerializer


class RnrViewSet(BaseViewSet):
	queryset = Rnr.objects.all()
	serializer_class = RnrSerializer
	filterset_class = RnrFilterSet
	permission_classes = [RnrPermission]
	http_method_names = ["get", "post"]
	
	def get_serializer(self, *args, **kwargs):
		kwargs["context"] = self.get_serializer_context()
		match self.action:
			case "list" | "retrieve":
				return RnrListSerializer(*args, **kwargs)
			case _:
				return super().get_serializer(*args, **kwargs)
	
	@method_decorator(ratelimit(key='ip', rate='10/m', method='POST', block=True))
	def create(self, request, *args, **kwargs):
		"""Create product"""
		return super().create(request, *args, **kwargs)
