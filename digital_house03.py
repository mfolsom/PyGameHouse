import pygame

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the background
background_color = (120, 200, 255)
screen.fill(background_color)

# Draw the house
house_color = (255, 200, 150)
roof_color = (255, 100, 50)
window_color = (255, 255, 255)

# Draw the walls
house_width = 200
house_height = 300
house_x = screen_width // 2 - house_width // 2
house_y = screen_height - house_height - 50
pygame.draw.rect(screen, house_color, (house_x, house_y, house_width, house_height))

# Draw the roof
roof_width = 250
roof_height = 150
roof_x = house_x - (roof_width - house_width) // 2
roof_y = house_y - roof_height + 50
pygame.draw.polygon(screen, roof_color, ((roof_x, roof_y + roof_height), (roof_x + roof_width, roof_y + roof_height), (house_x + house_width, house_y), (house_x, house_y)))

# Draw the windows
window_width = 50
window_height = 50
window_x1 = house_x + house_width // 4 - window_width // 2
window_x2 = house_x + 3 * house_width // 4 - window_width // 2
window_y = house_y + house_height // 4 - window_height // 2
pygame.draw.rect(screen, window_color, (window_x1, window_y, window_width, window_height))
pygame.draw.rect(screen, window_color, (window_x2, window_y, window_width, window_height))

# Draw the door
door_color = (150, 100, 50)
door_width = 70
door_height = 120
door_x = house_x + house_width // 2 - door_width // 2
door_y = house_y + house_height - door_height
pygame.draw.rect(screen, door_color, (door_x, door_y, door_width, door_height))

# Update the screen
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
