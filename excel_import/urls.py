from django.urls import path
from .views import ExcelUploadView

app_name= "excel_import"

urlpatterns = [
    path('upload/', ExcelUploadView.as_view(), name='upload'),
]