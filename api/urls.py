from django.urls import path, include

urlpatterns = [
    path('user/',
        include(('api.user.urls', 'user'), namespace='user')),
    path('trip/',
        include(('api.trip.urls', 'trip'), namespace='trip')),
]
