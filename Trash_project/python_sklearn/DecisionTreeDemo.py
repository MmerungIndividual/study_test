from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO


def getData():
    with open('E:\Trash_project\data\weather_pd.csv', 'r', encoding='UTF-8') as f:
        data = f.readlines()
    f.close()
    return data


# 读取数据
csvData = getData()
reader = csv.reader(csvData)
headers = next(reader)

# 标题title
print(headers)

# 特征数组
featureList = []
# 标记数组
labelList = []

for row in reader:
    labelList.append(row[len(row) - 1])
    rowDict = {}
    for i in range(1, len(row) - 1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)

# 打印数据
print(featureList)
print(labelList)

# features转换为one-hot数据
vec = DictVectorizer()
data_X = vec.fit_transform(featureList).toarray()
print("data_X:" + str(data_X))
print(vec.get_feature_names())

# label转换
lb = preprocessing.LabelBinarizer()
data_Y = lb.fit_transform(labelList)
print("data_Y:" + str(data_Y))

# 使用决策树
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(data_X, data_Y)
print("clf:" + str(clf))

# 保存dot文件
with open('output.dot', 'w') as f:
    f = tree.export_graphviz(clf,
                             feature_names=
                             vec.get_feature_names(),
                             out_file=f)

# 生成数据
temp_X = data_X[0, :]
print("temp_X:" + str(temp_X))
new_X = temp_X
new_X[0] = 1
new_X[2] = 0
print("new_X:" + str(new_X))
# 使用模型 f(x) = y
predict_Y = clf.predict([new_X])
print("predict_Y:" + str(predict_Y))
