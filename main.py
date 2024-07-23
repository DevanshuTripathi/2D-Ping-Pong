import pygame

pygame.init()

screen = pygame.display.set_mode((750,600))
color = (159, 43, 104)
pygame.display.set_caption('Pong')
icon = pygame.image.load('icon.jpg').convert()
pygame.display.set_icon(icon)

def gameLoop():

    clock = pygame.time.Clock()

    length = 100
    goal = 25
    rad = 10

    x = 25
    y = 338 - length/2

    X = 695
    Y = 338 - length/2

    ballx = 30 + rad + goal
    bally = 338
    ex=1
    ey=1

    sped=0.01

    gameTime = 80
    startTicks = int(pygame.time.get_ticks()/1000)

    running = True

    blueplayer = pygame.image.load('bluebar.png').convert()
    redplayer = pygame.image.load('redbar.png').convert()
    timeboard = pygame.image.load('board.png').convert()

    redscore = 0
    bluescore = 0

    font = pygame.font.Font('HomeVideo-BLG6G.ttf', 32)
    font2 = pygame.font.Font('HomeVideo-BLG6G.ttf', 64)
    font3 = pygame.font.Font('HomeVideo-BLG6G.ttf', 25)

    flag = 0

    min = 0
    sec = 0

    dt = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_RETURN]):
            flag = 1

        screen.fill("black")
        player = pygame.draw.rect(screen, "blue", pygame.Rect(x, y, 30, length))
        comp = pygame.draw.rect(screen, "blue", pygame.Rect(X, Y, 30, length))
        board = pygame.draw.rect(screen, color, pygame.Rect(0, 0, 750, 76))
        timeBoard = pygame.draw.rect(screen, color, pygame.Rect(250, 0, 250, 76))
        line = pygame.draw.rect(screen, "gray", pygame.Rect(375, 100, 2, 500))
        line1 = pygame.draw.rect(screen, "gray", pygame.Rect(0, 100, 2, 500))
        line2 = pygame.draw.rect(screen, "gray", pygame.Rect(750 - 2, 100, 2, 500))
        boardline = pygame.draw.rect(screen, "white", pygame.Rect(0, 76, 750, 1))
        subBoard = pygame.draw.rect(screen, "gray", pygame.Rect(0, 100, 750, 2))
        subBoard2 = pygame.draw.rect(screen, "gray", pygame.Rect(0, 599, 750, 2))
        screen.blit(blueplayer, player)
        screen.blit(redplayer, comp)
        screen.blit(timeboard, timeBoard)
        
        timeElapsed = int(pygame.time.get_ticks()/1000) - startTicks
        timeRemain = abs(gameTime - timeElapsed)
        if timeRemain >= 60 :
            min = 1
            sec = timeRemain - 60
        else :
            min = 0
            sec = timeRemain
        if timeRemain == 0 :
            running = False
            gameEnd(bluescore, redscore)
        Time = font.render(f'{min}:{sec}', True, "white", "black")
        TimeRect = Time.get_rect()
        TimeRect.center = (375,50)

        screen.blit(Time, TimeRect)

        blueScore = font2.render(f'{bluescore}', True, "black", color)
        blueScoreRect = blueScore.get_rect()
        blueScoreRect.center = (187,38)

        screen.blit(blueScore, blueScoreRect)

        redScore = font2.render(f'{redscore}', True, "black", color)
        redScoreRect = redScore.get_rect()
        redScoreRect.center = (563,38)

        screen.blit(redScore, redScoreRect)

        TimeText = font3.render('TIME', True, "gray", "black")
        TimeTextRect = TimeText.get_rect()
        TimeTextRect.center = (375,25)

        screen.blit(TimeText, TimeTextRect)

        ball = pygame.draw.circle(screen, "white", (ballx, bally), rad)

        vel = 300 * dt * 2

        if keys[pygame.K_w]:
            y -= vel
        if keys[pygame.K_s]:
            y += vel
        if y < 102:
            y=102
        if y > 598 - length:
            y=598 - length

        if keys[pygame.K_UP]:
            Y -= vel
        if keys[pygame.K_DOWN]:
            Y += vel
        if Y < 102:
            Y=102
        if Y > 598 - length:
            Y=598 - length

        xb = ballx
        yb = bally
        
        if (ballx <= rad/2 + goal):
            redscore+=1
            flag = 0
            x = 25
            y = 338 - length/2

            X = 695
            Y = 338 - length/2

            ballx = 30 + rad + goal
            bally = 338
            ex=1
            ey=1

            sped=0.01
            continue
        if (ballx >= 750 - rad/2 - goal):
            bluescore+=1
            flag = 0
            x = 25
            y = 338 - length/2

            X = 695
            Y = 338 - length/2

            ballx = 695 - rad
            bally = 338
            ex=-1
            ey=1

            sped=0.01
            continue
        elif (ballx <= goal + 30 + rad and (bally>=y and bally<= y + length/2)):
            ballx = xb
            ex = 1
            bally = yb
            ey = -1
            diff = abs(y+length/2 - bally)
            if (diff < length/6):
                sped = 0.01
            elif (diff < length/3):
                sped = 0.02
            else :
                sped = 0.03
        elif (ballx <= goal + 30 + rad and (bally>y + length/2 and bally< y + length)):
            ballx = xb
            ex = 1
            bally = yb
            ey = 1
            diff = abs(length - bally)
            if (diff < length/6):
                sped = 0.01
            elif (diff < length/3):
                sped = 0.02
            else :
                sped = 0.03
        elif (ballx >= 750 - goal - 30 - rad and (bally>=Y and bally<= Y + length/2)):
            ballx = xb
            ex = -1
            bally = yb
            ey = -1
            diff = abs(Y+length/2 - bally)
            if (diff < length/6):
                sped = 0.01
            elif (diff < length/3):
                sped = 0.02
            else :
                sped = 0.03
        elif (ballx >= 750 - goal - 30 - rad and (bally>Y + length/2 and bally< Y + length)):
            ballx = xb
            ex = -1
            bally = yb
            ey = 1
            diff = abs(length - bally)
            if (diff < length/6):
                sped = 0.01
            elif (diff < length/3):
                sped = 0.02
            else :
                sped = 0.03
        if flag == 1 :
            ballx += 300 * (sped + dt) * ex
            bally += 300 * (dt) * ey
        if bally > 600 - rad :
            bally = yb
            ey*= -1
        if bally < 100 + rad :
            bally = yb
            ey*= -1


        pygame.display.update()

        dt = clock.tick(60) / 1000

