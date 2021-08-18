import sys
import pygame


clock = pygame.time.Clock()
white = (255, 255, 255)
light_grey = (200, 200, 200)
w, h = size = (800, 600)
screen_color = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("tennis")


screen_rect = screen.get_rect()
ball = pygame.Rect(300, 400, 10, 10)
ball_speed_x = 5
ball_speed_y = 5

player = pygame.Rect(0, 0, 10, 70)
player.centery = screen_rect.centery
player_speed = 0

opponent = pygame.Rect(0, 260, 10, 70)
opponent.right = screen_rect.right
opponent_speed = 3

# Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 5
            if event.key == pygame.K_DOWN:
                player_speed += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 5
            if event.key == pygame.K_DOWN:
                player_speed -= 5


# To make sure player remains in screen
    if player.top <= 0:
        player.top = 0
    if player.bottom >= h:
        player.bottom = w

# movement of opponent
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= h:
        opponent.bottom = h

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    player.y += player_speed

    if ball.top <= 0 or ball.bottom >= h:
        ball_speed_y *= -1
    if ball.left <= 0:
        opponent_score += 1
        ball.center = (300, 400)
        ball.x += ball_speed_x
        ball.y += ball_speed_y
    if ball.right >= w:
        player_score += 1
        ball.center = (300, 400)
        ball.x += ball_speed_x
        ball.y += ball_speed_y

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
    screen.fill(screen_color)
    pygame.draw.rect(
        screen, white, player)
    pygame.draw.ellipse(
        screen, white, ball)
    pygame.draw.rect(
        screen, white, opponent)

    player_text = basic_font.render(f'{player_score}', False, light_grey)
    screen.blit(player_text, (600, 470))

    opponent_text = basic_font.render(
        f'{opponent_score}', False, light_grey)
    screen.blit(opponent_text, (660, 470))
    pygame.display.flip()
    clock.tick(60)
