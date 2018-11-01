import KNN
from numpy import *
dataSet,labels = KNN.createDataSet()
input = array([1.1, 0.3])
K = 3
output = KNN.classify(input, dataSet, labels, K)
print("测试数据为:", input, "分类结果为：", output)