# You found directions to hidden treasure only written in words. The possible directions are "NORTH", "SOUTH","WEST","EAST".
# "NORTH" and "SOUTH" are opposite directions, as are "EAST" and "WEST". Going one direction and coming back in the opposite direction leads to going nowhere. Someone else also has these directions to the treasure and you need to get there first. Since the directions are long, you decide to write a program to figure out the fastest and most direct route to the treasure.
# Write a function that will take a list of strings and will return a list of strings with the unneeded directions removed (NORTH<->SOUTH or EAST<->WEST side by side).
# Example 1:
# input: ['NORTH','EAST','WEST','SOUTH','WEST','SOUTH','NORTH','WEST']
# output:['WEST','WEST']
# In ['NORTH','EAST','WEST','SOUTH','WEST','SOUTH','NORTH','WEST'] 'NORTH' and 'SOUTH' are not directly opposite but they become directly opposite after reduction of 'EAST' and 'WEST'. The whole path can be reduced to ['WEST','WEST'].
# Example 2:
# input: ['EAST','NORTH','WEST','SOUTH']
# output:['EAST','NORTH','WEST','SOUTH']
# Not all paths are reducible. The path ['EAST','NORTH','WEST','SOUTH'] is not reducible. 'EAST' and 'NORTH', 'NORTH' and 'WEST', 'WEST' and 'SOUTH' are not directly opposite of each other and thus can't be reduced. The resulting path has not changed from the original path: ['EAST','NORTH','WEST','SOUTH']


def solution(path):
    opposites = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST',
    }
    still_long = True
    while still_long:
        still_long = False
        current_dir = 0
        while current_dir < len(path) - 1:
            if path[current_dir] == opposites[path[current_dir+1]]:
                for _ in range(2):
                    path.pop(current_dir)
                still_long = True
            current_dir += 1
    return path


