from lib2to3.pgen2 import token
from django.urls import path
from .views import MusicListView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('music-list', MusicListView.as_view(), name="music_list"),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]


# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1Mzk4Nzk2NiwiaWF0IjoxNjUzOTAxNTY2LCJqdGkiOiJjOWU3ZjA2ZWUyMTU0ODAyYmE0ZTRkMzczNjkwZWNhNSIsInVzZXJfaWQiOjF9.IC0xqiCnnEvdggaTSXOW6pVHaN9MJ9IDH29eNvcpfNk",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzOTAxODY2LCJpYXQiOjE2NTM5MDE1NjYsImp0aSI6IjQ3NDhiNzY0MGI0YjQyMjc5Mzg3MDM4N2YyNWI3ZWQwIiwidXNlcl9pZCI6MX0.NUuyuInL85Xp_eEzb2BeD_i6tnGzCWcqU0p719Jhb6Q"
# }


# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1Mzk4ODI4NywiaWF0IjoxNjUzOTAxODg3LCJqdGkiOiJkMmE2NWRjYzU2YjI0ZWQwODRmNjlhMDAxOTZjMDk0ZSIsInVzZXJfaWQiOjF9.dbx29EynP9SKp9rgqdx2AmWjQht-UUIdD-AweHJXddc",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzOTAyMTg3LCJpYXQiOjE2NTM5MDE4ODcsImp0aSI6IjEyYTAwYzIxOTliZjRmNzI4NTg0NjZkN2I2ZjY0YmFlIiwidXNlcl9pZCI6MX0.Udcy8vSUNQtRJHWVP1fQ7LN1FKDjGDNgNIxoRJZ0x94"
# }