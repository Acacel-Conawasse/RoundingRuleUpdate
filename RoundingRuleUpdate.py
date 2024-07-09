#Chrome Lenovo Split Screen Bottom 
#Input file contains the list of Workrules to be searched for. 
import pyautogui
import time

# Define the actions
def perform_actions(line):
    # Click on Mouse Coordinate 3608,563
    pyautogui.click(x=3608, y=563)
    time.sleep(1)
    
    # Press Ctrl+A and Backspace
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.press('backspace')
    time.sleep(0.5)
    
    # Write Line
    pyautogui.typewrite(line)
    time.sleep(1)
    
    # Press 1 tab and Enter
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    
    # Click on Coordinate 3505,612
    pyautogui.click(x=3505, y=612)
    time.sleep(1)
    
    # Click on 3681,527
    pyautogui.click(x=3681, y=527)
    time.sleep(1.7)
    # Click on Mouse 3839,622
    pyautogui.click(x=3839, y=622)  
    time.sleep(.3)
    pyautogui.click(x=3839, y=622)
    time.sleep(1)
    # Write date ("07/01/2024")
    pyautogui.typewrite("06/30/2024")
    time.sleep(1)
    
    # Press 4 tabs
    for _ in range(4):
        pyautogui.press('tab')
        time.sleep(0.0005)
    
    # Write JHM
    pyautogui.typewrite("JHM")
    time.sleep(1)
    
    # Print statements
    print("How does the commander look")
    print("Fine Sir!")
    time.sleep(1)
    pyautogui.click(x=3628, y=506)
    time.sleep(1)

# Read lines from input.txt and perform actions for each line
with open("input.txt", "r") as file:
    for line in file:
        perform_actions(line.strip())
        time.sleep(2)  # Add a delay between actions for each line

print("Script completed.")
