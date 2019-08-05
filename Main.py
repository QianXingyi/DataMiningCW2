from ReadFile import readTxt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from scipy.cluster import hierarchy
import seaborn as sns
import csv
import matplotlib.pyplot as plt
def create_csv(csvName):
    fileHeader = ["word", "tfidf"]
    csvFile = open(csvName+".csv", "w")
    writer = csv.writer(csvFile)
    writer.writerow(fileHeader)
    csvFile.close()


def write_csv(csvName,x1,x2):
    csvFile = open(csvName+".csv", "a+")
    writer = csv.writer(csvFile)
    row_data=[str(x1),str(x2)]
    writer.writerow(row_data)
    csvFile.close()

documents=[]
fileNames=[]
documents,fileNames=readTxt()

vectorizer = CountVectorizer(stop_words='english')

X = vectorizer.fit_transform(documents)

word = vectorizer.get_feature_names()

tfidf_transformer = TfidfTransformer()
tfidf_transformer.fit(X.toarray())
# create_csv('data')
# for idx, word in enumerate(vectorizer.get_feature_names()):
#         write_csv('data',word, tfidf_transformer.idf_[idx])

tfidf = tfidf_transformer.transform(X).toarray()

# for i in range(len(documents)):
#     create_csv(str(i))
#     for item in range(len(word)):
#         write_csv(str(i),word[item],tfidf[i][item])

print(fileNames)
Z = hierarchy.linkage(tfidf, method ='ward',metric='euclidean')
hierarchy.dendrogram(Z,labels=fileNames)

plt.show()

from sklearn.decomposition import PCA
pca=PCA(n_components=0.9)
newData=pca.fit_transform(tfidf)
print(len(newData[0]))
for i in range(len(newData)):
        plt.text(newData[i,0],newData[i,1],fileNames[i])
plt.plot(newData[:,0],newData[:,1],'ko')
plt.show()
Z = hierarchy.linkage(newData, method ='ward',metric='euclidean')
hierarchy.dendrogram(Z,labels=fileNames)
plt.show()
from sklearn.cluster import KMeans
estimator = KMeans(n_clusters=8)#构造聚类器，构造一个聚类数为3的聚类器
estimator.fit(newData)#聚类
label_pred = estimator.labels_ #获取聚类标签
centroids = estimator.cluster_centers_ #获取聚类中心
inertia = estimator.inertia_ # 获取聚类准则的总和
mark = ['or', 'ob', 'og', 'ok', 'oy','oc','om','*k']
cent=['xr', 'xb', 'xg', 'xk', 'xy','xc','xm','xk']
j = 0 
for i in label_pred:
    plt.plot([newData[j:j+1,0]], [newData[j:j+1,1]], mark[i], markersize = 5)
    j +=1
j=0
for i in centroids:
        plt.plot(i[0],i[1],cent[j],markersize=20)
        j+=1

for i in range(len(newData)):
        plt.text(newData[i,0],newData[i,1],fileNames[i])
plt.show()

def kMeansScore(count):
        pca=PCA(n_components=0.99)
        newtfidf=pca.fit_transform(tfidf)
        estimator = KMeans(n_clusters=count)#构造聚类器，构造一个聚类数为3的聚类器
        estimator.fit(newtfidf)#聚类
        inertia = estimator.inertia_ # 获取聚类准则的总和
        print(inertia)
        return inertia

ar=[]
ar2=[3,4,5,6,7,8,9,10,11,12]
ar.append(kMeansScore(3))
ar.append(kMeansScore(4))
ar.append(kMeansScore(5))
ar.append(kMeansScore(6))
ar.append(kMeansScore(7))
ar.append(kMeansScore(8))
ar.append(kMeansScore(9))
ar.append(kMeansScore(10))
ar.append(kMeansScore(11))
ar.append(kMeansScore(12))
plt.plot(ar2,ar,"k-")
plt.plot(ar2,ar,"rx")
plt.show()