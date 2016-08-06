# !/usr/bin/env python3

from selenium import webdriver
import sys
import time


class VideoCatcher(object):

    def get_youtube_video_url(self, driver, video_description):
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

        return video_url

    def download_video_in_mp3_format(self, driver, video_url):
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

    def download_video(self, video_description):
        driver = webdriver.Chrome()

        video_url = self.get_youtube_video_url(driver, video_description)
        self.download_video_in_mp3_format(driver, video_url)

        driver.close()


if __name__ == "__main__":
    video_name = sys.argv[1]
    downloader = VideoCatcher()
    downloader.download_video(video_name)
