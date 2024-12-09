class TennisGame:
    SCORE_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player_scores = {player1_name: 0, player2_name: 0}

    def won_point(self, player_name):
        if player_name in self.player_scores:
            self.player_scores[player_name] += 1

    def get_score(self):
        score1 = self.player_scores[self.player1_name]
        score2 = self.player_scores[self.player2_name]

        if score1 == score2:
            return self._get_equal_score(score1)
        elif score1 >= 4 or score2 >= 4:
            return self._get_advanced_score(score1, score2)
        else:
            return f"{self.SCORE_NAMES[score1]}-{self.SCORE_NAMES[score2]}"

    def _get_equal_score(self, score):
        if score < 3:
            return f"{self.SCORE_NAMES[score]}-All"
        return "Deuce"

    def _get_advanced_score(self, score1, score2):
        score_difference = score1 - score2
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"
