#################################################################
###### https://adventofcode.com/2022/day/2 ######################
#################################################################

file = "input.txt"

DAY_NO = "2"
PART = "2"

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
		self.outcomeTranslationDict = {'X':'Lose', 'Y': 'Draw', 'Z': 'Win'}
		self.input = input
		self.total_score = 0

		self.main()

	def determine_outcome(self, oponent_move, outcome):

		match (oponent_move, outcome):
			case ('Rock', 'Lose')|('Paper', 'Win')|('Scissors', 'Draw'): ##we playe scissors
				return self.action_score['Scissors'] + self.outcome_score[outcome]
			
			case ('Rock', 'Win')|('Paper', 'Draw')|('Scissors','Lose'): ##we play paper
				return self.action_score['Paper'] + self.outcome_score[outcome]
			
			case ('Rock', 'Draw')|('Paper', 'Lose')|('Scissors', 'Win'): ##we play rock
				return self.action_score['Rock'] + self.outcome_score[outcome]

	def main(self):
		for opponent_move, outcome in self.input:
			opponentMoveTranslated = self.opponentTranslationDict[opponent_move]
			outcomeTranslated = self.outcomeTranslationDict[outcome]
			self.total_score += self.determine_outcome(opponentMoveTranslated, outcomeTranslated)
		
		print(self.total_score)

game = Game(cleaner_input)

