import time

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


class MovementAgent:
    def __init__(self, main_agent) -> None:
        self.main_agent = main_agent
        self.doodle_template = cv.imread("/home/manuel/PycharmProjects/DoodleJumpCV/Scripts/movement/assets/doodle_template.png")
        self.platform_template = cv.imread("/home/manuel/PycharmProjects/DoodleJumpCV/Scripts/movement/assets/platform_template.png")
        self.fishing_thread = None

        self.lock = main_agent.lock

    def find_doodle(self):
        if self.main_agent.cur_img is not None:
            print("finding doodle..")
            doodle_res = cv.matchTemplate(self.main_agent.cur_img, self.doodle_template,cv.TM_CCOEFF_NORMED)
            doodle_loc_arr = np.array(doodle_res)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(doodle_loc_arr)
            print(max_loc)

            cv.rectangle(self.main_agent.cur_img, max_loc, (max_loc[0] + 230, max_loc[1] + 200), (255,0,0), 2)

    def find_platforms(self):
        if self.main_agent.cur_img is not None:
            print("finding platforms..")
            platform_res = cv.matchTemplate(self.main_agent.cur_img, self.platform_template,cv.TM_CCOEFF_NORMED)
            w = 224
            h = 58
            threshold = 0.8
            loc = np.where(platform_res >= threshold)
            print("new call")
            if loc[0].size > 0:
                for pt in zip(*loc[::-1]):
                    print("pt", pt)
                    cv.rectangle(self.main_agent.cur_img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)
            else:
                print("No matches found above the threshold.")


            self.main_agent.cur_img = cv.cvtColor(self.main_agent.cur_img, cv.COLOR_BGR2RGB)    #OpenCV uses BGR instead of RGB


            #why does imshow not work?
            #cv.imshow("platforms detected", self.main_agent.cur_img)
            plt.imshow(self.main_agent.cur_img)
            plt.show()







    def move_doodle(self):
        pass
        #left pyautogui.keydown("a")
        #pyautogui.keyup("a")
        #right pyautogui.keydown("d")
        #pyautogui.keyup("d")


    def run(self):
        while True:
            time.sleep(5)
            with self.lock:   # Thread verschließen (kein Zugang auf den screenshot cur_img von anderen Threads)
                self.find_doodle()
                self.find_platforms()




