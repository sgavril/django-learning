from django.urls import path

from . import views

app_name = 'tastings'

urlpatterns = [
    path(route='', view=views.TasteListView.as_view(), name='list'),
    path(route='<int:pk>', view=views.TasteDetailView.as_view(), name='detail'),
    path(route='<int:pk>',view=views.TasteResultsView.as_view(), name='results'),
    path(route='<int:pk>/update/', view=views.TasteUpdateView.as_view(), name='update'),
]