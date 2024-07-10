import pygame
import sys
import os
import ctypes
import subprocess
import requests
import shutil
import tkinter as tk
from tkinter import messagebox
import pyperclip
import zipfile

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
wave_fix_2_text = font.render('Wave Fix 2', True, WHITE)
wave_fix_3_text = font.render('Wave Fix 3', True, WHITE)
wave_fix_4_text = font.render('Wave Fix 4', True, WHITE)

# Get text dimensions
close_text_width, close_text_height = close_text.get_size()
rate_text_width, rate_text_height = rate_text.get_size()
fix_text_width, fix_text_height = fix_text.get_size()
wave_fix_2_text_width, wave_fix_2_text_height = wave_fix_2_text.get_size()
wave_fix_3_text_width, wave_fix_3_text_height = wave_fix_3_text.get_size()
wave_fix_4_text_width, wave_fix_4_text_height = wave_fix_4_text.get_size()

# Define button padding
padding_x = 20
padding_y = 10

# Define button dimensions and positions based on text size and padding
close_button_width = close_text_width + padding_x * 2
close_button_height = close_text_height + padding_y * 2
close_button_x = screen_width - close_button_width - 10  # 10 pixels from the right edge
close_button_y = 10  # 10 pixels from the top edge

# Calculate button positions for "Rate Wave", "Fix Wave", "Wave Fix 2", "Wave Fix 3", and "Wave Fix 4"
image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Textures', 'WaveRateButtonExstra.jpg')
try:
    button_image = pygame.image.load(image_path)
    image_width, image_height = button_image.get_size()

    # Calculate positions to form a square layout
    button_margin = 20
    button_y = (screen_height - 2 * image_height - button_margin) // 2

    rate_button_x = (screen_width - 2 * image_width - button_margin) // 2
    fix_button_x = rate_button_x + image_width + button_margin
    wave_fix_2_button_x = rate_button_x
    wave_fix_3_button_x = fix_button_x
    wave_fix_4_button_x = rate_button_x

except FileNotFoundError:
    print(f"Error: File '{image_path}' not found")
    pygame.quit()
    sys.exit()

# Draw the Close button
close_button_rect = pygame.Rect(close_button_x, close_button_y, close_button_width, close_button_height)
pygame.draw.rect(screen, RED, close_button_rect)
close_text_rect = close_text.get_rect(center=close_button_rect.center)
screen.blit(close_text, close_text_rect)

# Draw the Rate Wave button
rate_button_rect = pygame.Rect(rate_button_x, button_y, image_width, image_height)
screen.blit(button_image, rate_button_rect)
rate_text_rect = rate_text.get_rect(center=rate_button_rect.center)
screen.blit(rate_text, rate_text_rect)

# Draw the Fix Wave button
fix_button_rect = pygame.Rect(fix_button_x, button_y, image_width, image_height)
screen.blit(button_image, fix_button_rect)
fix_text_rect = fix_text.get_rect(center=fix_button_rect.center)
screen.blit(fix_text, fix_text_rect)

# Draw the Wave Fix 2 button
wave_fix_2_button_rect = pygame.Rect(wave_fix_2_button_x, button_y + image_height + button_margin, image_width, image_height)
screen.blit(button_image, wave_fix_2_button_rect)
wave_fix_2_text_rect = wave_fix_2_text.get_rect(center=wave_fix_2_button_rect.center)
screen.blit(wave_fix_2_text, wave_fix_2_text_rect)

# Draw the Wave Fix 3 button
wave_fix_3_button_rect = pygame.Rect(wave_fix_3_button_x, button_y + image_height + button_margin, image_width, image_height)
screen.blit(button_image, wave_fix_3_button_rect)
wave_fix_3_text_rect = wave_fix_3_text.get_rect(center=wave_fix_3_button_rect.center)
screen.blit(wave_fix_3_text, wave_fix_3_text_rect)

# Draw the Wave Fix 4 button
wave_fix_4_button_rect = pygame.Rect(wave_fix_4_button_x, button_y + 2 * (image_height + button_margin), image_width, image_height)
screen.blit(button_image, wave_fix_4_button_rect)
wave_fix_4_text_rect = wave_fix_4_text.get_rect(center=wave_fix_4_button_rect.center)
screen.blit(wave_fix_4_text, wave_fix_4_text_rect)

pygame.display.flip()

# Global variable for script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Function to open Node.js batch file as administrator
def open_node_installer():
    # Construct the path to the Node.js batch file
    bat_filename = 'Node js.bat'
    bat_path = os.path.join(script_dir, 'Wave Fixer Folder Files', bat_filename)
    
    if not os.path.exists(bat_path):
        print(f"Error: Batch file '{bat_filename}' not found at '{bat_path}'")
        return
    
    try:
        # Invoke UAC prompt for administrative access
        ctypes.windll.shell32.ShellExecuteW(None, "runas", bat_path, None, None, 1)
    except Exception as e:
        print(f"Error executing batch file: {e}")
        # Optionally, show an error message
        messagebox.showerror('Error', f"Error executing batch file: {e}")

# Function to open batch file as administrator using UAC prompt
def run_as_admin(bat_filename):
    global script_dir  # Use the global script_dir variable
    
    # Construct the path to the batch file relative to the script's directory
    bat_path = os.path.join(script_dir, 'Wave Fixer Folder Files', bat_filename)
    
    if not os.path.exists(bat_path):
        print(f"Error: Batch file '{bat_filename}' not found at '{bat_path}'")
        return
    
    # Create a confirmation dialog
    confirm = messagebox.askquestion('Confirm Action', f'Are you sure you want to open {bat_filename}?', icon='warning')
    if confirm == 'yes':
        try:
            # Invoke UAC prompt for administrative access
            ctypes.windll.shell32.ShellExecuteW(None, "runas", bat_path, None, None, 1)
        except Exception as e:
            print(f"Error executing batch file: {e}")
            # Optionally, show an error message
            messagebox.showerror('Error', f"Error executing batch file: {e}")
    else:
        print("Operation canceled.")

# Function to extract specified ZIP files to %localappdata%\Wave
def extract_zip_files():
    target_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'Wave')
    zip_files = ['workspace.zip', 'locales.zip', 'bin.zip', 'autoexec.zip']
    zip_dir = os.path.join(script_dir, 'Wave Fixer Folder Files')

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for zip_file in zip_files:
        zip_path = os.path.join(zip_dir, zip_file)
        if os.path.exists(zip_path):
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(target_dir)
                print(f"Extracted {zip_file} to {target_dir}")
            except zipfile.BadZipFile:
                print(f"Error: Bad ZIP file {zip_file}")
            except Exception as e:
                print(f"Error extracting {zip_file}: {e}")
        else:
            print(f"Error: ZIP file '{zip_file}' not found at '{zip_path}'")

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
                    run_as_admin('Wave Install Fixer.bat')  # Call function to run Wave Install Fixer.bat as admin
                elif wave_fix_2_button_rect.collidepoint(event.pos):
                    open_node_installer()  # Call function to open Node.js batch file as admin
                elif wave_fix_3_button_rect.collidepoint(event.pos):
                    run_as_admin('Wave Support Tool.bat')  # Call function to run Wave Support Tool.bat as admin
                elif wave_fix_4_button_rect.collidepoint(event.pos):
                    extract_zip_files()  # Call function to extract ZIP files

# Quit Pygame
pygame.quit()
sys.exit()
