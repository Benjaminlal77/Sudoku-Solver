class BoardSettings:
    size = 454
    width = size
    height = size
    outline_color = (0, 0, 0)
    outline_size = 1
    num_of_outline_border = 4

class BoardBoxSettings:
    num_of_boxes_per_section = 9
    box_size = int((BoardSettings.size - BoardSettings.num_of_outline_border)/num_of_boxes_per_section)
    box_width = box_height = box_size
    box_color = (255, 255, 255)
    
    border_size = 1
    border_width = border_height = box_size
    border_color = (190, 198, 212)
    
    text_color = (0, 0, 0)
    text_font_size = int(box_size - 1)

class GameSettings:
    screen_width, screen_height = 600, 550
    bg_color = (255, 255, 255)