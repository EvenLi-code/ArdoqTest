import pytest
import requests
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils import email_generator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.mark.order(1)
@allure.story('Register a new account')
@allure.title('Test User Registration')
@allure.description('This test case verifies the registration process for a new account.')
def test_register_account(driver):
    driver.get("https://magento.softwaretestingboard.com/customer/account/create/")

    # Fill in the registration form
    driver.find_element(By.ID, "firstname").send_keys("Yiwen")
    driver.find_element(By.ID, "lastname").send_keys("Li")
    driver.find_element(By.ID, "email_address").send_keys(email_generator.EmailGenerator.generate_email())
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "password-confirmation").send_keys("Password123")

    # Click "Create an Account" to submit the form
    submit_button = driver.find_element(By.XPATH, '//button[@title="Create an Account"]')
    submit_button.click()


@pytest.mark.order(2)
@allure.story('Verify account creation')
@allure.title('Test Account Creation Verification')
@allure.description('This test case verifies that the account was created successfully.')
def test_verify_account_created(driver):
    WebDriverWait(driver, 3).until(
        EC.url_to_be("https://magento.softwaretestingboard.com/customer/account/")
    )

    # Verify the presence of the My Account element
    my_account_element = driver.find_element(By.CSS_SELECTOR, 'span.base[data-ui-id="page-title-wrapper"]')
    assert my_account_element.text == "My Account"

    # Verify the success message
    driver.implicitly_wait(5)
    success_message = driver.find_element(By.CSS_SELECTOR,
                                          'div[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    assert "Thank you for registering with Main Website Store." in success_message.text


@pytest.mark.order(3)
@allure.story('Add products to cart')
@allure.title('Test Adding Products to Cart')
@allure.description('This test case adds products to the cart and verifies the actions.')
def test_add_product_to_cart(driver):
    """
    Add product: Beaumont Summit Kit
    """

    # Hover over Men
    driver.implicitly_wait(5)
    men_link = driver.find_element(By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/men.html"]')
    webdriver.ActionChains(driver).move_to_element(men_link).perform()

    # Hover over Tops
    tops_link = driver.find_element(By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/men/tops-men.html"]')
    webdriver.ActionChains(driver).move_to_element(tops_link).perform()

    # Click on Jackets
    jackets_link = driver.find_element(By.XPATH,
                                       '//a[@href="https://magento.softwaretestingboard.com/men/tops-men/jackets-men'
                                       '.html"]')
    jackets_link.click()

    # Hover over the specific product container to reveal options
    product_container = driver.find_element(By.XPATH, '//div[@class="product-item-info" and .//a['
                                                      '@href="https://magento.softwaretestingboard.com/beaumont'
                                                      '-summit-kit.html"]]')
    webdriver.ActionChains(driver).move_to_element(product_container).perform()

    # Select size L
    size_l = WebDriverWait(product_container, 1).until(
        EC.element_to_be_clickable((By.XPATH, './/div[@option-label="L"]'))
    )
    size_l.click()

    # Select color Red
    color_red = WebDriverWait(product_container, 1).until(
        EC.element_to_be_clickable((By.ID, "option-label-color-93-item-58"))
    )
    color_red.click()

    # Click Add to Cart
    add_to_cart = WebDriverWait(product_container, 1).until(
        EC.element_to_be_clickable((By.XPATH, './/button[@title="Add to Cart"]'))
    )
    add_to_cart.click()

    """
    Add product: Strike Endurance Tee
    """

    # Hover over Men
    driver.implicitly_wait(5)
    men_link = driver.find_element(By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/men.html"]')
    webdriver.ActionChains(driver).move_to_element(men_link).perform()

    # Hover over Tops
    tops_link = driver.find_element(By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/men/tops-men.html"]')
    webdriver.ActionChains(driver).move_to_element(tops_link).perform()

    # Click on Jackets

    tees_link = driver.find_element(By.XPATH,
                                    '//a[@href="https://magento.softwaretestingboard.com/men/tops-men/tees-men'
                                    '.html"]')
    tees_link.click()

    # Hover over the specific product container to reveal options
    product_container = driver.find_element(By.XPATH, '//div[@class="product-item-info" and .//a['
                                                      '@href="https://magento.softwaretestingboard.com/strike'
                                                      '-endurance-tee.html"]]')
    webdriver.ActionChains(driver).move_to_element(product_container).perform()

    # Select size L
    size_l = WebDriverWait(product_container, 1).until(
        EC.element_to_be_clickable((By.XPATH, './/div[@option-label="L"]'))
    )
    size_l.click()

    # Select color Black
    color_red = WebDriverWait(product_container, 1).until(
        EC.element_to_be_clickable((By.ID, "option-label-color-93-item-49"))
    )
    color_red.click()

    # Click Add to Cart
    add_to_cart = WebDriverWait(product_container, 1).until(
        EC.element_to_be_clickable((By.XPATH, './/button[@title="Add to Cart"]'))
    )
    add_to_cart.click()


@pytest.mark.order(4)
@allure.story('Complete purchase')
@allure.title('Test Purchase Process')
@allure.description('This test case verifies the purchase process including checkout and order submission.')
def test_purchase_product(driver):
    driver.implicitly_wait(5)

    # Click on the cart icon
    WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.action.showcart'))
    ).click()

    # Click Proceed to Checkout
    proceed_to_checkout_button = driver.find_element(By.ID, "top-cart-btn-checkout")
    proceed_to_checkout_button.click()
    WebDriverWait(driver, 50).until(
        EC.url_to_be("https://magento.softwaretestingboard.com/checkout/#shipping")
    )

    # Fill in the information
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "street[0]"))
    )
    element.send_keys("Street")
    driver.find_element(By.NAME, "city").send_keys("City")
    select_element = driver.find_element(By.NAME, "region_id")
    select = Select(select_element)
    select.select_by_index(1)
    driver.find_element(By.NAME, "postcode").send_keys("10000")
    driver.find_element(By.NAME, "telephone").send_keys("110")
    radio_button = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='flatrate_flatrate']")
    radio_button.click()

    # Click next
    button = driver.find_element(By.CSS_SELECTOR, 'button[data-role="opc-continue"]')
    button.click()
    WebDriverWait(driver, 15).until(
        EC.url_to_be("https://magento.softwaretestingboard.com/checkout/#payment")
    )

    # Submit order
    button = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//button[@title="Place Order"]'))
    )
    driver.execute_script("arguments[0].click();", button)
    WebDriverWait(driver, 10).until(
        EC.url_contains('https://magento.softwaretestingboard.com/checkout/onepage/success/')
    )

    # Check Http Api Status
    current_url = driver.current_url
    response = requests.get(current_url)
    if response.status_code == 200:
        print("Success: The request returned status code 200.")
    else:
        print(f"Failed: The request returned status code {response.status_code}.")


