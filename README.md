# **Lab 33: Authentication**

In this lab, I created a simple authentication system for my API's using [JWT](https://jwt.io/).

<br>

## **What is JWT?**


JWT is a JSON Web Token. It is a standard for representing claims to be transferred between parties in a secure way. It is a standard for representing claims to be transferred between parties in a secure way.

It is made up of three parts:


1. **Header**: A JSON object that contains a few meta-data about the token.
2. **Payload**: A JSON object that contains the claims to be transferred.
3. **Signature**: A signature that proves the authenticity of the token.

<br>

## **Feature Tasks and Requirements**

### **Poetry**

1. Create a poetry project.

2. ```poetry install```

3. run the following command:

    ```
    poetry add django djangorestframework djangorestframework-simplejwt
    ```

4. activate the poetry environment, using ```poetry shell```

### **Django**

1. Create a Django project:
```django-admin startproject auth_project .```

2. Migrate the database:
```python manage.py migrate```

3. Create a user:
```python manage.py createsuperuser```

4. Create an app:
```python manage.py startapp music```

5. Create a model, register it in the admin.

6. Add the app to INSTALLED_APPS in settings.py, in addition to rest_framework.

7. Add this to settings.py
    ```
    REST-FRAMEWORK = {
                "DEFAULT-PREMISSION-CLASSES":[
                    "rest-framework.simplejwt.authentication.JWTAuthentication",
                    "rest-framework.authentication.SessionAuthentication",
                    "rest-framework.authentication.BasicAuthentication",
                ]
                }
    ```
8. Create  "serializers.py" in the app and import: 
    ```
    from rest-framework import serializers
    from .models import Music
    ```

9. Create a serializer class:
    ```
    class MusicSerializer(serializers.ModelSerializer):
        class Meta:
            model = Music
            fields = "__all__"
    ```

10. In views.py:
    ```
    from django.http import HttpResponse
    from django.shortcuts import render
    from rest_framework.generics import ListCreateAPIView
    from rest_framework.permissions import IsAuthenticated

    from .models import Music
    from .serializers import MusicSerializer
    ```

11. Create a view class:
    ```
    class MusicListCreateAPIView(ListCreateAPIView):
        queryset = Music.objects.all()
        serializer_class = MusicSerializer
        permission_classes = [IsAuthenticated]
    ```

12. Add urls.py, with jwt:
    ```
    from lib2to3.pgen2 import token
    from django.urls import path
    from .views import MusicListView
    from rest_framework_simplejwt import views as jwt_views

    urlpatterns = [
        path('music-list', MusicListView.as_view(), name="music_list"),
        path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    ]

    ```
### **Docker**

1. Create a Dockerfile:

2. Create docker-compose.yml

3. run ```poetry export -f requirements.txt --output requirements.txt```

4. run ```docker-compose build```

5. run ```docker-compose up```

