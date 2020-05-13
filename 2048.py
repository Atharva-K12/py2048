import os
import random
import argparse
def rotation_anti(board,n):
    # rotates the complete board in anti clockwise sense
	for i in range(n // 2):
		for j in range(i, n-i-1):
			store_val=board[i][j]
			board[i][j]=board[j][n-1-i]
			board[j][n-1-i]=board[n-1-i][n-1-j]
			board[n-1-i][n-1-j]=board[n-1-j][i]
			board[n-1-j][i]=store_val
	return board
def rotation(board,n):
#rotates the complete board in clockwise sense
	for i in range(n // 2):
		for j in range(i, n-i-1):
			store_val=board[i][j]
			board[i][j]=board[n-1-j][i]
			board[n-1-j][i]=board[n-1-i][n-1-j]
			board[n-1-i][n-1-j]=board[j][n-i-1]
			board[j][n-i-1]=store_val
	return board
def print_board(board,n):
    #printing board
    for i in range(n):
        for j in range(n):
            print(board[i][j],end="  ")
        print()
def clr():
#for clearing screen
  if os.name=="nt" :
    os.system('cls')
  else:
    os.system('clear')
def shifting(board,n):
    #shifts the non zero board values to right
    #sets a flag if nothing changed
	flag=0
	temp=[[0 for i in range(n)] for j in range(n)]
	for i in range(n):
		c=0
		for j in range(n):
			if board[i][j]!=0:
				temp[i][n-c-1]=board[i][j]
				c+=1
	if temp==board:
		flag=1
	return (temp,flag)
def adding(board,n):
    #adds the similar value
    #addition starts from the left end of board like in the actual game
    #sets a flag if nothing is changed
	flag=0
	temp=board.copy()
	for i in range(n):
		for j in range(n-1,0,-1):
			if board[i][j]!=0:
				if board[i][j]==board[i][j-1]:
					board[i][j]*=2
					board[i][j-1]=0
	if temp==board:
		flag=1
	return (board,flag)
def new_2(board,n):
    #genarates random 2 on location with zero
    #non zero locations aren't affected
	while True:
		h=random.choice(range(n))
		k=random.choice(range(n))
		if board[h][k]==0:
			board[h][k]=2
			break
	return board
def moving(board,n):
    #a fn to shift then add and again shifts
    #3 flags are used to check is no changes occured in the Board
    #if all flags are true the new 2 should not be generated hence and
	board,flag1=shifting(board,n)
	board,flag2=adding(board,n)
	board,flag3=shifting(board,n)
	return (board,flag1*flag2*flag3)
def check(board,n,w):
    #fn to check win,loss
    #returns zero if zero(s) is/are present on Board
    #return end if won /lost
    #returns cons is zeros are exhausted but moves are still possible
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
    #this fn does the main work
	ret=check(board,n,w)
	if ret!="end":
		if ret=="zero" and flag==0:
            #flag is false if there was changes in moving
            #and ret is zero if board has zeros left
			board=new_2(board,n)
	ret=check(board,n,w)#rechecked
	if ret!="end":
		clr()
		print_board(board,n)
		while True:#validation of move input
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
			except KeyboardInterrupt:#to make exit possible without display of error
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
    #to take input of n,w and generate a all zero boar of desired size
	p=argparse.ArgumentParser()
	p.add_argument("--n",help="Provide Board size",type=int,nargs='?',default=5)
	p.add_argument("--w",help="win value",type=int,nargs='?',default=2048)
	arg=p.parse_args()
	board=[[0 for j in range(arg.n)]for i in range(arg.n)]
	game_2048(board,arg.n,arg.w,0)
if __name__ == '__main__':
	start()
