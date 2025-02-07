from lib.music_manager import *
import pytest

"""
test class instance is instance of MusicManager
"""
def test_music_manager_isinstance_of_MusicManager():
    music_manager = MusicManager()
    assert isinstance(music_manager, MusicManager) #isinstance returns True

"""
test class instance initialises with empty arr
"""
def test_music_manager_instances_with_tracks_empty_array():
    music_manager = MusicManager() # []
    assert music_manager.tracks == []

"""
test view_tracks returns tracklist
"""
def test_view_tracks_method_returns_tracklist():
    music_manager = MusicManager()
    assert music_manager.view_tracks() == []

"""
test add method successfully adds a track to the list
"""
def test_add_method_correctly_adds_track_to_list():
    music_manager = MusicManager()
    music_manager.add('track') # ['track']
    assert music_manager.view_tracks() == ['track']

"""
test add method raises err when input is empty str
"""
def test_add_method_raises_err_when_input_is_empty_str():
    with pytest.raises(Exception) as err:
        music_manager = MusicManager()
        music_manager.add('')
    err_msg = str(err.value)
    assert err_msg == 'Error: track must be a string with more than 1 char'

"""
test add method raises err when input not type str
"""
def test_add_method_raises_err_when_input_not_of_type_str():
    music_manager = MusicManager()
    with pytest.raises(Exception) as e:
        music_manager.add(42) 
    assert str(e.value) == 'Error: track must be a string with more than 1 char'