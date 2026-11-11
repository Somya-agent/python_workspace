def experiment(n, ans1):
    board1 = ["." * n for _ in range(n)]
    board = "." * n 
    print(board1)
    ans=board1
    ans1.append(list(board1))
    print(ans)
    print(ans1)
    

ans1=[]
experiment(4, ans1)

