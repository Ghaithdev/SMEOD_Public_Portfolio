import pygame
from os import path
from random import randint
from time import sleep

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, surf=False,image=False, speed=0,groups=None,transparent_pixels=True,x=0,y=0, dir=(0,0)):
        super().__init__(groups)
        if surf:
            self.image=surf
        elif transparent_pixels:
            self.image = pygame.image.load(path.join(images_path,image)).convert_alpha()
        else:
            self.image = pygame.image.load(path.join(images_path,image)).convert()
        self.rect=self.image.get_frect(center=(x,y))
        self.dir=pygame.math.Vector2(dir)
        self.speed=speed

class Star(Sprite):
    def __init__(self,x,y):
        super().__init__(star_surf,"star.png", 100 ,all_sprites,True,x,y, (0,1))

    def update(self,dt):
        self.rect.center+=self.dir*self.speed*dt
        if self.rect.top>win_height:
            Star(randint(0,win_width),-50)
            self.kill()
            
class AnimatedExplosion(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        self.frame_index=0
        self.frames=frames
        self.image=self.frames[self.frame_index]
        self.rect=self.image.get_frect(center=pos)


    def update(self, dt):
        self.frame_index+=20*dt
        if self.frame_index<=len(self.frames):
            self.image=self.frames[int(self.frame_index)]
        else:
            self.kill()

class Player(Sprite):

    def __init__(self):
        super().__init__(None,"player.png", 300 ,all_sprites,True,win_width/2,win_height/2, (0,0))
        self.can_shoot=True
        self.laser_shoot_time=0
        self.cooldown_duration=400
        self.health=5
        self.on_hit_invinvibility=2000
        self.last_hit=0

    def update(self,dt):
        keys=pygame.key.get_pressed()
        self.dir.x=int(keys[pygame.K_RIGHT])-int(keys[pygame.K_LEFT])
        self.dir.y=int(keys[pygame.K_DOWN])-int(keys[pygame.K_UP])
        self.dir= self.dir.normalize() if self.dir else self.dir
        self.rect.center+=self.dir*self.speed*dt

        r_keys=pygame.key.get_just_pressed()
        if keys[pygame.K_SPACE] and self.can_shoot:
            self.laser_shoot_time=pygame.time.get_ticks()
            self.can_shoot=False
            Laser(self.rect.midtop)
            laser_sound.play()

        
        self.recharge()

    def damage_check(self):
        current_time=pygame.time.get_ticks()
        self.can_shoot=True
        if current_time-self.last_hit>self.cooldown_duration:
            self.health-=1
            self.last_hit=current_time
            damage_sound.play()
        if self.health==0:
            self.kill()
            game_over()
            

    def recharge(self):
        if not self.can_shoot:
            current_time=pygame.time.get_ticks()
            if current_time-self.laser_shoot_time>=self.cooldown_duration:
                self.can_shoot=True

class Laser(Sprite):
    def __init__(self,pos):
        super().__init__(laser_surf,"laser.png", 450 ,[all_sprites,laser_sprites],True,win_width/2,win_height/2, (0,-1))
        self.rect.midbottom=pos

    def update(self,dt):
        self.rect.center+=self.dir*self.speed*dt
        if self.rect.bottom<0:
            self.kill()

class Meteor(Sprite):

    def __init__(self):
        super().__init__(meteor_surf,"meteor.png", randint(100,500) ,[all_sprites,meteor_sprites],True,randint(0,win_width),-50, ((randint(-50,50)/100),1))
        self.original_image=meteor_surf
        self.rotation=0
        self.rotation_speed=randint(-80,80)

    def update(self,dt):
        self.rect.center+=self.dir*self.speed*dt
        self.rotation+=self.rotation_speed*dt
        self.image=pygame.transform.rotozoom(self.original_image, self.rotation,1)
        if self.rect.top>win_height:
            self.kill()
        self.rect=self.image.get_frect(center=self.rect.center)
        
def collisions():
    lasers=laser_sprites
    for laser in lasers:
        bullseye=pygame.sprite.spritecollide(laser, meteor_sprites, True, pygame.sprite.collide_mask)
        if bullseye:
            bullseye[0].kill()
            laser.kill()
            AnimatedExplosion(explosion_frames,laser.rect.midtop,all_sprites)
            explosion_sound.play()
    damage=pygame.sprite.spritecollide(player,meteor_sprites,True,pygame.sprite.collide_mask)
    if damage:
        player.damage_check()

def game_over():
    global running
    font=pygame.font.Font(path.join(images_path,'Oxanium-Bold.ttf'), 30)
    text_surf=font.render("Game Over", True, "#f0f0f0")
    display_surface.blit(text_surf, (win_width/2,win_height/2))
    sleep(3)
    running=False
    
def display_score():
    current_time=pygame.time.get_ticks()
    text_surf=font.render(str(current_time),True,(240,240,240))
    text_rect=text_surf.get_frect(midbottom=(win_width/2, win_height-50))
    display_surface.blit(text_surf,text_rect)
    pygame.draw.rect(display_surface,(240,240,240),text_rect.inflate(15,20).move(0,-8),5,10)

# General setup
pygame.init()
pygame.display.set_caption("Space Shooter")
win_width,win_height= 1280, 720
display_surface=pygame.display.set_mode((win_width,win_height))
running=True
clock=pygame.time.Clock()

main_fp=path.dirname(path.abspath(__file__))
images_path=path.join(main_fp,"..","images")
sound_path=path.join(main_fp,"..","audio")

#imports
star_surf=pygame.image.load(path.join(images_path,"star.png")).convert_alpha()
laser_surf=pygame.image.load(path.join(images_path,"laser.png")).convert_alpha()
meteor_surf=pygame.image.load(path.join(images_path,"meteor.png")).convert_alpha()
font=pygame.font.Font(path.join(images_path,"Oxanium-Bold.ttf"), 20)
explosion_frames=[pygame.image.load(path.join(images_path,"explosion" ,f"{i}.png")).convert_alpha() for i in range(21)]
bgm=pygame.mixer.Sound(path.join(sound_path,"game_music.wav"))
laser_sound=pygame.mixer.Sound(path.join(sound_path,"laser.wav"))
explosion_sound=pygame.mixer.Sound(path.join(sound_path,"explosion.wav"))
damage_sound=pygame.mixer.Sound(path.join(sound_path,"damage.ogg"))
bgm.play(loops=-1)


#groups
all_sprites=pygame.sprite.Group()
meteor_sprites=pygame.sprite.Group()
laser_sprites=pygame.sprite.Group()

for i in range(20):
    star= Star(randint(0,win_width),randint(0,win_height))
player=Player()
meteor_event=pygame.event.custom_type()
pygame.time.set_timer(meteor_event,500)



while running:
    dt=clock.tick()/1000
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type==meteor_event:
            Meteor()
    
    #update gamestate
    all_sprites.update(dt)
    collisions()

    # Draw the game
    display_surface.fill('midnightblue')
    display_score()
    all_sprites.draw(display_surface)
    pygame.display.update()

pygame.quit()