def gameMenu():

    clock = pygame.time.Clock()

    font = pygame.font.Font('HomeVideo-BLG6G.ttf', 100)

    start = font.render('Start', True, "black", color)
    startRect = start.get_rect()
    startRect.center = (375,250)

    swidth = start.get_width()
    sheight = start.get_height()

    quit = font.render('Quit', True, "black", color)
    quitRect = quit.get_rect()
    quitRect.center = (375,350)

    qwidth = quit.get_width()
    qheight = quit.get_height()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 375 - swidth/2 <= x <= 375 + swidth/2 and 250 - sheight/2 <= y <= 250 + sheight/2 :
                    gameLoop()
                    running = False
                if 375 - qwidth/2 <= x <= 375 + qwidth/2 and 350 - qheight/2 <= y <= 350 + qheight/2 :
                    running = False

        screen.fill(color)
        screen.blit(start, startRect)
        screen.blit(quit, quitRect)
        
        pygame.display.update()

        clock.tick(60)

def gameEnd(bluescore, redscore):
    clock = pygame.time.Clock()

    font = pygame.font.Font('HomeVideo-BLG6G.ttf', 100)
    font1 = pygame.font.Font('HomeVideo-BLG6G.ttf', 50)

    blue = font.render(f'{bluescore}', True, "black", color)
    blueRect = blue.get_rect()
    blueRect.center = (281.25,250)

    red = font.render(f'{redscore}', True, "black", color)
    redRect = red.get_rect()
    redRect.center = (468.75,250)

    line = font.render('-', True, "black", color)
    lineRect = line.get_rect()
    lineRect.center = (375,250)

    start = font1.render('Play Again', True, "black", color)
    startRect = start.get_rect()
    startRect.center = (375,350)

    quit = font1.render('Quit', True, "black", color)
    quitRect = quit.get_rect()
    quitRect.center = (375,400)

    swidth = start.get_width()
    sheight = start.get_height()

    qwidth = quit.get_width()
    qheight = quit.get_height()

    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 375 - swidth/2 <= x <= 375 + swidth/2 and 350 - sheight/2 <= y <= 350 + sheight/2 :
                    gameLoop()
                    running = False
                if 375 - qwidth/2 <= x <= 375 + qwidth/2 and 400 - qheight/2 <= y <= 400 + qheight/2 :
                    running = False
        screen.fill(color)
        screen.blit(blue, blueRect)
        screen.blit(red, redRect)
        screen.blit(line, lineRect)
        screen.blit(start, startRect)
        screen.blit(quit, quitRect)

        pygame.display.update()

        clock.tick(60)
gameMenu()
pygame.quit()