"""1.过滤型"""
# from sklearn.datasets import load_iris
# from sklearn.feature_selection import SelectKBest
# from sklearn.feature_selection import chi2
#
# iris=load_iris()
# X,y=iris.data,iris.target
# print(X.shape)
# X_new=SelectKBest(chi2,k=2).fit_transform(X,y)
# print (X_new.shape)

"""输出：
        (150L, 4L)
        (150L, 2L)"""

# """2.包裹型"""
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

boston=load_boston()
X=boston["data"]
Y=boston["target"]
print(Y)
names=boston["feature_names"]

lr=LinearRegression()
rfe=RFE(lr,n_features_to_select=1)#选择剔除1个
selector = rfe.fit(X,Y)
print(selector)

print ("features sorted by their rank:")
print (sorted(zip(map(lambda x:round(x,5), rfe.ranking_),names)))
#
# """输出：按剔除后AUC排名给出
# features sorted by their rank:
# [(1.0, 'NOX'), (2.0, 'RM'), (3.0, 'CHAS'), (4.0, 'PTRATIO'), (5.0, 'DIS'), (6.0, 'LSTAT'), (7.0, 'RAD'), (8.0, 'CRIM'), (9.0, 'INDUS'), (10.0, 'ZN'), (11.0, 'TAX')
# , (12.0, 'B'), (13.0, 'AGE')]"""
#
#
# """3.嵌入型 ，老的版本没有SelectFromModel"""
from sklearn.svm import  LinearSVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

# iris=load_iris()
# X,y=iris.data,iris.target
# print(X.shape)
#
# lsvc=LinearSVC(C=0.01,penalty='l1',dual=False).fit(X,y)
# model=SelectFromModel(lsvc,prefit=True)
# X_new=model.transform(X)
# print(X_new.shape)
#
# """输出：
#             (150,4)
#             (150,3)
#             """
