# Create empy set by calling set()
# Sets ignore duplicate values
# Sets are not ordered 
colors = {'red', 'green', 'blue'}
colors.add('yellow') # adds item to end if not present 
colors.remove('blue') # throws error if item not present
colors.discard('blue') # does not throw error if item not present

numbers = {1, 2, 3}
numbers.update(colors) # Adds set to the end of set in ()

# Check for membership
'red' in colors

rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'violet'}
my_fav_colors = {'red', 'gold', 'green'}

rainbow_colors | my_fav_colors # | == union()

rainbow_colors & my_fav_colors # & == intersection()

rainbow_colors ^ my_fav_colors # ^ == diff()
