import pygame,collision_detct,gamefunctions,json,datetime
from pygame.locals import *
from pygame import mixer

felder = []
counter_felder=0
player_coords,player_coords_c=[],[]
moves = []
black = pygame.Color('black')


def titlescreen(data, data_1):
    send_data=False
    global field_blit,sounds
    screen = data['screen']
    background_titlescreen = data_1['background_titlescreen']
    background_xy = data['background_xy']
    play_button=data_1['play_button']
    skin_button=data_1['skin_button']
    quit_button=data_1['quit_button']
    howto_button=data_1['howto_button']
    leaderboard_button=data_1['leaderboard_button']
    buttons_titlescreen_xy = data_1['buttons_titlescreen_xy']
    play_button_rect=data_1['play_button_rect']
    skin_button_rect=data_1['skin_button_rect']
    quit_button_rect=data_1['quit_button_rect']
    button_highscore=data_1['button_highscore']
    leaderboard_button_rect=data_1['leaderboard_button_rect']
    howto_button_rect=data_1['howto_button_rect']
    screenmode=data['screenmode']
    main_path=data['main_path']
    upperplayername = playername.upper()
    base_font = pygame.font.SysFont(None, 110)
    text_surface = base_font.render(upperplayername,False,(255,255,255))
    screen.blit(background_titlescreen, (background_xy[0],background_xy[1])) 
    screen.blit(play_button, (buttons_titlescreen_xy[0],buttons_titlescreen_xy[1]))
    screen.blit(skin_button, (buttons_titlescreen_xy[0],buttons_titlescreen_xy[1]))
    screen.blit(quit_button, (buttons_titlescreen_xy[0],buttons_titlescreen_xy[1]))
    screen.blit(howto_button, (buttons_titlescreen_xy[0],buttons_titlescreen_xy[1]))
    screen.blit(leaderboard_button, (buttons_titlescreen_xy[0],buttons_titlescreen_xy[1]))
    screen.blit(text_surface,(50,20))
    grey = pygame.Color('black')

    if field_blit == True:
        if sounds == 'on':
            sounds = 'off'
        elif sounds == 'off':
            sounds = 'on'
            mixer.music.play(-1)
        print(sounds)
        pygame.draw.rect(screen,grey,(1500,900,110,50))
        field_blit = False
        print(sounds)

    second_font = pygame.font.SysFont(None, 90)
    sound_surface = second_font.render(f'SOUNDS: {sounds.upper()}',False,(255,255,255))
    screen.blit(sound_surface,(1200,900))

    if sounds == 'off':
        mixer.music.pause()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print('Quit game ...')
            pygame.quit() 
            exit(0) 

        # detect mousepos on categories
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            if x > play_button_rect[0] and y > play_button_rect[1] and x < play_button_rect[2] and y < play_button_rect[3]:
                screenmode='timer' #screenmode='gamescreen' # to skip seq 
                send_data=True           
            elif x > skin_button_rect[0] and y > skin_button_rect[1] and x < skin_button_rect[2] and y < skin_button_rect[3]:
                screenmode='skinscreen'
                send_data=True           
            elif x > quit_button_rect[0] and y > quit_button_rect[1] and x < quit_button_rect[2] and y < quit_button_rect[3]:
                screenmode='quitscreen'
                send_data=True 
            elif x > howto_button_rect[0] and y > howto_button_rect[1] and x < howto_button_rect[2] and y < howto_button_rect[3]:
                screenmode='howto'
                send_data=True 
            elif x > leaderboard_button_rect[0] and y > leaderboard_button_rect[1] and x < leaderboard_button_rect[2] and y < leaderboard_button_rect[3]:
                screenmode='highscore'
                send_data=True
            if x > 1500 and y > 900 and x < 1590 and y < 950:
                    print('clicked')
                    field_blit = True 

    if send_data==True:
        return screenmode


def skinscreen(data, data_3,data_2):
    global player
    send_data=False
    screen = data['screen']
    background_xy = data['background_xy']
    background_skinscreen=data_3['background_skinscreen']
    screenmode=data['screenmode']
    skins_skinscreen=data_3['skins_skinscreen']
    skins = data['skins']
    screen.blit(background_skinscreen, (background_xy[0],background_xy[1]))
    c=0
    
    for skin in skins_skinscreen:
        l=[112,485,870,1230]
        screen.blit(skins_skinscreen[c], (l[c],375))
        c+=1

    for event in pygame.event.get():
        if event.type==pygame.QUIT: # stoppt Script
            print('Quit game ...')
            pygame.quit() 
            exit(0) 

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:            
                print('escape')
                player = data_2['player']
                screenmode='titlescreen'
                send_data=True

        # load skins
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            if x > 112 and y > 375 and x < 392 and y < 655:
                print('Skin 1 picked')
                player = skins[0]
                screenmode='titlescreen'
                send_data=True
            if x > 485 and y > 375 and x < 765 and y < 655:
                print('Skin 2 picked')
                player = skins[1]
                screenmode='titlescreen'
                send_data=True           
            if x > 870 and y > 375 and x < 1150 and y < 655:
                print('Skin 3 picked')
                player = skins[2]
                screenmode='titlescreen'
                send_data=True
            if x > 1230 and y > 375 and x < 1510 and y < 655:
                print('Skin 4 picked')
                player = skins[3]
                screenmode='titlescreen'
                send_data=True 

    if send_data==True:
        return screenmode


