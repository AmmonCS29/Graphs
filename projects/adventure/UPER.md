# UPER
## Understand
-Graph consisting 500 rooms
-Objective: Create `traversal_path` to do a search function of the graph that will visit every room once. 

ADV.py
    Four Parts
    1. World generation code: DO NOT MODIFY THIS
    2. An incomplete list of directions: FILL THIS WITH CORRECT DIRECTIONS
    3. test code that can be ran in the terminal `python3 adv.py`
    4. REPL code. You can uncomment this and run `python3 adv.py` to walk around the map.

Commands: Remember thes and look into using for PLANNING
- `player.current_room.id`
- `player.current_room.get_exits()`
- `player.travel(direction)`

Construct my own traversal graph to solve. 
    -This is a dictionary with key value pairs.
    -`key` = room number
    -`value` = dictionary with direction as key and the room number as the value. The default value is a ? until you travel to the position. Then replace it with the room number or None if you can't go any other direction. 
Start in room `0`
`0` has the directions `['n', 's', 'w', 'e']`

You are done when you have 500 enteries in the graph 0 - 499 and no `?` in the values of the directions

## Plan
create a stack
Record the current room in visited
load the current room to the stack
pop off the current room to the stack

pick a random direction from players current room that have not been visited. 
move in that direction
record to visited graph
do it again. 
if not able to move in that direction: 
    assign direction value None
    pick an unvisited direction
    if able to move there:

# First pass solution: 
-  Record the room in visited
-  Get all the exits with the room.
-  Move in one direction, add this to the traversal path and pop it off the directions associated with the room
-  Work out the opposite direction and add this to a reverse path so that backtracking is possible and remove the opposite direction from the unexplored paths
-  Get exits for the new room and keep note of this (in visited)
-  Move in a random direction again and add to the traversal path and pop it off the possible directions
-  Keep moving until you reach a dead end
-  When there are no more unexplored exits - backtrack along the last direction on the backtracked path and remove it from the backtracked path and add it to the traversal path
-  Check that room for unexplored directions and repeat the process again
-  This keeps going until the number of rooms visited reaches the length of the rooms graph


## Execute

## Review/Revise