
from PIL import Image, ImageGrab
import numpy as np
import cv2 as cv
import time
from threading import Thread


class MainAgent:
    def __init__(self) -> None:
        self.agents = []
        self.movement_thread = None

        self.cur_img = None     #BGR Image
        self.cur_imgHSV = None  #HSV Image


def update_screen(agent):

    t0 = time.time()
    while True:
        agent.cur_img = ImageGrab.grab()       #takes snapshot of desktop
        agent.cur_img = np.array(agent.cur_img)   #store image as numpy array
        agent.cur_img = cv.cvtColor(agent.cur_img, cv.COLOR_RGB2BGR)    #OpenCV uses BGR instead of RGB
        agent.cur_imgHSV = cv.cvtColor(agent.cur_img, cv.COLOR_BGR2HSV) #Store a HSV Image additionally to the BGR Image

        cv.imshow("Computer Vision", agent.cur_img)
        key = cv.waitKey(1)     #0 as argument would be holding until I press a new key, any other number is in ms
        if key == ord('q'):      #if the q-key is pressed the loop will break
            break
        ex_time = time.time() - t0
        print("FPS: " + str(1 / ex_time))
        t0 = time.time()

def print_menu():
    print("Enter a command:")
    print("\tS\tStart the main agent.")
    print("\tF\tStart the movement agent.")
    print("\tQ\tQuit.")

if __name__ == "__main__":
    main_agent = MainAgent()

    print_menu()
    while True:
        user_input = input()
        user_input = str.lower(user_input).strip()

        if user_input == "s":
            update_screen_thread = Thread(target=update_screen, args=(main_agent,), name="update screen thread", daemon=True)
            update_screen_thread.start()
            print("Thread started")
        if user_input == "f":
            pass
        if user_input == "q":
            print("Exiting application")
            break
        else:
            print("Input error.")
            print_menu()

    print("Done.")


