# -*- coding: UTF-8 -*-
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from test.functional.ajh_android import desired_capabilities

# the emulator is sometimes slow and needs time to think
# unittest.TestCase

SLEEPY_TIME = 2


class AndroidAJHTests(unittest.TestCase):

    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('AiJiHui_V4.29.0_[official].apk')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_create_order(self):

        action = TouchAction(self.driver)

        package = self.driver.current_package
        self.assertEquals('aihuishou.aijihui', package)

        activity = self.driver.current_activity
        print('activity = ', activity)

        if activity == '.activity.login.LaunchScreenActivity':
            sleep(5)

        user_text = self.driver.find_element_by_id('aihuishou.aijihui:id/login_activity_et_username')
        print('user_text = ', user_text)
        self.driver.set_value(user_text, '13000000006')

        psd_text = self.driver.find_element_by_id('aihuishou.aijihui:id/login_activity_et_password')
        print('psd_text = ', psd_text)
        self.driver.set_value(psd_text, '304021')

        psd_save = self.driver.find_element_by_id('aihuishou.aijihui:id/login_activity_cb_save_password')
        print('psd_save = ', psd_save)
        action.tap(psd_save).perform()

        login_btn = self.driver.find_element_by_id('aihuishou.aijihui:id/login_btn')
        action.tap(login_btn).perform()
        sleep(10)

        activity = self.driver.current_activity
        if activity == '.activity.homepage.HomeTabActivity':
            sleep(7)

        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']

        x = int(x * 0.5)
        y = int(y * 0.5)

        # container_framlayout = self.driver.find_element_by_id('aihuishou.aijihui:id/dialogplus_content_container')
        # if container_framlayout is not None:
        #     # action.tap(container_framlayout).perform()
        #     # 取消弹出层
        #     print '点击弹层 x,y =', x, y
        #     self.driver.tap([(x, y)])
        #     sleep(1)

        print('点击弹层 x,y =', x, y)
        self.driver.tap([(x, y)])
        sleep(1)

        # 点击下单
        self.driver.tap([(700, 2626)])
        sleep(1)

        # 点击创建订单
        self.driver.tap([(200, 2100)])
        sleep(1)

        # 点击手动下单
        create_order_manual = self.driver.find_element_by_id('aihuishou.aijihui:id/manual_create_iv_id')
        action.tap(create_order_manual).perform()
        sleep(3)

        activity = self.driver.current_activity
        print('activity: ', activity)

        # root = self.driver.find_elements_by_class_name('android.widget.FrameLayout')
        # print 'root ', root

        # category = self.driver.find_element_by_id('aihuishou.aijihui:id/text')
        # print 'category ', category

        brands = self.driver.find_elements_by_id('aihuishou.aijihui:id/typename')
        print('brands ', brands)
        # sometimes numbers shift
        for el in brands:
            text = el.text
            if text == '苹果':
                action.tap(el).perform()
            elif text == 'OPPO':
                pass

        # 点击其他品牌
        # self.driver.tap([(500, 500)])
        # sleep(1)

        # 点击苹果
        self.driver.tap([(500, 700)])
        sleep(1)

        # mobile_brand = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").text("苹果")')
        # mobile_brand = self.driver.find_element_by_xpath('//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView')
        # mobile_brand = self.driver.find_element_by_accessibility_id("苹果")
        # mobile_brand = self.driver.find_element_by_class_name("android.widget.TextView")
        # print '点击了 苹果手机', mobile_brand
        # action.tap(mobile_brand).perform()
        # sleep(2)

        # mobile_model = self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().className("android.widget.TextView").text("苹果 iPhone 7 Plus")')
        # print '点击了 ', mobile_model
        # action.tap(mobile_model).perform()
        # sleep(2)

        # 选择7p
        self.driver.tap([(800, 700)])
        sleep(2)

        # 选择手动下单原因 触摸失灵
        self.driver.tap([(600, 1100)])
        sleep(2)

        # 手动选择属性
        # prop01 = self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().className("android.widget.TextView").text("其他")')
        # print '点击了 ', prop01
        # action.tap(prop01).perform()
        #
        # prop02 = self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().className("android.widget.TextView").text("电池老化")')
        # print '点击了 ', prop02
        # action.tap(prop02).perform()
        #
        # prop03 = self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().className("android.widget.TextView").text("拍摄功能正常")')
        # print '点击了 ', prop03
        # action.tap(prop03).perform()

        props = self.driver.find_elements_by_class_name("android.widget.TextView")
        print('属性 ', props)
        for el in props:
            text = el.text
            print('prop text ', text)
            if text == '苹果':
                action.tap(el).perform()
            elif text == 'OPPO':
                pass

        # action.tap(mobile_brand).perform()
        # sleep(2)

    def swipe_up(self, t=500, n=1):
        size = self.get_window_size()
        x1 = size['width'] * 0.5
        y1 = size['height'] * 0.75
        y2 = size['height'] * 0.25

        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, t=500, n=1):
        size = self.get_window_size()
        x1 = size['width'] * 0.5
        y1 = size['height'] * 0.25
        y2 = size['height'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swip_left(self, t=500, n=1):
        size = self.get_window_size()
        x1 = size['width'] * 0.75
        y1 = size['height'] * 0.5
        x2 = size['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swip_right(self, t=500, n=1):
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

        return left, top, right, bottom

    def start_activity(self, activity):
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
