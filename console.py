import pdb
from models.event import Event
from models.player import Player
from models.match import Match

import repositories.event_repository as event_repository
import repositories.match_repository as match_repository
import repositories.player_repository as player_repository

event1 = Event("Jacob", "Jaocb", "skcsc")
event_repository.save(event1)

jacob_player = Player("Jacob", "Male", 73)
player_repository.save(jacob_player)

john_player = Player("John", "Male", 73)




