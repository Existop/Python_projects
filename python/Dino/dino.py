import pygame
import random
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

display_width = 800
display_heihgt = 600

display = pygame.display.set_mode((display_width, display_heihgt))
pygame.display.set_caption('Run Dino! Run!')

pygame.mixer.music.load('Dino/img/background.mp3')
pygame.mixer.music.set_volume(0.3)

jump_sound = pygame.mixer.Sound('Dino/img/Rrr.wav')
fall_sound = pygame.mixer.Sound('Dino/img/Bdish.wav')
loss_sound = pygame.mixer.Sound('Dino/img/loss.wav')


icon = pygame.image.load('Dino/img/icon.png')
pygame.display.set_icon(icon)

cactus_img = [pygame.image.load('Dino/img/Cactus0.png'), pygame.image.load(
    'Dino/img/Cactus1.png'), pygame.image.load('Dino/img/Cactus2.png')]
cactus_options = [69, 449, 37, 410, 40, 420]

stone_img = [pygame.image.load(
    'Dino/img/Stone0.png'), pygame.image.load('Dino/img/Stone1.png')]
cloud_img = [pygame.image.load(
    'Dino/img/Cloud0.png'), pygame.image.load('Dino/img/Cloud1.png')]

dino_img = [pygame.image.load('Dino/img/Dino2_0.png'), pygame.image.load('Dino/img/Dino2_1.png'), pygame.image.load(
    'Dino/img/Dino2_2.png'), pygame.image.load('Dino/img/Dino2_3.png'), pygame.image.load('Dino/img/Dino2_4.png')]

health_img = pygame.image.load('Dino/img/heart.png')
health_img = pygame.transform.scale(health_img, (30,30))

img_counter = 0
health = 2

class Object:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            return True
        else:
            return False

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x, self.y))


usr_width = 60
usr_height = 100
usr_x = display_width // 3
usr_y = display_heihgt - 100 - usr_height
cactus_widht = 20
cactus_height = 70
cactus_x = display_width - 50
cactus_y = display_heihgt - cactus_height - 100
clock = pygame.time.Clock()
make_jump = False
jump_counter = 30

scores = 0
max_scores = 0
max_above = 0


def run_game():
    global make_jump

    pygame.mixer.music.play(-1)
    game = True
    cactus_arr = []
    create_cactus_arr(cactus_arr)
    land = pygame.image.load('Dino/img/LandLevel.jpg')

    stone, cloud = open_random_oblects()

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True
        if keys[pygame.K_ESCAPE]:
            pause()

        if make_jump:
            jump()
        count_scores(cactus_arr)

        


        display.blit(land, (0, 0))
        print_text("Scores: " + str(scores), 600, 10)
        draw_array(cactus_arr)
        move_objects(stone, cloud)
        draw_dino()

        if check_collision(cactus_arr):
            #pygame.mixer.music.stop()
            #pygame.mixer.Sound.play(fall_sound)
            # if not check_health():
            game = False

        show_health()

        pygame.display.update()
        clock.tick(60)
    return game_over()
     

def jump():
    global usr_y, jump_counter, make_jump
    if jump_counter >= -30:
        if jump_counter == 30:
            pygame.mixer.Sound.play(jump_sound)
        if jump_counter == -25:
            pygame.mixer.Sound.play(fall_sound)
        usr_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


def create_cactus_arr(array):
    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 20, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 300, height, width, img, 4))
    
    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 600, height, width, img, 4))


def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)
    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 280
    else:
        radius = maximum
    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(250, 400)
    return radius


def draw_array(array):
    for cactus in array:
        check = cactus.move()
        if not check:
            object_return(array, cactus)
            radius = find_radius(array)

            choice = random.randrange(0, 3)
            img = cactus_img[choice]
            width = cactus_options[choice * 2]
            height = cactus_options[choice * 2 + 1]

            cactus.return_self(radius, height, width, img)

def object_return(objects, obj):
    radius = find_radius(objects)
    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    obj.return_self(radius, height, width, img)


