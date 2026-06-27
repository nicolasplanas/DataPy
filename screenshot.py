from   utils import config

import pygetwindow as gw
import pyautogui

windows    = gw.getActiveWindow(config.esst0596)

screenshot = pyautogui.screenshot(

    region=(

        windows.left,
        windows.top,
        windows.width,
        windows.height
        
    )

)