import config

def isValidRGB(red: int, green: int, blue: int) -> bool:
    if(red < 0 or 255 < red):
        return False
    
    if(green < 0 or 255 < green):
        return False
    
    if(blue < 0 or 255 < blue):
        return False
    
    return True


def isOnCanvas(x: int, y: int) -> bool:
    if(x < 0 or config.Canvas_Width < x):
        return False
    
    if(y < 0 or config.Canvas_Width < y):
        return False
    
    return True