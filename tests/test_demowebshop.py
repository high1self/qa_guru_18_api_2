import os
import allure
from dotenv import load_dotenv
from selene import have
from selene.support.shared import browser

load_dotenv()


def test_login(browser_config):
    browser.open("")
    with allure.step('Пользователь может залогиниться'):
        browser.element(".account").should(have.text(os.getenv("LOGIN")))


def test_delete_product_from_wishlist(demoshop, browser_config):
    browser.open("")
    with allure.step('Пользователь может добавить товар в список желаемого'):
        demoshop.post("addproducttocart/details/14/2", json={"addtocart_14.EnteredQuantity": '1'})
    with allure.step('Пользователь может увидеть, что товар пропал из желаемого'):
        browser.element('.ico-wishlist').click()
        browser.element('[name="removefromcart"]').click()
        browser.element('[name="updatecart"]').click()

        browser.element('.wishlist-content').should(have.text('The wishlist is empty!'))


def test_delete_product_from_bucket(demoshop, browser_config):
    browser.open("")
    with allure.step('Пользователь может добавить товар в корзину'):
        demoshop.post("addproducttocart/catalog/31/1/1")
    with allure.step('Пользователь может увидеть, что товар пропал из корзины'):
        browser.element('.ico-cart').click()
        browser.element('[name="removefromcart"]').click()
        browser.element('[name="updatecart"]').click()

        browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_delete_customer_address(demoshop, browser_config):
    browser.open("")
    with allure.step('Пользователь может добавить адрес'):
        demoshop.post("customer/addressadd", json={"Address.Id": "0",
                                                   "Address.FirstName": "Kirill",
                                                   "Address.LastName": "Kirillov",
                                                   "Address.Email": "kkk@yandex.ru",
                                                   "Address.CountryId": "66",
                                                   "Address.City": "Moscow",
                                                   "Address.Address1": "Pushkina, 1",
                                                   "Address.ZipPostalCode": "1234444",
                                                   "Address.PhoneNumber": "89161112223",
                                                   })
    with allure.step('Пользователь может удалить адрес'):
        browser.element('.account').click()
        browser.element('.side-2 [href="/customer/addresses"]').click()
        browser.element('.delete-address-button').click()

        browser.driver.switch_to.alert.accept()

        browser.element('.address-list').should(have.text('No addresses'))


def test_logout(browser_config):
    browser.open("")
    with allure.step('Пользователь может выйти из аккаунта'):
        browser.element('.ico-logout').click()

        browser.element('.ico-login').should(have.text('Log in'))
