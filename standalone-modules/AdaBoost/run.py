#coding=utf-8
#建立AdaBoost集成算法模型并使用训练集训练
#输入：x_train,y_train（dataframe)
#参数：learning_rate, n_estimators
#输出：adaboost_classifier
#---------------------------------------------------------------
import pandas as pd 
from sklearn.ensemble import AdaBoostClassifier

def main(params, inputs, outputs):
    ### 读入训练数据 ###
    x_train = pd.read_pickle(inputs.x_train)
    y_train = pd.read_pickle(inputs.y_train)
    
    ### 读入参数 ###
    learning_rate = params.learning_rate
    n_estimators = params.n_estimators
    
    ### 训练模型 ###
    adaboost_classifier = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(), learning_rate=learning_rate, 
                                            n_estimators=n_estimators, algorithm="SAMME.R")
    adaboost_classifier.fit(X_train, y_train)
    
    ### 预测结果 ###
    pred = adaboost_classifier.predict(x_train)
    prob = adaboost_classifier.predict_proba(x_train)

    ### 模型输出 ###
    with open(outputs.adaboost_classifier, "wb") as out:
        pickle.dump(adaboost_classifier, out) 