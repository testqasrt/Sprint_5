from selenium.webdriver.common.by import By


# Форма регистрации/авторизации
# поле ввода имени
form_name_input = By.XPATH, './/label[text()="Имя"]/parent::div/input'
# поле ввода email
form_email_input = By.XPATH, './/label[text()="Email"]/parent::div/input'
# поле ввода пароля
form_password_input = By.XPATH, './/label[text()="Пароль"]/parent::div/input'
# кнопка на форме
form_button = By.CSS_SELECTOR, 'form>button'

# ошибка при некорректном пароле
wrong_password_error = By.XPATH, './/p[text()="Некорректный пароль"]'

# Страница авторизации
# Заголовок над формой авторизации
login_form_header = By.XPATH, '//h2[text()="Вход"]'


# Главная страница
# кнопка Входа в аккаунт
main_page_login_button = By.XPATH, './/button[text()="Войти в аккаунт"]'
# кнопка Оформить заказ
main_page_order_create_button = By.XPATH, './/button[text()="Оформить заказ"]'

# Страница регистрации
reg_page_login_button = By.CSS_SELECTOR, '[href="/login"]'


# Header
personal_cabinet_button = By.CSS_SELECTOR, '[href="/account"]'
constructor_button = By.XPATH, '//p[text()="Конструктор"]'


# personal_page
personal_page_profile_button = By.CSS_SELECTOR, '[href="/account/profile"]'
personal_page_logout_button = By.XPATH, '//button[text()="Выход"]'

# constructor_page
constructor_title = By.XPATH, '//h1[text()="Соберите бургер"]'
filling_button = By.XPATH, '//span[text()="Начинки"]/parent::div'
sauce_button = By.XPATH, '//span[text()="Соусы"]/parent::div'
bun_button = By.XPATH, '//span[text()="Булки"]/parent::div'
