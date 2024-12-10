import pygame
import sys
import random

WINDOW_SIZE = 600
CELL_SIZE = 20
FPS = 2      # początkowa prędkość węża
GAME_TIME = 120

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)      # dobry owoc
RED = (255, 0, 0)        # zatruty owoc
SNAKE_COLOR = (50, 205, 50)

UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

OPPOSITE_DIRECTIONS = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}

# rysowanie planszy
def draw_grid(screen):
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, WINDOW_SIZE))
    for y in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WINDOW_SIZE, y))


# generowanie owocu
def generate_fruit(snake, lifetime):
    while True:
        position = (random.randint(0, (WINDOW_SIZE // CELL_SIZE) - 1), random.randint(0, (WINDOW_SIZE // CELL_SIZE) - 1))
        # owoc nie może pojawić się na wężu
        if position not in snake:
            fruit_type = random.choice(['good', 'bad'])
            return {'position': position,'type' : fruit_type, 'lifetime': lifetime}


# obsługa kursora i obliczenie kierunku
def calculate_direction(snake, mouse_position, current_direction):
    head_x, head_y = snake[-1][0] * CELL_SIZE, snake[-1][1] * CELL_SIZE
    mouse_x, mouse_y = mouse_position

    if abs(mouse_x - head_x) > abs(mouse_y - head_y):      # ruch poziomy
        if mouse_x - head_x > 0:
            new_direction = RIGHT
        else:
            new_direction = LEFT
    else:  # ruch poziomy
        if mouse_y - head_y > 0:
            new_direction = UP
        else:
            new_direction = DOWN

    if new_direction == OPPOSITE_DIRECTIONS[current_direction]:
        return current_direction, True

    return new_direction, False


# zmienianie pozycji węża
def move_snake(snake, direction, fruit):
    head = snake[-1]
    new_head = ((head[0] + direction[0]) % (WINDOW_SIZE // CELL_SIZE), (head[1] + direction[1]) % (WINDOW_SIZE // CELL_SIZE))
    if new_head in snake:
        return False, "collision"
    snake.append(new_head)
    if new_head == fruit['position']:
        if fruit['type'] == 'bad':
            return False, "bad_fruit"
        return True, "good_fruit"
    snake.pop(0)
    return True, None


def draw_game(screen, snake, fruit):
    screen.fill(BLACK)
    draw_grid(screen)
    for part in snake:
        rect = pygame.Rect(part[0] * CELL_SIZE, part[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, SNAKE_COLOR, rect)
        fruit_color = GREEN if fruit['type'] == 'good' else RED
        fruit_rect = pygame.Rect(fruit['position'][0] * CELL_SIZE, fruit['position'][1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, fruit_color, fruit_rect)
        pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    snake = [(10, 10)]
    direction = RIGHT
    fruit = generate_fruit(snake, 20)
    score = 0
    speed = FPS
    game_time = GAME_TIME
    start_ticks = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                new_direction, invalid_move = calculate_direction(snake, mouse_position, direction)
                if invalid_move:
                    print("Tried to go backwards! Game Over!")
                    pygame.quit()
                    sys.exit()
                direction = new_direction

        game_active, result = move_snake(snake, direction, fruit)
        if not game_active:
            if result == "bad_fruit":
                print("Bad fruit eaten! Game Over!")
            elif result == "collision":
                print("Snake collision! Game Over!")
            break

        if result == "good_fruit":
            score += 1
            fruit = generate_fruit(snake, 20)

        elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
        remaining_time = game_time - elapsed_time
        if remaining_time <= 0:
            print("Time's up!")
            break

        if elapsed_time % 30 == 0:
            speed += 1

        draw_game(screen, snake, fruit)
        pygame.display.set_caption(f"Snake Game | Score: {score} | Time Left: {remaining_time}s")
        clock.tick(speed)

    print(f"Game Over! Your score: {score}")
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()