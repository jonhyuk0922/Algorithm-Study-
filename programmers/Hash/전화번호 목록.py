def solution(phone_book):
    """
    전화번호부가 주어졌을 때, 어떠한 번호가 다른 번호의 접두어인 경우
    가 있는 지 판단하는 함수
    """
    answer = True
    #어떤 번호가 다른 번호의 접두어인 경우
    #폰번호중 가장 짧은 길이로 앞부터 잘라서 비교
    min_len = min([len(i) for i in phone_book]) 
    min_phone_book = [num[:min_len] for num in phone_book]
    
    if len(min_phone_book) != len(set(min_phone_book)):
        answer = False
        #최저길이로는 같지만 그 뒷부분이 다른 경우 == 겹치는 부분이 최저길이가 아닌 경우!
        #e.g) 1234 1235 153 -> 123 123 153 으로 겹쳐보이지만 안겹친다.
        #아직 못짬
    
    return answer

#test 11,14번 틀림
