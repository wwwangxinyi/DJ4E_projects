from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name = 'gadgets'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.GadgetCreate.as_view(), name='gadget_create'),
    path('main/<int:pk>/update/', views.GadgetUpdate.as_view(), name='gadget_update'),
    path('main/<int:pk>/delete/', views.GadgetDelete.as_view(), name='gadget_delete'),
    path('lookup/', views.BrandView.as_view(), name='brand_list'),
    path('lookup/create/', views.BrandCreate.as_view(), name='brand_create'),
    path('lookup/<int:pk>/update/', views.BrandUpdate.as_view(), name='brand_update'),
    path('lookup/<int:pk>/delete/', views.BrandDelete.as_view(), name='brand_delete'),
]
