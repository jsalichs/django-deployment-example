from django.urls import path
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'


urlpatters= [
    path('',views.relative, name='relative'),
    path('',views.other, name='other'),
]
