from text_class import Text
from datetime import datetime
from settings import BoardSettings

class StopWatch:
    def __init__(self):
        self.start()
        
        self.marginx = 10
        self.marginy = 15

    def start(self):
        self.start_time = datetime.now()

    def update(self):   
        def hours_left_in(seconds):
            minutes = seconds//60
            hours = minutes//60
            return hours
        
        def mins_left_in(seconds):
            hours = hours_left_in(seconds)
            
            seconds_in_hours = hours * 3600
            seconds_left = seconds - seconds_in_hours
            
            minutes = seconds_left//60
 
            return minutes
        
        def secs_left_in(seconds):
            hours = hours_left_in(seconds)
            minutes = mins_left_in(seconds)
            
            seconds_in_hours = hours * 3600
            seconds_in_minutes = minutes * 60
            
            seconds_left = seconds - seconds_in_hours - seconds_in_minutes
            
            return seconds_left
        
        def update_text():
            if self.mins_run < 10:
                self.mins_run = '0' + str(self.mins_run)
            if self.secs_run < 10:
                self.secs_run = '0' + str(self.secs_run)
            
            self.time_text = str(self.hours_run) + ':' + str(self.mins_run) + ':' + str(self.secs_run)
            self.time_text = Text(self.time_text, 75, (0, 0, 0), (0,0))
            self.time_text.text_rect.right = BoardSettings.width - self.marginx
            self.time_text.text_rect.top = BoardSettings.height + self.marginy

        self.elasped_time = datetime.now() - self.start_time
        self.elasped_secs = self.elasped_time.seconds
        self.hours_run = hours_left_in(self.elasped_secs)
        self.mins_run = mins_left_in(self.elasped_secs)
        self.secs_run = secs_left_in(self.elasped_secs)
        update_text()
        
    def reset(self):
        self.start()
        
    def draw_time_clock(self, screen):
        screen.blit(self.time_text.text_image, self.time_text.text_rect)
        