import pygame, random, copy, nltk

pygame.init()

from nltk.corpus import words 
nltk.download('words')

wordlist = words.words() #it turns out words is just an assorted list of words that nltk provided so this method is just to get the words to refer to later in generate_level()
len_indexes = [] #len_indexes = [54, 230, 1740, 7253, 17675, 35508,...,] , this is just a reminder for me what index to refer to for what letter length "letter length of 2 starts at index 54"
length = 1




'''with open('Algorithm and programing final/assets/muaha the french.txt', 'r') as f:
    french_words = [line.strip() for line in f]

french_words.sort(key=len)'''




#wordlist sorting method

wordlist.sort(key=len)#tells Python to sort the list based on the length of each word.

for i in range(len(wordlist)): #to generate the index of len_indexes, i made a for loop where if the lenth of a word in wordlist is bigger than 'length', then it does the following:
    if len(wordlist[i]) > length: #it starts with the lenth of 2
        length +=1
        len_indexes.append(i)

len_indexes.append(len(wordlist))
#print(len_indexes)



#game initialization
WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Typer")
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
timer = pygame.time.Clock()
fps = 60

#game variables
level = 1
active_string = ''
score = 0
high_score = 1
lives = 0
new_level = True
paused = True #make the pause menu the start menu 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
submit = ''
word_objects = []
#new_level = True

# 2 letter to 8 letter choices as boolean
choices = [False, True,False, False, False, False, False] #it's suppose to be the choice for letter length, refer to generate_level() for how it works


# load assets like fonts, sound fx and music
header_font = pygame.font.Font('Algorithm and programing final/assets/Fonts/1up.ttf',35)
pause_font = pygame.font.Font('Algorithm and programing final/assets/Fonts/1up.ttf',38)
banner_font = pygame.font.Font('Algorithm and programing final/assets/Fonts/1up.ttf',28)
wrd_font = pygame.font.Font('Algorithm and programing final/assets/Fonts/1up.ttf',48)

#high score read in from txt
file = open('Algorithm and programing final/HighScore.txt', 'r')
read = file.readlines()
high_score = int(read[0])
file.close()


