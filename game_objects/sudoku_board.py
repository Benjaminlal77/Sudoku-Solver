import pygame 
import random

from settings import GameSettings, BoardSettings, BoardBoxSettings        
from text_box import Text
from events import check_events_while_solving
from update import update_screen_while_solving

class SudokuBoard:
    class BoardOutline:
        def __init__(self):
            self.rect = pygame.Rect(0, 0, 0, 0)
            self.rect.width = BoardSettings.width
            self.rect.height = BoardSettings.height
            
            self.color = BoardSettings.outline_color
            
        def draw_outline(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)
            
    class Box:
        def __init__(self, box_num):
            self.box_num = box_num
            self.unsolved_box_num = 0
            
            # Define location
            
            self.column = self.get_column()
            self.row = self.get_row()
            self.large_box = self.get_large_box()
            self.x, self.y = self.get_cords()
            
            self.nums_tried = []
            self.correct_num = None

            self.selected = False
            self.solved = False
            
            self.make_border()
            self.make_box()
            
        def get_column(self):
            if self.box_num % SudokuBoard.num_of_boxes_in_column == 1:
                return 1
            elif self.box_num % SudokuBoard.num_of_boxes_in_column == 2:
                return 2
            elif self.box_num % SudokuBoard.num_of_boxes_in_column == 3:
                return 3
            elif self.box_num % SudokuBoard.num_of_boxes_in_column == 4:
                return 4
            elif self.box_num % SudokuBoard.num_of_boxes_in_column == 5:
                return 5
            elif self.box_num % SudokuBoard.num_of_boxes_in_column == 6:
                return 6
            elif self.box_num % SudokuBoard.num_of_boxes_in_column == 7:
                return 7
            elif self.box_num % SudokuBoard.num_of_boxes_in_column == 8:
                return 8
            elif self.box_num % SudokuBoard.num_of_boxes_in_column == 0:
                return 9
        
        def get_row(self):
            if self.box_num <= SudokuBoard.num_of_boxes_in_row:
                return 1
            elif self.box_num <= SudokuBoard.num_of_boxes_in_row * 2:
                return 2
            elif self.box_num <= SudokuBoard.num_of_boxes_in_row * 3:
                return 3
            elif self.box_num <= SudokuBoard.num_of_boxes_in_row * 4:
                return 4
            elif self.box_num <= SudokuBoard.num_of_boxes_in_row * 5:
                return 5
            elif self.box_num <= SudokuBoard.num_of_boxes_in_row * 6:
                return 6
            elif self.box_num <= SudokuBoard.num_of_boxes_in_row * 7:
                return 7
            elif self.box_num <= SudokuBoard.num_of_boxes_in_row * 8:
                return 8
            elif self.box_num <= SudokuBoard.num_of_boxes_in_row * 9:
                return 9
            
        def get_large_box(self):
            if self.is_in_first_large_box_column() and self.is_in_first_large_box_row():
                return 1
            elif self.is_in_second_large_box_column() and self.is_in_first_large_box_row():
                return 2
            elif self.is_in_third_large_box_column() and self.is_in_first_large_box_row():
                return 3
                
            elif self.is_in_first_large_box_column() and self.is_in_second_large_box_row():
                return 4
            elif self.is_in_second_large_box_column() and self.is_in_second_large_box_row():
                return 5
            elif self.is_in_third_large_box_column() and self.is_in_second_large_box_row():
                return 6
            
            elif self.is_in_first_large_box_column() and self.is_in_third_large_box_row():
                return 7
            elif self.is_in_second_large_box_column() and self.is_in_third_large_box_row():
                return 8
            elif self.is_in_third_large_box_column() and self.is_in_third_large_box_row():
                return 9
            
        def is_in_first_large_box_column(self):
            return self.column >= 1 and self.column <= 3
            
        def is_in_second_large_box_column(self):
            return self.column >= 4 and self.column <= 6
        
        def is_in_third_large_box_column(self):
            return self.column >= 7 and self.column <= 9
            
        def is_in_first_large_box_row(self):
            return self.row >= 1 and self.row <= 3
            
        def is_in_second_large_box_row(self):
            return self.row >= 4 and self.row <= 6
        
        def is_in_third_large_box_row(self):
            return self.row >= 7 and self.row <= 9
                    
        def get_cords(self):
            def find_outlines_passed():
                self.num_of_column_outline_passed = 0
                self.num_of_row_outline_passed = 0
                
                if self.is_in_first_large_box_column():
                    self.num_of_column_outline_passed = 1
                elif self.is_in_second_large_box_column():
                    self.num_of_column_outline_passed = 2   
                elif self.is_in_third_large_box_column():
                    self.num_of_column_outline_passed = 3
                    
                if self.is_in_first_large_box_row():
                    self.num_of_row_outline_passed = 1
                elif self.is_in_second_large_box_row():
                    self.num_of_row_outline_passed = 2
                elif self.is_in_third_large_box_row():
                    self.num_of_row_outline_passed = 3
         
            find_outlines_passed()
                
            x = (self.column * BoardBoxSettings.box_width) - BoardBoxSettings.box_width
            x += (BoardSettings.outline_size * self.num_of_column_outline_passed)
            
            y = (self.row * BoardBoxSettings.box_height) - BoardBoxSettings.box_height
            y += BoardSettings.outline_size * self.num_of_row_outline_passed
            
            return x,y
               
        def is_first_unsolved_box(self):
            return self.unsolved_box_num == 1
               
        def is_last_box(self):
            return self.box_num == SudokuBoard.num_of_boxes
               
        def is_clicked(self):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            return self.box.collidepoint(mouse_x, mouse_y)

        def is_solved(self, num_input):
            return num_input == self.correct_num
                
        def tried_all_nums(self):
            return len(self.nums_tried) == 9
                
        def make_box(self):
            self.box = pygame.Rect(0, 0, 0, 0)
            
            self.box.x = self.x + BoardBoxSettings.border_size
            self.box.y = self.y + BoardBoxSettings.border_size
            
            self.box.w = BoardBoxSettings.box_width - (BoardBoxSettings.border_size * 2)
            self.box.h = BoardBoxSettings.box_height - (BoardBoxSettings.border_size * 2)
        
            self.box_color = BoardBoxSettings.box_color
                
        def make_border(self):
            self.border = pygame.Rect(0,0,0,0)
            
            self.border.x = self.x
            self.border.y = self.y
            
            self.border.w = BoardBoxSettings.border_width
            self.border.h = BoardBoxSettings.border_height
            
            self.border_color = BoardBoxSettings.border_color
            
        def prep_num(self):
            text = self.correct_num
            text_size = self.box.width - 1
            text_color = (0, 0, 0)
            text_cords = self.box.center
            
            self.num_text = Text(text, text_size, text_color, text_cords)
            
        def draw_box(self, screen):
            screen.fill(self.border_color, self.border)
            screen.fill(self.box_color, self.box)
            
            if self.solved:
                screen.blit(self.num_text.text_image, self.num_text.text_rect)

    num_of_possible_nums = 9
    num_of_boxes_in_column = 9
    num_of_boxes_in_row = 9
    num_of_boxes = num_of_boxes_in_column * num_of_boxes_in_row
    
    def __init__(self):
        self.outline = self.BoardOutline()
        self.boxes = [self.Box(num) for num in range(1, SudokuBoard.num_of_boxes + 1)]    
        
        self.boxes_solved = 0
        self.solved = False
        self.solve_speed = BoardSettings.solve_speed

        self.randomize_board()


    def check_if_solved(self):
        for box in self.boxes:
            if box.solved:
                if box.is_last_box():
                    self.solved = True
            else:
                self.solved = False
                break
    
    def check_for_box_select(self, stats):
        for box in self.boxes:
            box.selected = False
            if box.is_clicked():
                if not box.solved:
                    box.selected = True
                elif stats.creating_board:
                    box.selected = True
    
    def update_unsolved_boxes(self):
        self.clear_unsolved_nums()
        unsolved_box_num = 0
        for box in self.boxes:
            if not box.solved:
                unsolved_box_num += 1
                box.unsolved_box_num = unsolved_box_num
            
    def clear_unsolved_nums(self):
        for box in self.boxes:
            if not box.solved:
                box.correct_num = None
    
    def find_empty_box(self):
        for box in self.boxes:
            if box.correct_num == None:
                return box
    
    def num_is_valid(self, box, num_to_try):
        for other_box in self.boxes:
            if box == other_box:
                continue
            
            if box.row == other_box.row:
                if num_to_try == other_box.correct_num:
                    return False
            if box.column == other_box.column:
                if num_to_try == other_box.correct_num:
                    return False
            if box.large_box == other_box.large_box:
                if num_to_try == other_box.correct_num:
                    return False

        return True
    
    def randomize_board(self):
        def randomize():    
            box = self.find_empty_box()
            
            if not box:
                return True
            
            while not box.tried_all_nums():
                num_to_try = random.randint(1, SudokuBoard.num_of_possible_nums)
                if num_to_try not in box.nums_tried:
                    box.nums_tried.append(num_to_try)
                else:
                    continue
                    
                if self.num_is_valid(box, num_to_try):
                    box.correct_num = num_to_try
                    if randomize():
                        return True
                    else:                        
                        box.correct_num = None
                        continue
                        
            box.nums_tried.clear()
            return False
                      
        def randomize_nums_solved():
            while self.boxes_solved < GameSettings.boxes_solved_to_start:
                for box in self.boxes:
                    if not box.solved:
                        chance = random.randint(1, SudokuBoard.num_of_boxes) == 1
                        if chance:
                            self.boxes_solved += 1
                            box.solved = True
                
        randomize()
        randomize_nums_solved()
                
        for box in self.boxes:
            box.prep_num()
                
    def solve(self, screen, game_objects, stats):
        box = self.find_empty_box()
                    
        if not box:
            return True
        
        if box.is_first_unsolved_box() and box.tried_all_nums():
            return False
        
        for num_to_try in range(1, SudokuBoard.num_of_possible_nums + 1):  
            box.nums_tried.append(num_to_try)
            if self.num_is_valid(box, num_to_try):
                box.correct_num = num_to_try
                box.solved = True
                box.prep_num()

                check_events_while_solving(stats)
                if not stats.fast_solve:
                    update_screen_while_solving(screen, game_objects)
                    pygame.time.Clock().tick(self.solve_speed)
                
                if self.solve(screen, game_objects, stats):
                    return True
                
                else:                
                    box.correct_num = None
                    box.solved = False
                    box.border_color = (255, 0, 0)
                    box.make_border()
            
        return False
            
    def reset(self):
        self.boxes_solved = 0
        for box in self.boxes:   
            box.selected = False  
            box.correct_num = None
            box.nums_tried.clear()
            box.solved = False   
                                   
    def draw_board(self, screen):
        self.outline.draw_outline(screen)
        for box in self.boxes:
            box.draw_box(screen)
            