# Import necessary libraries
import pyautogui
import time
import keyboard
import random
import pydirectinput
import sys
import traceback

# Function to simulate a safe mouse click using pydirectinput
def safety_click(x, y):
    pydirectinput.moveTo(x, y)
    time.sleep(random.uniform(0.005, 0.01))  # Reduced sleep time for faster clicks
    pydirectinput.click()

# Function to simulate a double mouse click at given coordinates
def double_click(x, y):
    safety_click(x, y)
    time.sleep(random.uniform(0.01, 0.015))  # Reduced sleep time
    safety_click(x, y)

# Function to get a counter value
def get_counter():
    return 100  # Reduced counter value for quicker actions

# Function to check for air bubbles on the screen
def check_air_bubbles_on_screen():
    try:
        s = pyautogui.screenshot()
        colorcode = (68, 252, 234)  # Blue bubbles
        for x in range(770, 1160, 5):  # Step increased for efficiency
            for y in range(350, 730, 5):
                tempvar = all(
                    s.getpixel((x + x2, y)) == colorcode for x2 in range(5)
                )
                if tempvar:
                    print(f"Air bubbles detected at ({x}, {y})")
                    return True
        return False
    except Exception as e:
        print("Error in check_air_bubbles_on_screen:", e)
        return False

# Function to simulate a random throw click
def click_random_throw():
    x, y = random.randint(960, 970), random.randint(520, 530)
    safety_click(x, y)

# Function to simulate a double random throw click
def double_click_random_throw():
    click_random_throw()
    time.sleep(random.uniform(0.01, 0.015))  # Reduced sleep time
    click_random_throw()

# Function to sell items when inventory is full
def sell_items():
    backpack_color = (106, 155, 106)  # Hex color 6A9B6A
    sell_button_color = (106, 155, 106)
    confirm_button_color = (106, 155, 106)
    yes_button_color = (106, 155, 106)

    # Click on the backpack
    safety_click(1230, 1000)
    time.sleep(0.5)  # Wait for the backpack to open

    # Verify that the backpack is open
    try:
        pixel_backpack = pyautogui.pixel(1230, 1000)
        if pixel_backpack == backpack_color:
            print("Backpack opened successfully.")
        else:
            print("Failed to open backpack. Color mismatch:", pixel_backpack)
            return
    except Exception as e:
        print("Error verifying backpack opening:", e)
        return

    # Click on the sell button
    safety_click(1075, 330)
    time.sleep(0.2)

    # Verify sell button color
    try:
        pixel_sell = pyautogui.pixel(1075, 330)
        if pixel_sell == sell_button_color:
            print("Sell button clicked.")
        else:
            print("Sell button color mismatch:", pixel_sell)
            return
    except Exception as e:
        print("Error verifying sell button:", e)
        return

    # Click on the confirm button
    safety_click(1225, 420)
    time.sleep(0.2)

    # Verify confirm button color
    try:
        pixel_confirm = pyautogui.pixel(1225, 420)
        if pixel_confirm == confirm_button_color:
            print("Confirm button clicked.")
        else:
            print("Confirm button color mismatch:", pixel_confirm)
            return
    except Exception as e:
        print("Error verifying confirm button:", e)
        return

    # Click the yes button twice with slight delay
    safety_click(1225, 420)
    time.sleep(0.1)
    safety_click(1225, 420)
    time.sleep(0.1)

    # Optionally verify yes button color
    try:
        pixel_yes = pyautogui.pixel(1225, 420)
        if pixel_yes == yes_button_color:
            print("Yes button clicked twice.")
        else:
            print("Yes button color mismatch:", pixel_yes)
    except Exception as e:
        print("Error verifying yes button:", e)

    print("Items sold successfully.")

# Initialize counters and flags
counter = 0
fish_counter = 0
fish_found = False

# Main loop to check for fish and bubbles until 'q' is pressed
try:
    while not keyboard.is_pressed('q'):
        # Check if fish is found
        try:
            pixel1 = pyautogui.pixel(847, 820)
            pixel2 = pyautogui.pixel(860, 800)
            # Uncomment the next line for debugging
            # print(f"Pixel1 at (847,820): {pixel1}, Pixel2 at (860,800): {pixel2}")

            if pixel1[0] == 255 or pixel2[0] == 255:
                print("Fish detected via pixel check")
                click_random_throw()
                counter = get_counter()
                fish_found = True
        except Exception as e:
            print("Error while checking for fish pixels:", e)
            continue

        # Increase fish counter if found
        if fish_found:
            try:
                pixel3 = pyautogui.pixel(830, 800)
                # Uncomment the next line for debugging
                # print(f"Checking pixel at (830,800): {pixel3}")
                if pixel3 != (83, 250, 83):
                    fish_counter += 1
                    print('Fish caught: ' + str(fish_counter))
                    fish_found = False
                    double_click_random_throw()
            except Exception as e:
                print("Error while updating fish counter:", e)
                fish_found = False  # Reset fish_found to avoid getting stuck

        # If fish not found, check for air bubbles
        if not fish_found and check_air_bubbles_on_screen():
            print("Fish detected via air bubbles")
            click_random_throw()
            counter = get_counter()
            fish_found = True

        if counter <= 0:
            double_click_random_throw()
            counter = get_counter()

        # If inventory is full, sell
        if fish_counter >= 2000:
            print('Inventory full, selling...')
            sell_items()
            fish_counter = 0  # Reset fish counter after selling

        counter -= 1
        time.sleep(0.01)  # Reduced sleep time for faster loop iteration
except Exception as e:
    print("An error occurred in the main loop:", e)
    traceback.print_exc()
finally:
    print("Script terminated.")
