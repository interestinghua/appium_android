import unittest
from appium import webdriver
import desired_capabilities

# the emulator is sometimes slow and needs time to think
# unittest.TestCase
SLEEPY_TIME = 1


class AndroidAJHTests(unittest.TestCase):

    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('AiJiHui_V4.29.0_[official].apk')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_swipe_up(self, t=500, n=1):
        size = self.get_window_size()
        x1 = size['width'] * 0.5
        y1 = size['height'] * 0.75
        y2 = size['height'] * 0.25

        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def test_swipe_down(self, t=500, n=1):
        size = self.get_window_size()
        x1 = size['width'] * 0.5
        y1 = size['height'] * 0.25
        y2 = size['height'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def test_swip_left(self, t=500, n=1):
        size = self.get_window_size()
        x1 = size['width'] * 0.75
        y1 = size['height'] * 0.5
        x2 = size['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def test_swip_right(self, t=500, n=1):
        size = self.get_window_size()
        x1 = size['width'] * 0.25
        y1 = size['height'] * 0.5
        x2 = size['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def get_window_size(self):
        size = self.driver.get_window_size()

        return size

    def get_element_location(self, element_id):
        element = self.driver.find_element_by_accessibility_id(element_id)

        left = element.location['x']
        top = element.location['y']
        right = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height']

        return {left, top, right, bottom}

    def test_start_activity(self, activity):
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

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    print("run")

    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidAJHTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
