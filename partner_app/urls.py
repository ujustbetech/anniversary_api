from partner_app.views import Registration,partnerlogin
# ,postimg,imgdata
from django.urls import  path

urlpatterns = [
    path('reg/', Registration),
    path('login/<int:pk>/', partnerlogin),
    # path('img/<int:post>/', imgdata),
    # path('postimg/', postimg),
]

# from django.urls import include, path
# from rest_framework import routers
# from partner_app.views import partnerViewSet

# router = routers.DefaultRouter()
# router.register(r'partner', partnerViewSet)
# router.register(r'login', partnerViewSet)

# urlpatterns = [
#    path('', include(router.urls)),
# ]