def gamescreen(data, data_2,remo_list):
<<<<<<< HEAD
    #t1 = gamefunctions.start_timer() # to start timer
=======
    t1 = gamefunctions.start_timer() # to start timer
>>>>>>> master
    global counter_felder,block_coords,player_coords,player,points,sounds,t3
    send_data=False
    points = 0
    screenmode=data['screenmode']
    keys = data['keys']
    path = data['path']
    screen = data['screen']
    start1=data_2['start']
    start_xy=data_2['start_xy']
    end_xy=data_2['end_xy']
    player_xy=data_2['player_xy']
    display_xy=data_2['display_xy']
    end2=data_2['end2']
    block_coords = data_2['block_coords']
    walls_rect=data_2['walls_rect'] #[wallnr][wallcoord(x,y,-x-y)]
    newgame=data['newgame']
    coin2=data_2['coin2']
    coins_rect = data_2['coins_rect']
    game_over = data['game_over']
    player_rect = pygame.Rect(player_xy[0],player_xy[1],44,44)
    repo = data['repo']
    remote = data['remote']
    prepo = data['prepo']

    # Sounds
    movesound = pygame.mixer.Sound(path + "audio/Sounds/move.wav")
    movesound.set_volume(0.25)
    lose_sound = pygame.mixer.Sound(path + "audio/Sounds/lose.wav")
    lose_sound.set_volume(0.5)
    win_sound = pygame.mixer.Sound(path + "audio/Sounds/win.wav")

    # play audio
    if sounds == 'off':
            mixer.music.pause()

    # Sprites hinzufügen
    counter = 0
    if counter == 0:
        list_coords = collision_detct.move(screen,player_xy,False)
        counter += 1
    if counter != 0:
        collision_detct.move(screen,player_xy,True)

    collision_detct.drawing(screen,walls_rect)
    coinskin = gamefunctions.random_coinskin(path1 = path,coin1 = coin2)
    endskin = gamefunctions.random_endskin(path1 = path, end1 = end2)

    screen.blit(endskin, (end_xy[0],end_xy[1]))
    screen.blit(start1, (start_xy[0],start_xy[1])) 
    gamefunctions.background(screen, path)
    collision_detct.playerpath(remo_list,screen,player_xy)

    # if no player selected
    try:
        screen.blit(player, (player_xy[-2],player_xy[-1])) 
    except NameError:
        player = pygame.image.load(path+"images/gamescreen/player.png")

    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            print('Quit game ...')
            pygame.quit() 
            exit(0) 

        # detect for keyboard inputs
        elif event.type == pygame.KEYDOWN:
            if event.key==K_w or event.key==K_UP:
                keys[0]=True
            elif event.key==K_a or event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_s or event.key==K_DOWN:
                keys[2]=True 
            elif event.key==K_d or event.key==K_RIGHT:
                keys[3]=True
            elif event.key==K_q:
                    keys[5] = True

        elif event.type == pygame.KEYUP:
            if event.key==pygame.K_w or event.key==K_UP:
                keys[0]=False
            elif event.key==pygame.K_a or event.key==K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_s or event.key==K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_d  or event.key==K_RIGHT:
                keys[3]=False
            elif event.key==pygame.K_q:
                keys[5] = False

            elif event.key == K_ESCAPE:
                screenmode=='titlescreen'
                send_data = True

    if keys[0] or keys[1] or keys[2] or keys[3]:
        counter_felder=1
        for e in remo_list:
            counter_felder+=1
        counter_felder += 1
        if sounds == 'on':
            movesound.play()
        collision_detct.run(screen,player_xy,player)
        collision_detct.check_counter(screen,remo_list,coinskin,coins_rect)
        remo_list = collision_detct.collideplayer(player_xy,list_coords,remo_list,False)

    if keys[5]:
        gamefunctions.show_points(points,remo_list,screen,coins_rect,t3)
    if keys[4]:
        collision_detct.check_counter(screen,remo_list,coinskin,coins_rect)  

        # move player
        if keys[0]:
            player_xy[1]-=49
            if player_xy[1] < 5:
                player_xy[1] += 49
                remo_list.pop(-1)
        elif keys[2]:
            player_xy[1]+=49
            if player_xy[1] > 987:
                player_xy[1] -= 49
                remo_list.pop(-1)
        elif keys[1]:
            player_xy[0]-=49
            if player_xy[0] < 5:
                player_xy[0] += 49
                remo_list.pop(-1)
        elif keys[3]:
            player_xy[0]+=49
            if player_xy[0] > 1624:
                player_xy[0] -= 49
                remo_list.pop(-1)

        points += 1
        collide=collision_detct.wall_collision(walls_rect,player_xy)
        screenmode = collision_detct.collideplayer(player_xy,list_coords,remo_list,5)
        if screenmode == 'game_over.True':
            if sounds == 'on':
                lose_sound.play()
            return screenmode
        remo_list = collision_detct.collideplayer(player_xy,list_coords,remo_list,True)
        points = gamefunctions.calculate_points(points,remo_list,coins_rect)

        if collide=='game_over.True':
            newgame=True
            screenmode = 'game_over.True'

    if player_xy == end_xy:
        global playername
        played_time = gamefunctions.return_endtime(t3)
        print(f'You ended this round as {playername} with {points} points in {played_time} minutes')
        if points >=150:
            gamefunctions.scores(points,playername,played_time,path)
            gamefunctions.push_repo(remote,prepo,playername)
        send_data=True
    
    if screenmode=='titlescreen' or newgame==True or screenmode == 'game_over.True':
        send_data=True
    if send_data==True:
        if player_xy == end_xy:
            screenmode='win.True'
            if sounds == 'on':
                win_sound.play()
        elif screenmode == 'game_over.True':
            screenmode='game_over.True'
            if sounds == 'on':
                lose_sound.play()
        else:
            screenmode='titlescreen.True'
        return screenmode
    #gamefunctions.end_timer(t1,' to load frame') # print how long it takes to load a frame


