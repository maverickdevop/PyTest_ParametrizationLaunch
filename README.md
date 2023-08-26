# PyTest_ParametrizationLaunch
Задание: https://stepik.org/lesson/237240/step/10?unit=209628
ВНИМАНИЕ!! time.sleep в тестах очень плохая практика, поэтому хардкод в 30 секунд я заменил EC

1. Установите окружение на локальной машине python -m venv venv
2. Установите все модули и пакеты для работы с тестами


Файл конфигурации conftest.py содержит в себе опцию --language для выбора любого из доступных языков, по дефолту выбран en default='en'
Прописывать дополнительный парааметр для запуска браузера не стал

Тест test_items.py содержит в себе тест на проверку элмента на странице, выводит сообщение об успехе/провале через обработчик исключения

Для запуска тестов установите все из файла requirement.txt
pip install -r requirement.txt

В файле configuration.py есть класс Data, хранящий в себе переменную ссылки

Для запуска теста выберите параметр --language=ru/en/es и т.д

В выводе должен быть текст с текстом кнопки
![1](https://github.com/maverickdevop/PyTest_ParametrizationLaunch/assets/57834199/b6c32b1b-5f06-490a-88c2-20457ece88fe)
![2](https://github.com/maverickdevop/PyTest_ParametrizationLaunch/assets/57834199/abb911ae-cf48-4682-af02-5eb383f20515)
