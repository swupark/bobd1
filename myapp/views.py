from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RecommendListSerializer
from django.shortcuts import get_object_or_404, render, redirect
from excel_import.models import FoodModel
import pandas as pd
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

df = pd.read_csv('C:/Users/82102/PycharmProjects/bob_d/accountapp/2train.csv')

class Predict(APIView):
    def get(self, request,imageId, category, format=None):
        # Load the trained Doc2Vec model
        model = Doc2Vec.load('./rcmd_model.pkl')
        i = int(imageId)
        word_vector = model.infer_vector([str(df.iloc[i]['new_train'])])
        return_docs = model.docvecs.most_similar(positive=[word_vector], topn=126)
        result_list = []

        for rd in return_docs:
            matching_rows = df[df['RCP_NM'] == rd[0]]
            for index, row in matching_rows.iterrows():
                if (row['RCP_WAY2'] == df.iloc[i-1]['RCP_WAY2']) and (row[category] == 1):
                    result_list.append({
                        'index': index,
                        'recipe_name': rd[0],
                        'similarity': rd[1],
                        'new_train': row['new_train'],
                        'recipe_way2': row['RCP_WAY2']
                    })

        rcp = get_object_or_404(FoodModel, id=imageId)
        serializer = RecommendListSerializer(result_list, many=True)
        return render(request, 'recipesapp/templates/recipesapp/menu_list.html', {'post': imageId, 'rcp': rcp, 'list': serializer.data})
