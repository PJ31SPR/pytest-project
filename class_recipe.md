# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem


As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicManager:
    # User-facing properties:
    #   tracks: array of strings

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   Will create instance of class with empty arr
        pass # No code here yet

    def add(self, track):
        # Parameters:
        #   track: string
        # Returns:
        #   Nothing
        # Side-effects
        #   adds track to list 
        pass # No code here yet

    def view_tracks(self):
        # Returns:
        #   A list of all added tracks
        # Side-effects:
        #   none
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
test class instance is instance of MusicManager
"""
music_manager = MusicManager() #isinstance returns True


"""
test class instance initialises with empty arr
"""
music_manager = MusicManager() # []

"""
test view_tracks returns tracklist
"""
music_manager = MusicManager()
music_manager.view_tracks() # []

"""
test add method successfully adds a track to the list
"""
music_manager = MusicManager()
music_manager.add('track') # ['track']

"""
test add method raises err when input is empty str
"""
music_manager = MusicManager()
music_manager.add('') # err msg

"""
test add method raises err when input not type str
"""
music_manager = MusicManager()
music_manager.add(42) # err msg 

"""
test add method raises err msg when user tries to add more than 1 track at once
"""
music_manager = MusicManager()
music_manager.add('californication', 'happy birthday') # err msg

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
