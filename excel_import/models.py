from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class FoodModel(models.Model):
    ATT_FILE_NO_MAIN = models.CharField(max_length=150, null=True, blank=True)
    ATT_FILE_NO_MK = models.CharField(max_length=150, null=True, blank=True)
    HASH_TAG = models.CharField(max_length=150, null=True, blank=True)

    INFO_CAR_x = models.IntegerField(null=True, blank=True)
    INFO_ENG_x = models.IntegerField(null=True, blank=True)
    INFO_FAT_x = models.IntegerField(null=True, blank=True)
    INFO_NA = models.IntegerField(null=True, blank=True)
    INFO_PRO = models.IntegerField(null=True, blank=True)
    INFO_WGT = models.IntegerField(null=True, blank=True)

    MANUAL_IMG01 = models.CharField(max_length=150, null=True, blank=True)
    MANUAL_IMG02 = models.CharField(max_length=150, null=True, blank=True)
    MANUAL_IMG03 = models.CharField(max_length=150, null=True, blank=True)
    MANUAL_IMG04 = models.CharField(max_length=150, null=True, blank=True)
    MANUAL_IMG05 = models.CharField(max_length=150, null=True, blank=True)
    MANUAL_IMG06 = models.CharField(max_length=150, null=True, blank=True)
    MANUAL_IMG07 = models.CharField(max_length=150, null=True, blank=True)
    MANUAL_IMG08 = models.CharField(max_length=150, null=True, blank=True)
    MANUAL_IMG09 = models.CharField(max_length=150, null=True, blank=True)
    MANUAL_IMG10 = models.CharField(max_length=150, null=True, blank=True)
    MANUAL_IMG11 = models.CharField(max_length=150, null=True, blank=True)

    MANUAL01 = models.CharField(max_length=300, null=True, blank=True)
    MANUAL02 = models.CharField(max_length=300, null=True, blank=True)
    MANUAL03 = models.CharField(max_length=300, null=True, blank=True)
    MANUAL04 = models.CharField(max_length=300, null=True, blank=True)
    MANUAL05 = models.CharField(max_length=300, null=True, blank=True)
    MANUAL06 = models.CharField(max_length=300, null=True, blank=True)
    MANUAL07 = models.CharField(max_length=300, null=True, blank=True)
    MANUAL08 = models.CharField(max_length=300, null=True, blank=True)
    MANUAL09 = models.CharField(max_length=300, null=True, blank=True)
    MANUAL10 = models.CharField(max_length=300, null=True, blank=True)
    MANUAL11 = models.CharField(max_length=300, null=True, blank=True)

    RCP_NA_TIP = models.CharField(max_length=150, null=True, blank=True)
    RCP_NM = models.CharField(max_length=150, null=True, blank=True)
    RCP_PARTS_DTLS = models.CharField(max_length=300, null=True, blank=True)
    RCP_PAT2 = models.CharField(max_length=150, null=True, blank=True)
    RCP_SEQ = models.IntegerField(null=True, blank=True)
    RCP_WAY2 = models.CharField(max_length=150, null=True, blank=True)
    LOW_NA = models.IntegerField(null=True, blank=True)
    HIGH_PRO = models.IntegerField(null=True, blank=True)
    VEGAN = models.IntegerField(null=True, blank=True)
    DIETS = models.IntegerField(null=True, blank=True)


field2 = models.IntegerField(
    validators=[
        MinValueValidator(1, message="Value must be at least 1"),
        MaxValueValidator(100, message="Value cannot exceed 100"),
    ]
)

