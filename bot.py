# Import necessary libraries
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import pydirectinput

# Function to simulate a safe mouse click using pydirectinput
def safety_click(x, y):
    pydirectinput.moveTo(x, y)
    time.sleep(random.uniform(0.01, 0.05))
    pydirectinput.click()

# Function to simulate a double mouse click at given coordinates
def double_click(x, y):
    safety_click(x, y)
    time.sleep(random.uniform(0.02, 0.025))
    safety_click(x, y)

# Function to get a counter value
def get_counter():
    return 150

# Function to check for air bubbles on the screen
def check_air_bubbles_on_screen():
    s = pyautogui.screenshot()
    colorcode = (68, 252, 234)  # Blue bubbles
    for x in range(770, 1160):
        for y in range(350, 730):
            tempvar = all(
                s.getpixel((x + x2, y)) == colorcode for x2 in range(5)
            )
            if tempvar:
                print(f"Air bubbles detected at ({x}, {y})")
                return True
    return False

# Function to simulate a random throw click
def click_random_throw():
    x, y = random.randint(960, 970), random.randint(520, 530)
    safety_click(x, y)

# Function to simulate a double random throw click
def double_click_random_throw():
    click_random_throw()
    time.sleep(random.uniform(0.02, 0.025))
    click_random_throw()

# Initialize counters and flags
counter = 0
fish_counter = 0
fish_found = False

# Main loop to check for fish and bubbles until 'q' is pressed
while not keyboard.is_pressed('q'):
    # Check if fish is found
    pixel1 = pyautogui.pixel(847, 820)
    pixel2 = pyautogui.pixel(860, 800)
    #print(f"Pixel1 at (847,820): {pixel1}, Pixel2 at (860,800): {pixel2}")

    if pixel1[0] == 255 or pixel2[0] == 255:
        print("Fish detected via pixel check")
        click_random_throw()
        counter = get_counter()
        fish_found = True

    # Increase fish counter if found
    if fish_found:
        pixel3 = pyautogui.pixel(830, 800)
        print(f"Checking pixel at (830,800): {pixel3}")
        if pixel3 != (83, 250, 83):
            fish_counter += 1
            print('Fish caught: ' + str(fish_counter))
            fish_found = False
            double_click_random_throw()

    # If fish not found, check for air bubbles
    if not fish_found and check_air_bubbles_on_screen():
        print("Fish detected via air bubbles")
        click_random_throw()
        counter = get_counter()
        fish_found = True

    if counter == 0:
        double_click_random_throw()
        counter = get_counter()

    # If inventory is full, sell
    if fish_counter == 2000:
        print('Inventory full, selling...')
        exit()

    counter -= 1
    time.sleep(0.025)
