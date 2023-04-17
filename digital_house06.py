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

# Draw a cloud

cloud_color = (255, 255, 255)
cloud_radius = 30
cloud_x = 100
cloud_y = 100

pygame.draw.circle(screen, cloud_color, (cloud_x + 50, cloud_y), cloud_radius)
pygame.draw.circle(screen, cloud_color, (cloud_x + cloud_radius, cloud_y), cloud_radius)
pygame.draw.circle(screen, cloud_color, (cloud_x - cloud_radius, cloud_y), cloud_radius)
pygame.draw.circle(screen, cloud_color, (cloud_x, cloud_y + cloud_radius), cloud_radius)
pygame.draw.circle(screen, cloud_color, (cloud_x, cloud_y - cloud_radius), cloud_radius)
pygame.draw.circle(screen, cloud_color, (cloud_x + 25 + cloud_radius, cloud_y + cloud_radius), cloud_radius)
pygame.draw.circle(screen, cloud_color, (cloud_x - cloud_radius - 25, cloud_y + cloud_radius - 25), cloud_radius)
pygame.draw.circle(screen, cloud_color, (cloud_x + cloud_radius, cloud_y - cloud_radius), cloud_radius)
pygame.draw.circle(screen, cloud_color, (cloud_x - cloud_radius, cloud_y - cloud_radius), cloud_radius)

# Draw the hills
hill_colors = [(204, 204, 255),(50, 150, 50),(100, 200, 100), (0, 100, 0), (50, 150, 50)]
hill_rects = [(0, 300, 200, 300), (150, screen_height // 3, 300, 500), (300, 200, 300, 400), (600, 300, 250, 300), (450, 300, 250, 300), ]
for i, rect in enumerate(hill_rects):
    pygame.draw.ellipse(screen, hill_colors[i % len(hill_colors)], rect)

# Draw the grass
grass_color = (50, 150, 50)
grass_rect = pygame.Rect(0, 400, screen_width, screen_height // 2)
pygame.draw.rect(screen, grass_color, grass_rect)

# Set the Colors
house_color = (255, 200, 150)
roof_color = (255, 100, 50)
window_color = (255, 255, 255)
chimney_color = (100, 100, 100)
flower1_color = (255, 0, 0)
flower2_color = (0, 255, 0)
flower3_color = (0, 0, 255)
stem_color = (0, 150, 0)

# Draw the walls
house_width = 400
house_height = 300
house_x = screen_width // 2 - house_width // 2
house_y = screen_height - house_height - 50
pygame.draw.rect(screen, house_color, (house_x, house_y, house_width, house_height))

# Draw the door
door_color = (150, 100, 50)
door_width = 70
door_height = 120
door_x = house_x + house_width // 2 - door_width // 2
door_y = house_y + house_height - door_height
pygame.draw.rect(screen, door_color, (door_x, door_y, door_width, door_height))

# Draw the roof
roof_width = house_width + 50
roof_height = 150
roof_x = house_x - (roof_width - house_width) // 2
roof_y = house_y - roof_height + 50
pygame.draw.polygon(screen, roof_color, ((roof_x, roof_y + roof_height), (roof_x + roof_width, roof_y + roof_height), (house_x + house_width, house_y), (house_x, house_y)))

# Draw the chimney
chimney_width = 40
chimney_height = 60
chimney_x = roof_x + roof_width - 100
chimney_y = roof_y + roof_height // 2 - chimney_height // 2 + 20
pygame.draw.rect(screen, chimney_color, (chimney_x, chimney_y, chimney_width, chimney_height))

# Draw the windows
window_width = 50
window_height = 50
window_x1 = house_x + house_width // 4 - window_width // 2
window_x2 = house_x + 3 * house_width // 4 - window_width // 2
window_y = house_y + (house_height - (door_height + window_height)) // 2
pygame.draw.rect(screen, window_color, (window_x1, window_y, window_width, window_height))
pygame.draw.rect(screen, window_color, (window_x2, window_y, window_width, window_height))

# Draw the flowers
flower_width = 20
flower_height = 20
flower_x1 = door_x - flower_width
flower_x2 = door_x + door_width
flower_x3 = door_x + door_width + 60
flower_y = door_y + door_height - 40
pygame.draw.ellipse(screen, flower1_color, (flower_x1, flower_y, flower_width, flower_height))
pygame.draw.ellipse(screen, flower2_color, (flower_x2, flower_y, flower_width, flower_height))
pygame.draw.ellipse(screen, flower3_color, (flower_x3, flower_y, flower_width, flower_height))

# Draw the stems
stem_width = 5
stem_x1 = flower_x1 + flower_width // 2 - stem_width // 2
stem_x2 = flower_x2 + flower_width // 2 - stem_width // 2
stem_x3 = flower_x3 + flower_width // 2 - stem_width // 2

stem_y1 = flower_y + flower_height
stem_y2 = flower_y + flower_height
stem_y3 = flower_y + flower_height
stem_height = 80
pygame.draw.rect(screen, stem_color, (stem_x1, stem_y1, stem_width, stem_height))
pygame.draw.rect(screen, stem_color, (stem_x2, stem_y2, stem_width, stem_height))
pygame.draw.rect(screen, stem_color, (stem_x3, stem_y2, stem_width, stem_height))


# Draw the picket fence
picket_color = (255, 255, 255)
picket_width = 20
picket_height = 80
picket_gap = 10
picket_count = 5


#Draw the fence posts
fence_x1 = house_x - 30
fence_x2 = fence_x1 - picket_width - 10
fence_x3 = fence_x2 - picket_width - 10
fence_x4 = fence_x3 - picket_width - 10
fence_x5 = fence_x4 - picket_width - 10
fence_y = house_y + house_height - picket_height
pygame.draw.rect(screen, picket_color, (fence_x1, fence_y, picket_width, picket_height))
pygame.draw.rect(screen, picket_color, (fence_x2, fence_y, picket_width, picket_height))
pygame.draw.rect(screen, picket_color, (fence_x3, fence_y, picket_width, picket_height))
pygame.draw.rect(screen, picket_color, (fence_x4, fence_y, picket_width, picket_height))
pygame.draw.rect(screen, picket_color, (fence_x5, fence_y, picket_width, picket_height))

# Draw the pointy tops
fence_top_height = 20
fence_top_width = picket_width
pygame.draw.polygon(screen, picket_color, [(fence_x1, fence_y), (fence_x1, fence_y - fence_top_height), (fence_x1 + fence_top_width, fence_y)])
pygame.draw.polygon(screen, picket_color, [(fence_x2, fence_y), (fence_x2, fence_y - fence_top_height), (fence_x2 + fence_top_width, fence_y)])
pygame.draw.polygon(screen, picket_color, [(fence_x3, fence_y), (fence_x3, fence_y - fence_top_height), (fence_x3 + fence_top_width, fence_y)])
pygame.draw.polygon(screen, picket_color, [(fence_x4, fence_y), (fence_x4, fence_y - fence_top_height), (fence_x4 + fence_top_width, fence_y)])
pygame.draw.polygon(screen, picket_color, [(fence_x5, fence_y), (fence_x5, fence_y - fence_top_height), (fence_x5 + fence_top_width, fence_y)])


# Update the screen
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
