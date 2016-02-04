from nose.tools import eq_
from gothonweb.map import *

def test_room():
    gold = Room('GoldRoom', 
        '''
        This room has gold in it you can grab. There's a door to the north.
        ''')
    eq_(gold.name, 'GoldRoom')
    eq_(gold.paths, {})
    
def test_room_paths():
    center = Room('Center', 'Test room in the center.')
    north = Room('North', 'Test room in the north.')
    south = Room('South', 'Test room in the south.')
    
    center.add_paths({ 'north': north, 'south': south })
    
    eq_(center.go('north'), north)
    eq_(center.go('south'), south)
    
def test_map():
    start = Room('Start', 'You can go west and down a hole.')
    west = Room('Trees', 'There are tress here, you can go east.')    
    down = Room('Dungeon', 'It\'s dark down here, you can go up.')
    
    start.add_paths({ 'west': west, 'down': down })
    west.add_paths({ 'east': start })
    down.add_paths({ 'up': start })
    
    eq_(start.go('west'), west)
    eq_(start.go('west').go('east'), start)
    eq_(start.go('down').go('up'), start)
    
def test_gothon_game_map():
    eq_(START.go('shoot!'), generic_death)
    eq_(START.go('dodge!'), generic_death)
    
    room = START.go('tell a joke')
    eq_(room, laser_weapon_armory)