class Word:
    def __init__(self, text, speed, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.text = text
        self.speed = speed
    def draw(self):
        color = 'red'
        screen.blit(wrd_font.render(self.text, True, color), (self.x_position, self.y_position))
        active_len = len(active_string)
        if active_string == self.text[:active_len]:
            screen.blit(wrd_font.render(active_string, True, 'green'), (self.x_position, self.y_position))

    def update(self):
        self.x_position -= self.speed #the position of the word goes from right to left by decreasing it with the speed which is random

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

        self.surf.blit(pause_font.render(self.text, True, 'white'), (self.x_position - 15, self.y_position - 25))


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

        self.surf.blit(pause_font.render(self.text, True, 'white'), (self.x_position + 50, self.y_position - 25))



languages = ['english', 'finnish', 'french']  # Available languages
current_language = 'english' 

def load_wordlist(language):
    # Load word list based on the selected language
    filepath = f'Algorithm and programing final/assets/lang_{language}.txt'
    with open(filepath, 'r') as file:
        da_words = file.read().splitlines()
    da_words.sort(key=len)  # Ensure words are sorted by length
    len_indexes = []
    length = 1
    for i in range(len(da_words)):
        if len(da_words[i]) > length:
            length += 1
            len_indexes.append(i)
    len_indexes.append(len(da_words))
    return da_words, len_indexes



def draw_screen():
    # draw background, boxes for text, score, etc.
    pygame.draw.rect(screen, (32,42,68), [0, HEIGHT - 100, WIDTH, 100])
    pygame.draw.rect(screen,'white', [0,0, WIDTH, HEIGHT], 5)
    pygame.draw.line(screen,'white',(250, HEIGHT - 100), (250, HEIGHT), 2)
    pygame.draw.line(screen,'white',(700, HEIGHT - 100), (700, HEIGHT), 2)
    pygame.draw.line(screen,'white',(0, HEIGHT - 100), (WIDTH, HEIGHT - 100), 2)

    # text for showing the current level, player's current input, high score, score, lives, and pause

    screen.blit(header_font.render(f'Level: {level}', True, 'white'), (10, HEIGHT - 75))
    screen.blit(header_font.render(f'{active_string}', True, 'white'), (270, HEIGHT - 75))

    #pause button
    pause_button = button(748, HEIGHT - 52, 'II', False, screen)
    pause_button.draw()

    screen.blit(banner_font.render(f'Score:{score}', True, 'white'), (250, 10))
    screen.blit(banner_font.render(f'Best:{high_score}', True, 'white'), (550, 10))
    screen.blit(banner_font.render(f'Lives:{lives}', True, 'white'), (10, 10))

    return pause_button.clicked 

def draw_pause():
    global current_language
    choice_commits = copy.deepcopy(choices) #deepcopy to avoid changing the original list
    surface = pygame.Surface((WIDTH, HEIGHT),pygame.SRCALPHA)
    pygame.draw.rect(surface, (0, 0, 0, 100), [300,300,600,300], 0, 5) # parameters: (screen, [red, blue, green], [left, top, width, height], filled)
    pygame.draw.rect(surface, (0, 0, 0, 200), [300,300,600,300], 5, 5) #border
    # define buttons for pause menu
    resume_button = button(360, 400, '>', False, surface)
    resume_button.draw()
    quit_button = button(610, 400, 'X', False, surface)
    quit_button.draw()
    #define text for pause menu
    surface.blit(header_font.render('MENU', True, 'white'), (310,310))
    surface.blit(header_font.render('PLAY', True, 'white'), (410,375))
    surface.blit(header_font.render('QUIT', True, 'white'), (650,375))
    surface.blit(header_font.render('Letter length:', True, 'white'), (310,450))


    # Language selection buttons
    for i, lang in enumerate(languages):
        lang_button = LANG_button(150 , 300 + i * 150, lang.upper(), False, surface)
        lang_button.draw()
        if lang_button.clicked:
            current_language = lang  # Update the language
        if current_language == lang:
            pygame.draw.circle(surface, 'green', (150, 300 + i * 150), 35, 5)

    # define buttons for letter length selection
    for i in range(len(choices)):
        butn = button(360 + (i * 80), 550, str(i + 2), False, surface) #arguments : (x position, y position, string starts at 2, status false or unoressed, where the button is drawn which is pause menu in this case)
        butn.draw()
        if butn.clicked:
            if choice_commits[i]:
                choice_commits[i] = False

            else:
                choice_commits[i] = True
        if choices[i]:
            pygame.draw.circle(surface, 'green', (360 + (i * 80), 550), 35, 5)
    
    screen.blit(surface,(0,0)) #remember to draw the pause menu to the screen
    return resume_button.clicked, choice_commits, quit_button.clicked #allows reaction depending on the status of the button and commits

def check_answer(scr):
    for wrd in word_objects:
        if wrd.text == submit: #if generated string is the same as submit, the following occurs,
            points = wrd.speed * len(wrd.text) * 10 * (len(wrd.text) / 3) #scoring method
            scr += int(points)
            word_objects.remove(wrd)
            #play successful entry sound 
    return scr

def generate_level():
    word_obj = []
    include = []
    vertical_spacing = (HEIGHT - 150) // level  

    '''
    if True not in choices:
        random_choice = random.randint(0, len(len_indexes) - 2)
        choices = [i == random_choice for i in range(len(len_indexes) - 1)] #there is a bug where the game keeps starting at level 2 idk why but this solution did not work
    '''

    if True not in choices: #if there are no choices then it is ensured choices at index 0 becomes true which is length of 2
        choices[0] = True
    
    for i in range(len(choices)): #iterates over choices list
        if choices [i] == True: #for choices that are true, do the following
            include.append((len_indexes[i], len_indexes[i+1])) #append 'include' list with tuples of len_indexes of index i and i+1 (on the start of the level it would be (54,120) to add to 'include' for example)

    for i in range(level): #so it generates for depending on the level, it iterates according to the level
        speed = random.randint(2 + level//3 , 3 + level//3 )#speed is random either 2 or 3 but increases as the level increases though i added //3 bcause it got too fast (thanks to sir jude for the idea)
        y_pos = random.randint(10 + (i * vertical_spacing), (i + 1) * vertical_spacing) 
        x_pos = random.randint(WIDTH, WIDTH + 500) #so it generates from outside of the rightside of the box
        
        index_sel = random.choice(include) #the choice of the tuples which is picked from 'include' is random 
        index = random.randint(index_sel[0], index_sel[1])#for picking from wordlist using index with the range of the tuples from index_sel
        text = wordlist[index].lower()#this is why wordlist needed to be sorted

        new_word = Word(text, speed,x_pos ,y_pos) #draw the words using Word class
        word_obj.append(new_word) #adds Word to the word_obj list

    #print(f"Level: {level}, Words Generated: {len(word_obj)}") 

    return word_obj

def check_high_score():
    global high_score
    if score > high_score:
        high_score = score
        file = open('HighScore.txt', 'w') #this method is not recommended but it works for now
        file.write(str(int(high_score)))
        file.close()


#------------------------------MAIN GAME LOOP---------MAIN GAME LOOP---------------------------------------------------------------------------------------------------------


run = True
while run:
    screen.fill('black')
    timer.tick(fps)
    #draw background screen stuff and statuses and get pause button status
    pause_button = draw_screen()
    
    
    if paused:
        
        resume_button, changes, quit_button = draw_pause() #if paused is true such as the case when starting the game, draw the pause menu
        
        if resume_button: #if resume button is clicked, unpause
            paused = False
            wordlist, len_indexes = load_wordlist(current_language)
        if quit_button: # added an ingame quit button just to make it prettier, does the same thing as pygame.QUIT
            check_high_score() #add high score checking before exit
            run = False 
    #update: it turnsout the bug was cause by using elif instead of if in the code below
    if new_level and not paused: #if new_level is true and its not paused generate the words
        word_objects = generate_level()
        new_level = False

    else:
        for w in word_objects: 
            w.draw()
            if not paused:
                w.update()
            if w.x_position < -200: #if  the word exits the left side of the screen decrease the life
                word_objects.remove(w)
                lives += 1
    
    if len(word_objects) <= 0 and not paused: #if there are no words left on the screen, generate a new level
        level += 1  
        new_level = True

    if submit != '': #as soon as submit contains a string, 
        init = score
        score = check_answer(score)
        submit = ''
        if init == score:
            #play entry sound later
            pass

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:# standard method to quit the loop
            check_high_score() #add high score checking and add to text file before exit            
            run = False #after check highscore, quit the game

        if event.type == pygame.KEYDOWN:
            if not paused:
                if event.unicode.lower() in letters: #so that the input could only be in letters (see game variables up above)
                    active_string += event.unicode.lower()
                if event.key == pygame.K_BACKSPACE and len(active_string) > 0:
                    active_string = active_string[:-1] #just to delete the words when backspacing
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE: #RETURN key = enter key
                    submit = active_string #assign submit with active string
                    active_string = '' # resets the active string after pressing enter
            
            if event.key == pygame.K_ESCAPE: #can also use escape to pause
                if paused:
                    paused = False
                else:
                    paused = True
        if event.type == pygame.MOUSEBUTTONUP and paused:
            if event.button == 1:
                choices = changes

    if pause_button: #if pause button is pressed, pause 
        paused = True


    if lives >= 10: #restarting
        paused = True
        level = 1
        lives = 0
        word_objects = []
        new_level = True
        check_high_score()
        score = 0

    pygame.display.update()  

pygame.quit()          