from django.urls import path
from .views import HomeView, UploadFileView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('upload/', UploadFileView.as_view(), name='upload_file'),
]
