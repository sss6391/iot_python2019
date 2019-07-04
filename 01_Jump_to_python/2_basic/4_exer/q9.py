# coding: cp949


a = dict()
a['name'] = 'python'
a[('a')] = 'python'
a[[1]] = 'python' # 리스트는 딕셔너리 key로 사용불가능
                    # 리스트는 수정이 가능해서 사용불가
a[250] = 'python'
