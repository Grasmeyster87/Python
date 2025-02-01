"""
        ВСТРОЕННЫЕ МОДУЛИ

os - работа с файлами
time - разные действия со временем
sys - выполнение системных функций
math - математические операции
smtplib - отправка email
zipfile - создавать архивы или распаковывать архивы
csv - создание и чтение csv файлов
statistics - статистические расчёты
pprint - форматирование вывода данных в терминал
calendar - работа с датами в python
regex - действия связанные с регулярными выражениями
random - генерация случайных чисел

"""

"""
https://docs.python.org/uk/3.13/library/index.html

Стандартна бібліотека Python

Хоча Довідник з мови Python описує точний синтаксис і семантику мови Python, цей довідковий посібник з бібліотеки описує стандартну бібліотеку, яка поширюється разом з Python. Він також описує деякі додаткові компоненти, які зазвичай входять до дистрибутивів Python.

Стандартна бібліотека Python дуже обширна, пропонує широкий спектр можливостей, про що свідчить довгий зміст, наведений нижче. Бібліотека містить вбудовані модулі (написані мовою C), які надають доступ до системних функцій, таких як файловий ввід/вивід, які інакше були б недоступні для програмістів на Python, а також модулі, написані на Python, які надають стандартизовані рішення для багатьох проблем, які виникають у щоденне програмування. Деякі з цих модулів явно розроблено для заохочення та покращення переносимості програм Python шляхом абстрагування специфіки платформи в нейтральних до платформи API.

Інсталятори Python для платформи Windows зазвичай містять усю стандартну бібліотеку, а також багато додаткових компонентів. Для Unix-подібних операційних систем Python зазвичай надається як набір пакетів, тому може знадобитися використовувати інструменти пакування, що надаються разом з операційною системою, щоб отримати деякі або всі додаткові компоненти.

На додаток до стандартної бібліотеки, існує активна колекція сотень тисяч компонентів (від окремих програм і модулів до пакетів та цілих фреймворків для розробки додатків), доступних у Python Package Index.

    Вступ
        Примітки щодо наявності
    Вбудовані функції
    Вбудовані константи
        Константи, додані модулем site
    Вбудовані типи
        Перевірка значення на істинність
        Булеві операції — and, or, not
        Порівняння
        Числові типи — int, float, complex
        Boolean Type - bool
        Типи ітераторів
        Типи послідовностей — list, tuple, range
        Тип текстової послідовності — str
        Типи бінарних послідовностей — bytes, bytearray, memoryview
        Типи наборів — set, frozenset
        Типи зіставлення — dict
        Типи менеджера контексту
        Типи анотацій типу — Загальний псевдонім, Об’єднання
        Інші вбудовані типи
        Спеціальні атрибути
        Integer string conversion length limitation
    Вбудовані винятки
        Контекст винятків
        Успадкування від вбудованих винятків
        Базові класи
        Конкретні винятки
        Попередження
        Exception groups
        Ієрархія винятків
    Послуги обробки тексту
        string — Common string operations
        re — Regular expression operations
        difflib — Helpers for computing deltas
        textwrap — Text wrapping and filling
        unicodedata — Unicode Database
        stringprep — Internet String Preparation
        readline — GNU readline interface
        rlcompleter — Completion function for GNU readline
    Служби двійкових даних
        struct — Interpret bytes as packed binary data
        codecs — Codec registry and base classes
    Типи даних
        datetime — Basic date and time types
        zoneinfo — IANA time zone support
        calendar — General calendar-related functions
        collections — Container datatypes
        collections.abc — Abstract Base Classes for Containers
        heapq — Heap queue algorithm
        bisect — Array bisection algorithm
        array — Efficient arrays of numeric values
        weakref — Слабкі посилання
        types — Dynamic type creation and names for built-in types
        copy — Shallow and deep copy operations
        pprint — Data pretty printer
        reprlib — Alternate repr() implementation
        enum — Support for enumerations
        graphlib — Functionality to operate with graph-like structures
    Числові та математичні модулі
        numbers — Numeric abstract base classes
        math — Mathematical functions
        cmath — Mathematical functions for complex numbers
        decimal — Decimal fixed-point and floating-point arithmetic
        fractions — Rational numbers
        random — Generate pseudo-random numbers
        statistics — Mathematical statistics functions
    Модулі функціонального програмування
        itertools — Functions creating iterators for efficient looping
        functools — Higher-order functions and operations on callable objects
        operator — Standard operators as functions
    Доступ до файлів і каталогів
        pathlib — Object-oriented filesystem paths
        os.path — Common pathname manipulations
        stat — Interpreting stat() results
        filecmp — File and Directory Comparisons
        tempfile — Generate temporary files and directories
        glob — Unix style pathname pattern expansion
        fnmatch — зіставлення імен файлів у Unix
        linecache — Random access to text lines
        shutil — High-level file operations
    Постійність даних
        pickle — Python object serialization
        copyreg — Register pickle support functions
        shelve — Python object persistence
        marshal — Internal Python object serialization
        dbm — Interfaces to Unix «databases»
        sqlite3 — DB-API 2.0 interface for SQLite databases
    Стиснення та архівування даних
        zlib — Compression compatible with gzip
        gzip — Support for gzip files
        bz2 — Support for bzip2 compression
        lzma — Compression using the LZMA algorithm
        zipfile — Work with ZIP archives
        tarfile — Read and write tar archive files
    Формати файлів
        csv — CSV File Reading and Writing
        configparser — Configuration file parser
        tomllib — Parse TOML files
        netrc — netrc file processing
        plistlib — Generate and parse Apple .plist files
    Криптографічні послуги
        hashlib — Secure hashes and message digests
        hmac — Keyed-Hashing for Message Authentication
        secrets — Generate secure random numbers for managing secrets
    Загальні служби операційної системи
        os — Miscellaneous operating system interfaces
        io — Core tools for working with streams
        time — Time access and conversions
        logging — Logging facility for Python
        logging.config — Logging configuration
        logging.handlers — Logging handlers
        platform — Access to underlying platform’s identifying data
        errno — Standard errno system symbols
        ctypes — A foreign function library for Python
    Command Line Interface Libraries
        argparse — Parser for command-line options, arguments and subcommands
        optparse — Parser for command line options
        getpass — Portable password input
        fileinput — Iterate over lines from multiple input streams
        curses — Terminal handling for character-cell displays
        curses.textpad — Віджет введення тексту для програм curses
        curses.ascii — Utilities for ASCII characters
        curses.panel — A panel stack extension for curses
    Паралельне виконання
        threading — Thread-based parallelism
        multiprocessing — Process-based parallelism
        multiprocessing.shared_memory — Shared memory for direct access across processes
        The concurrent package
        concurrent.futures — Launching parallel tasks
        subprocess — Subprocess management
        sched — Event scheduler
        queue — A synchronized queue class
        contextvars — Context Variables
        _thread — Low-level threading API
    Мережа та міжпроцесна комунікація
        asyncio — Asynchronous I/O
        socket — Low-level networking interface
        ssl — TLS/SSL wrapper for socket objects
        select — Waiting for I/O completion
        selectors — High-level I/O multiplexing
        signal — Set handlers for asynchronous events
        mmap — Memory-mapped file support
    Обробка даних в Інтернеті
        email — An email and MIME handling package
        json — JSON encoder and decoder
        mailbox — Manipulate mailboxes in various formats
        mimetypes — Map filenames to MIME types
        base64 — Base16, Base32, Base64, Base85 Data Encodings
        binascii — Convert between binary and ASCII
        quopri — Encode and decode MIME quoted-printable data
    Інструменти обробки структурованої розмітки
        html — Підтримка мови розмітки гіпертексту (HTML)
        html.parser — Simple HTML and XHTML parser
        html.entities — Definitions of HTML general entities
        Модулі обробки XML
        xml.etree.ElementTree — The ElementTree XML API
        xml.dom — The Document Object Model API
        xml.dom.minidom — Minimal DOM implementation
        xml.dom.pulldom — Support for building partial DOM trees
        xml.sax — Support for SAX2 parsers
        xml.sax.handler — Base classes for SAX handlers
        xml.sax.saxutils — SAX Utilities
        xml.sax.xmlreader — Interface for XML parsers
        xml.parsers.expat — Fast XML parsing using Expat
    Інтернет-протоколи та підтримка
        webbrowser — Convenient web-browser controller
        wsgiref — WSGI Utilities and Reference Implementation
        urllib — модулі обробки URL
        urllib.request — Extensible library for opening URLs
        urllib.response — Response classes used by urllib
        urllib.parse — Parse URLs into components
        urllib.error — Exception classes raised by urllib.request
        urllib.robotparser — Parser for robots.txt
        http — HTTP modules
        http.client — HTTP protocol client
        ftplib — FTP protocol client
        poplib — POP3 protocol client
        imaplib — IMAP4 protocol client
        smtplib — SMTP protocol client
        uuid — UUID objects according to RFC 4122
        socketserver — A framework for network servers
        http.server — HTTP servers
        http.cookies — HTTP state management
        http.cookiejar — Cookie handling for HTTP clients
        xmlrpc — XMLRPC server and client modules
        xmlrpc.client — XML-RPC client access
        xmlrpc.server — Basic XML-RPC servers
        ipaddress — IPv4/IPv6 manipulation library
    Мультимедійні послуги
        wave — Read and write WAV files
        colorsys — Conversions between color systems
    Інтернаціоналізація
        gettext — Multilingual internationalization services
        locale — Internationalization services
    Програмні рамки
        turtle — Графіка черепахи
        cmd — Support for line-oriented command interpreters
        shlex — Simple lexical analysis
    Графічний інтерфейс користувача з Tk
        tkinter — Python interface to Tcl/Tk
        tkinter.colorchooser — Color choosing dialog
        tkinter.font — Tkinter font wrapper
        Діалоги Tkinter
        tkinter.messagebox — Tkinter message prompts
        tkinter.scrolledtext — Scrolled Text Widget
        tkinter.dnd — Drag and drop support
        tkinter.ttk — Tk themed widgets
        IDLE
    Засоби розробки
        typing — Підтримка підказок типу
        pydoc — Documentation generator and online help system
        Режим розробки Python
        doctest — Test interactive Python examples
        unittest — Unit testing framework
        unittest.mock — mock object library
        unittest.mock — getting started
        test — Regression tests package for Python
        test.support — Утиліти для набору тестів Python
        test.support.socket_helper — Утиліти для тестування сокетів
        test.support.script_helper — Утиліти для тестів виконання Python
        test.support.bytecode_helper — Інструменти підтримки для тестування правильної генерації байт-коду
        test.support.threading_helper — Утиліти для потокових тестів
        test.support.os_helper — Утиліти для тестування ОС
        test.support.import_helper — Утиліти для імпортування тестів
        test.support.warnings_helper — Утиліти для перевірки попереджень
    Налагодження та профілювання
        Таблиця подій аудиту
        bdb — Debugger framework
        faulthandler — Dump the Python traceback
        pdb — Налагоджувач Python
        Профайлери Python
        timeit — Measure execution time of small code snippets
        trace — Trace or track Python statement execution
        tracemalloc — Trace memory allocations
    Упаковка та розповсюдження програмного забезпечення
        ensurepip — Bootstrapping the pip installer
        venv — Creation of virtual environments
        zipapp — Manage executable Python zip archives
    Служби виконання Python
        sys — System-specific parameters and functions
        sys.monitoring — Execution event monitoring
        sysconfig — Provide access to Python’s configuration information
        builtins — Built-in objects
        __main__ — Top-level code environment
        warnings — Warning control
        dataclasses — Data Classes
        contextlib — Утиліти для контекстів операторів with
        abc — Abstract Base Classes
        atexit — Exit handlers
        traceback — Print or retrieve a stack traceback
        __future__ — Future statement definitions
        gc — Garbage Collector interface
        inspect — Inspect live objects
        site — Site-specific configuration hook
    Спеціальні інтерпретатори Python
        code — Interpreter base classes
        codeop — Compile Python code
    Імпорт модулів
        zipimport — Import modules from Zip archives
        pkgutil — Package extension utility
        modulefinder — Find modules used by a script
        runpy — Locating and executing Python modules
        importlib — Реалізація import
        importlib.resources – Package resource reading, opening and access
        importlib.resources.abc – Abstract base classes for resources
        importlib.metadata – Accessing package metadata
        The initialization of the sys.path module search path
    Служби мови Python
        ast — Abstract Syntax Trees
        symtable — Access to the compiler’s symbol tables
        token — Constants used with Python parse trees
        keyword — Тестування ключових слів Python
        tokenize — Tokenizer for Python source
        tabnanny — Виявлення неоднозначних відступів
        pyclbr — Python module browser support
        py_compile — Compile Python source files
        compileall — Byte-compile Python libraries
        dis — Disassembler for Python bytecode
        pickletools — Tools for pickle developers
    Спеціальні служби MS Windows
        msvcrt — Useful routines from the MS VC++ runtime
        winreg — Windows registry access
        winsound — Sound-playing interface for Windows
    Спеціальні служби Unix
        posix — The most common POSIX system calls
        pwd — The password database
        grp — The group database
        termios — POSIX style tty control
        tty — Terminal control functions
        pty — Pseudo-terminal utilities
        fcntl — The fcntl and ioctl system calls
        resource — Resource usage information
        syslog — Unix syslog library routines
    Modules command-line interface (CLI)
    Замінені модулі
        getopt — C-style parser for command line options
    Removed Modules
    Міркування безпеки


"""

# help('modules')
# help('calendar')
# help('zlib')

import math
print(math.pi)
print(math.pow(5, 7))

print(type(math))

print(dir(math))