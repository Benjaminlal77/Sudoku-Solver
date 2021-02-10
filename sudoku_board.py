import pygame 
import random

from settings import BoardSettings, BoardBoxSettings         
from Text_class import Text

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
            
            self.column = self.get_column()
            self.row = self.get_row()
            self.large_box = self.get_large_box()
            self.x, self.y = self.get_cords()
            
            self.nums_tried = []
            self.correct_num = None
            self.solved = False
            self.selected = False
            
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
            if self.column >= 1 and self.column <= 3:
                return True
            else:
                return False
            
        def is_in_second_large_box_column(self):
            if self.column >= 4 and self.column <= 6:
                return True
            else:
                return False
        
        def is_in_third_large_box_column(self):
            if self.column >= 7 and self.column <= 9:
                return True
            else:
                return False
            
        def is_in_first_large_box_row(self):
            if self.row >= 1 and self.row <= 3:
                return True
            else:
                return False
            
        def is_in_second_large_box_row(self):
            if self.row >= 4 and self.row <= 6:
                return True
            else:
                return False
        
        def is_in_third_large_box_row(self):
            if self.row >= 7 and self.row <= 9:
                return True
            else:
                return False
            
           
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
                
            x = ((self.column * BoardBoxSettings.box_width)
                - BoardBoxSettings.box_width) + (BoardSettings.outline_size * self.num_of_column_outline_passed)
            y = ((self.row * BoardBoxSettings.box_height)
                - BoardBoxSettings.box_height) + (BoardSettings.outline_size * self.num_of_row_outline_passed)
            return x,y
                
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
    
        def is_clicked(self):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self.box.collidepoint(mouse_x, mouse_y):
                return True
            else:
                return False

        def is_solved(self, num_input):
            if num_input == self.correct_num:
                return True
            else:
                return False
            
    num_of_possible_nums = 9
    num_of_boxes_in_column = 9
    num_of_boxes_in_row = 9
    num_of_boxes = num_of_boxes_in_column * num_of_boxes_in_row
    def __init__(self):
        self.outline = self.BoardOutline()
        self.boxes = [self.Box(num) for num in range(1, SudokuBoard.num_of_boxes + 1)]    
        self.boxes_solved = 0
        self.solved = False

        self.randomize_board()
        
        for box in self.boxes:
            box.prep_num()
    
    def randomize_board(self):
        def randomize():
            def num_is_valid():
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
                            
            def find_empty_box():
                for box in self.boxes:
                    if box.correct_num == None:
                        return box

            box = find_empty_box()
            
            if not box:
                return True
            
            while len(box.nums_tried) < 9:
                num_to_try = random.randint(1, SudokuBoard.num_of_possible_nums)
                if num_to_try not in box.nums_tried:
                    box.nums_tried.append(num_to_try)
                else:
                    continue
                    
                if num_is_valid():
                    box.correct_num = num_to_try
                    if randomize():
                        return True
                        
                    box.correct_num = None
                    continue
                        
            box.nums_tried.clear()
            return False
                      
        def randomize_nums_solved():
            while self.boxes_solved < BoardSettings.boxes_solved_to_start:
                for box in self.boxes:
                    if random.randint(1, SudokuBoard.num_of_boxes) == 1 and not box.solved:
                        self.boxes_solved += 1
                        box.solved = True
                
        randomize()
        randomize_nums_solved()
                
    def draw_board(self, screen):
        self.outline.draw_outline(screen)
        for box in self.boxes:
            box.draw_box(screen)
            
    def check_if_solved(self):
        for box in self.boxes:
            if box.solved:
                if box.box_num == SudokuBoard.num_of_boxes:
                    self.solved = True
            else:
                self.solved = False
                break
            