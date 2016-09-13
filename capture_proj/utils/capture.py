#coding:utf-8
import os
import sys
from datetime import datetime
from time import sleep

from django.conf import settings

from selenium import webdriver


browser = webdriver.PhantomJS()
browser.set_window_size(2000, 1000)


def login(username, password):
    browser.get(settings.LOGIN_URL)

    username = browser.find_element_by_name('username')
    password = browser.find_element_by_name('password')
    submit_btn = browser.find_element_by_xpath('//button[@type="submit"]')

    username.send_keys(settings.USERNAME)
    password.send_keys(settings.PASSWORD)

    submit_btn.click()
    sleep(2)


def mk_picture_dir(dir_name):
    target_dir = os.path.join(settings.PICTURE_DIR, dir_name)
    os.mkdir(target_dir)

    return target_dir


def get_picture(url, name, target_dir):
    browser.get(url)
    sleep(2)

    browser.save_screenshot(target_dir+'/'+name+'.jpg')
    print name, url, 'shot ok!'


def fetch_picture():
    login(settings.USERNAME, settings.PASSWORD)

    now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    target_dir = mk_picture_dir(now)

    for _ in settings.TARGET_URL:
        for k, v in _.items():
            get_picture(v, k, target_dir)

    browser.close()


