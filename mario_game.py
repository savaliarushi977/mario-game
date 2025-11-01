import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LEVEL_WIDTH = 4000
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (92, 148, 252)
GROUND_BROWN = (139, 69, 19)
MARIO_RED = (255, 0, 0)
MARIO_BLUE = (0, 0, 255)
MARIO_SKIN = (255, 206, 180)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario Game")
clock = pygame.time.Clock()


class Mario(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 32
        self.height = 48
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.draw_mario()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.start_y = y
        
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.jump_power = -15
        self.gravity = 0.8
        self.on_ground = False
        self.facing_right = True
        self.is_dead = False
        
    def draw_mario(self):
        self.image.fill((0, 0, 0, 0))
        
        # Hat (red)
        pygame.draw.rect(self.image, MARIO_RED, (8, 8, 20, 8))
        
        # Face (skin)
        pygame.draw.rect(self.image, MARIO_SKIN, (8, 16, 20, 12))
        
        # Eyes
        pygame.draw.rect(self.image, BLACK, (12, 18, 3, 3))
        pygame.draw.rect(self.image, BLACK, (21, 18, 3, 3))
        
        # Mustache
        pygame.draw.rect(self.image, BLACK, (10, 24, 16, 4))
        
        # Body (red shirt)
        pygame.draw.rect(self.image, MARIO_RED, (10, 28, 16, 12))
        
        # Overalls (blue)
        pygame.draw.rect(self.image, MARIO_BLUE, (12, 32, 12, 8))
        
        # Arms (skin)
        pygame.draw.rect(self.image, MARIO_SKIN, (6, 30, 4, 8))
        pygame.draw.rect(self.image, MARIO_SKIN, (26, 30, 4, 8))
        
        # Legs (blue)
        pygame.draw.rect(self.image, MARIO_BLUE, (12, 40, 5, 8))
        pygame.draw.rect(self.image, MARIO_BLUE, (19, 40, 5, 8))
        
    def respawn(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.is_dead = False
        
    def die(self):
        self.is_dead = True
        
    def update(self, platforms, camera_x):
        if self.is_dead:
            return
            
        keys = pygame.key.get_pressed()
        
        self.vel_x = 0
        if keys[pygame.K_LEFT]:
            self.vel_x = -self.speed
            self.facing_right = False
        if keys[pygame.K_RIGHT]:
            self.vel_x = self.speed
            self.facing_right = True
            
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False
        
        self.vel_y += self.gravity
        
        if self.vel_y > 15:
            self.vel_y = 15
            
        self.rect.x += self.vel_x
        self.check_collision_x(platforms)
        
        self.rect.y += self.vel_y
        self.on_ground = False
        self.check_collision_y(platforms)
        
        if self.rect.left < camera_x:
            self.rect.left = camera_x
        if self.rect.right > camera_x + SCREEN_WIDTH:
            self.rect.right = camera_x + SCREEN_WIDTH
            
        if self.rect.top > SCREEN_HEIGHT:
            self.die()
            
    def check_collision_x(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_x > 0:
                    self.rect.right = platform.rect.left
                elif self.vel_x < 0:
                    self.rect.left = platform.rect.right
                    
    def check_collision_y(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=GROUND_BROWN):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        
        brick_size = 16
        for i in range(0, width, brick_size):
            for j in range(0, height, brick_size):
                pygame.draw.rect(self.image, (100, 50, 10), (i, j, brick_size-2, brick_size-2))
                
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 32
        self.height = 32
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(ORANGE)
        pygame.draw.circle(self.image, BLACK, (16, 10), 4)
        pygame.draw.circle(self.image, BLACK, (22, 10), 4)
        pygame.draw.rect(self.image, BLACK, (12, 22, 12, 3))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Pit(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        self.width = width
        self.height = 50
        self.image = pygame.Surface((width, self.height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, x, y, checkpoint_num):
        super().__init__()
        self.width = 40
        self.height = 80
        self.checkpoint_num = checkpoint_num
        self.activated = False
        self.image = pygame.Surface((self.width, self.height))
        self.draw_flag()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw_flag(self):
        if self.activated:
            self.image.fill((0, 0, 0, 0))
            pygame.draw.rect(self.image, GREEN, (5, 0, 5, 80))
            pygame.draw.polygon(self.image, GREEN, [(10, 10), (35, 20), (10, 30)])
        else:
            self.image.fill((0, 0, 0, 0))
            pygame.draw.rect(self.image, YELLOW, (5, 0, 5, 80))
            pygame.draw.polygon(self.image, YELLOW, [(10, 10), (35, 20), (10, 30)])
    
    def activate(self):
        self.activated = True
        self.draw_flag()


def create_level():
    platforms = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    pits = pygame.sprite.Group()
    checkpoints = pygame.sprite.Group()
    
    ground_segments = [
        Platform(0, 550, 600, 50),
        Platform(800, 550, 400, 50),
        Platform(1400, 550, 500, 50),
        Platform(2100, 550, 400, 50),
        Platform(2700, 550, 600, 50),
        Platform(3500, 550, 500, 50),
    ]
    for segment in ground_segments:
        platforms.add(segment)
    
    level_platforms = [
        Platform(250, 450, 120, 20, (210, 105, 30)),
        Platform(450, 380, 100, 20, (210, 105, 30)),
        Platform(650, 320, 120, 20, (210, 105, 30)),
        
        Platform(900, 450, 150, 20, (210, 105, 30)),
        Platform(1100, 380, 120, 20, (210, 105, 30)),
        Platform(1300, 450, 100, 20, (210, 105, 30)),
        
        Platform(1550, 420, 140, 20, (210, 105, 30)),
        Platform(1750, 350, 120, 20, (210, 105, 30)),
        Platform(1950, 420, 130, 20, (210, 105, 30)),
        
        Platform(2200, 450, 120, 20, (210, 105, 30)),
        Platform(2400, 380, 140, 20, (210, 105, 30)),
        Platform(2600, 450, 100, 20, (210, 105, 30)),
        
        Platform(2850, 420, 150, 20, (210, 105, 30)),
        Platform(3050, 350, 130, 20, (210, 105, 30)),
        Platform(3250, 420, 140, 20, (210, 105, 30)),
        Platform(3450, 320, 120, 20, (210, 105, 30)),
    ]
    for plat in level_platforms:
        platforms.add(plat)
    
    pits.add(Pit(600, 550, 200))
    pits.add(Pit(1200, 550, 200))
    pits.add(Pit(1900, 550, 200))
    pits.add(Pit(2500, 550, 200))
    
    enemies.add(Enemy(400, 350))
    enemies.add(Enemy(950, 420))
    enemies.add(Enemy(1600, 390))
    enemies.add(Enemy(2250, 420))
    enemies.add(Enemy(2900, 390))
    enemies.add(Enemy(3300, 390))
    
    checkpoints.add(Checkpoint(750, 470, 1))
    checkpoints.add(Checkpoint(1850, 470, 2))
    checkpoints.add(Checkpoint(2650, 470, 3))
    checkpoints.add(Checkpoint(3700, 470, 4))
    
    return platforms, enemies, pits, checkpoints


def show_winner_screen():
    screen.fill(SKY_BLUE)
    big_font = pygame.font.Font(None, 100)
    small_font = pygame.font.Font(None, 40)
    
    winner_text = big_font.render("WINNER!", True, YELLOW)
    congrats_text = small_font.render("You cleared all checkpoints!", True, WHITE)
    restart_text = small_font.render("Press ENTER to restart or ESC to quit", True, WHITE)
    
    screen.blit(winner_text, (SCREEN_WIDTH//2 - winner_text.get_width()//2, 200))
    screen.blit(congrats_text, (SCREEN_WIDTH//2 - congrats_text.get_width()//2, 320))
    screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, 400))
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_ESCAPE:
                    return False
    return False


def main():
    mario = Mario(100, 450)
    platforms, enemies, pits, checkpoints = create_level()
    
    camera_x = 0
    score = 0
    lives = 3
    current_checkpoint = 0
    last_checkpoint_pos = (100, 450)
    game_won = False
    
    font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if not game_won:
            mario.update(platforms, camera_x)
            
            camera_x = max(0, min(mario.rect.x - SCREEN_WIDTH // 3, LEVEL_WIDTH - SCREEN_WIDTH))
            
            if mario.is_dead:
                lives -= 1
                if lives > 0:
                    mario.respawn(last_checkpoint_pos[0], last_checkpoint_pos[1])
                else:
                    running = False
            
            for enemy in enemies:
                if mario.rect.colliderect(enemy.rect) and not mario.is_dead:
                    mario.die()
            
            for pit in pits:
                if mario.rect.colliderect(pit.rect) and not mario.is_dead:
                    mario.die()
            
            for checkpoint in checkpoints:
                if mario.rect.colliderect(checkpoint.rect) and not checkpoint.activated:
                    checkpoint.activate()
                    if checkpoint.checkpoint_num > current_checkpoint:
                        current_checkpoint = checkpoint.checkpoint_num
                        last_checkpoint_pos = (checkpoint.rect.x + 60, checkpoint.rect.y - 50)
                        score += 100
                        
                        if current_checkpoint == 4:
                            game_won = True
        
        screen.fill(SKY_BLUE)
        
        for platform in platforms:
            screen.blit(platform.image, (platform.rect.x - camera_x, platform.rect.y))
        
        for pit in pits:
            screen.blit(pit.image, (pit.rect.x - camera_x, pit.rect.y))
        
        for enemy in enemies:
            screen.blit(enemy.image, (enemy.rect.x - camera_x, enemy.rect.y))
        
        for checkpoint in checkpoints:
            screen.blit(checkpoint.image, (checkpoint.rect.x - camera_x, checkpoint.rect.y))
        
        if not mario.is_dead:
            screen.blit(mario.image, (mario.rect.x - camera_x, mario.rect.y))
        
        score_text = font.render(f"SCORE: {score}", True, WHITE)
        lives_text = font.render(f"LIVES: {lives}", True, WHITE)
        checkpoint_text = font.render(f"CHECKPOINT: {current_checkpoint}/4", True, WHITE)
        
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (SCREEN_WIDTH - 150, 10))
        screen.blit(checkpoint_text, (10, 50))
        
        controls_font = pygame.font.Font(None, 24)
        controls_text = controls_font.render("Arrow Keys: Move | Space: Jump", True, WHITE)
        screen.blit(controls_text, (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT - 30))
        
        pygame.display.flip()
        
        if game_won:
            pygame.time.wait(1000)
            restart = show_winner_screen()
            if restart:
                mario = Mario(100, 450)
                platforms, enemies, pits, checkpoints = create_level()
                camera_x = 0
                score = 0
                lives = 3
                current_checkpoint = 0
                last_checkpoint_pos = (100, 450)
                game_won = False
            else:
                running = False
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
