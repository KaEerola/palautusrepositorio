import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # Injektoi "stub" StatisticsService-luokalle
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Lemieux")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")

    def test_search_returns_none_for_nonexistent_player(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
        self.assertTrue(all(player.team == "EDM" for player in team_players))

    def test_team_returns_empty_list_for_nonexistent_team(self):
        team_players = self.stats.team("XYZ")
        self.assertEqual(len(team_players), 0)

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(len(top_players), 2)

    def test_top_handles_zero_players(self):
        top_players = self.stats.top(0, SortBy.POINTS)
        self.assertEqual(len(top_players), 0)

    def test_top_returns_correct_goal_leaders(self):
        top_player = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(top_player[0].name, "Lemieux")
    
    def test_returns_correct_top_assister(self):
        top_player = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(top_player[0].name, "Gretzky")