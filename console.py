import pdb
from models.event import Event
from models.player import Player
from models.match import Match

import repositories.event_repository as event_repository
import repositories.match_repository as match_repository
import repositories.player_repository as player_repository

match_repository.delete_all()
player_repository.delete_all()
event_repository.delete_all()

event1 = Event("Scottish Championships", "Largs", "10/11/2021")
event_repository.save(event1)

event2 = Event("Scottish Open", "Motherwell", "19/01/2022")
event_repository.save(event2)

event3 = Event("English Open", "London", "02/02/2022")
event_repository.save(event3)

jacob_player = Player("Jacob", "Male", 73)
player_repository.save(jacob_player)

john_player = Player("John", "Male", 73)
player_repository.save(john_player)

james_player = Player ("James", "Male", 75)
player_repository.save(james_player)

match1 = Match(jacob_player, john_player, event1, jacob_player)
match_repository.save(match1)

match2 = Match(jacob_player, james_player, event2, jacob_player)
match_repository.save(match2)

match3 = Match(james_player, john_player, event1, john_player)

pdb.set_trace()



