import pygame 
import random 
from datetime import datetime
from order import Order


class CustomerAsSprite(pygame.sprite.Sprite, Order):

    def __init__(self, x, y, patience_in_seconds, earth_group, state_obj):
        pygame.sprite.Sprite.__init__(self)
        self.names = ["emma", "gary", "jane", "terry"]
        self._name_chosen = random.randint(0,3)
        self.mood = "happy"
        self.image = pygame.transform.scale(pygame.image.load(f"./Assets/{self.names[self._name_chosen]}/{self.mood}.png"), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.move_counter = 0
        self.move_direction = 1
        self.patience_in_seconds = patience_in_seconds #round(random.uniform(40,120)) 
        self._time_at_init = datetime.now()
        self.clicked = False
        self.switch = False
        self.earth_group = earth_group
        Order.__init__(self)
        # Explosion
        self.explosion_images = []
        for num in range(1,6):
            img = pygame.image.load(f"./Assets/explosions/exp{num}.png")
            img = pygame.transform.scale(img, (100,100))
            # add the image to the list
            self.explosion_images.append(img)
        self.index = 0
        #self.image = self.images[self.index]
        #self.rect = self.image.get_rect()
        #self.rect.center = [x, y]
        self.counter = 0
        self.attacking_customer_destroyed = False
        self.state = state_obj

    def _time_elapsed(self):
        time_now = datetime.now()
        time_delta = time_now-self._time_at_init
        return time_delta.total_seconds()

    def _update_mood(self):
        has_status_changed = False
        self.percent_patience_remaining = 1-(self._time_elapsed()/self.patience_in_seconds)
        if self.percent_patience_remaining >= 2/3: # checks if customer should be happy
            if self.mood != "happy": # if customer is not happy then this will need to be changed
                self.mood =  "happy" # change to happy
                has_status_changed = True # so we can update the face image because there has been a change
        elif self.percent_patience_remaining >= 1/3: # checks if a customer should be waiting
            if self.mood != "waiting": # if customer is not waiting then this should be changed
                self.mood =  "waiting" # change to waiting
                has_status_changed = True # so we can update the face image because there has been a change
        elif self.percent_patience_remaining >= 0: # you get the idea if you've read the above comments
            if self.mood != "cross": 
                self.mood =  "cross"
                has_status_changed = True
        else:
            if self.mood != "attack":
                self.mood = "attack"
                has_status_changed = True
        if has_status_changed: # checks for change in status
            self.image = pygame.transform.scale(pygame.image.load(f"./Assets/{self.names[self._name_chosen]}/{self.mood}.png"), (20, 20))

    def explosion_update(self):
        explosion_speed = 3
        # update explosion animation
        self.counter += 1
        if self.counter >= explosion_speed and self.index < len(self.explosion_images)-1:
            self.counter = 0
            self.index +=1
            self.image = self.explosion_images[self.index]
        
        # if the animation is complete, delete explosion. 
        if self.index >= len(self.explosion_images) -1 and self.counter >= explosion_speed:
            self.kill()

    def update(self):
        self._update_mood()
        self.rect.x += self.move_direction
        self.move_counter += 2
        if self.mood == "attack":
            self.rect.y += 1
            if self.attacking_customer_destroyed:
                self.explosion_update()
                #self.kill()
        elif abs(self.move_counter) >75:
            self.move_direction *= -1
            self.move_counter *= self.move_direction
            self.rect.y += 1
        if self.rect.x > 725 or self.rect.x<-10:   #bottom<0:
            self.kill()
        # if collides with earth then death.    
        if pygame.sprite.spritecollide(self, self.earth_group, False, pygame.sprite.collide_mask):
            self.explosion_update()
            #self.state.curr_state = self.state.game_over_state
            # set the game over logic
            #game_over = True
            #return game_over
            # need to set up explosion noises
            #explosion_fx.play()
            #explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
            #explosion_group.add(explosion)

        
        