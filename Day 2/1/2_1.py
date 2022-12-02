#################################################################
###### https://adventofcode.com/2022/day/2 ######################
#################################################################

file = "input.txt"

DAY_NO = "2"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	raw_input = fd.readlines()

cleaner_input = []
for i in raw_input:
	cleaner_input += [i.strip('\n').split(' ')]

print(cleaner_input)

class Game():

	def __init__(self, input) -> None:
		self.outcome_score = {'Lose': 0, 'Draw': 3, 'Win': 6}
		self.action_score = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

		self.opponentTranslationDict = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
		self.playerTranslationDict = {'X':'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
		self.input = input
		self.total_score = 0

		self.main()

	def determine_outcome(self, oponent_move, player_move):

		match (oponent_move, player_move):
			case ('Rock', 'Scissors')|('Paper', 'Rock')|('Scissors', 'Paper'): ##oponent wins
				return self.action_score[player_move] + self.outcome_score['Lose']
			
			case ('Rock', 'Rock')|('Paper', 'Paper')|('Scissors','Scissors'): ##player draws
				return self.action_score[player_move] + self.outcome_score['Draw']
			
			case ('Rock', 'Paper')|('Paper', 'Scissors')|('Scissors', 'Rock'): ##player wins
				return self.action_score[player_move] + self.outcome_score['Win']

	def main(self):
		for opponent_move, player_move in self.input:
			opponentMoveTranslated = self.opponentTranslationDict[opponent_move]
			playerMoveTranslated = self.playerTranslationDict[player_move]
			self.total_score += self.determine_outcome(opponentMoveTranslated, playerMoveTranslated)
		
		print(self.total_score)

game = Game(cleaner_input)

