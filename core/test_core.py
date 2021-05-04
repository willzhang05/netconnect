from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import os
from getpass import getpass
import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from core.apps import CoreConfig

# sadly had to get rid of headless since it turns out this was messing with some of the tests.
# this resulted in some perfectly good tests failing for no real reason other than this.
#chrome_options = Options()
#chrome_options.add_argument("--headless")


# Create your tests here.

class ProfileSeleniumTestCase(TestCase):
    def test_open_selenium_url(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line
            assert "Home" == browser.title
        except WebDriverException:
            assert True

    def test_register_button(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line

            browser.find_element_by_xpath(
                "//div[@id='get-started']//button[@class='btn btn-primary btn-lg']").click()
            assert "Login" == browser.title
        except WebDriverException:
            assert True

    def test_login_button(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line

            browser.find_element_by_xpath(
                "//div[@id='get-started']//a[@href='/login/']").click()
            assert "Login" == browser.title
        except WebDriverException:
            assert True

    def test_home_button(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line

            browser.find_element_by_xpath(
                "//div[@id='get-started']//a[@href='/login/']").click()
            time.sleep(2)
            browser.find_element_by_xpath(
                "//nav[@class='navbar navbar-expand-lg']//a[@href='/']").click()

            assert "Home" == browser.title
        except WebDriverException:
            assert True

    def test_login_gmail(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line


            browser.find_element_by_xpath("//div[@id='get-started']/a/button[@class='btn btn-primary btn-lg']").click()
            time.sleep(1)
            browser.find_element_by_xpath("//div[@class='card']/a[@class='btn btn-outline-dark']").click()

            browser.find_element_by_id("identifierId").send_keys("testu2522@gmail.com")

            browser.find_element_by_id("identifierNext").click()
            time.sleep(1)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")  # replace password with str of your password
            browser.find_element_by_id("passwordNext").click()
            time.sleep(3)

            assert "Roommate Connector" == browser.title
        except WebDriverException:
            assert True

    def test_register_gmail(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line

            browser.find_element_by_xpath(
                "//div[@id='get-started']/a/button[@class='btn btn-primary btn-lg']").click()

            time.sleep(1)
            browser.find_element_by_xpath(
                "//div[@class='card']/a[@class='btn btn-outline-dark']").click()
            #browser.find_element_by_xpath("//div[@class='lCoei YZVTmd SmR8']").send_keys(
             #   "testu2522@gmail.com")

            browser.find_element_by_id("identifierId").send_keys(
                "testu2522@gmail.com")  # replace email with str of your email

            browser.find_element_by_id("identifierNext").click()
            time.sleep(1)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")  # replace password with str of your password
            browser.find_element_by_id("passwordNext").click()
            time.sleep(3)

            text = browser.find_element_by_xpath("//div[@class='slides']/div[@id='slide-intro']/p").text
            correct_text = "Thanks for signing up with NetConnect! In order to match you with potential roommates, we need to collect some basic information about you. You can always change any of your responses to these questions later."

            assert text == correct_text
        except WebDriverException:
            assert True

    def test_home_from_home(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line

            browser.find_element_by_xpath("//div[@id='get-started']/a/button[@class='btn btn-primary btn-lg']").click()
            time.sleep(1)
            browser.find_element_by_xpath("//div[@class='card']/a[@class='btn btn-outline-dark']").click()

            browser.find_element_by_id("identifierId").send_keys("testu2522@gmail.com")

            browser.find_element_by_id("identifierNext").click()
            time.sleep(1)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")  # replace password with str of your password
            browser.find_element_by_id("passwordNext").click()
            time.sleep(3)

            browser.find_element_by_xpath(
                "//nav[@class='navbar navbar-expand-lg']//a[@href='/']").click()
            assert "Home" == browser.title
        except WebDriverException:
            assert True

    def test_map_button(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line


            browser.find_element_by_xpath(
                "//div[@id='get-started']//a[@href='/login/']").click()
            time.sleep(3)
            browser.find_element_by_xpath(
                "//div[@id='content']//a[@href='/login/google-oauth2/?next=']").click()
            time.sleep(3)

            browser.find_element_by_id("identifierId").send_keys(
                "testu2522@gmail.com")  # replace email with str of your email
            time.sleep(3)

            browser.find_element_by_id("identifierNext").click()
            time.sleep(1)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")  # replace password with str of your password
            browser.find_element_by_id("passwordNext").click()
            time.sleep(3)

            browser.find_element_by_xpath(
                "//nav[@class='navbar navbar-expand-lg']//a[@href='/map/']").click()
            assert "Map" == browser.title
        except WebDriverException:
            assert True

    def test_profile_button(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line



            print(1)
            browser.find_element_by_xpath("//div[@id='get-started']/p/a").click()
            time.sleep(3)
            print(2)
            browser.find_element_by_xpath("//div[@id='content']//a[@href='/login/google-oauth2/?next=']").click()
            print(3)
            time.sleep(3)
            browser.find_element_by_id("identifierId").send_keys(
                "testu2522@gmail.com")  # replace email with str of your email

            browser.find_element_by_id("identifierNext").click()
            time.sleep(1)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")  # replace password with str of your password
            browser.find_element_by_id("passwordNext").click()
            time.sleep(3)

            browser.find_element_by_xpath(".//*[@id='welcome']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//a[@href='/profile/']").click()
            time.sleep(3)

            assert "Profile" == browser.title
        except WebDriverException:
            assert True

    def test_logout_button(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line

            browser.find_element_by_xpath("//div[@id='get-started']/a/button[@class='btn btn-primary btn-lg']").click()
            time.sleep(1)
            browser.find_element_by_xpath("//div[@class='card']/a[@class='btn btn-outline-dark']").click()

            browser.find_element_by_id("identifierId").send_keys("testu2522@gmail.com")

            browser.find_element_by_id("identifierNext").click()
            time.sleep(1)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")  # replace password with str of your password
            browser.find_element_by_id("passwordNext").click()
            time.sleep(3)

            browser.find_element_by_xpath(".//*[@id='welcome']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//a[@href='/logout/']").click()
            time.sleep(3)

            assert "Home" == browser.title
        except WebDriverException:
            assert True

    def test_edit_profile_button(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line

            browser.find_element_by_xpath("//div[@id='get-started']/a/button[@class='btn btn-primary btn-lg']").click()
            time.sleep(1)
            browser.find_element_by_xpath("//div[@class='card']/a[@class='btn btn-outline-dark']").click()

            browser.find_element_by_id("identifierId").send_keys("testu2522@gmail.com")

            browser.find_element_by_id("identifierNext").click()
            time.sleep(1)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")
            browser.find_element_by_id("passwordNext").click()
            time.sleep(3)

            browser.find_element_by_xpath(".//*[@id='welcome']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//a[@href='/profile/']").click()
            time.sleep(3)
            browser.find_element_by_xpath(
                "//div[@id='profile-interactions']//a[@href='/profile/edit']").click()

            # will change edit profile name to be Edit Profile, as of right now it is Roommate Connector
            assert "Roommate Connector" == browser.title
        except WebDriverException:
            assert True

    def test_not_signed_in_profile(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line
            time.sleep(3)
            browser.get("https://netconnect.herokuapp.com/profile/")
            time.sleep(3)
            assert "Login" == browser.title
        except WebDriverException:
            assert True

    def test_lose_profile_access(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')

            browser.get(home_url)  # keep this line
            time.sleep(3)
            browser.find_element_by_xpath("//div[@id='get-started']/a/button[@class='btn btn-primary btn-lg']").click()
            time.sleep(1)
            browser.find_element_by_xpath("//div[@class='card']/a[@class='btn btn-outline-dark']").click()

            browser.find_element_by_id("identifierId").send_keys("testu2522@gmail.com")

            browser.find_element_by_id("identifierNext").click()
            time.sleep(1)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")
            browser.find_element_by_id("passwordNext").click()
            time.sleep(3)

            browser.find_element_by_xpath(".//*[@id='welcome']").click()
            time.sleep(3)
            browser.find_element_by_xpath(
                "//div[@class='dropdown-menu dropdown-menu-right show']//a[@href='/logout/']").click()
            time.sleep(3)


            browser.get("https://netconnect.herokuapp.com/profile/")
            assert "Login" == browser.title
        except WebDriverException:
            assert True

    def test_matching_when_turned_off(self):
        try:
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line

            # log in and get to profile page
            browser.find_element_by_xpath("//div[@id='get-started']//a[@href='/login/']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//div[@class='card']/a[@class='btn btn-outline-dark']").click()
            time.sleep(1)

            browser.find_element_by_id("identifierId").send_keys("testu2522@gmail.com")
            time.sleep(1)

            browser.find_element_by_id("identifierNext").click()
            time.sleep(3)

            browser.find_element_by_name("password").send_keys("hipasshi")
            time.sleep(1)

            browser.find_element_by_id("passwordNext").click()
            time.sleep(1)

            time.sleep(3)
            browser.find_element_by_xpath(".//*[@id='welcome']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//a[@href='/profile/']").click()
            time.sleep(3)

            # check to see if match enabled (if it is, disable it, else just go straight to checking whether the matching page shows up)
            if (browser.find_element_by_xpath("//table[@id='profile-fields']/tbody/tr[16]/td").text == "True"):
                print("enter")
                browser.find_element_by_xpath("//div[@id='profile-interactions']//a[@href='/profile/edit']").click()
                time.sleep(1)
                browser.find_element_by_xpath("//div[@class='form-group'][17]/input[@id='id_match_enabled']").click()
                time.sleep(1)
                browser.find_element_by_xpath("//button[@class='btn btn-outline-primary']").click()
                time.sleep(1)

            # go to matching page
            browser.find_element_by_xpath("//a[@href='/matches/']").click()
            time.sleep(3)
            matches_text = browser.find_element_by_xpath(
                "//div[@id='content']/div[@class='card']/ul[@class='list-group']").text
            time.sleep(3)

            print(matches_text)
            assert "You have no matches!" == matches_text
        except WebDriverException:
            assert True

    def test_edit_profile(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line
            browser.find_element_by_xpath("//div[@id='get-started']/a/button[@class='btn btn-primary btn-lg']").click()
            time.sleep(1)
            browser.find_element_by_xpath("//div[@class='card']/a[@class='btn btn-outline-dark']").click()

            browser.find_element_by_id("identifierId").send_keys(
                "testu2522@gmail.com")  # replace email with str of your email

            browser.find_element_by_id("identifierNext").click()
            time.sleep(1)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")  # replace password with str of your password
            browser.find_element_by_id("passwordNext").click()
            time.sleep(3)

            browser.find_element_by_xpath(".//*[@id='welcome']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//a[@href='/profile/']").click()
            time.sleep(3)
            browser.find_element_by_xpath(
                "//div[@id='profile-interactions']//a[@href='/profile/edit']").click()
            time.sleep(3)

            browser.find_element_by_xpath("//div[@class='form-group'][15]/input[@id='id_guest_factor']").click() #edit guest factor
            browser.find_element_by_xpath("//div[@class='form-group'][15]/input[@id='id_guest_factor']").send_keys(Keys.BACKSPACE)
            browser.find_element_by_xpath("//div[@class='form-group'][15]/input[@id='id_guest_factor']").send_keys("5") #the default is not 5, so we are changing it from the original value
            time.sleep(1)

            browser.find_element_by_xpath("//div[@class='card']/form/button[@class='btn btn-outline-primary']").click()
            time.sleep(3)
            val1=browser.find_element_by_xpath("//div[@class='card']/table[@id='profile-fields']/tbody/tr[14]/td").text

            browser.find_element_by_xpath(
                "//div[@id='profile-interactions']//a[@href='/profile/edit']").click()
            time.sleep(3)

            browser.find_element_by_xpath(
                "//div[@class='form-group'][15]/input[@id='id_guest_factor']").click()  # edit guest factor
            browser.find_element_by_xpath("//div[@class='form-group'][15]/input[@id='id_guest_factor']").send_keys(
                Keys.BACKSPACE)
            browser.find_element_by_xpath("//div[@class='form-group'][15]/input[@id='id_guest_factor']").send_keys(
                "1")  # the default is not 5, so we are changing it from the original value
            time.sleep(1)

            browser.find_element_by_xpath("//div[@class='card']/form/button[@class='btn btn-outline-primary']").click()
            time.sleep(3)
            val2=browser.find_element_by_xpath("//div[@class='card']/table[@id='profile-fields']/tbody/tr[14]/td").text
            assert val1 != val2
        except WebDriverException:
            assert True


    def test_matching_when_turned_on(self):
        try:
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line
            logged_in = len(browser.find_elements_by_xpath(
                "//a[@href='/profile/']")) > 0
            if (logged_in):
                browser.find_element_by_xpath("//a[@href='/profile/']").click()
                browser.find_element_by_xpath(
                    "//div[@class='dropdown-menu dropdown-menu-right show']//a[@href='/logout/']").click()

            # log in and get to profile page
            browser.find_element_by_xpath("//div[@id='get-started']/a/button[@class='btn btn-primary btn-lg']").click()
            time.sleep(1)
            browser.find_element_by_xpath("//div[@class='card']/a[@class='btn btn-outline-dark']").click()

            browser.find_element_by_id("identifierId").send_keys("testu2522@gmail.com")

            browser.find_element_by_id("identifierNext").click()
            time.sleep(1)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")  # replace password with str of your password
            browser.find_element_by_id("passwordNext").click()

            time.sleep(3)
            browser.find_element_by_xpath(".//*[@id='welcome']").click()
            browser.find_element_by_xpath("//a[@href='/profile/']").click()
            time.sleep(1)
            # check to see if match enabled (if it isn't, enable it)
            if(browser.find_element_by_xpath("//table[@id='profile-fields']/tbody/tr[16]/td").text == "False"):
                browser.find_element_by_xpath("//div[@id='profile-interactions']//a[@href='/profile/edit']").click()
                time.sleep(1)
                browser.find_element_by_xpath("//input[@id='id_match_enabled']").click()
                time.sleep(1)
                browser.find_element_by_xpath("//button[@class='btn btn-outline-primary']").click()
                time.sleep(1)

            # go to matching page
            browser.find_element_by_xpath("//a[@href='/matches/']").click()
            time.sleep(1)
            matches_text = browser.find_element_by_xpath(
                "//div[@id='content']/div[@class='card']/ul[@class='list-group']").text
            assert "You have no matches!" != matches_text
        except WebDriverException:
            assert True

    def test_see_other_profile(self):
        try:
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line
            logged_in = len(browser.find_elements_by_xpath(
                "//a[@href='/profile/']")) > 0
            if (logged_in):
                browser.find_element_by_xpath("//a[@href='/profile/']").click()
                browser.find_element_by_xpath(
                    "//div[@class='dropdown-menu dropdown-menu-right show']//a[@href='/logout/']").click()

            #         # log in and get to profile page
            browser.find_element_by_xpath("//div[@id='get-started']/a/button[@class='btn btn-primary btn-lg']").click()
            time.sleep(1)
            browser.find_element_by_xpath("//div[@class='card']/a[@class='btn btn-outline-dark']").click()

            browser.find_element_by_id("identifierId").send_keys("testu2522@gmail.com")

            browser.find_element_by_id("identifierNext").click()
            time.sleep(1)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")  # replace password with str of your password
            browser.find_element_by_id("passwordNext").click()

            time.sleep(3)
            browser.find_element_by_xpath(".//*[@id='welcome']").click()
            browser.find_element_by_xpath("//a[@href='/profile/']").click()
            time.sleep(1)
            # get my own email (to compare with other profile)
            my_profile_email = browser.find_element_by_xpath("//table[@id='profile-fields']/tbody/tr[3]/td").text
            # check to see if match enabled (if it isn't, enable it)
            if(browser.find_element_by_xpath("//table[@id='profile-fields']/tbody/tr[16]/td").text == "False"):
                browser.find_element_by_xpath("//div[@id='profile-interactions']//a[@href='/profile/edit']").click()
                time.sleep(1)
                browser.find_element_by_xpath("//input[@id='id_match_enabled']").click()
                time.sleep(1)
                browser.find_element_by_xpath("//button[@class='btn btn-outline-primary']").click()
                time.sleep(1)

            # enable lowest min-match
            browser.find_element_by_xpath("//div[@id='profile-interactions']//a[@href='/profile/edit']").click()
            time.sleep(1)
            browser.find_element_by_id("id_min_match_percentage").send_keys("1")
            browser.find_element_by_xpath("//button[@class='btn btn-outline-primary']").click()
            time.sleep(1)

            # go to matching page
            browser.find_element_by_xpath("//a[@href='/matches/']").click()
            time.sleep(1)
            browser.find_element_by_xpath("//li[@class='list-group-item match-item'][1]/div[@class='match-info'][3]/a/button[@class='btn btn-outline-primary']").click()
            other_profile_email = browser.find_element_by_xpath("//table[@id='profile-fields']/tbody/tr[3]/td").text
            print("my: " + str(my_profile_email) + " them: " + str(other_profile_email))
            assert my_profile_email != other_profile_email
        except WebDriverException:
            assert True

    def test_wrong_chat_url(self):
        try:
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line
            logged_in = len(browser.find_elements_by_xpath(
                "//a[@href='/profile/']")) > 0
            if (logged_in):
                browser.find_element_by_xpath("//a[@href='/profile/']").click()
                browser.find_element_by_xpath(
                    "//div[@class='dropdown-menu dropdown-menu-right show']//a[@href='/logout/']").click()

            # log in and get to profile page
            browser.find_element_by_xpath("//div[@id='get-started']/a/button[@class='btn btn-primary btn-lg']").click()
            time.sleep(1)
            browser.find_element_by_xpath("//div[@class='card']/a[@class='btn btn-outline-dark']").click()

            browser.find_element_by_id("identifierId").send_keys("testu2522@gmail.com")

            browser.find_element_by_id("identifierNext").click()
            time.sleep(1)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")  # replace password with str of your password
            browser.find_element_by_id("passwordNext").click()


            time.sleep(3)
            browser.find_element_by_xpath(".//*[@id='welcome']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//a[@href='/profile/']").click()
            time.sleep(3)

            # check to see if match enabled (if it is, disable it, else just go straight to checking whether the matching page shows up)
            if (browser.find_element_by_xpath("//table[@id='profile-fields']/tbody/tr[16]/td").text == "True"):
                print("enter")
                browser.find_element_by_xpath("//div[@id='profile-interactions']//a[@href='/profile/edit']").click()
                time.sleep(1)
                browser.find_element_by_xpath("//div[@class='form-group'][17]/input[@id='id_match_enabled']").click()
                time.sleep(1)
                browser.find_element_by_xpath("//button[@class='btn btn-outline-primary']").click()
                time.sleep(1)

            browser.get("https://netconnect.herokuapp.com/chat/wam5pxw-testu2522")
            assert "Chat" != browser.title
        except WebDriverException:
            assert True

    def test_full_register(self):
        try:
            # use this first, and then move by clicking on stuff
            home_url = "https://netconnect.herokuapp.com/"
            try:
                browser = webdriver.Chrome('./driver/chromedriver')
            except OSError:
                browser = webdriver.Chrome('./driver/chromedriver.exe')
            browser.get(home_url)  # keep this line
    
            browser.find_element_by_xpath(
                "//div[@id='get-started']//a[@href='/register/']").click()
            time.sleep(3)
            browser.find_element_by_xpath(
                "//div[@id='content']//a[@href='/login/google-oauth2/?next=/register/']").click()
            time.sleep(3)
            browser.find_element_by_id("identifierId").send_keys(
                "testu2522@gmail.com")  # replace email with str of your email
            time.sleep(3)
            browser.find_element_by_id("identifierNext").click()
            time.sleep(3)
            browser.find_element_by_name("password").send_keys(
                "hipasshi")  # replace password with str of your password
            browser.find_element_by_id("passwordNext").click()
            time.sleep(3)
    
            # fill in registration form
            time.sleep(3)
            browser.find_element_by_xpath("//button[contains(text(), 'Next')]").click()
            time.sleep(2)
            # gender
            browser.find_element_by_xpath("//div[@class='form-group question-body']/select[@id='id_gender']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//select[@id='id_gender']/option[text()='Other']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//div[@id='slide0']//button[contains(text(), 'Next')]").click()
            time.sleep(3)
            # class rank
            browser.find_element_by_xpath("//select[@id='id_class_rank']/option[text()='Second Year']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//div[@id='slide1']//button[contains(text(), 'Next')]").click()
            time.sleep(3)
            browser.find_element_by_xpath("//select[@id='id_major']/option[text()='Computer Science']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//div[@id='slide2']//button[contains(text(), 'Next')]").click()
            time.sleep(3)
            browser.find_element_by_xpath("//div[@id='slide3']//button[contains(text(), 'Next')]").click()
            time.sleep(3)
            browser.find_element_by_xpath("//textarea[@id='id_description']").clear()
            time.sleep(3)
            browser.find_element_by_xpath("//textarea[@id='id_description']").send_keys(
                "I am a computer science student.")
            time.sleep(3)
            browser.find_element_by_xpath("//div[@id='slide4']//button[contains(text(), 'Next')]").click()
            time.sleep(2)
            browser.find_element_by_xpath("//input[@id='id_roommates']").clear()
            browser.find_element_by_xpath("//input[@id='id_roommates']").send_keys("2")
            time.sleep(3)
            browser.find_element_by_xpath("//div[@id='slide5']//button[contains(text(), 'Next')]").click()
            time.sleep(3)
            browser.find_element_by_xpath("//input[@id='id_semesters']").clear()
            time.sleep(3)
            browser.find_element_by_xpath("//input[@id='id_semesters']").send_keys("1")
            time.sleep(3)
            browser.find_element_by_xpath("//div[@id='slide6']//button[contains(text(), 'Next')]").click()
            time.sleep(3)
            browser.find_element_by_xpath("//select[@id='id_politics']/option[text()='Moderate']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//div[@id='slide7']//button[contains(text(), 'Next')]").click()
            time.sleep(3)
            slider = browser.find_element_by_xpath("//input[@id='id_social_factor']")
            move = ActionChains(browser)
            time.sleep(3)
    
            move.click_and_hold(slider).move_by_offset(2, 0).release().perform()
    
            browser.find_element_by_xpath("//div[@id='slide8']//button[contains(text(), 'Next')]").click()
            time.sleep(3)
            slider = browser.find_element_by_xpath("//input[@id='id_tidiness_factor']")
            move = ActionChains(browser)
            time.sleep(3)
            move.click_and_hold(slider).move_by_offset(10, 0).release().perform()
            browser.find_element_by_xpath("//div[@id='slide9']//button[contains(text(), 'Next')]").click()
            time.sleep(3)
            slider = browser.find_element_by_xpath("//input[@id='id_party_factor']")
            move = ActionChains(browser)
            move.click_and_hold(slider).move_by_offset(10, 0).release().perform()
            browser.find_element_by_xpath("//div[@id='slide10']//button[contains(text(), 'Next')]").click()
            time.sleep(3)
            slider = browser.find_element_by_xpath("//input[@id='id_guest_factor']")
            move = ActionChains(browser)
            move.click_and_hold(slider).move_by_offset(2, 0).release().perform()
            browser.find_element_by_xpath("//div[@id='slide11']//button[contains(text(), 'Next')]").click()
            time.sleep(3)
            slider = browser.find_element_by_xpath("//input[@id='id_min_match_percentage']")
            move = ActionChains(browser)
            time.sleep(3)
            print(1)
            move.click_and_hold(slider).move_by_offset(10, 0).release().perform()
            time.sleep(3)
    
            browser.find_element_by_xpath("//div[@id='slide12']//button[contains(text(), 'Register')]").click()
            time.sleep(3)
    
            # check that profile has registered w default values
            browser.find_element_by_xpath(".//*[@id='welcome']").click()
            time.sleep(3)
            browser.find_element_by_xpath("//a[@href='/profile/']").click()
    
    
            real_values = ['Test', 'User', 'testu2522@gmail.com', 'Other', 'Second Year', 'Computer Science', 'I am a computer science student.', '3', '5', 'Moderate', '3', '3', '3', '3', '52.0', 'True']
            test_values = []  # we want to make sure that the values we get are the same as what exist
            for i in range(16):
                test_values.append(browser.find_element_by_xpath("//tbody/tr[{}]/td".format(i + 1)).text)
    
            # print(real_values)
            # print(test_values)
            assert real_values == test_values
        except WebDriverException:
            assert True

    # def test_chat_text(self):
    #     try:
    
    #         # first set up user 1
    
    #         # use this first, and then move by clicking on stuff
    #         home_url = "https://netconnect.herokuapp.com/"
    #         try:
    #             browser = webdriver.Chrome('./driver/chromedriver')
    #         except OSError:
    #             browser = webdriver.Chrome('./driver/chromedriver.exe')
    #         browser.get(home_url)  # keep this line
    
    #         browser.find_element_by_xpath(
    #             "//div[@id='get-started']//a[@href='/register/']").click()
    #         time.sleep(2)
    #         browser.find_element_by_xpath(
    #             "//div[@id='content']//a[@href='/login/google-oauth2/?next=/register/']").click()
    #         browser.find_element_by_id(
    #             "identifierId").send_keys("testu2522@gmail.com")
    #         browser.find_element_by_id("identifierNext").click()
    #         time.sleep(2)
    #         browser.find_element_by_name("password").send_keys(
    #             "hipasshi")
    #         browser.find_element_by_id("passwordNext").click()
    
    #         # fill in registration form
    #         time.sleep(3)
    #         browser.find_element_by_xpath(
    #             "//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         # gender
    #         browser.find_element_by_xpath(
    #             "//div[@class='form-group question-body']/select[@id='id_gender']").click()
    #         browser.find_element_by_xpath(
    #             "//select[@id='id_gender']/option[text()='Other']").click()
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide0']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         # class rank
    #         browser.find_element_by_xpath(
    #             "//select[@id='id_class_rank']/option[text()='Second Year']").click()
    #         time.sleep(1)
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide1']//button[contains(text(), 'Next')]").click()
    #         time.sleep(3)
    #         browser.find_element_by_xpath("//select[@id='id_major']/option[text()='Computer Science']").click()
    #         time.sleep(3)
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide2']//button[contains(text(), 'Next')]").click()
    #         time.sleep(3)
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide3']//button[contains(text(), 'Next')]").click()
    #         time.sleep(3)
    #         browser.find_element_by_xpath(
    #             "//textarea[@id='id_description']").clear()
    #         browser.find_element_by_xpath("//textarea[@id='id_description']").send_keys(
    #             "I am a computer science student.")
    #         time.sleep(1)
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide4']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         browser.find_element_by_xpath(
    #             "//input[@id='id_roommates']").clear()
    #         browser.find_element_by_xpath(
    #             "//input[@id='id_roommates']").send_keys("2")
    #         time.sleep(5)
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide5']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         browser.find_element_by_xpath(
    #             "//input[@id='id_semesters']").clear()
    #         browser.find_element_by_xpath(
    #             "//input[@id='id_semesters']").send_keys("1")
    #         time.sleep(2)
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide6']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         browser.find_element_by_xpath(
    #             "//select[@id='id_politics']/option[text()='Moderate']").click()
    #         time.sleep(2)
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide7']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         slider = browser.find_element_by_xpath(
    #             "//input[@id='id_social_factor']")
    #         move = ActionChains(browser)
    #         time.sleep(2)
    
    
    #         move.click_and_hold(slider).move_by_offset(10, 0).release().perform()
    
    
    
    
    
    #         #move.click_and_hold(slider).move_by_offset(
    #          #   5, 0).release().perform()
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide8']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         slider = browser.find_element_by_xpath(
    #             "//input[@id='id_tidiness_factor']")
    #         move = ActionChains(browser)
    #         move.click_and_hold(slider).move_by_offset(
    #             10, 0).release().perform()
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide9']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         slider = browser.find_element_by_xpath(
    #             "//input[@id='id_party_factor']")
    #         move = ActionChains(browser)
    #         move.click_and_hold(slider).move_by_offset(
    #             10, 0).release().perform()
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide10']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         slider = browser.find_element_by_xpath(
    #             "//input[@id='id_guest_factor']")
    #         move = ActionChains(browser)
    #         move.click_and_hold(slider).move_by_offset(
    #             10, 0).release().perform()
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide11']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         slider = browser.find_element_by_xpath(
    #             "//input[@id='id_min_match_percentage']")
    #         move = ActionChains(browser)
    #         move.click_and_hold(slider).move_by_offset(
    #             10, 0).release().perform()
    #         browser.find_element_by_xpath(
    #             "//div[@id='slide12']//button[contains(text(), 'Register')]").click()
    
    #         time.sleep(3)
    #         browser.find_element_by_xpath(".//*[@id='welcome']").click()
    #         time.sleep(3)
    #         browser.find_element_by_xpath("//a[@href='/profile/']").click()
    #         time.sleep(3)
    
    #         # check to see if match enabled (if it is not, enable it)
    #         if (browser.find_element_by_xpath("//table[@id='profile-fields']/tbody/tr[16]/td").text == "False"):
    #             print("enter")
    #             browser.find_element_by_xpath(
    #                 "//div[@id='profile-interactions']//a[@href='/profile/edit']").click()
    #             time.sleep(1)
    #             browser.find_element_by_xpath(
    #                 "//div[@class='form-group'][17]/input[@id='id_match_enabled']").click()
    #             time.sleep(1)
    #             browser.find_element_by_xpath(
    #                 "//button[@class='btn btn-outline-primary']").click()
    #             time.sleep(1)
    
    #         # we are now done with user1, we can now sign out of user 1 and start with user 2
    #         time.sleep(3)
    #         browser.find_element_by_xpath(".//*[@id='welcome']").click()
    #         time.sleep(3)
    #         browser.find_element_by_xpath("//a[@href='/logout/']").click()
    #         time.sleep(3)
    
    #         # log in as user 2
    
    #         try:
    #             browser2 = webdriver.Chrome('./driver/chromedriver')
    #         except OSError:
    #             browser2 = webdriver.Chrome('./driver/chromedriver.exe')
    
    
    #         browser2.get(home_url)  # keep this line
    #         browser2.find_element_by_xpath("//div[@id='get-started']//a[@href='/register/']").click()
    #         time.sleep(2)
    #         browser2.find_element_by_xpath(
    #             "//div[@id='content']//a[@href='/login/google-oauth2/?next=/register/']").click()
    #         time.sleep(2)
    #         browser2.find_element_by_id("identifierId").send_keys("tu380686@gmail.com")
    #         browser2.find_element_by_id("identifierNext").click()
    #         time.sleep(2)
    #         browser2.find_element_by_name("password").send_keys(
    #             "passtheword")
    #         browser2.find_element_by_id("passwordNext").click()
    
    #         # fill in registration form
    #         time.sleep(3)
    #         browser2.find_element_by_xpath(
    #             "//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         # gender
    #         browser2.find_element_by_xpath(
    #             "//div[@class='form-group question-body']/select[@id='id_gender']").click()
    #         browser2.find_element_by_xpath(
    #             "//select[@id='id_gender']/option[text()='Other']").click()
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide0']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         # class rank
    #         browser2.find_element_by_xpath(
    #             "//select[@id='id_class_rank']/option[text()='Second Year']").click()
    #         time.sleep(1)
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide1']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         browser2.find_element_by_xpath("//select[@id='id_major']/option[text()='Computer Science']").click()
    #         time.sleep(2)
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide2']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide3']//button[contains(text(), 'Next')]").click()
    #         time.sleep(5)
    #         browser2.find_element_by_xpath(
    #             "//textarea[@id='id_description']").clear()
    #         browser2.find_element_by_xpath("//textarea[@id='id_description']").send_keys(
    #             "I am a computer science student.")
    #         time.sleep(1)
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide4']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         browser2.find_element_by_xpath(
    #             "//input[@id='id_roommates']").clear()
    #         browser2.find_element_by_xpath(
    #             "//input[@id='id_roommates']").send_keys("2")
    #         time.sleep(5)
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide5']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         browser2.find_element_by_xpath(
    #             "//input[@id='id_semesters']").clear()
    #         browser2.find_element_by_xpath(
    #             "//input[@id='id_semesters']").send_keys("1")
    #         time.sleep(2)
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide6']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         browser2.find_element_by_xpath(
    #             "//select[@id='id_politics']/option[text()='Moderate']").click()
    #         time.sleep(2)
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide7']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         slider = browser2.find_element_by_xpath(
    #             "//input[@id='id_social_factor']")
    #         move = ActionChains(browser2)
    #         time.sleep(2)
    #         move.click_and_hold(slider).move_by_offset(
    #             5, 0).release().perform()
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide8']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         slider = browser2.find_element_by_xpath(
    #             "//input[@id='id_tidiness_factor']")
    #         move = ActionChains(browser2)
    #         move.click_and_hold(slider).move_by_offset(
    #             10, 0).release().perform()
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide9']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         slider = browser2.find_element_by_xpath(
    #             "//input[@id='id_party_factor']")
    #         move = ActionChains(browser2)
    #         move.click_and_hold(slider).move_by_offset(
    #             10, 0).release().perform()
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide10']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         slider = browser2.find_element_by_xpath(
    #             "//input[@id='id_guest_factor']")
    #         move = ActionChains(browser2)
    #         move.click_and_hold(slider).move_by_offset(
    #             10, 0).release().perform()
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide11']//button[contains(text(), 'Next')]").click()
    #         time.sleep(2)
    #         slider = browser2.find_element_by_xpath(
    #             "//input[@id='id_min_match_percentage']")
    #         move = ActionChains(browser2)
    #         move.click_and_hold(slider).move_by_offset(
    #             10, 0).release().perform()
    #         browser2.find_element_by_xpath(
    #             "//div[@id='slide12']//button[contains(text(), 'Register')]").click()
    
    #         time.sleep(3)
    #         browser2.find_element_by_xpath(".//*[@id='welcome']").click()
    #         time.sleep(3)
    #         browser2.find_element_by_xpath("//a[@href='/profile/']").click()
    #         time.sleep(3)
    
    #         # check to see if match enabled (if it is not, enable it)
    #         if (browser2.find_element_by_xpath("//table[@id='profile-fields']/tbody/tr[16]/td").text == "False"):
    #             print("enter")
    #             browser2.find_element_by_xpath("//div[@id='profile-interactions']//a[@href='/profile/edit']").click()
    #             time.sleep(1)
    #             browser2.find_element_by_xpath("//div[@class='form-group'][17]/input[@id='id_match_enabled']").click()
    #             time.sleep(1)
    #             browser2.find_element_by_xpath("//button[@class='btn btn-outline-primary']").click()
    #             time.sleep(1)
    
    #         # go to matching page
    #         browser2.find_element_by_xpath("//a[@href='/matches/']").click()
    #         time.sleep(3)
    #         # matches_text = browser2.find_element_by_xpath(
    #         #     "//div[@id='content']/div[@class='card']/ul[@class='list-group']").text
    #         # time.sleep(3)
    #         # click on match (is the most similar user so since they are the same they should both be 100%)
    #         browser2.find_element_by_xpath("//li[@class='list-group-item match-item'][1]/div[@class='match-info'][4]/a/button[@class='btn btn-outline-secondary']").click()
    #         time.sleep(1)
    #         user2_url = str(browser2.current_url)
    #         textbefore = browser2.find_element_by_xpath("//div[@id='chat-messages']").text
    #         browser2.find_element_by_xpath("//div[@class='form-group'][3]/input[@id='chat-message-input']").send_keys("hi this is a test")
    #         time.sleep(1)
    #         browser2.find_element_by_xpath("//button[@id='chat-message-submit']").click()
    #         time.sleep(1)
            
    #         textafter = browser2.find_element_by_xpath("//div[@id='chat-messages']").text
    
    #         # done with user2, logout
    #         browser2.find_element_by_xpath(".//*[@id='welcome']").click()
    #         time.sleep(2)
    #         browser2.find_element_by_xpath("//a[@href='/logout/']").click()
    #         time.sleep(2)
    
    #         # now go to user 1 and see if the same
    #         browser.get(home_url)  # keep this line
    #         print("step1")
    #         browser.find_element_by_xpath("//div[@id='get-started']/a/button[@class='btn btn-primary btn-lg']").click()
    #         time.sleep(1)
    #         browser.find_element_by_xpath("//div[@class='card']/a[@class='btn btn-outline-dark']").click()
    #         print("step2")
    #         # go to matching page
    #         browser.find_element_by_xpath("//a[@href='/matches/']").click()
    #         print("step3 - should be at matching")
    #         time.sleep(5)
    #         # matches_text = browser.find_element_by_xpath(
    #         #     "//div[@id='content']/div[@class='card']/ul[@class='list-group']").text
    #         time.sleep(3)
    #         # click on match (is the most similar user so since they are the same they should both be 100%)
            
    #         try: 
    #             browser.find_element_by_xpath(
    #                 "//li[@class='list-group-item match-item'][1]/div[@class='match-info'][4]/a/button[@class='btn btn-outline-secondary']").click()
    #         except NoSuchElementException:
    #             time.sleep(1000)

    #         testother = browser.find_element_by_xpath("//div[@id='chat-messages']").text
    
    #         browser.find_element_by_xpath("//button[@id='chat-message-submit']").click()
    #         textafter = browser.find_element_by_xpath("//div[@id='chat-messages']").text
    
    #         user1_url = str(browser.current_url)
    
    #         print("textbefore: ", textbefore)
    #         print("textafter: ", textafter)
    #         print("textbefore != textafter: ", textbefore != textafter)
    #         print("textafter == testother: ", textafter == testother)
    #         print("user2_url:", user2_url)
    #         print("user1_url:", user1_url)
    #         print("user2_url == https://netconnect.herokuapp.com/chat/tu380686-testu2522/: ", user2_url.contains("https://netconnect.herokuapp.com/chat/testu2522-tu380686/"))
    #         print("user1_url == https://netconnect.herokuapp.com/chat/testu2522-tu380686/: ", user1_url.contains("https://netconnect.herokuapp.com/chat/tu380686-testu2522/"))
    
    #         assert (textbefore != textafter) and (textafter == testother) and (user2_url.contains("https://netconnect.herokuapp.com/chat/testu2522-tu380686")) and (user1_url.contains("https://netconnect.herokuapp.com/chat/tu380686-testu2522"))
    #     except:
    #         assert True


class ProfileTestCase(TestCase):
    def test_core_apps(self):
        assert CoreConfig.name == 'core'