def loginscreen(data,number):
    global playername,sounds,field_blit
    field_blit = False
    sounds = 'on'
    playername = ""
    send_data=False
    screen = data['screen']
    base_font = pygame.font.SysFont(None, 160)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(725, 400,50, 130)
    color_inactive = pygame.Color('white')
    color_active = pygame.Color('grey')
    red = pygame.Color('red')
    blue = pygame.Color('blue')
    green = pygame.Color('darkgreen')
    colors = [red,blue,green]
    color = color_inactive
    active = False
    play_button=data['start1']
    rand_unten=data['rand_unten']
    rand_oben=data['rand_oben']
    rand_links=data['rand_links']
    rand_rechts=data['rand_rechts']
    corners=data['corners']
    logo = data['logo']
    screenmode=data['screenmode']
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print('Quit game ...')
                pygame.quit() 
                exit(0) 

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

                if x > 600 and y > 600 and x < 1005 and y < 735 and len(playername) > 0:
                    screenmode = 'titlescreen'
                    send_data = True
                if x > 1500 and y > 900 and x < 1590 and y < 950:
                    print('clicked')
                    field_blit = True
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                            print(playername)
                            if len(playername) > 0:
                                screenmode = 'titlescreen'
                                send_data = True
                    elif event.key == pygame.K_BACKSPACE:
                            playername = playername[:-1]
                    else:
                        if len(playername) < 7:
                            playername = playername + event.unicode

        screen.fill(colors[number])
        text_surface = base_font.render(f'Name: {playername}',True,(255,255,255))
        width = max(475, text_surface.get_width()-400)
        input_box.w = width

        pygame.draw.rect(screen, color, input_box, 2)
        blit_list=[text_surface,play_button,rand_links,rand_rechts,rand_unten,rand_oben,corners,corners,corners,corners,logo]
        list2=[(input_box.x-350, input_box.y+5),(600,600),(0,0),(1613,0),(0,985),(0,0),(1602,0),(0,0),(0,970),(1602,970),(435,150)]
        c=0

        for img in blit_list:
            screen.blit(img,list2[c])
            c+=1
        if field_blit == True:
            if sounds == 'on':
                sounds = 'off'
            elif sounds == 'off':
                sounds = 'on'
                mixer.music.play(-1)
            print(sounds)
            pygame.draw.rect(screen,colors[number],(1500,900,110,50))
            field_blit = False
            print(sounds)
        second_font = pygame.font.SysFont(None, 90)
        sound_surface = second_font.render(f'SOUNDS: {sounds.upper()}',False,(255,255,255))
        screen.blit(sound_surface,(1200,900))
        if sounds == 'off':
            mixer.music.pause()

        pygame.display.flip()
        clock.tick(30)
        if send_data==True:
            return screenmode


