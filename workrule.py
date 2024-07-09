import pyautogui
import pyperclip
import time

def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip().split('|') for line in lines]

def click_and_type(x, y, text):
    pyautogui.click(x, y)
    time.sleep(0.5)
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')

def perform_actions(data):
    for line in data:
        col0, col1, col2 = line
        
        # Step 1: Search for Work Rule
        pyautogui.click(1060, 377)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(.35)
        pyautogui.press('backspace')
        click_and_type(1060, 377, col0)
        pyautogui.press('tab')
        time.sleep(.35)
        pyautogui.press('enter')
        time.sleep(2)
        
        # Step 2: Select searched work rule
        pyautogui.click(1016, 411)
        time.sleep(.5)
        pyautogui.click(1190, 345)
        time.sleep(2.5)
        
        # Step 3: Enter Effective Date
        pyautogui.click(1329, 435)
        time.sleep(1)
        pyperclip.copy('07/14/2024')
        time.sleep(.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        
        # Step 4: Navigate and write col2
        for _ in range(4):
            pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.write(col2)
        
        # Step 5: Save and return
        pyautogui.click(1098, 330)
        time.sleep(2)
        
        log_message = f"{col0} completed\n"
        print(log_message.strip())
        with open('completed_log.txt', 'a') as log_file:
            log_file.write(log_message)
        print("---------------------------------------------------------------------------")
        time.sleep(1)

        
       
    

if __name__ == "__main__":
    data = read_input_file('input.txt')
    perform_actions(data)
