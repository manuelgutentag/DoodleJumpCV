

import cv2 as cv
import numpy as np
import pyautogui

class MovementAgent:
    def __init__(self, main_agent) -> None:
        self.main_agent = main_agent
        self.doodle_target = cv.imread("/home/manuel/PycharmProjects/DoodleJumpCV/Scripts/movement/assets/doodle_left.png")
        self.fishing_thread = None

    def find_doodle(self):
        if self.main_agent.cur_img is not None:
            cur_img = self.main_agent.cur_img
            print("finding doodle..")
            doodle_location = cv.matchTemplate(cur_img, self.doodle_target,cv.TM_CCOEFF_NORMED)
            doodle_loc_arr = np.array(doodle_location)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(doodle_loc_arr)
            print(max_loc)




        #cv.imshow("Match Template", doodle_loc_arr)
        #cv.waitKey(0)



    def find_platforms(self):
        pass

    def move_doodle(self):
        pass
        #left pyautogui.keydown("a")
        #pyautogui.keyup("a")
        #right pyautogui.keydown("d")
        #pyautogui.keyup("d")


    def run(self):
        self.find_doodle()




