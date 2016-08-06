# !/usr/bin/env python3

from selenium import webdriver
import sys
import time

video_name = sys.argv[1]
driver = webdriver.Chrome()

driver.get('https://www.youtube.com/?gl=BR')

search_box = driver.find_element_by_id('masthead-search-term')
search_box.send_keys(video_name)
search_box.submit()
time.sleep(1)
video = driver.find_elements_by_class_name('yt-uix-tile')[0]
video.click()
video_url = driver.current_url

print('url: {}'.format(video_url))
# wait youtube stuff...
time.sleep(5)

driver.get('http://catchvideo.net/')

converter_box = driver.find_element_by_id('input1')
converter_box.clear()
converter_box.send_keys(video_url)
converter_button = driver.find_element_by_id('grab1')
converter_button.click()
# wait video processing...
time.sleep(20)
convert_button = driver.find_element_by_id('convertmp3')
convert_button.click()
time.sleep(5)
download_button = driver.find_element_by_id('download1')
download_button.click()
# wait video download...
time.sleep(60)
driver.close()
