class GameSettings:
    screen_width, screen_height = 454, 550
    screen_center = (screen_width/2, screen_height/2)
    bg_color = (255, 255, 255)
    FPS = 20
    
    max_strikes = 3

class BoardSettings:
    size = 454
    width = size
    height = size
    
    outline_color = (0, 0, 0)
    outline_size = 1
    num_of_outline_border = 4
    
    boxes_solved_to_start = 30

class BoardBoxSettings:
    num_of_boxes_per_section = 9
    box_size = int((BoardSettings.size - BoardSettings.num_of_outline_border)/num_of_boxes_per_section)
    box_width = box_height = box_size
    box_color = (255, 255, 255)
    
    border_size = 1
    border_width = border_height = box_size
    border_color = (190, 198, 212)
    selected_border_color = (0, 122, 204)
    
class StrikeSettings:
    margin = 5

    size = 45
    width = height = size
    