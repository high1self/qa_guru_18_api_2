import os
import allure
from dotenv import load_dotenv
from selene import have

load_dotenv()


def test_login(browser_config):
    browser_config.open("")
    with allure.step('Пользователь может залогиниться'):
        browser_config.element(".account").should(have.text(os.getenv("LOGIN")))


def test_delete_product_from_wishlist(demoshop, browser_config):
    browser_config.open("")
    with allure.step('Пользователь может добавить товар в список желаемого'):
        demoshop.post("addproducttocart/details/14/2", json={"addtocart_14.EnteredQuantity": '1'})
    with allure.step('Пользователь может увидеть, что товар пропал из желаемого'):
        browser_config.element('.ico-wishlist').click()
        browser_config.element('[name="removefromcart"]').click()
        browser_config.element('[name="updatecart"]').click()

        browser_config.element('.wishlist-content').should(have.text('The wishlist is empty!'))


def test_delete_product_from_bucket(demoshop, browser_config):
    browser_config.open("")
    with allure.step('Пользователь может добавить товар в корзину'):
        demoshop.post("addproducttocart/catalog/31/1/1")
    with allure.step('Пользователь может увидеть, что товар пропал из корзины'):
        browser_config.element('.ico-cart').click()
        browser_config.element('[name="removefromcart"]').click()
        browser_config.element('[name="updatecart"]').click()

        browser_config.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_delete_customer_address(demoshop, browser_config):
    browser_config.open("")
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
        browser_config.element('.account').click()
        browser_config.element('.side-2 [href="/customer/addresses"]').click()
        browser_config.element('.delete-address-button').click()

        browser_config.driver.switch_to.alert.accept()

        browser_config.element('.address-list').should(have.text('No addresses'))


def test_logout(browser_config):
    browser_config.open("")
    with allure.step('Пользователь может выйти из аккаунта'):
        browser_config.element('.ico-logout').click()

        browser_config.element('.ico-login').should(have.text('Log in'))
