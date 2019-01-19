from rest_framework.viewsets import ModelViewSet

from apps.trip.models import Trip


class TripViewSet(ModelViewSet):
    # 여행 뷰셋
    queryset = Trip.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.filter(
            user=self.request.user
        )