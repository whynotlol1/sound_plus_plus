import pygame

def main():
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Roboto', 30)
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Sound++")
    clock = pygame.time.Clock()
    running = True
    starting_coords = [150, 100]
    coords:list[float] = [154, 100]
    values:list[float] = [0, 0]
    while running:
        clock.tick(60)
        screen.fill((160, 160, 160))
        pygame.draw.rect(screen, (90, 90, 90), (starting_coords[1], starting_coords[0], 100, 7.5))
        pygame.draw.circle(screen, (0, 0, 0), (coords[1], coords[0]), 5)

        value_drawn = f"{values[0]}{'+' if values[1] < 0 else ''}{-values[1] if values[1] != 0 else ''}{'i' if values[1] != 0 else ''}"
        text = my_font.render(f"Sound value: {value_drawn}", False, (255, 255, 255))
        screen.blit(text, (10, 50))

        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and coords[0] > 0:
            coords[0] -= 0.5
        elif keys[pygame.K_DOWN] and coords[0] < 300:
            coords[0] += 0.5
        if keys[pygame.K_RIGHT] and coords[1] < 300:
            coords[1] += 0.5
        elif keys[pygame.K_LEFT] and coords[1] > 0:
            coords[1] -= 0.5

        values[0] = coords[1] - starting_coords[1]
        values[1] = coords[0] - (starting_coords[0] + 4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
    exit(0)

if __name__ == "__main__":
    main()
