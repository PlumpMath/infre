import urllib.request
from selenium import webdriver
from time import sleep


class Infre:
    def __init__(self):
        self.driver = webdriver.PhantomJS('D://chromedriver.exe')
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(0, 0)
        pass

    def __enter__(self):
        pass

    def __exit__(self, **kwargs):
        self.driver.quit()

    def dispose(self):
        self.__exit__()

    def join(self, s_id, pw, name, gender, msg):
        print('join')
        self.driver.get('http://infre.kr/Account/join.php')
        f_id = self.driver.find_element_by_id('join_user_id')
        f_pw = self.driver.find_element_by_id('join_user_pw')
        f_name = self.driver.find_element_by_id('join_user_name')
        f_msg = self.driver.find_element_by_id('join_user_msg')

        f_id.clear()
        f_pw.clear()
        f_name.clear()
        f_msg.clear()

        f_id.send_keys(s_id)
        f_pw.send_keys(pw)
        f_name.send_keys(name)
        f_msg.send_keys(msg)

        if gender == 'M' or gender == 'm':
            self.driver.find_element_by_id('join_user_gender_M').click()
        else:
            self.driver.find_element_by_id('join_user_gender_F').click()
        self.driver.execute_script('joinSubmit();')
        sleep(0.1)
        self.driver.switch_to.alert.accept()
        # self.driver.execute_script('window.confirm = function(msg) { return true; }')

if __name__ == '__main__':
    i = Infre()
    i.join('00112', '1234', '안뇽', 'm', '메시지')
    i.dispose()
