#current_min, current_max => current value of the screen
#new_min, new_max => eto yung ortho size
#value => eto yung gusto mo i-map na point

#where the current point is in relation to the ratio of the ortho
def map_value(current_min, current_max, new_min, new_max, value):
    current_range = current_max - current_min       #how long the x or y axis is, ex: if 0 to 1000 that's 1000 pero if -100 to 1000 that's 1100
    new_range = new_max - new_min
    return new_min + new_range * ((value - current_min)/current_range)