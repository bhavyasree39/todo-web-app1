from django.urls import path
from . import views

urlpatterns=[
    path('',views.list1),
    path('pending/',views.pending),
    path('approve/<int:id>/',views.approve),
    path('approved/',views.approved),
    path('delete/<int:id>/',views.delete),
]