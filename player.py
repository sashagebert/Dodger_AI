import pygame


class Player(pygame.sprite.Sprite):

    RED = (255, 0, 0)

    init_x = 100
    init_y = 678

    jump_height = 150
    jump_speed = 8
    jump_speed_accel = 2

    def __init__(self, images):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.init_image = images[0]
        self.image = self.init_image
        self.image.set_colorkey(Player.RED)
        #self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = Player.init_x
        self.rect.y = Player.init_y
        self.velocity = 5
        self.score_update = pygame.time.get_ticks()
        self.score = 0
        self.jumping = False
        self.inair = False
        self.current_jump_speed = 0
        self.run_count = 0
        # TODO jumping animation
        self.jump_count = 0

    def update(self):

        if self.run_count + 1 >= 18:
            self.run_count = 0

        if pygame.time.get_ticks() - self.score_update > 100:
            self.score_update = pygame.time.get_ticks()
            self.score += 10

        if self.rect.y >= Player.init_y:
            self.inair = False
        else:
            self.inair = True

        if self.jumping:
            self.rect.y -= Player.jump_speed
            self.current_jump_speed += Player.jump_speed_accel
            if self.rect.y <= Player.init_y - Player.jump_height:
                self.jumping = False

        else:
            self.current_jump_speed -= Player.jump_speed_accel
            if self.rect.y <= Player.init_y:
                self.rect.y += Player.jump_speed

            self.image = self.images[self.run_count//6]
            self.image.set_colorkey(Player.RED)
            self.run_count += 1

    def jump(self):
        self.current_jump_speed = Player.jump_speed
        self.inair = True
        if self.rect.y >= Player.init_y:
            self.jumping = True

# https://www.youtube.com/watch?v=xxRhvyZXd8
# https://medium.com/@sanilkhurana7/building-a-neural-network-that-learns-to-play-a-game-part-1-e408ae7106d0

# to spawn enemies
# spawn every x to y seconds
# where x is the jump time
# spwan at least x sec in between to allow the player to jump
#
