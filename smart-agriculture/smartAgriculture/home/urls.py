from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('irrigation', views.irrigation,name='irrigation'),
    path('cropHealth', views.cropHealth,name='cropHealth'),
    path('diseaseDetection', views.diseaseDetection,name='disease'),
    path('weather', views.weather,name='weather'),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('api/getCurWeather',views.getWeatherAPI,name="CurWeatherAPI"),
    path('api/getAllWeather',views.getAllWeatherAPI,name="AllWeatherAPI"),
    path('api/getNdvi',views.getNDVIAPI,name="NdviAPI"),
    path('api/getIrrigationData',views.getIrrigationData,name="IrrigationAPI"),
    path('api/createNewUser',views.createNewUser,name="New User"),
]
