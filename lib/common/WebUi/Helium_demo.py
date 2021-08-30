"""
Helium
https://github.com/mherrmann/selenium-python-helium
https://github.com/mherrmann/selenium-python-helium/blob/master/doc/Cheatsheet.md
"""
from helium import *
# base_url="https://www.baidu.com"
# driver=start_chrome(url=base_url)
# write('NBA')
# press(ENTER)
# kill_browser()

base_url="https://www.baidu.com"
driver=start_chrome(url=base_url)
if Text("//*[@id=\"su\"]").exists():
    write("NBA")
    press(ENTER)
kill_browser()