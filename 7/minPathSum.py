def minPathSum(N):
    dp = []
    # N x N 크기의 2차원 배열 생성
    for i in range(1,N+1):
        k=[]
        for j in range(1,N+1):
            k.append(i*j)
        dp.append(k)
    
    for i in range(N):  #i+1만큼 이동했을때 갈 수 있는 수들
        k=[]
        for j in range(N): #j번째 행
            k.append(dp[j][i+1-j])
        if N in k:
            return(i+1)

try:
    N = int(input())
    if(N < 0):
        raise Exception("minus num")
    result = minPathSum(N)
    print(result)
except:
    print("적절한 입력을 해주세요.")