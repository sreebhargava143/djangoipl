from django.urls import include, path
from rest_framework import routers
from drf_api import views
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.SimpleRouter()
# router.register(r"matches", views.MatchViewSet.as_view({'get':'list', 'post': 'create'}
# ), basename="matches")
# router.register(r"deliveries", views.DeliveryViewSet.as_view({'get': 'list', 'post': 'create'}), basename="deliveries")
# router.register(r"matches/<int:pk>", views.MatchDetailViewSet.as_view({'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'}), basename="match_detail")
# router.register(r"deliveries/<int:pk>", views.DeliveryDetailViewSet.as_view({'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'}), basename="delivery_detail")

urlpatterns = [
    #  path(r'', include(router.urls)),
    path('matches/', views.MatchViewSet.as_view()),
    path('matches/<int:pk>/', views.MatchDetailViewSet.as_view()),

    path('deliveries/', views.DeliveryViewSet.as_view()),
    path('deliveries/<int:pk>/', views.DeliveryDetailViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)