import pygame
import sys
import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# Initialize Pygame
pygame.init()

# Get screen dimensions
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Create a fullscreen window
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Fullscreen Black Window')

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Set the window color to black
screen.fill(BLACK)

# Define font and render text
font = pygame.font.Font(None, 36)
close_text = font.render('Close', True, WHITE)
rate_text = font.render('Rate Wave', True, WHITE)
fix_text = font.render('Fix Wave', True, WHITE)

# Get text dimensions
close_text_width, close_text_height = close_text.get_size()
rate_text_width, rate_text_height = rate_text.get_size()
fix_text_width, fix_text_height = fix_text.get_size()

# Define button padding
padding_x = 20
padding_y = 10

# Define button dimensions and positions based on text size and padding
close_button_width = close_text_width + padding_x * 2
close_button_height = close_text_height + padding_y * 2
close_button_x = screen_width - close_button_width - 10  # 10 pixels from the right edge
close_button_y = 10  # 10 pixels from the top edge

# Construct the image path relative to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'Textures', 'WaveRateButtonExstra.jpg')

# Load image
try:
    rate_button_image = pygame.image.load(image_path)
    fix_button_image = pygame.image.load(image_path)
except FileNotFoundError:
    print(f"Error: File '{image_path}' not found")
    pygame.quit()
    sys.exit()

image_width, image_height = rate_button_image.get_size()

# Calculate button positions
rate_button_x = (screen_width // 2) - (image_width + 50)  # Offset for spacing
rate_button_y = (screen_height // 2) - (image_height // 2)

fix_button_x = (screen_width // 2) + 50  # Offset for spacing
fix_button_y = rate_button_y

# Draw the Close button
close_button_rect = pygame.Rect(close_button_x, close_button_y, close_button_width, close_button_height)
pygame.draw.rect(screen, RED, close_button_rect)
close_text_rect = close_text.get_rect(center=close_button_rect.center)
screen.blit(close_text, close_text_rect)

# Draw the Rate Wave button
rate_button_rect = pygame.Rect(rate_button_x, rate_button_y, image_width, image_height)
screen.blit(rate_button_image, rate_button_rect)
rate_text_rect = rate_text.get_rect(center=rate_button_rect.center)
screen.blit(rate_text, rate_text_rect)

# Draw the Fix Wave button
fix_button_rect = pygame.Rect(fix_button_x, fix_button_y, image_width, image_height)
screen.blit(fix_button_image, fix_button_rect)
fix_text_rect = fix_text.get_rect(center=fix_button_rect.center)
screen.blit(fix_text, fix_text_rect)

pygame.display.flip()

# Function to run batch file as administrator
def run_as_admin():
    bat_path = os.path.join(script_dir, 'Wave Fixer Folder Files', 'Wave Install Fixer.bat')
    if not os.path.exists(bat_path):
        print(f"Error: Batch file '{bat_path}' not found")
        return
    
    # Create a confirmation dialog
    confirm = messagebox.askquestion('Confirm Action', 'Are you sure you want to open Wave Install Fixer?', icon='warning')
    if confirm == 'yes':
        # Run batch file as administrator
        subprocess.Popen([bat_path], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        print("Operation canceled.")

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if close_button_rect.collidepoint(event.pos):
                    running = False
                elif rate_button_rect.collidepoint(event.pos):
                    print("Rate Wave button clicked")
                elif fix_button_rect.collidepoint(event.pos):
                    run_as_admin()  # Call function to run batch file as admin

# Quit Pygame
pygame.quit()
sys.exit()
