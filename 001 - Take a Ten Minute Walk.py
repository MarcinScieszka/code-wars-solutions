"""
"Take a Ten Minute Walk"

You live in the city of Cartesia where all roads are laid out in a perfect grid. 
You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
The city provides its citizens with a Walk Generating App on their phones -
- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block. 

Create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) 
and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). 
It will never give you an empty array (that's not a walk, that's standing still!).
"""


#determine if walk is valid
def is_valid_walk_0(walk):
    if len(walk) != 10:
        # walk is shorter/longer than 10 minutes
        return False

    x_coordinate = 0
    y_coordinate = 0

    for direction in walk:
        if direction == 'n':
            x_coordinate += 1
        elif direction == 's':
            x_coordinate -= 1
        elif direction == 'w':
            y_coordinate += 1
        elif direction == 'e':
            y_coordinate -= 1

    if (not x_coordinate) and (not y_coordinate):
        # x and y are in the original position
        return True
    else:
        return False

def is_valid_walk_1(walk):
    # walk is valid when it is 10 minutes long and nr of north-south and west-east directions are equal
    if len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e'):
        return True
    else:
        return False