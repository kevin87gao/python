#!/usr/bin/env python
# coding=utf-8

from numpy import *
import operator

##给出训练数据以及对应的类别
def createDataSet():
    group = array([[1.0, 2.0],[1.2, 0.1],[0.1, 1.4],[0.3, 3.5]])
    labels = ['A', 'A', 'B', 'B']
    return group,labels

###通过KNN进行分类
def classify(input, dataSet, label, k):
    dataSize = dataSet.shape[0]         #　第一维里面元素的个数
    ####计算欧式距离
    # title() 将input在横向重复dataSetSize次，纵向重复1次
    diff = tile(input, (dataSize, 1)) - dataSet  #input数据与dataSet数据的分别相减
    #print(diff)
    sqdiff = diff ** 2      #平方　数组里面各个值分别平方
    #print(sqdiff)
    squareDist = sum(sqdiff, axis = 1)###行向量分别相加，从而得到新的一个行向量
    #print(squareDist)
    dist = squareDist ** 0.5    #开方
    #print(dist)

    ##对距离进行排序
    sortedDistIndex = argsort(dist)##argsort()根据元素的值从大到小对元素进行排序，返回下标
    #print(sortedDistIndex)

    classCount={}
    for i in range(k):
        voteLabel = label[sortedDistIndex[i]]
        ###对选取的K个样本所属的类别个数进行统计
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1  #dict.get(key,default=None),字典的get()方法,返回指定键的值,如果值不在字典中返回默认值。
        #print(voteLabel, classCount[voteLabel])

    # 选取出现的类别次数最多的类别，两种方式：
    #　方式一
    '''
    # key=operator.itemgetter(1)根据字典的值进行排序
    # key=operator.itemgetter(0)根据字典的键进行排序
    # reverse降序排序字典

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # 结果sortedClassCount = [('A', 2), ('B', 1)]

    print("sortedClassCount:", sortedClassCount)

    return sortedClassCount[0][0]
    '''

    #　方式二
    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key

    return classes
