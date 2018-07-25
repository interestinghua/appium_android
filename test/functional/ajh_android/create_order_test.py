import unittest
from zipfile import ZipFile
import json
import os
import random
from time import sleep
from dateutil.parser import parse

from webdriver.applicationstate import ApplicationState
from selenium.common.exceptions import NoSuchElementException

from appium import webdriver
import desired_capabilities

# the emulator is sometimes slow and needs time to think
SLEEPY_TIME = 1


class AndroidAJHTests(unittest.TestCase):

    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def startActivity(self, activity):

        self.driver.start_activity('aihuishou.aijihui', activity)
        self.driver.press_keycode(3)
        self.driver.find_element_by_accessibility_id('create_tv_id')

        el = self.driver.find_element_by_class_name('android.widget.TextView')
        el.set_value('Testing')

        package = self.driver.current_package
        self.assertEquals('aihuishou.aijihui', package)

        activity = self.driver.current_activity
        self.assertEquals('.ApiDemos', activity)

    def shake(self):
        self.driver.shake()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
