# Class to represent a Player
class Player:

    # Constructor to initialize player details
    def __init__(self, name, jersey_no, runs):
        self.name = name
        self.jersey_no = jersey_no
        self.runs = runs

    # Method to determine player category based on runs
    def category(self):
        if self.runs >= 1000:
            return "Excellent"
        elif self.runs >= 500:
            return "Good"
        else:
            return "Average"

    # Method to display player details
    def display(self):
        print("Player Name:", self.name)
        print("Jersey Number:", self.jersey_no)
        print("Runs:", self.runs)
        print("Category:", self.category())
        print("------------------------")


# Class to represent a Team
class Team:

    # Constructor to initialize team name and player list
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    # Method to add a player to the team
    def add_player(self, player):
        self.players.append(player)

    # Method to display details of all players
    def display_players(self):
        print("Team:", self.team_name)
        print("========================")
        for player in self.players:
            player.display()


# Creating a Team object
team = Team("India")

# Creating Player objects
p1 = Player("Virat", 18, 1200)
p2 = Player("Rohit", 45, 800)
p3 = Player("Rahul", 1, 300)

# Adding players to the team
team.add_player(p1)
team.add_player(p2)
team.add_player(p3)

# Displaying all player details
team.display_players()