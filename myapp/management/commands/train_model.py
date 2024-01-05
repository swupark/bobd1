import pandas as pd
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Train the model'
    def handle(self, *args, **options):
        df = pd.read_csv('C:/Users/gusth/PycharmProjects/bob_d/accountapp/2train.csv')
        doc_df = df[['RCP_NM', 'new_train']].values.tolist()
        tagged_data = [TaggedDocument(words=_d, tags=[uid]) for uid, _d in doc_df]

        max_epochs = 15
        model = Doc2Vec(
            window=3,
            vector_size=100,
            alpha=0.025,
            min_alpha=0.025,
            min_count=2,
            dm=1,  # PV-DM
            negative=1,
            seed=9999
        )

        model.build_vocab(tagged_data)

        for epoch in range(max_epochs):
            model.train(tagged_data,
                        total_examples=model.corpus_count,
                        epochs=model.epochs)
            # decrease the learning rate
            model.alpha -= 0.002
            # fix the learning rate, no decay
            model.min_alpha = model.alpha
            print(epoch,"번째 학습")

        model.save('./rcmd_model.pkl')
        self.stdout.write(self.style.SUCCESS('Successfully trained the model'))
        #redirect_url = f'http://127.0.0.1:8000/account/list/{imageId}/{category}'
        # URL로 리다이렉트
        # redirect_url = reverse('accountapp:list', kwargs={'imageId': imageId, 'category': category})
        # return HttpResponseRedirect(redirect_url)