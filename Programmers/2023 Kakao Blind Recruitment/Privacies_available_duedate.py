# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# Lv.1
# 문제: 개인정보 수집 유효기간
# 2023 Kakao Blind Recruitment

def terms_to_dict(terms):
    dict_obj = {t.split()[0]: int(t.split()[1]) for t in terms}
    return dict_obj

def privacies_to_dict(privacies):
    dict_obj = {p.split()[0]: p.split()[1] for p in privacies}
    return dict_obj
    
def solution(today, terms, privacies):
    answer = []
    # 하나의 iteration에 terms와 privacies 동시에 사용(순서 동일)
    # terms dict 할당
    terms_dict = terms_to_dict(terms)
    # privacies iteration
    for index, privacy in enumerate(privacies):
        # 유효기간 숫자로 저장
        term_months = terms_dict[privacy.split()[1]]
        # 계약 시작기간 저장
        start_date = privacy.split()[0]
        # 계약 시작기간 연월일 리스트로 생성
        temp1 = start_date.split('.')
        temp2 = today.split('.')
        
        start_date_l = [int(item) for item in temp1]
        today_l = [int(item) for item in temp2]

        # privacies 연월일 별 today와 date 비교
        # 지난 개월 계산
        if(start_date_l[1]>today_l[1]):
            result = 12-start_date_l[1]+today_l[1]+12*(today_l[0]-start_date_l[0]-1)       
        elif(start_date_l[1]<=today_l[1]):
            result = today_l[1]-start_date_l[1]+12*(today_l[0]-start_date_l[0])
        # 계약기간 지났는지 판별
        if(result>term_months):
            answer.append(index+1)
        if(result==term_months):
            if(start_date_l[2]<=today_l[2]):
                answer.append(index+1)
    # 결과 저장
    return answer