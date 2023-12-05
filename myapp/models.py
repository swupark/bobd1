from django.db import models
from excel_import.models import FoodModel
from django.db import models

class MyModel(models.Model):
    model_file = models.FileField(upload_to='models/',null=True)
    # 필요한 다른 필드들을 추가할 수 있습니다.



