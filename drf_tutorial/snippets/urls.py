from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from .views import *

urlpatterns = [
    path('', views.api_root),
    path('api/', views.api_root, name='api_root'),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]