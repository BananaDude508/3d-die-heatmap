from vpython import vector, color

lowest_color = color.blue
expected_color = color.white
highest_color = color.red

def blend(c1,c2,t): # literally just lerping vectors
    x = c1.x * (1-t) + c2.x * t
    y = c1.y * (1-t) + c2.y * t
    z = c1.z * (1-t) + c2.z * t
    return vector(x,y,z)

def calculate_color(weightmap, face):
    value = weightmap[face]
    max_value = max(weightmap)
    min_value = min(weightmap)
    expected = sum(weightmap)/len(weightmap)
    
    if (value == expected):
        return expected_color;
    if (value > expected):
        return blend(expected_color, highest_color, (expected - value) / (expected - max_value))
    if (value < expected):
        return blend(lowest_color, expected_color, (min_value - value) / (min_value - expected))