import pygame as pg

pg.init()

# To see different informations like the size of the laptop screen
VideoInfo = pg.display.Info()

# To collect the width and the height of the laptop
WIDTH = VideoInfo.current_w
HEIGHT = VideoInfo.current_h

# To create the clock and permit to have the same break time
FPSHorloge = pg.time.Clock()
FPS = 50

RUNNING = True

# For the window of the game
screen = pg.display.set_mode((1000, 500))

class Character(pg.sprite.Sprite):
    def __init__(self, file, width, height):
        super().__init__()
        self.file = pg.image.load(file)
        self.mask = pg.mask.from_surface(self.file)
        self.width_file = self.file.get_width()
        self.height_file = self.file.get_height()
        self.X, self.Y = (width/3), (height-self.height_file)
        self.rect = self.file.get_rect(x=self.X, y=self.Y)
        self.rect.y -= 20
        self.speed = 5
        self.velocity = [0, 0]        

    def draw(self, screen, frame_rect):
        screen.blit(self.file, self.rect, area=frame_rect)

'''la classe et le code d'en dessous sont séparé dans deux codes différents, file étant mon image'''
file = Character('assets/Anakin_Skywalker1-removebg-preview.png',1000, 500)
frame = 0
width_perso = 100
frame_rect = pg.Rect(frame*width_perso, 0, 50, file.height_file)
time_next = 10
current_time = pg.time.get_ticks()


while RUNNING:
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    if current_time+100 < pg.time.get_ticks():
        current_time = pg.time.get_ticks()
        # To change the partition of image
        frame = (frame+1) % 13
        frame_rect = pg.Rect(frame * width_perso, -10, 33, file.height_file)
    file.draw(screen, frame_rect)

    pg.display.flip()   # Mise à jour de l’affichage de la fenêtre
    FPSHorloge.tick(FPS) 