import os
from bs4 import BeautifulSoup
import nltk.stem
from nltk.stem import WordNetLemmatizer  
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.metrics import edit_distance
from nltk.corpus import stopwords
stemmer = nltk.stem.SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()
list_stopWords=list(set(stopwords.words('english')))
def readFile(parameter_list):
    path = parameter_list
    files = os.listdir(path)
    s = []
    file_list = []

    for file in files:
        print(file)
        if (os.path.isdir(path+"/"+file)):
            dir_path = path+"/"+file
            file_list = os.listdir(dir_path)
            print(dir_path)
            gap = []
            tempStr=""
            for fileName in file_list:
                if not os.path.isdir(fileName):
                    f = open(dir_path+"/"+fileName)  # 打开文件
                    iter_f = iter(f)  # 创建迭代器
                    str1 = ""
                    for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                        str1 = str1 + line
                    gap.append(str1)
            for htmlFile in gap:
                soup = BeautifulSoup(htmlFile, 'html.parser')
                for x in soup.find_all('span'):
                    
                    if(x.string != None):
                        tempStr += checkTxt(x.string)
                        # print(x.string)
            s.append(tempStr)
    return s


def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

def readTxt():
    path="txt"
    path_list=os.listdir(path)
    s=[]
    filesNames=[]
    for fileName in path_list:
        gap=[]
        if "txt" in fileName:
            print(fileName)
            filesNames.append(fileName.replace('.txt',''))
            f = open(path+"/"+fileName)  # 打开文件
            iter_f = iter(f)  # 创建迭代器
            str1 = ""
            for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                str1 = str1 + line
            gap.append(str1)
            fileTxt=str(gap)
            s.append(fileTxt)
    return s,filesNames
def checkTxt(checkStr):
    str1=""
    temp=''
    for i in word_tokenize(checkStr):
        if str(i).isalpha():
            temp=stemmer.stem(lemmatizer.lemmatize(i))
            if not temp in list_stopWords:
                str1+=temp+" "
    return str1
def createTxt(filePath):
    data = readFile(filePath)
    print(len(data))
    i = 0
    for item in data:
        nameStr = str(i)+'.txt'
        print(len(item))
        save_to_file(nameStr, item)
        print(i)
        i += 1

# createTxt("gap-html")
# print(checkTxt("He is playing the  books! @#$% 123 (3)"))