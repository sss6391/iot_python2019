from sklearn import svm, metrics
import glob, os.path, re, json

# 텍스트를 읽어 들이고 출현 빈도 조사하기
# 파일명 앞에 두 글자는 아래 규식을 갑는다.
#  en: 영어
#  fr : 프랑스어
#  id : 인도네시아어
#  fr : 타갈로그어
#

def check_freq(fname):
    name = os.path.basename(fname)
    # 파일 이름에서 앞 2개의 문자(label)를 구하기 위한 정규식
    lang = re.match(r'^[a-z]{2,}', name).group()
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower() # 소문자 변환
    cnt = [0 for n in range(0, 26)] # [0,0,0,0,0 .... 0] <=0이 26개로 초기화된 리스트
    code_a = ord("a") #알파벳의 아스키 값
    code_z = ord("z")

    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z: # a~z 사이에 있을 때
            cnt[n - code_a] += 1
    total = sum(cnt)
    freq = list(map(lambda n: n / total, cnt))
    return (freq, lang)

def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)
    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs":freqs, "labels":labels}

data = load_files("./lang/train/*.txt")
test = load_files("./lang/test/*.txt")

# 이후를 대비해서 JSON으로 결과 저장하기
with open("./lang/freq.json", "w", encoding="utf-8") as fp:
    json.dump([data, test], fp)

# 학습하기
clf = svm.SVC()
clf.fit(data['freqs'], data["labels"])

# 예측하기
predict = clf.predict(test['freqs'])

# 결과 테스트하기
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test['labels'], predict)
print("리포트 =")
print(cl_report)
print("정답률 =", ac_score)

