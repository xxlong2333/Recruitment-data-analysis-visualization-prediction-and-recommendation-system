import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv('./jobData.csv')

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(data['title'])

#计算相似度
consine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

#定义函数来实现推荐

def get_recommendations(title, consine_sim=consine_sim):
    idx = data[data['title'] == title].index[0]

    #获取与指定职位相似的职位索引
    sim_scores = list(enumerate(consine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    #返回相似职位的索引
    similar_titles = [(data.iloc[i]['title'],i) for i,_ in sim_scores[1:]]
    # print(similar_titles)
    return similar_titles

recommend_title = get_recommendations('java开发实习生[中关村]')