
def solution(participant, completion):
    """
    마라톤 참여자 중 완주하지 못한 1명을 출력
    (단, 참여자중 동명이인이 있을 수 있다.)
    """
    answer = []
    #동명이인 없을 경우
    if list(set(participant) - set(completion)) != []:
        answer = list(set(participant) - set(completion))[0]
    
    #동명이인 있을 경우
    else: 
        for i in list(set(completion)):
            participant.remove(i)
        answer = participant[0]
        
    return answer

## 1차 시도 : 테스트5 실패
    
