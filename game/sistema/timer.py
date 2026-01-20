
class Timer:
    def __init__(self, total_time):
        self.total_time = total_time
        self.time_left = total_time

    def update(self, dt):
        self.time_left -= dt
        if self.time_left < 0:
            self.time_left = 0

    def is_over(self):
        return self.time_left <= 0

    def draw(self, screen, font):
        minutes = int(self.time_left) // 60
        seconds = int(self.time_left) % 60
        text = f"Encontre o Trem: {minutes:02d}:{seconds:02d}"
        surf = font.render(text, True, (255, 255, 255))
        screen.blit(surf, (10, 10))
