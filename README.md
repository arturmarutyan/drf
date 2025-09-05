API продуктов на основе Django REST Framework, где рассмотрены все основные возможности фреймворка:  

Аутентификация и соответствующие разрешения: посмотреть список и создать новый продукт могут все  
авторизованные, смотреть на определенный продукт может только их владелец.  

В рамках обучения и эскперимента использовал как функциональные разрешения, так и на основе класса.  
Также умение работать с миксинами, кастомными методами get_queryset(), perform_<>() и так далее.  


Для различных запросов к API пользоваться данной навигацией и скриптами в py_script:  
/api/ - list всех объектов или create новый продукт - без аутентификации  
/api/auth/ - авторизация, получение токена  
/api/products/ - list, create + auth  
/api/products/{primary key}/update/ - update + auth  
/api/products/{primary key} - detail view + auth  
Скрипты:
basic.py - auth + create
update.py - auth + update
list.py - auth + list
detail.py - auth + detail

Для запуска кода запустить venv и в нем pip install -r requirements.txt 