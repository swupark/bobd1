from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from gensim.models.doc2vec import Doc2Vec
from .models import FoodModel
from myapp.serializers import RecommendListSerializer
import pandas as pd
df = pd.read_csv('C:/Users/gusth/PycharmProjects/bob_d/accountapp/2train.csv')
origin_df=pd.read_csv('C:/Users/gusth/PycharmProjects/bob_d/accountapp/1259final_dataset.csv')
class Predict(APIView):
    def get(self, request, imageId, category, format=None):
        # Load the trained Doc2Vec model
        model = Doc2Vec.load('./rcmd_model.pkl')
        i = int(imageId)
        word_vector = model.infer_vector([str(df.iloc[i]['new_train'])])
        return_docs = model.docvecs.most_similar(positive=[word_vector], topn=126)
        result_list = []

        for rd in return_docs:
            matching_rows = origin_df[origin_df['RCP_NM'] == rd[0]]
            for index, row in matching_rows.iterrows():
                if (row['RCP_WAY2'] == df.iloc[i - 1]['RCP_WAY2']) and (row[category] == 1):
                    result_list.append({
                        'index': index,
                        'recipe_name': rd[0],
                        'img_food': row['ATT_FILE_NO_MAIN'],
                    })
        return (imageId, result_list)
def menu_detail(request, imageId, category):
    menu = FoodModel.objects.get(pk=imageId)
    rcmd = Predict()
    image_num,list_data = rcmd.get(request, imageId, category)
    return render(request, 'recipesapp/menu_detail.html' ,{'menu':menu,'food_id':image_num,'list':list_data, 'category':category})