@pytest.mark.order(5)
@allure.story('Verify order information')
@allure.title('Test Order Information Verification')
@allure.description('This test case verifies the order information, including the status, individual item prices, '
                    'and grand total on the account page.')
def test_verify_information(driver):
    driver.implicitly_wait(5)
    dropdown = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.customer-name[role="button"]'))
    )
    dropdown.click()

    # Click My Account
    my_account = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'My Account'))
    )
    my_account.click()
    WebDriverWait(driver, 10).until(
        EC.url_contains('https://magento.softwaretestingboard.com/customer/account/')
    )

    # Click My Orders
    my_orders = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'My Orders'))
    )
    my_orders.click()

    # Click View Order
    view_order_link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//a[contains(@class, "action") and contains(@class, "view")]'))
    )
    view_order_link.click()

    # Verify Order Status
    order_status = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.order-status'))
    ).text
    assert order_status == "PENDING", f"Expected 'PENDING' for order status, but got '{order_status}'"

    # Verify Prices Of Two Orders
    order_rows = WebDriverWait(driver, 15).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'tr[id^="order-item-row-"]'))
    )
    price_1 = order_rows[0].find_element(By.CSS_SELECTOR, '.price').text
    assert price_1 == "$42.00", f"Expected '$42.00' for first order, but got '{price_1}'"
    price_2 = order_rows[1].find_element(By.CSS_SELECTOR, '.price').text
    assert price_2 == "$39.00", f"Expected '$39.00' for second order, but got '{price_2}'"

    # Verify Grand Total
    grand_total_element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//td[@class="amount" and @data-th="Grand Total"]//span[@class="price"]'))
    ).text
    assert grand_total_element == "$91.00", f"Expected '$91.00' for grand total, but got '{grand_total_element}'"


if __name__ == "__main__":
    pytest.main()
