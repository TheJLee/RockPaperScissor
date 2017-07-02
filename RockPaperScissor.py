from random import randint

def StartGame():
	print "hello"
	Answer = raw_input("Type yes if you want to play the game and no if you dont ")
	State = 0
	UserScore = 0
	ComputerScore= 0
	if(Answer == "yes"):
		Active = True;
	else:
		Active = False
	
	while(Active):
		print ("Score" , UserScore, ComputerScore)
		Selection = raw_input("Type rock, paper, or scissor ")

		State = Process(Selection,State)
		if(State>0):
			UserScore += 1
		elif(State==0):
			print "no increase because tie"
		else:
			ComputerScore += 1
		Answer = raw_input("Type yes if you want to continue and no if otherwise ")
		if(Answer == "yes"):
			Active = True;
			Score = 0
		else:
			Active = False
	print "Exiting"

def Process(Selection, Score):
	pick = randint(0,2)
	RPS_List = ["rock","paper","scissor"]
	if(Selection==RPS_List[pick]):
		print"Tie"
		return Score
	elif(Selection == "rock" and RPS_List[pick] == "paper"):
		print "Lose"
		Score -= 1
		return Score
	elif(Selection == "rock" and RPS_List[pick] == "scissor"):
		print "Win"
		Score += 1
		return Score
	elif(Selection == "paper" and RPS_List[pick] == "scissor"):
		print "Lose"
		Score -= 1
		return Score
	elif(Selection == "paper" and RPS_List[pick] == "rock"):
		print "Win"
		Score += 1
		return Score
	elif(Selection == "scissor" and RPS_List[pick] == "rock"):
		print "Lose"
		Score -= 1
		return Score
	elif(Selection == "scissor" and RPS_List[pick] == "paper"):
		print "Win"
		Score += 1
		return Score			

StartGame()
