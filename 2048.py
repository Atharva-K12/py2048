import os
import random
import argparse
def rotation_anti(board,n):
	for i in range(n // 2):
		for j in range(i, n-i-1):
			store_val=board[i][j]
			board[i][j]=board[j][n-1-i]
			board[j][n-1-i]=board[n-1-i][n-1-j]
			board[n-1-i][n-1-j]=board[n-1-j][i]
			board[n-1-j][i]=store_val
	return board
def rotation(board,n):
	for i in range(n // 2):
		for j in range(i, n-i-1):
			store_val=board[i][j]
			board[i][j]=board[n-1-j][i]
			board[n-1-j][i]=board[n-1-i][n-1-j]
			board[n-1-i][n-1-j]=board[j][n-i-1]
			board[j][n-i-1]=store_val
	return board
def print_board(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end="  ")
        print()
def clr():
  if os.name=="nt" :
    os.system('cls')
  else:
    os.system('clear')
def shifting(board,n):
	flag=False
	temp=[[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		c=0
		for j in range(n):
			if board[i][j]!=0:
				temp[i][n-c-1]=board[i][j]
				c+=1
	if temp==board:
		flag=True
	return (temp,flag)
def adding(board,n):
	flag=False
	temp=board.copy()
	for i in range(n):
		for j in range(n-1,0,-1):
			if board[i][j]!=0:
				if board[i][j]==board[i][j-1]:
					board[i][j]*=2
					board[i][j-1]=0
	if temp==board:
		flag=True
	return (board,flag)
def new_2(board,n):
	while True:
		h=random.choice(range(n))
		k=random.choice(range(n))
		if board[h][k]==0:
			board[h][k]=2
			break
	return board
def moving(board,n):
	board,flag1=shifting(board,n)
	board,flag2=adding(board,n)
	board,flag3=shifting(board,n)
	return (board,flag1 and flag2 and flag3)
def check(board,n,w):
	for i in range(n):
		if w in board[i]:
			clr()
			print_board(board,n)
			print("You Win!")
			return "end"
	for i in range(n):
		if 0 in board[i]:
			return "zero"
		else:
			for j in range(n):
				if j==n-1:
					for h in range(n-1):
						if board[j][h]==board[j][h+1] or board[h][j]==board[h+1][j]:
							return "cons"
	clr()
	print_board(board,n)
	print("You lost")
	return "end"
def game_2048(board,n,w,flag):
	ret=check(board,n,w)
	if ret!="end":
		if ret=="zero" or not flag:
			board=new_2(board,n)
	ret=check(board,n,w)
	if ret!="end":
		clr()
		print_board(board,n)
		while True:
			try:
				move=input('''Enter move:
	w for up
	d for down
	a for left
	d for right
	ctrl+c to forfeit \n ''').lower()
				if move not in ('w','a','s','d'):
					print("Invalid Input ")
				else:
					break
			except KeyboardInterrupt:
				clr()
				print("This was the final board, the game was forfeited by user")
				print_board(board,n)
				return 0
		if move=='w':
			board=rotation(board,n)
			board,flag=moving(board,n)
			board=rotation_anti(board,n)
		elif move=='a':
			board=rotation(board,n)
			board=rotation(board,n)
			board,flag=moving(board,n)
			board=rotation(board,n)
			board=rotation(board,n)
		elif move =='s':
			board=rotation_anti(board,n)
			board,flag=moving(board,n)
			board=rotation(board,n)
		elif move=='d':
			board,flag=moving(board,n)
		game_2048(board,n,w,flag)
def start():
	p=argparse.ArgumentParser()
	p.add_argument("--n",help="Provide Board size",type=int,nargs='?',default=5)
	p.add_argument("--w",help="win value",type=int,nargs='?',default=2048)
	arg=p.parse_args()
	board=[[0 for j in range(arg.n)]for i in range(arg.n)]
	game_2048(board,arg.n,arg.w,False)
if __name__ == '__main__':
	start()
