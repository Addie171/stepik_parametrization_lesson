import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_buy_btn_exists(browser):
    browser.get(link)
    buy_btn = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert buy_btn is not None, 'Кнопки "купить" нет на странице'


