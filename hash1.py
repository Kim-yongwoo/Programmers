def solution(participant, completion):
    # 해시값의 총 합을 저장할 변수
    tmp = 0
    # 해시값과 이름이 저장되는 키값 구조
    dic = {}

    for p in participant:
        dic[hash(p)] = p

        tmp += int(hash(p))

    for com in completion:
        tmp -= hash(com)

    return dic[tmp]