
print "Welcome to the tic tac toe"
player = raw_input("Please select a player, (1): Player One, (2): Player Two")
letter = raw_input("Please select (x): x or (o): o")
location = int(raw_input("Where would you like to put the piece? (1-9) "))


class Board(object):
	def __init__(self):
		self.boardarray = [1,2,3,4,5,6,7,8,9]

	def showBoard(self):
		print "{0} - {1} - {2}".format(self.boardarray[0], self.boardarray[1], self.boardarray[2])
		print "{0} - {1} - {2}".format(self.boardarray[3], self.boardarray[4], self.boardarray[5])
		print "{0} - {1} - {2}".format(self.boardarray[6], self.boardarray[7], self.boardarray[8])

	def addLetter(self, letter, location):
		if self.boardarray[int(location-1)] != "x" or self.boardarray[int(location-1)] != "o":
			self.boardarray[int(location-1)] = str(letter)

newboard = Board()
while letter != "q":
	if letter == "x":
		location = raw_input("Where would you like to place the letter? (1-9) ")
	elif letter == "o":
		location = raw_input("Where would you like to place the letter? (1-9) ")
	else:
		print "You messed up our game, jerk" 

	newboard.addLetter(letter, location)
	newboard.showBoard()

	letter = raw_input("Please select (x): x or (o): o ")
	location = int(raw_input("Where would you like to put the piece? (1-9) "))






# def letterSelection(letter, location):
# 	while letter != 'q':
# 		if letter == 'x':
# # 			newboard.addLetter(letter, location)
# # 			newboard.showBoard()
# # 		if letter == 'o':
# # 			newboard.addLetter(letter, location)
# # 			newboard.showBoard()

# newboard = Board()
# # letterSelection(letter, location)
# newboard.showBoard() 
