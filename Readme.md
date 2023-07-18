# **Install packages**
## Install Ruby and DivKit
    1.	Скачать Ruby WIth DivKit
    2.	Установить Ruby 
    3.	git clone https://github.com/urbanadventurer/Wh...
    4.	gem install bundler 
    5.	bundle install
    6.	bundle update
    7.	gem install bson 
    8.	gem install bson_ext
    9.	gem install mongo 
    10.	gem install rchardet
## Install Node.js
    -> https://nodejs.org/en/
# Options
В файле options.txt можно осуществить настройки скрипта
## [whatweb]
Список комманд для whatweb. Полный список комманд тут -> https://github.com/urbanadventurer/WhatWeb

**Example:**

    [whatweb]
    -v
    -a=2
    
## [wappalyzer]
Список комманд для wappalyzer. Полный список комманд тут -> https://github.com/wappalyzer/wappalyzer

**Example:**

    [wappalyzer]
    -d
    -t


## [open_file]
Укажите имя файла, в котором находится список доменов. (Указывать один файл, другие он проскипает)

**Example:**

    [open_file]
    Url_links.txt
    
## [PATH_TOOLS_ONE]
Указать путь, где установлен whatweb (ОБЯЗАТЕЛЬНО!!!)

**Example:**

    [PATH_TOOLS_ONE]
    E:/whaweb/WhatWeb-0.5.5
    
## [PATH_TOOLS_TWO]
Указать путь, где установлен wappalyzer (ОБЯЗАТЕЛЬНО!!!)

**Example:**

    [PATH_TOOLS_ONE]
    E:/wappalyzer

# Fast Launch

В терминале вести следующую комманду
    
    name_programm command 
    
|       command     |                    Описание                                        |
| -----------               | -----------                                                           |
|       open_with    *name.txt*   |   Открывает файл с списком доменов           |
|  url |  Анализирует файл переданный через комадную консоль (не работает) |


# Errors

## Error 001
    
    Ошибка выполнения анализа, а не самого скрипта
## Error 002

    Файл  options.txt пустой или неверный синтаксис
    
    
# Output
Генерятся ЖСОНЫ, где каждый джсон создается по каждый сайт в списке. Структура JSON следующая:

    {
	«site» : «https://url» //наименования сайта
	«plugins» : [ {} ] // массив объектов, где каждый объект яв-ся испольуземой технологией на сайте.
    }
Возможные поля объектов плагинов.

|       Имя поля     |                    Описание                                        |
| -----------               | -----------                                                           |
| Name| Имя используемой технологии. Тип string |  
  | Version| Версия используемой технологии. Тип string |  
| String|Указываются дополнительные расширения для данной технологии( Пример: HTTPSerber может использовать kittenx в вк) или найденные заголовки в технологии (Пример: PHP может быть найдены заголовки, которым помогают обрабатывать кэш и контет для браузера). Может иметь тип string или array.
|Categories| Указывает категорию технологии (Пример : reCAPTCHA относится к категории безопасность). Тип dict или array |
|Certainty|Данное поле показывает вероятность того, что данная технология действительно ей является. Значение принимается от 0 до 100, все что ниже 50 в исходный JSON не поподает. Тип int|