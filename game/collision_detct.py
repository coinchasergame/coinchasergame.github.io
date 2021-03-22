import pygame,random

#Erkennt ob man eine Wand mit dem Spieler berührt
def wall_collision(walls,player):
    c=0
    player_rect = pygame.Rect(player[0],player[1],44,44) #Spieler
    for wall in range(11):
        wall=pygame.Rect(walls[c])
        c+=1
        if wall.colliderect(player_rect):
            return 'game_over.True' #titlescreen.True


# zeigt die Position vom Spieler an
def run(screen,player,player_skin) :
    red = pygame.Color('red') #Farbe
    blue = pygame.Color('blue')
    green = pygame.Color('green')
    colors = [red,blue,green]
    listposition = random.randint(0,2) #wählt eine Position für die Liste Colors aus
    pygame.Rect(player[0],player[1],44,44) #Spieler
    field = pygame.Rect(player[0],player[1],44,44) # das Feld, wo sich der Spieler gerade befindet 
    pygame.draw.rect(screen,colors[listposition],field) #Zeichnet ein Rechteck auf der Position auf dem sich der Spieler befindet
    screen.blit(player_skin,field)


# schaut ob ein Spieler eine Münze berührt hat
def check_counter(screen,remo_list,coinskin,coins_rect): 
    for remove in remo_list:
        if remove.colliderect(coins_rect[0]) or remove.colliderect(coins_rect[1]) or remove.colliderect(coins_rect[2]) or remove.colliderect(coins_rect[3]) or remove.colliderect(coins_rect[4]) or remove.colliderect(coins_rect[5]) or remove.colliderect(coins_rect[6]) or remove.colliderect(coins_rect[7]) or remove.colliderect(coins_rect[8]) or remove.colliderect(coins_rect[9]):
            screen.blit(coinskin,(remove[0],remove[1])) #Es erscheint eine Münze auf dem Screen


# zählt die Punkte die man von den Münzen bekommen kann zusammen
def point_counter(points,remo_list,coins_rect): 
    for remove in remo_list:
        if remove.colliderect(coins_rect[0]) or remove.colliderect(coins_rect[1]) or remove.colliderect(coins_rect[2]) or remove.colliderect(coins_rect[3]) or remove.colliderect(coins_rect[4]) or remove.colliderect(coins_rect[5]) or remove.colliderect(coins_rect[6]) or remove.colliderect(coins_rect[7]) or remove.colliderect(coins_rect[8]) or remove.colliderect(coins_rect[9]):
            points += 100
    return points


# erstellt liste für alle felder (weisse quadrate)
def move(screen,player_coords,statement):
    black = pygame.Color('black')
    pygame.Rect(player_coords[0],player_coords[1],44,44)
    x = 0
    y = 0
    if statement == False: #Dieser Block erstellt eine Liste mit den Koordinaten von jedem Block
        list_coords = []
        while x != 34 and y != 21:
            buttons = pygame.Rect(0+((50-1)*x+7),0+((50-1)*y+7),44,44)
            places = pygame.draw.rect(screen,black,buttons)
            list_coords.append(places)
            x += 1
            if x == 34:
                y+=1
                x=0
        return list_coords
    if statement == True:   #Dieser Block zeichnet die Felder
        while x != 34 and y != 21:
            buttons = pygame.Rect(0+((50-1)*x+7),0+((50-1)*y+7),44,44)
            places = pygame.draw.rect(screen,black,buttons)
            x += 1
            if x == 34:
                y+=1
                x=0


# collisiondetect für begangene felder und speichert sie
def collideplayer(player,list_coords,remo_list,statement):
    player_rect = pygame.Rect(player[0],player[1],44,44)
    pygame.Rect(player[0],player[1],44,44)
    if statement == True: # Dieser Block schaut ob der Spieler das Feld schon besucht hat
        for blocks in list_coords:
            if player_rect.colliderect(blocks):
                x = blocks
        if x in list_coords:
            if x in remo_list:
                print('lost')
                remo_list=str(remo_list)+'.True'
        return remo_list
    elif statement == False: # Dieser Block fügt die Koordinaten vom Spieler in die Remove Liste
        for blocks in list_coords:
            if player_rect.colliderect(blocks):
                x = blocks
        if x in list_coords:
            remo_list.append(x)
            return remo_list
    if statement == 5: # Dieser Block blendet den Game Over Screen ein bei Collision Detection
        s = None
        for blocks in list_coords:
            if player_rect.colliderect(blocks):
                x = blocks
        if x in list_coords:
            if x in remo_list:
                print('lost')
                s = 'game_over.True'#remo_list=str(remo_list)+'.True'
        return s

# zeichnet wände
def drawing(screen,walls, index_wall,random_number,color,exception):
    real_color_wall = color
    print(color)
        #random color
    red = pygame.Color('red')
    blue = pygame.Color('blue')
    green = pygame.Color('green')
    colors = [red,blue,green]
    x = random.randint(0,2)
    colors = [red,blue,green]
    settings_change_wall = ['RAINBOW','RANDOM','RED','BLUE','GREEN','CUSTOM']
    if settings_change_wall[index_wall] == 'RAINBOW' or exception == True:
        real_color_wall = colors[x]
    #Wechsel zwischen Farben
    settings_change_wall = ['RAINBOW','RANDOM','RED','BLUE','GREEN','CUSTOM']

  
    c=0
    for e in range(11):
        pygame.draw.rect(screen,real_color_wall,walls[c])
        c+=1


# playerpath: zeigt alle begangen Felder an
def playerpath(remo_list,screen,player,color_one,index_path,exceeption):
    real_color_path = color_one
    red = pygame.Color('red')
    blue = pygame.Color('blue')
    green = pygame.Color('green')
    x = random.randint(0,2)
    colors = [red,blue,green]
    settings_change_path = ['RAINBOW','RANDOM','RED','BLUE','GREEN','CUSTOM']
    if settings_change_path[index_path] == 'RAINBOW' or exceeption == True:
        real_color_path = colors[x]
        
    pygame.Rect(player[0],player[1],44,44)
    for element in remo_list:
        pygame.draw.rect(screen,real_color_path,element)
