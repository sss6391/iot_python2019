from sklearn import model_selection, svm, metrics

# csv파일을 읽어 들이고 가공하기
def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2: continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {"labels":labels, "images":images}

data = load_csv("./mnist/train.csv")
test = load_csv("./mnist/t10k.csv")

#  학습하기
clf = svm.SVC()
clf.fit(data['images'], data["labels"])

# 예측하기
predict = clf.predict(test["images"])

# 결과 확인하기
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test['labels'], predict)
print("리포트 =")
print(cl_report)
print("정답률 =", ac_score)




''' 전체 데이터 머신러닝
리포트 =
              precision    recall  f1-score   support

           0       0.96      0.99      0.97       980
           1       0.97      0.99      0.98      1135
           2       0.94      0.93      0.93      1032
           3       0.93      0.94      0.93      1010
           4       0.93      0.96      0.94       982
           5       0.93      0.91      0.92       892
           6       0.95      0.97      0.96       958
           7       0.96      0.93      0.94      1028
           8       0.94      0.92      0.93       974
           9       0.94      0.92      0.93      1009

    accuracy                           0.94     10000
   macro avg       0.94      0.94      0.94     10000
weighted avg       0.94      0.94      0.94     10000

정답률 = 0.9443
'''