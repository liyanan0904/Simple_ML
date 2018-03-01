#===============================================================================
# File  : knn.py
# Desc  : 
#  
# Date  : 2018.02.13
# Author: bitgirl
# Email : liyanan0904@126.com
#===============================================================================
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy



def classify(inX, dataSet, labels, k):
    """
        
    """
    if len(dataSet) != len(labels):
        raise ValueError("DataSet or labels was too less!"
                "The length of dataSet is %s"
                "But the length of labels is %s"%(len(dataSet), len(labels)))

    dArrays = numpy.array(dataSet)
    inArray = numpy.array(inX)
    result = ((dArrays - inArray)**2).sum(axis = 1) ** 0.5
    index_list = result.argsort()
    classCount = dict()
    for i in range(k):
        label = labels[index_list[i]]
        classCount[label] = classCount.get(label, 0) + 1

    return sorted(classCount, key=lambda x : classCount[x],reverse=True)[0]




if __name__ == "__main__":
    inX = [1,4,5]
    dataSet = [[7,3,4],[5,6,7],[3,4,5],[1,4,3],[2,2,5]]
    labels = [1,3,1,3,1]
    print classify(inX, dataSet, labels, 2)


