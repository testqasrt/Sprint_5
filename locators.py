# Форма регистрации/авторизации
# поле ввода имени
form_name_input = './/label[text()="Имя"]/parent::div/input'
# поле ввода email
form_email_input = './/label[text()="Email"]/parent::div/input'
# поле ввода пароля
form_password_input = './/label[text()="Пароль"]/parent::div/input'
# кнопка на форме
form_button = 'form>button'

# ошибка при некорректном пароле
wrong_password_error = './/p[text()="Некорректный пароль"]'

# Страница авторизации
# Заголовок над формой авторизации
login_form_header = '//h2[text()="Вход"]'


# Главная страница
# кнопка Входа в аккаунт
main_page_login_button = './/button[text()="Войти в аккаунт"]'
# кнопка Оформить заказ
main_page_order_create_button = './/button[text()="Оформить заказ"]'

# Страница регистрации
reg_page_login_button = '[href="/login"]'


# Header
personal_cabinet_button = '[href="/account"]'
constructor_button = '//p[text()="Конструктор"]'


# personal_page
personal_page_profile_button = '[href="/account/profile"]'
personal_page_logout_button = '//button[text()="Выход"]'

# constructor_page
constructor_title = '//h1[text()="Соберите бургер"]'
filling_button = '//span[text()="Начинки"]/parent::div'
sauce_button = '//span[text()="Соусы"]/parent::div'
bun_button = '//span[text()="Булки"]/parent::div'
