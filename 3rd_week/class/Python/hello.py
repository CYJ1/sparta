a = 'spartacodingclub@gmail.com'


# 메일주소가 맞는지 판단하기
def check_mail(s):
    return s.find('@') > -1


# 메일주소 찾기
def get_mail(s):
    mail = s.split('@')[1]
    return mail.split('.')[0]


# 결과값
print(check_mail(a))
print(get_mail(a))
