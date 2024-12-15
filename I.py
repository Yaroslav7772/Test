import streamlit as str
import time
str.title('The password game')
str.markdown("<h1 style='text-align: center; color: green;'>Hello!</h1>", unsafe_allow_html=True)
def check(password):
    current = time.localtime()
    hour = time.strftime('%H')
    date = time.strftime('%d')
    day = time.strftime('%A')
    count_spec_symbols = 0
    count_numbers = 0
    count_upper = 0
    count_lower = 0
    for symbol in password:
        if symbol in '}{\|<~>$@#%^&*[!"№%:,.;()_-+=/?':
            count_spec_symbols += 1
        if symbol in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
            count_upper += 1
    if len(password) <8:
        str.markdown('Простите, но ваш пароль должен содержать как минимум 8 символов')
    elif len(password) >50:
        str.markdown('Ваш пароль слишком большой, уменьшите количество символов в пароле как минимум до 50')
    elif hour not in password:
        str.markdown('Добавьте в пароль текущий час')
    elif date not in password:
        str.markdown('Пароль должен содержать текущую дату')
    elif day not in password:
        str.markdown('Пароль должен содержать название дня недели(с заглавной буквы)')
    elif count_spec_symbols < 1:
        str.markdown('В вашем пароле должно быть как минимум 1 спец. символ')
    elif count_upper < 5:
        str.markdown('В вашем пароле должно быть как минимум 5 заглавных русских букв')
    else:
        str.markdown('Ура, ваш пароль подходит')
        
password=str.text_input('The password game', max_chars= 50,type = 'password')
check(password)
