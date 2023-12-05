from random import shuffle
from django.shortcuts import render, get_object_or_404
from excel_import.models import FoodModel
import pandas as pd
from gensim.models.doc2vec import TaggedDocument,Doc2Vec

def homepage(request):
    VEGAN = list(FoodModel.objects.filter(VEGAN=1).all())
    HIGH_PRO = list(FoodModel.objects.filter(HIGH_PRO=1).all())
    LOW_NA = list(FoodModel.objects.filter(LOW_NA=1).all())
    DIETS = list(FoodModel.objects.filter(DIETS=1).all())
    #dislike_ingredient = request.GET.get('dislike_ingredient', '')
    #vegan_img,hp_img,ln_img,dt_img=dislike()
    # if dislike_ingredient:
    #     vegan_img = [recipe for recipe in vegan_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    #     hp_img = [recipe for recipe in hp_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    #     ln_img = [recipe for recipe in ln_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    #     dt_img = [recipe for recipe in dt_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    shuffle(VEGAN)
    shuffle(HIGH_PRO)
    shuffle(LOW_NA)
    shuffle(DIETS)

    return render(request, 'accountapp/home.html',{'vegan_img': VEGAN, 'hp_img': HIGH_PRO, 'ln_img': LOW_NA, 'dt_img': DIETS})

def recommendlist(request,imageId,category):
    df = pd.read_csv('C:/Users/82102/PycharmProjects/bob_d/accountapp/train.csv')
    doc_df = df[['RCP_NM', 'new_train']].values.tolist()
    tagged_data = [TaggedDocument(words=_d, tags=[uid]) for uid, _d in doc_df]
    max_epochs = 15
    model = Doc2Vec(
        window=15,
        vector_size=100,
        alpha=0.025,
        min_alpha=0.025,
        min_count=2,
        dm=1,  # PV-DM
        negative=1,
        seed=9999)

    model.build_vocab(tagged_data)

    for epoch in range(max_epochs):
        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=model.epochs)
        # decrease the learning rate
        model.alpha -= 0.002
        # fix the learning rate, no decay
        model.min_alpha = model.alpha
    i = int(imageId)
    print("학습 완료!")

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
                print(index,rd[0],rd[1],row['new_train'],row['RCP_WAY2'])

    rcp = get_object_or_404(FoodModel, id=imageId)

    return render(request,'accountapp/details.html',{'post':imageId, 'rcp':rcp,'list':result_list})

# def dislike():
    # 싫어하는 재료를 입력받습니다.
    #dislike_ingredient = dislike_igt

    # 모든 레시피를 가져옵니다.


    # 사용자가 입력한 싫어하는 재료가 있을 경우 해당하는 레시피를 제거합니다.
    # if dislike_ingredient:
    #     vegan_img = [recipe for recipe in vegan_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    #     hp_img = [recipe for recipe in hp_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    #     ln_img = [recipe for recipe in ln_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    #     dt_img = [recipe for recipe in dt_img if dislike_ingredient not in recipe.RCP_PARTS_DTLS]
    # return (vegan_img,  hp_img,  ln_img, dt_img)