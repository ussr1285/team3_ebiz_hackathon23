# 건물을 최대한 많이 쌓아야 함.
def find_max_added_building(data):
    maximum = 0
    max_list = []
    for i in range(int(n)): #i번째 행부터 최댓값 찾기
        for j in range(int(n)): #i번째 행 j번째 열
            if data[i][j] == max(data[i]):
                max_list.append([i,j])

    for i in range(int(n)):
        k= 0 #i번째 열의 최댓값 (계속 갱신됨)
        t=[] #i 열의 최댓값의 위치를 기록할 리스트
        for j in range(int(n)):
            
            if data[j][i] > k:
                k = data[j][i]
                t = [j,i] # 열의 최댓값을 찾을 때 k값을 바꾼 마지막 수의 위치 기록해두기
            elif data[j][i] == k:
                t.append([j,i])
        for z in t:
            max_list.append(z)
    #max_list의 최댓값들의 좌표값 저장해놓기
    
    max_lists = []
    [max_lists.append(x) for x in max_list if x not in max_lists]
    max_list= max_lists
    # print(max_list) #max_list에서 중복값을 삭제한다.
    
    for i in range(int(n)): #i행부터 시작
        for j in range(int(n)): #i행 j열부터 시작
            if [i,j] in max_list:
                pass
            else:
                x = max(data[i]) #x축의 최댓값
                y = max([data[z][j]for z in range(int(n))]) #y축의 최댓값
                max_mini = min(x,y) #x축 y축 두 최댓값 중 더 작은 값
                maximum += max_mini-data[i][j]
    return(maximum)
    
def get_data(n):
    data = []
    for i in range(n):
        input_lines = input()
        if(len(input_lines) != n):
            return(-1)
        temp_data = []
        for j in range(n):
            temp_data.append(int(input_lines[j]))
        data.append(temp_data)
    return(data)

try:
    n = int(input())
    data = get_data(n)
    value = find_max_added_building(data)
    print(value)
except:
    print("적절한 입력을 해주세요.")