def highscorescreen(data):
    base_font = pygame.font.SysFont(None, 80)
    screen = data['screen']
    banner = data['banner']
    return_banner = data['return_banner']
    black = pygame.Color('black')
    screen.fill(black)
    screen.blit(banner,(410,15))
    screen.blit(return_banner,(1225,900))
    path = data['path']

    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print('Quit game ...')
                pygame.quit() 
                exit(0) 
            if event.type == pygame.KEYDOWN:
                    screenmode = 'titlescreen'
                    send_data = True
                    return screenmode
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if x > 1225 and y > 900 and x < 1630 and y < 1035:
                    screenmode='titlescreen'
                    send_data=True
                    return screenmode

    # blit categories
    titles,pos = ['Time','Name','Points'],[300,700,1100]
    for i,j in zip(titles,pos):
        header = base_font.render(i,True,(255,255,255))
        screen.blit(header,(j,200))
    with open(path+'scores/web/scores.json') as file:
        data_score = json.load(file)

    c=300
    c1=1
    for p in data_score['scores']:
        if c1 == 8:
            break
        # setzt var auf den inhalt der JSON Datei
        time = p['time']
        name = p['name']
        points = str(p['points'])

        # zeigt die Inhalte an
        blitlist = [time,name,points]
        for i,j in zip(blitlist,pos):
            screen.blit(base_font.render(i,True,(255,255,255)),(j,c))
        c += 80
        c1 += 1


def howto(data,img,return_manuels,settings_manuels):
    screen = data['screen']
    screen.blit(img,(1,1))
    screen.blit(settings_manuels,(1600,1))
    screen.blit(return_manuels,(30,1))
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print('Quit game ...')
                pygame.quit() 
                exit(0) 
            if event.type == pygame.KEYDOWN:
                   screenmode='titlescreen'
                   return screenmode
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if x > 30 and y > 1 and x < 77 and y < 136:
                    screenmode='titlescreen'
                    return screenmode


def game_over(data):
    global points,playername
    screen = data['screen']
    game_over = data['game_over']
    screen.blit(game_over,(1,1))
    points_blit = str('NONE')
    name_blit = str(playername)
    message_blit = 'PRESS ANY KEY TO CONTINUE'
    base_font = pygame.font.SysFont(None, 180)
    message_font = pygame.font.SysFont(None, 65)
    points_surface = base_font.render(points_blit,False,(255,255,255))
    name_surface = base_font.render(name_blit,False,(255,255,255))
    message_surface = message_font.render(message_blit,False,(255,255,255))
    screen.blit(points_surface, (850,750))
    screen.blit(name_surface, (850,560))
    screen.blit(message_surface,(500,950))

    for event in pygame.event.get():
            if event.type==pygame.QUIT: # stoppt Script
                print('Quit game ...')
                pygame.quit() 
                exit(0) 
            if event.type == pygame.KEYDOWN:
                screenmode='titlescreen'
                return screenmode


def win(data):
    global points
    global playername
    screen = data['screen']
    path = data['path']
    win = data['win']
    screen.blit(win,(1,1))
    points_blit = str(points)
    name_blit = str(playername)
    message_blit = 'PRESS ANY KEY TO CONTINUE'
    base_font = pygame.font.SysFont(None, 180)
    message_font = pygame.font.SysFont(None, 65)
    points_surface = base_font.render(points_blit,False,(255,255,255))
    name_surface = base_font.render(name_blit,False,(255,255,255))
    message_surface = message_font.render(message_blit,False,(255,255,255))
    screen.blit(name_surface, (850,520))
    screen.blit(points_surface, (850,700))
    screen.blit(message_surface,(500,950))

    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print('Quit game ...')
                pygame.quit() 
                exit(0) 
            if event.type == pygame.KEYDOWN:
                screenmode='titlescreen'
                return screenmode

def timer(data,timer,number):
    global t3
    t3 = None
    screen = data['screen']
    logo = data['logo']
    clock = pygame.time.Clock()
    counter, text = 3, '3'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont(None, 230)
    red = pygame.Color('red')
    blue = pygame.Color('blue')
    green = pygame.Color('darkgreen')
    colors = [red,blue,green]
    first_render_pos = (150+70,100+150)
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else ''
            if e.type == pygame.QUIT: 
                run = False
            if counter == 0:
                t3 = datetime.datetime.now()
                return 'gamescreen'
        pygame.display.flip()
        screen.fill(colors[number])
        screen.blit(logo,(490,0))
        screen.blit(font.render(text+' SECONDS', True, (255, 255, 255)), (182+60, 600+150))
        screen.blit(font.render('GAME STARTS',True,(255, 255, 255)),first_render_pos)
        screen.blit(font.render('IN',True,(255, 255, 255)),(725+25,350+150))
        clock.tick(60)

