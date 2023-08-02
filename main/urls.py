from django.urls import path

from main.views import DocumentCreateView, DocumentListView, download

app_name = 'main'

urlpatterns = [
    path('', DocumentListView.as_view(), name='index'),
    path('upload/', DocumentCreateView.as_view(), name='upload'),
    path('download/<int:doc_id>/', download, name='download'),
]
