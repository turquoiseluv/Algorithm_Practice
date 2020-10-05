'''
1차 86.7/100 추후 풀이 정리
였지만, 사실 "`(None)`" -> "(None)"
이거 차이였네 ;;

2차 100/100
고칠 점들: cleanTune 쪽 "#" 처리하는 방법으로,
getTune에서 result로 붙여넣기 전에 #이면 앞의 문자를 바꾸던가

info = re.compile('[A-G]#?').findall(song)
정규식 방식으로 #을 포함한 문자열 list로 추출해서 len(i)가 2일 때,
i[0]을 다른 문자로 바꾼다 'C#' => 'c'  
'''

def cleanTune(melody):
    melody = list(melody)
    for m_idx in range(len(melody)):
        if melody[m_idx] == "#":
            if melody[m_idx-1] == "A":
                melody[m_idx-1] = "H"
            if melody[m_idx-1] == "C":
                melody[m_idx-1] = "I"
            if melody[m_idx-1] == "D":
                melody[m_idx-1] = "J"
            if melody[m_idx-1] == "F":
                melody[m_idx-1] = "K"
            if melody[m_idx-1] == "G":
                melody[m_idx-1] = "L"
    melody = list(filter(lambda m: m != "#", melody))
    return melody


def getTune(time, melody):
    result = ""
    melody = cleanTune(melody)
    for t in range(time):
        result += melody[t % len(melody)]
    return result


def getDur(strtime):
    strtime = strtime.split(":")
    return int(strtime[0])*60 + int(strtime[1])


def solution(m, musicinfos):
    answer = ""
    ans_time = 0
    infos = []
    m = "".join(cleanTune(m))

    for info in musicinfos:
        infos.append(info.split(","))

    for info in infos:
        time = getDur(info[1])-getDur(info[0])
        tune = getTune(time, info[3])
        if m in tune:
            if ans_time < time:
                ans_time = time
                answer = info[2]

    if answer == "":
        return "(None)"
    return answer
