
from PIL import Image, ImageGrab
import numpy as np
import cv2 as cv
import time
import threading
from threading import Thread
from movement.movement_agent import MovementAgent
import pyautogui

class MainAgent:
    def __init__(self) -> None:
        self.agents = []
        self.movement_thread = None

        self.cur_img = None     #BGR Image
        self.cur_imgHSV = None  #HSV Image

        self.lock = threading.Lock()   # Instantiierung von lock Objekt

        #boundaries für screenshot
        self.left = 3200
        self.top = 0
        self.width = 1350
        self.height = 2160


def update_screen(agent):

    t0 = time.time()
    while True:
        with main_agent.lock: # Thread locken
            # Capture the entire screen
            screenshot = pyautogui.screenshot()

            # Crop the screenshot to the defined region
            region = (agent.left, agent.top, agent.left + agent.width, agent.top + agent.height)
            captured_region = screenshot.crop(region)

            agent.cur_img = captured_region #takes snapshot of desktop
            agent.cur_img = np.array(agent.cur_img)   #store image as numpy array
            agent.cur_img = cv.cvtColor(agent.cur_img, cv.COLOR_RGB2BGR)    #OpenCV uses BGR instead of RGB
            agent.cur_imgHSV = cv.cvtColor(agent.cur_img, cv.COLOR_BGR2HSV) #Store an HSV Image additionally to the BGR Image

        #cv.imshow("Computer Vision", agent.cur_img)
        key = cv.waitKey(1)     #0 as argument would be holding until I press a new key, any other number is in ms
        if key == ord('q'):      #if the q-key is pressed the loop will break
            break
        ex_time = time.time() - t0
       # print("FPS: " + str(1 / ex_time))
        t0 = time.time()

if __name__ == "__main__":
    main_agent = MainAgent()

    update_screen_thread = Thread(target=update_screen, args=(main_agent,), name="update screen thread", daemon=True)
    update_screen_thread.start()

    movement_agent = MovementAgent(main_agent)
    movement_agent.run()



