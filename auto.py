import pyautogui 
import time

# FAIL-SAFE 
pyautogui.FAILSAFE = True

time.sleep(3)
counter = 0
while counter < 1:
  # FULL NAME
  pyautogui.moveTo(327,1120)
  pyautogui.moveTo(607,1008)
  pyautogui.click(clicks=3)
  pyautogui.hotkey('ctrl', 'c')
  pyautogui.moveTo(2011,574)
  pyautogui.click(clicks=1)
  pyautogui.hotkey('ctrl', 'v')
  time.sleep(0.5)

  # EMAIL
  pyautogui.moveTo(443,1112)
  pyautogui.moveTo(607,1008)
  pyautogui.click(clicks=3)
  pyautogui.hotkey('ctrl', 'c')
  pyautogui.moveTo(1953,614)
  pyautogui.click(clicks=1)
  pyautogui.hotkey('ctrl', 'v')
  time.sleep(0.5)

  # BIRTHDATE
  pyautogui.moveTo(567,1110)
  pyautogui.moveTo(607,1008)
  pyautogui.click(clicks=3)
  pyautogui.hotkey('ctrl', 'c')
  pyautogui.moveTo(1959,666)
  pyautogui.click(clicks=1)
  pyautogui.hotkey('ctrl', 'v')
  time.sleep(0.5)

  #ADDRESS
  pyautogui.moveTo(691,1113)
  pyautogui.moveTo(607,1008)
  pyautogui.click(clicks=3)
  pyautogui.hotkey('ctrl', 'c')
  pyautogui.moveTo(1970,699)
  pyautogui.click(clicks=1)
  pyautogui.hotkey('ctrl', 'v')
  time.sleep(0.5)

  # PHONE
  pyautogui.moveTo(810,1114)
  pyautogui.moveTo(607,1008)
  pyautogui.click(clicks=3)
  pyautogui.hotkey('ctrl', 'c')
  pyautogui.moveTo(1996,743)
  pyautogui.click(clicks=1)
  pyautogui.hotkey('ctrl', 'v')
  time.sleep(1)
  pyautogui.click(clicks=1)
  time.sleep(0.5)

  # PASSWORD
  pyautogui.moveTo(920,1114)
  pyautogui.moveTo(607,1008)
  pyautogui.click(clicks=3)
  pyautogui.hotkey('ctrl', 'c')
  pyautogui.moveTo(1982,784)
  pyautogui.click(clicks=1)
  pyautogui.hotkey('ctrl', 'v')
  time.sleep(0.5)

  # CLICK THE NEW BUTTON ON EXCEL
  pyautogui.moveTo(2191,607)
  pyautogui.click(clicks=1)
  time.sleep(0.5)
  pyautogui.moveTo(130,80)
  pyautogui.click(clicks=1)
  time.sleep(0.5)
