from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from .models import FoodModel
from .forms import ExcelUploadForm

class ExcelUploadView(View):
    template_name = 'upload.html'

    def get(self, request):
        form = ExcelUploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_data = pd.read_csv(request.FILES['excel_file']).fillna(0)
            for index, row in excel_data.iterrows():
                FoodModel.objects.create(
                    ATT_FILE_NO_MAIN=row['ATT_FILE_NO_MAIN'],
                    ATT_FILE_NO_MK=row['ATT_FILE_NO_MK'],
                    HASH_TAG=row['HASH_TAG'],

                    INFO_CAR_x=row['INFO_CAR_x_x'],
                    INFO_ENG_x=row['INFO_ENG_x_x'],
                    INFO_FAT_x=row['INFO_FAT_x_x'],
                    INFO_NA=row['INFO_NA'],
                    INFO_PRO=row['INFO_PRO'],
                    INFO_WGT=row['INFO_WGT'],

                    MANUAL_IMG01=row['MANUAL_IMG01'],
                    MANUAL_IMG02=row['MANUAL_IMG02'],
                    MANUAL_IMG03=row['MANUAL_IMG03'],
                    MANUAL_IMG04=row['MANUAL_IMG04'],
                    MANUAL_IMG05=row['MANUAL_IMG05'],
                    MANUAL_IMG06=row['MANUAL_IMG06'],
                    MANUAL_IMG07=row['MANUAL_IMG07'],
                    MANUAL_IMG08=row['MANUAL_IMG08'],
                    MANUAL_IMG09=row['MANUAL_IMG09'],
                    MANUAL_IMG10=row['MANUAL_IMG10'],
                    MANUAL_IMG11=row['MANUAL_IMG11'],

                    MANUAL01=row['MANUAL01'],
                    MANUAL02=row['MANUAL02'],
                    MANUAL03=row['MANUAL03'],
                    MANUAL04=row['MANUAL04'],
                    MANUAL05=row['MANUAL05'],
                    MANUAL06=row['MANUAL06'],
                    MANUAL07=row['MANUAL07'],
                    MANUAL08=row['MANUAL08'],
                    MANUAL09=row['MANUAL09'],
                    MANUAL10=row['MANUAL10'],
                    MANUAL11=row['MANUAL11'],

                    RCP_NA_TIP=row['RCP_NA_TIP'],
                    RCP_NM=row['RCP_NM'],
                    RCP_PARTS_DTLS=row['RCP_PARTS_DTLS'],
                    RCP_PAT2=row['RCP_PAT2'],
                    RCP_SEQ=row['RCP_SEQ'],
                    RCP_WAY2=row['RCP_WAY2'],
                    LOW_NA=row['LOW_NA'],
                    HIGH_PRO=row['HIGH_PRO'],
                    VEGAN=row['VEGAN'],
                    DIETS=row['DIETS'],
                )

            return HttpResponse("데이터 업로드 성공")

        return render(request, self.template_name, {'form': form})

