import pygame, time, random

pygame.init()

run=True
f=0
t=100
k=0
h=1
start1=False
start2=False
start3=False
start4=False
cl=pygame.time.Clock()
scr_w=600
scr_h=375
bg_x=0
bg_y=0
cr_x=20
cr_y=290
f_x=600
f_y=random.randrange(0,3)
if f_y==0: f_y=260
elif f_y==1: f_y=290
else: f_y=320
ff_x=600
ff_y=random.randrange(0,3)
if ff_y==0: ff_y=260
elif ff_y==0: ff_y=290
else: ff_y=320
r1_x=600
r1_y=random.randrange(0,3)
r2_x=600
r2_y=random.randrange(0,3)
if r1_y==0: r1_y=270
elif r1_y==1: r1_y=300
else: r1_y=330
if r2_y==0: r2_y=270
elif r2_y==1: r2_y=300
else: r2_y=330
sk_x=600
sk_y=random.randrange(0,3)
if sk_y==0: sk_y=260
elif sk_y==1: sk_y=290
else: sk_y=320
v=2

# Color
Red=pygame.Color(255,0,0)
White=pygame.Color(255,255,255)

# Main
screen=pygame.display.set_mode((scr_w,scr_h))
pygame.display.set_caption("Candy Crab <3")
bg=pygame.image.load('graphic/background.jpg')
crab=pygame.image.load('graphic/crab.png')
fish=pygame.image.load('graphic/fish.png')
fake_fish=pygame.image.load('graphic/fakefish.png')
rock1=pygame.image.load('graphic/rock1.png')
rock2=pygame.image.load('graphic/rock2.png')
skull=pygame.image.load('graphic/skull.png')
font1=pygame.font.Font('font/04B_19.ttf',20)
font2=pygame.font.Font('font/Symtext.ttf',70)
font3=pygame.font.Font('font/game_over.ttf',70)
sbg=pygame.mixer.Sound('sound/sound_background.wav')
eat1=pygame.mixer.Sound('sound/eat.wav')
eat2=pygame.mixer.Sound('sound/w_eat.wav')
gameover=pygame.mixer.Sound('sound/game_over.wav')

sbg.set_volume(1)
gameover.set_volume(1)
eat1.set_volume(1)
eat2.set_volume(1)
sbg.play(-1)

def show():
    # fish
    surf_f=font1.render('FISH: {0}'.format(f),True,White)
    rect_f=surf_f.get_rect()
    rect_f.midtop=(50,10)
    screen.blit(surf_f,rect_f)
    # speed
    surf_sp=font1.render('SPEED: {0} km/h'.format(t/50),True,White)
    rect_sp=surf_sp.get_rect()
    rect_sp.midtop=(97,30)
    screen.blit(surf_sp,rect_sp)

def check(k):
    if k==260 or k==290 or k==320: return True
    return False

def game_over():
    surf_g=font2.render('GAME OVER',True,Red)
    rect_g=surf_g.get_rect()
    rect_g.midtop=(300,50)
    screen.blit(surf_g,rect_g)
    surf_f=font3.render('FISH: {0}'.format(f),True,Red)
    rect_f=surf_f.get_rect()
    rect_f.midtop=(290,130)
    screen.blit(surf_f,rect_f)
    sbg.stop()
    gameover.play()
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

