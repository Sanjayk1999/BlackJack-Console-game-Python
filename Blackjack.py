import random

cards = ['CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CK','CQ','CJ',
		'DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DK','DQ','DJ',
		'HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HK','HQ','HJ',
		'SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SK','SQ','SJ']

playersum = [0,0]
dealersum = [0,0]
playerhand = []
dealerhand = []
blackjack = False
bust = False
dealerwon = False
newround = False
playercash = 0
dealercash = 0

#To Get the initial Cards for the player and dealer
def initialCards(cards,arr,hand):
	j=0
	while(j<2):
		i = random.randint(0,len(cards)-1)
		hand.append(cards[i])
		if(cards[i][1]=='1' or cards[i][1]=='K' or cards[i][1]=='Q' or cards[i][1]=='J'):
			arr[0] = arr[0]+10
			arr[1] = arr[1]+10
			cards.pop(i)
		elif(cards[i][1]=='A'):
			arr[0] = arr[0]+1
			arr[1] = arr[1]+11
			cards.pop(i)
		else:
			n = int(cards[i][1])
			arr[0] = arr[0]+n
			arr[1] = arr[1]+n
			cards.pop(i)			
		j = j+1
	return arr
	return hand

#Display the Player cards
def displayPlayerCard(card,cardsum):
	print('Player cards are \n')
	for i in range(0,len(card)):
		print(card[i],end=" ")
	print('\n')
	print('Player card sum')
	# for i in range(0,len(cardsum)):
	# 	print(cardsum[i],end="/")
	# print('\n')
	print(cardsum[0],'/',cardsum[1])

#Display the dealer cards at first. only display the first card
def displayDealerCard(card,cardsum):
	print('Dealer cards is ')
	print(card[0],'?',end=" ")
	print('\n')

def startNewRound():
	global blackjack,dealerwon,bust,newround,playersum,dealersum,dealerhand,playerhand
	playersum = [0,0]
	dealersum = [0,0]
	dealerhand = []
	playerhand = []
	blackjack= False
	dealerwon = False
	bust = False
	newround = False
#Check if player and dealers hands is blackjack
def checkBlackjack(psum,dsum):
	global blackjack,playercash,dealercash,dealerwon
	for i in range(0,len(psum)):
		if(psum[i]==21):
			print('Blackjack! Player Won')
			blackjack = True
			playercash = playercash + 20
			print(playercash,dealercash)
			break
	for j in range(0,len(dsum)):
		if(dsum[i]==21):
			print('Blackjack! Dealer Won')
			blackjack = True
			dealerwon = True
			dealercash = dealercash + 20
			print(playercash,dealercash)
			break
#Hit function for the Player

def hit(cards,arr,hand):
	i = random.randint(0,len(cards)-1)
	hand.append(cards[i])
	if(cards[i][1]=='1' or cards[i][1]=='K' or cards[i][1]=='Q' or cards[i][1]=='J'):
		arr[0] = arr[0]+10
		arr[1] = arr[1]+10
		cards.pop(i)
	elif(cards[i][1]=='A'):
		arr[0] = arr[0]+1
		arr[1] = arr[1]+11
		cards.pop(i)
	else:
		n = int(cards[i][1])
		arr[0] = arr[0]+n
		arr[1] = arr[1]+n
		cards.pop(i)

# Hit function for the Dealer
def hitDealer(cards,arr,hand):
	i = random.randint(0,len(cards)-1)
	hand.append(cards[i])
	print(cards[i])
	print('\n')
	if(cards[i][1]=='1' or cards[i][1]=='K' or cards[i][1]=='Q' or cards[i][1]=='J'):
		arr[0] = arr[0]+10
		arr[1] = arr[1]+10
		cards.pop(i)
	elif(cards[i][1]=='A'):
		arr[0] = arr[0]+1
		arr[1] = arr[1]+11
		cards.pop(i)
	else:
		n = int(cards[i][1])
		arr[0] = arr[0]+n
		arr[1] = arr[1]+n
		cards.pop(i)

#Check If cards Bust

def checkBust(psum,dsum):
	global bust,playercash,dealercash
	if(psum[0]>21 and psum[1]>21):
		print('Player\'s Cards Busted')
		bust = True
		dealercash = dealercash + 10
		# print(playercash,dealercash)
		print('Player cash is ',playercash)
		print('Dealer cash is ',dealercash)
	if(dsum[0]>21 and dsum[1]>21):
		print('Dealer\'s Cards Busted')
		bust = True
		playercash = playercash + 10
		print('Player cash is ',playercash)
		print('Dealer cash is ',dealercash)
		print(dsum[0],dsum[1])

def displayAllCards(hand):
	for i in range(0,len(hand)):
		print(hand[i],end=' ')
	print('\n')

def checkWin(psum,dsum):
	global dealerwon
	if((dsum[0]==dsum[1]) and dsum[0]<21):
		if(dsum[0]>psum[0] and dsum[0]>psum[1]):
			dealerwon = True
	if(dsum[0]>psum[0] and dsum[0]<21):
		dealerwon = True
	if(dsum[0]>psum[1] and dsum[0]<21):
		dealerwon = True
	if(dsum[1]>psum[0] and dsum[1]<21):
		dealerwon = True
	if(dsum[1]>psum[1] and dsum[1]<21):
		dealerwon = True

#Stand function
def stand(cards,dsum,hand):
	global playercash,dealercash,newround,blackjack
	print(dsum[0],dsum[1])
	checkWin(playersum,dealersum)
	while((dsum[0]<21 or dsum[1]<21) and  not dealerwon):
		hitDealer(cards,dsum,hand)
		checkBlackjack(playersum,dealersum)
		print(dsum[0],dsum[1])
		checkWin(playersum,dealersum)
	if(dealerwon and blackjack):
		print('Dealer Won')
		print('Dealer cash is ',dealercash)
	elif(dealerwon):
		dealercash = dealercash + 10
		print('Dealer Won')
		print('Dealer cash is ',dealercash)		
	else:
		print('Player Won')
		playercash = playercash+10
		print('Player cash is',playercash)
	newround = True

while(len(cards)>3):
	initialCards(cards,playersum,playerhand)
	initialCards(cards,dealersum,dealerhand)
	displayPlayerCard(playerhand,playersum)
	displayDealerCard(dealerhand,dealersum)
	checkBlackjack(playersum,dealersum)
	while(not blackjack and not bust and not newround):
		print('1.Hit and 2. Stand')
		choice = int(input())
		if(choice == 1):
			hit(cards,playersum,playerhand)
			displayPlayerCard(playerhand,playersum)
			checkBlackjack(playersum,dealersum)
			checkBust(playersum,dealersum)
		elif(choice==2):
			stand(cards,dealersum,dealerhand)
		else:
			print("enter the right choice")
	print('Next round')
	print('The player cash is ',playercash)
	print('The delaer cash is ',dealercash)
	startNewRound()