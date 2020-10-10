'''
1차 100/100

개선안
* 리스트 2개 연동은 zip 함수를 쓰자!
짧게 썼을 뿐이지, 접근은 같았다. 굿
'''

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    ans = []
    dict = {}
    sumDict = {}

    sumDict = {e: 0 for e in set(genres)} # 이 부분만 개선 -> 각 dict 항목마다 빈 리스트 생성도 가능
    # types = list(set(genres))
    # for type in types:
    #     sumDict[type] = 0

    chart = []
    for i in range(len(genres)):
        chart.append([genres[i],plays[i], i])

    for album in chart:
        sumDict[album[0]] += album[1]
    sumDict = sorted(sumDict.items(), key=lambda x: x[1], reverse=True)
    print(sumDict)
        
    chart.sort(reverse=True, key=lambda x: x[1])

    for album in chart:
        if album[0] in dict.keys():
             dict[album[0]].append(album[2])
        else:
            dict[album[0]] = [album[2]]

    for info in sumDict:
        ans += dict[info[0]][:2]
    
    return ans

print(solution(genres, plays))