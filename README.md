# PyTest_ParametrizationLaunch
Задание: https://stepik.org/lesson/237240/step/10?unit=209628
ВНИМАНИЕ!! time.sleep в тестах очень плохая практика, поэтому хардкод в 30 секунд я заменил EC


Файл конфигурации conftest.py содержит в себе опцию --language для выбора любого из доступных языков, по дефолту выбран en default='en'
Прописывать дополнительный парааметр для запуска браузера не стал

Тест test_items.py содержит в себе тест на проверку элмента на странице, выводит сообщение об успехе/провале через обработчик исключения

Для запуска тестов установите все из файла requirement.txt
pip install -r requirement.txt

В файле configuration.py есть класс Data, хранящий в себе переменную ссылки

Для запуска теста выберите параметр --language=ru/en/es и т.д

В выводе должен быть текст с текстом кнопки
