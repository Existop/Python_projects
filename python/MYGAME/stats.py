from pygame.event import wait


class Stats():
    # Отслеживание статистики

    def __init__(self):    # Инициализирует статистику
        self.reset_stats()
        self.run_game = True
        with open('MYGAME/highscore.txt', 'r') as f: # 'MYGAME/
            self.high_score = int(f.readline())

    def reset_stats(self):
        # статистика, изменяющаяся во время игры
        self.guns_left = 1
        self.score = 0