while True:
    cl.tick(t)

    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            pygame.quit()
        if i.type==pygame.KEYDOWN:
            # if i.key==pygame.K_SPACE:
            #     mu-=1
            if i.key==pygame.K_UP and check(cr_y-30):
                cr_y-=30
            if i.key==pygame.K_DOWN and check(cr_y+30):
                cr_y+=30   
    # Background
    screen.blit(bg,(bg_x,bg_y))
    screen.blit(bg,(bg_x+600,bg_y))
    if run: bg_x-=v
    if bg_x==-600: bg_x=0
    # Rocks
    screen.blit(rock1,(r1_x,r1_y))
    if run: r1_x-=v
    if r1_x==-10:
        r1_x=1000
        r1_y=random.randrange(0,3)
        if r1_y==0: r1_y=270
        elif r1_y==1: r1_y=300
        else: r1_y=330

    if start1==False: a=random.randrange(200,300)
    if r1_x==a and start1==False: start1=True
    if start1:
        screen.blit(rock2,(r2_x,r2_y))
        if run: r2_x-=v
        if r2_x==-10:
            r2_x=1000
            r2_y=random.randrange(0,3)
            if r2_y==0: r2_y=270
            elif r2_y==1: r2_y=300
            else: r2_y=330

        if r2_x==r1_x and r2_y==r1_y:
            r2_x==1000
            r2_y=random.randrange(0,3)
            if r2_y==0: r2_y=270
            elif r2_y==1: r2_y=300
            else: r2_y=330
    # Skull
    if f==10: start4=True
    if start4:
        screen.blit(skull,(sk_x,sk_y))
        if run: sk_x-=v
        if sk_x==-10:
            sk_x=1000
            sk_y=random.randrange(0,3)
            if sk_y==0: sk_y=260
            elif sk_y==1: sk_y=290
            else: sk_y=320
        if sk_y==r1_y-10 or sk_y==r2_y-10 or sk_y==f_y or sk_y==ff_y:
            if (sk_x-r1_x>=-30 and sk_x-r1_x<=30) or (sk_x-r2_x>=-30 and sk_x-r2_x<=30) or (sk_x-f_x>=-30 and sk_x-f_x<=30) or (sk_x-ff_x>=-30 and sk_x-ff_x<=30):
                sk_x+=60
    # Crab
    screen.blit(crab,(cr_x,cr_y))
    # Fish
    if r1_x<0: start2=True
    if start2:
        screen.blit(fish,(f_x,f_y))
        if run: f_x-=v
        if f_x==-10:
            f_x=1000
            f_y=random.randrange(0,3)
            if f_y==0: f_y=260
            elif f_y==1: f_y=290
            else: f_y=320
        if f_y==r1_y-10 or f_y==r2_y-10:
            if (f_x-r1_x>=-30 and f_x-r1_x<=30) or (f_x-r2_x>=-30 and f_x-r2_x<=30):
                f_y=random.randrange(0,3)
                if f_y==0: f_y=260
                elif f_y==1: f_y=290
                else: f_y=320

    if f==5: start3=True
    if start3:
        screen.blit(fake_fish,(ff_x,ff_y))
        if run: ff_x-=v
        if ff_x==-10:
            ff_x=1000
            ff_y=random.randrange(0,3)
            if ff_y==0: ff_y=260
            elif ff_y==1: ff_y=290
            else: ff_y=320
        if ff_y==r1_y-10 or ff_y==r2_y-10 or ff_y==f_y:
            if (ff_x-r1_x>=-30 and ff_x-r1_x<=30) or (ff_x-r2_x>=-30 and ff_x-r2_x<=30) or (ff_x-f_x>=-30 and ff_x-f_x<=30):
                ff_x+=60
    # <>
    if (cr_x+30==r1_x and cr_y==r1_y-10) or (cr_x+30==r1_x+30 and cr_y==r1_y-10) or (cr_x+30==r2_x and cr_y==r2_y-10) or (cr_x+30==r2_x+30 and cr_y==r2_y-10) or (cr_x==sk_x and cr_y==sk_y) or (cr_x==sk_x+30 and cr_y==sk_y):
        run=False
    if (f_y==cr_y and f_x==cr_x) or (f_y==cr_y and f_x==cr_x+10) or (f_y==cr_y and f_x==cr_x+20):
        f+=1
        eat1.play()
        k+=1
        f_x=1000
        f_y=random.randrange(0,3)
        if f_y==0: f_y=260
        elif f_y==1: f_y=290
        else: f_y=320
    if k==h:
        t+=20
        k-=h
        h+=1
    if (ff_y==cr_y and ff_x==cr_x) or (ff_y==cr_y and ff_x==cr_x+10) or (ff_y==cr_y and ff_x==cr_x+20):
        f-=1
        eat2.play()
        ff_x=1000
        ff_y=random.randrange(0,3)
        if ff_y==0: ff_y=260
        elif ff_y==1: ff_y=290
        else: ff_y=320

    if run==False: game_over()
    show()

    pygame.display.flip()