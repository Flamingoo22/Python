players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]



# C1:
class Player:
    def __init__(self, array):
        self.name = array["name"]
        self.age = array["age"]
        self.position = array["position"]
        self.team = array["team"]

Player_Joel = Player(players[-2])

print(Player_Joel.name)
# C2
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

# Create your Player instances here!
class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.age = dict["age"]
        self.position = dict["position"]
        self.team = dict["team"]
# player_jason = ???
player_jason = Player(jason)



#C3
class Player:
    team=[]
    def __init__(self, array):
        self.name = array["name"]
        self.age = array["age"]
        self.position = array["position"]
        self.team = array["team"]
        Player.team.append(array)
        
    @classmethod
    def get_team(cls,team_list):
        for i in range(len(players)):
            Player.team[i]["team"] = team_list
        return cls



new_team = []

for i in range(len(players)):
    new_team.append(Player(players[i]))

Player.get_team("SeaWolf")

print(Player.team)