def open_random_oblects():
    choice = random.randrange(0, 2)
    img_of_stone = stone_img[choice]

    choice = random.randrange(0, 2)
    img_of_cloud = cloud_img[choice]

    stone = Object(display_width, display_heihgt - 80, 10, img_of_stone, 4)
    cloud = Object(display_width, 80, 70, img_of_cloud, 2)
    return stone, cloud


def move_objects(stone, cloud):
    check = stone.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_stone = stone_img[choice]
        stone.return_self(display_width, 500 +
                          random.randrange(10, 80), stone.width, img_of_stone)

    check = cloud.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud.return_self(display_width,  random.randrange(
            10, 200), cloud.width, img_of_cloud)


def draw_dino():
    global  img_counter
    if img_counter == 25:
        img_counter = 0

    display.blit(dino_img[img_counter // 5], (usr_x, usr_y))
    img_counter += 1

def print_text(message, x, y, font_color =(220,20,60), font_type = ('Dino/img/PingPong.ttf'), font_size = 30):
    font_type  = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))

def pause():
    paused = True

    pygame.mixer.music.pause()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('Paused. Press enter to cointinue', 160, 300)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
           paused = False
        pygame.display.update()
        clock.tick(15)

    pygame.mixer.music.unpause()

def check_collision(barriers):
    for barrier in barriers:
        if barrier.y == 449: # little cactus
            if not make_jump:
                if barrier.x <= usr_x + usr_width - 35 <= barrier.x + barrier.width:
                    if check_health():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True                                               
            elif jump_counter >=0:
                if usr_y + usr_height - 5 >=  barrier.y:
                    if barrier.x <= usr_x + usr_width - 40 <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True    
            else:
                if usr_y + usr_height - 10 >=  barrier.y:
                    if barrier.x <= usr_x  <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True   
        else:
            if not make_jump:
                if barrier.x <= usr_x + usr_width - 5 <= barrier.x + barrier.width:
                    if check_health():
                        object_return(barriers, barrier)
                        return False
                    else:
                        return True   
            elif jump_counter == 10:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 5 <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True   
            elif jump_counter >= -1:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 35 <= barrier.x + barrier.width:
                        if check_health():
                            object_return(barriers, barrier)
                            return False
                        else:
                            return True   
                else:
                    if usr_y + usr_height - 10 >=  barrier.y:
                        if barrier.x <= usr_x +5  <= barrier.x + barrier.width:
                            if check_health():
                                object_return(barriers, barrier)
                                return False
                            else:
                                return True          
    return False


def count_scores(barriers):
    global scores, max_above
    above_cactus = 0
    if - 20 <= jump_counter < 25:
        for barrier in barriers:
            if usr_y + usr_height - 5 <= barrier.y:
                if barrier.x <= usr_x  <= barrier.x + barrier.width:                
                    above_cactus += 1
                elif barrier.x <= usr_x + usr_width  <= barrier.x + barrier.width:     
                    above_cactus += 1
        max_above = max(max_above, above_cactus)
    else:
        if jump_counter == -30:
            scores += max_above
            max_above = 0
    
def game_over():
    global scores, max_scores
    if scores > max_scores:
        max_scores = scores
    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('GAME OVER. Press enter to play again, Esc to exit', 50, 300)
        print_text('Max scores: ' + str(max_scores), 250, 350)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
           return True
        if keys[pygame.K_ESCAPE]:
            return False

        pygame.display.update()
        clock.tick(15)

def show_health():
    global health
    show = 0
    x = 20
    while show != health:
        display.blit(health_img, (x, 20 ))
        x += 40
        show +=1

def check_health():
    global health
    health -= 1
    if health ==0:
        pygame.mixer.Sound.play(loss_sound)
        return False
    else:
        pygame.mixer.Sound.play(fall_sound)
        return True
        




while run_game():
    scores = 0
    make_jump = False
    jump_counter = 30
    usr_y = display_heihgt - usr_height - 100
    health = 2
pygame.QUIT
quit()