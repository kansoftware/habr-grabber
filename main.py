from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
from weasyprint import HTML
import gc

favorites = 'https://m.habr.com/ru/users/U_NAME_HERE/favorites/posts/'
logon = 'https://account.habr.com/login/'
save_path = '~/habr_save/'

driver = webdriver.Firefox(executable_path='~/Soft/geckodriver')#, options=profile
# driver.install_addon("~/.mozilla/firefox/4mby2918.default/extensions/adguardadblocker@adguard.com.xpi")
driver.set_script_timeout(30)

driver.get(logon)
elem = driver.find_element_by_xpath('//*[@id="email_field"]')
elem.send_keys("u e-name here")
elem = driver.find_element_by_xpath('//*[@id="password_field"]')
elem.send_keys("getmeyousecters")
elem.send_keys(Keys.RETURN)
time.sleep(2)

while True:
    driver.get(favorites)
    elem = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/main/div/div/div/div[3]/div[2]/div/div[1]/div[1]/article')
    elem1 = elem.find_element_by_class_name("tm-article-title__link")
    head = elem1.text
    print(head)
    url = elem1.get_attribute("href")
    driver.get(url)

    elem = driver.find_elements_by_class_name('tm-article-hubs__hub')
    tags = [elem[i].text for i in range(0, len(elem))]

    #elem = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/main/div/div/article/div[4]/div[2]/span[2]')
    elem = driver.find_elements_by_class_name('tm-icon-text_enhanced')
    i=0
    while len(elem) == 0:
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        elem = driver.find_elements_by_class_name('tm-icon-text_enhanced')
        i = i+1
        if i > 5:
            print('fail unmark')
            exit(0)
            #break

    elem[1].click()

    ltlt = str(head).replace(" ", "_")
    ltlt = re.sub(r"[\/:*?\"<>|]", "", ltlt)

    time.sleep(1)

    print("weasyprint")
    HTML(url).write_pdf(save_path + ltlt + '.pdf')

    print("save info")
    with open(save_path + ltlt + '.txt', 'w') as file:
        file.write('head: {}\n'.format(head))
        file.write('file: {}.pdf\n'.format(ltlt))
        file.write('tags: {}\n'.format(tags))
        file.write('url: {}\n'.format(url))

    gc.collect()
    print("done!")

driver.close()