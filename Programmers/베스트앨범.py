'''
합쳐는 놨는데... 이렇게 하는게 아닌거 같기도 하다.
'''

def solution(genres, plays):
    chart = []
    for i in range(len(genres)):
        chart.append([genres[i],plays[i]])
        
    chart.sort(reverse=True, key=lambda x: x[1])
    print(chart)