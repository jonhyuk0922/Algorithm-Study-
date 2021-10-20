import re 

def solution(new_id):
    """
    기준에 맞지 않을 시, 유사한 아이디 추천해주는 함수
    """
    #1단계 : 대문자 -> 소문자 치환
    answer = new_id.lower()
    print(answer)
    
    #2단계 : 문자제거
    answer = re.compile('[0-9a-z_.\-]+').findall(new_id)
    answer = ''.join(new_id)
    print(answer)
    
    #3단계
    re.sub('\.\.+','.',answer)
    print(answer)
    return answer
