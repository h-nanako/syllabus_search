from gensim import models
import numpy as np
from scipy import spatial
import MeCab

def vector(syllabus_vector2):
    syllabus_vector1 = np.load('vector.npy')
    # ベクトルの類似度を計算
    u_answer = [1 - spatial.distance.cosine(syllabus_vector1[i], syllabus_vector2) for i in range(len(syllabus_vector1))] # コサイン類似度

    # 距離が近い科目を上位10個出力
    with open('syllabus_title.txt', 'r', encoding='utf-8')as f:
        labels = f.read().splitlines()
        answer_list = sorted(u_answer, reverse=True)
        sylla_sim = [labels[u_answer.index(answer_list[j])] for j in range(10)]
        return sylla_sim

m = MeCab.Tagger("-Owakati")
# do2vecのモデルをロード
Doc_model = models.Doc2Vec.load('vector.model')

# 文章を入力し、形態素解析によって名詞のみを抽出する
def word(word):
    word1 = []
    for i in (m.parse(word)).splitlines():
        if len(i.split()) >= 3:
            if ',' not in i.split()[0] and '.' not in i.split()[0] and '-' not in i.split()[0]:
                word1.append(i.split()[0])
    return word1

def word_vector(word1):
    syllabus_vector2 = Doc_model.infer_vector(word1)
    return syllabus_vector2
