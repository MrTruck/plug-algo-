import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
fps = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Game")
timer = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)
# Game Variables
word_objects = [] # <--- what stores the generated words that appear on screen
mistkaets = 0
score = 0
paused = True
active_string = ""
submit = ""
wspeed = 1  # Speed of words
spawn_interval = 2  # Time in seconds between spawns
last_spawn_time = time.time()

# Load Wordlist
'''
wordlist = []
with open("Algorithm and programing final/assets/lang_french.txt", "r") as file:
    wordlist = [line.strip() for line in file.readlines()]
    '''


class Word:
    """Class to represent a falling word."""
    def __init__(self, text, speed, x, y):
        self.text = text
        self.speed = speed
        self.x_position = x
        self.y_position = y

    def draw(self):
        color = 'red'
        screen.blit(font.render(self.text, True, color), (self.x_position, self.y_position))
        active_len = len(active_string)
        if active_string == self.text[:active_len]: #if the active string is the same as the wtext on screen, the text turns green
            screen.blit(font.render(active_string, True, 'green'), (self.x_position, self.y_position))

    def update(self):
        self.x_position -= self.speed

class button:
    def __init__(self, x_position, y_position, text, clicked, surf):
        self.x_position = x_position
        self.y_position = y_position
        self.text = text
        self.clicked = clicked
        self.surf = surf

    def draw(self):
        cir = pygame.draw.circle(self.surf,(45, 89, 135), (self.x_position, self.y_position), 35) #arguments : (surface to draw, color, center position(x,y), radius)
        if cir.collidepoint(pygame.mouse.get_pos()):
            btn = pygame.mouse.get_pressed()
            if btn[0]: #in pygame button 0 is left click
                pygame.draw.circle(self.surf, (190, 35, 35), (self.x_position, self.y_position), 35) #interface for feedback upon clicking
                self.clicked = True
            else:
                pygame.draw.circle(self.surf, (190, 89, 135), (self.x_position, self.y_position), 35) #highlighted but not clicked

        pygame.draw.circle(self.surf,'white', (self.x_position, self.y_position), 35, 3)

        self.surf.blit(font.render(self.text, True, 'white'), (self.x_position - 15, self.y_position - 25))


class LANG_button:
    def __init__(self, x_position, y_position, text, clicked, surf):
        self.x_position = x_position
        self.y_position = y_position
        self.text = text
        self.clicked = clicked
        self.surf = surf

    def draw(self):
        cir = pygame.draw.circle(self.surf,(45, 89, 135), (self.x_position, self.y_position), 35) #arguments : (surface to draw, color, center position(x,y), radius)
        if cir.collidepoint(pygame.mouse.get_pos()):
            btn = pygame.mouse.get_pressed()
            if btn[0]: #in pygame button 0 is left click
                pygame.draw.circle(self.surf, (190, 35, 35), (self.x_position, self.y_position), 35) #interface for feedback upon clicking
                self.clicked = True
            else:
                pygame.draw.circle(self.surf, (190, 89, 135), (self.x_position, self.y_position), 35) #highlighted but not clicked

        pygame.draw.circle(self.surf,'white', (self.x_position, self.y_position), 35, 3)

        self.surf.blit(font.render(self.text, True, 'white'), (self.x_position + 50, self.y_position - 25))



def draw_screen():
    """Draw the score, lives, and active string."""
    score_text = font.render(f"Score: {score}", True, BLACK)
    lives_text = font.render(f"Miss: {mistkaets}/10", True, BLACK)
    active_text = font.render(active_string, True, RED)

    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 150, 10))
    screen.blit(active_text, (WIDTH // 2 - 100, HEIGHT - 50))


def generate_word():
    """Spawns a new word at a random position."""
    global wspeed


    y_pos = random.randint(10, HEIGHT - 100)

    x_pos = random.randint(WIDTH, WIDTH + 300)
    text = random.choice(wordlist).lower()

    new_word = Word(text, wspeed, x_pos, y_pos)
    word_objects.append(new_word)


def check_answer():
    """Checks if the active string matches any word."""
    global word_objects
    for w in word_objects:
        if w.text == submit:
            word_objects.remove(w)
            return score + 10
    return score


languages = ['english', 'finnish', 'french']  # Available languages
current_language = 'english' 

def load_wordlist(language):
    # Load word list based on the selected language
    filepath = f'Algorithm and programing final/assets/lang_{language}.txt'
    with open(filepath, 'r') as file:
        da_words = file.read().splitlines()
    da_words.sort(key=len)  # Ensure words are sorted by length

    return da_words

def draw_pause():
    """Draw the pause menu."""
    pause_text = font.render("Paused. Press ESC to resume.", True, BLACK)
    screen.blit(pause_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))

    global current_language

    surface = pygame.Surface((WIDTH, HEIGHT),pygame.SRCALPHA)
    pygame.draw.rect(surface, (0, 0, 0, 100), [300,300,600,300], 0, 5) # parameters: (screen, [red, blue, green], [left, top, width, height], filled)
    pygame.draw.rect(surface, (0, 0, 0, 200), [300,300,600,300], 5, 5) #border
    # define buttons for pause menu
    resume_button = button(360, 400, '>', False, surface)
    resume_button.draw()
    quit_button = button(610, 400, 'X', False, surface)
    quit_button.draw()
    #define text for pause menu
    surface.blit(font.render('MENU', True, 'white'), (310,310))
    surface.blit(font.render('PLAY', True, 'white'), (410,375))
    surface.blit(font.render('QUIT', True, 'white'), (650,375))


    # Language selection buttons
    for i, lang in enumerate(languages):
        lang_button = LANG_button(150 , 300 + i * 150, lang.upper(), False, surface)
        lang_button.draw()
        if lang_button.clicked:
            current_language = lang  # Update the language
        if current_language == lang:
            pygame.draw.circle(surface, 'green', (150, 300 + i * 150), 35, 5)
    screen.blit(surface,(0,0))
    return resume_button.clicked,  quit_button.clicked

def check_high_score():
    """Checks and saves high scores."""
    # Placeholder for high score logic
    pass



# Game Loop
run = True
while run:
    screen.fill("grey")
    timer.tick(fps)

    if paused == True:
        
        resume_button, quit_button = draw_pause() #if paused is true such as the case when starting the game, draw the pause menu
        
        if resume_button: #if resume button is clicked, unpause
            paused = False
            wordlist = load_wordlist(current_language)
        if quit_button: # added an ingame quit button just to make it prettier, does the same thing as pygame.QUIT
            check_high_score() #add high score checking before exit
            run = False 
    else:
        draw_screen()

        # Spawn new words periodically
        if time.time() - last_spawn_time > spawn_interval:
            generate_word()
            last_spawn_time = time.time()

        # Update and draw words
        for w in word_objects[:]:
            w.draw()
            w.update()

            # Remove words that go off-screen
            if w.x_position < -200:
                word_objects.remove(w)
                mistkaets += 1

        # Gradually increase word speed
        wspeed += 0.0001

    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check_high_score()
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
            if not paused:
                if event.unicode.isalpha():
                    active_string += event.unicode.lower()
                if event.key == pygame.K_BACKSPACE and len(active_string) > 0:
                    active_string = active_string[:-1]
                if event.key == pygame.K_RETURN:
                    submit = active_string
                    active_string = ''

    # Handle submission
    if submit != '':
        score = check_answer()
        submit = ""

    # Restart game if lives run out
    if mistkaets >= 10:
        paused = True
        mistkaets = 0
        word_objects.clear()
        wspeed = 2
        check_high_score()
        score = 0

    pygame.display.flip()

pygame.quit()
