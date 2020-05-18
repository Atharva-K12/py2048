from os import system,name
import random
import argparse
from copy import deepcopy
try:
	if name=="nt":
		import msvcrt as getch
	else:
		import getch
except ImportError:
	print("Importing module....")
	system('pip install getch')
def rotation_anti(board,n):
	for i in range(n // 2):
		for j in range(i, n-i-1):
			board[i][j],board[j][n-i-1],board[n-1-i][n-1-j],board[n-1-j][i]=\
			board[j][n-i-1],board[n-1-i][n-1-j],board[n-1-j][i],board[i][j]
	return board
def rotation(board,n):
	for i in range(n // 2):
		for j in range(i, n-i-1):
			board[i][j],board[n-1-j][i],board[n-1-i][n-1-j],board[j][n-1-i]=\
			board[n-1-j][i],board[n-1-i][n-1-j],board[j][n-1-i],board[i][j]
	return board
def print_board(board,n):
	print('\n\n'.join('\t'.join(str(element) for element in row) for row in board))
def clr():
	system('cls')if name=="nt" else system('clear')
def shifting(board,n):
	flag,temp,=1,[[0 for i in range(n)]for j in range(n)]
	for i in range(n):
		c=0
		for j in range(n):
			if board[i][j]!=0:
				temp[i][c],c=board[i][j],c+1
	if temp==board:
		flag=0
	return (temp,flag)
def adding(board,n):
	flag,temp=1,deepcopy(board)
	for i in range(n):
		for j in range(n-1):
			if board[i][j]!=0:
				if board[i][j]==board[i][j+1]:
					board[i][j]*=2
					board[i][j+1]=0
	if temp==board:
		flag=0
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
	return (board,flag1+flag2)
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
	for i in range(n):
		for j in range(n):
			if j==n-1 or i==n-1:
				for h in range(n-1):
					if board[n-1][h]==board[n-1][h+1] or board[h][n-1]==board[h+1][n-1]:
						return "cons"
			else:
				if board[i][j]==board[i+1][j] or board[i][j]==board[i][j+1]:
					return "cons"
	clr()
	print_board(board,n)
	print("You lost")
	return "end"
def game_2048(board,n,w,flag):
	ret=check(board,n,w)
	if ret!="end":
		if ret=="zero" and flag!=0:
			board=new_2(board,n)
		else:
			print("Try another move")
	ret=check(board,n,w)
	if ret!="end":
		clr()
		print_board(board,n)
		while True:
			print('''Enter move:\n\tw for up\n\td for down\n\ta for left\n\td for right\n\tq to forfeit \n ''')
			move=getch.getche().decode("ASCII").lower()
			if move=='q':
				clr()
				print("This was the final board, the game was forfeited by user")
				print_board(board,n)
				return 0
			if move not in ('w','a','s','d'):
				print("Invalid Input")
			else:
				 break
		if move=='s':
			board,flag=moving(rotation(board,n),n)
			board=rotation_anti(board,n)
		elif move=='d':
			board,flag=moving(rotation(rotation(board,n),n),n)
			board=rotation(rotation(board,n),n)
		elif move =='w':
			board,flag=moving(rotation_anti(board,n),n)
			board=rotation(board,n)
		elif move=='a':
			board,flag=moving(board,n)
		game_2048(board,n,w,flag)
def start():
	p=argparse.ArgumentParser()
	p.add_argument("--n",help="Provide Board size",type=int,nargs='?',default=5,choices=range(1,40))
	p.add_argument("--w",help="win value",type=int,nargs='?',default=2048,choices=[2**j for j in range(1,50)] )
	arg=p.parse_args()
	board=[[0 for j in range(arg.n)]for i in range(arg.n)]
	game_2048(board,arg.n,arg.w,1)
start()
