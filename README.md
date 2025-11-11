# Contributions
Данный инструмент позволяет импортировать и отображать вклад в приватные проекты без копирования самого кода в один проект с макетом вклада, модифицирован под macOS на основе [оригинального](https://github.com/miromannino/Contributions-Importer-For-Github)
![](https://github.com/Deni0S/Contribution/blob/master/Image.webp)

## Инструкция по установкам
### Установить Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
### Установить Python
```bash
brew install python
python3 --version
pip3 --version
```
### Установить Git
```bash
brew install git
git --version
```

### Установить GitPython
`# Виртуальное окружение: Создаем Активируем Устанавливаем Проверяем`
```bash
python3 -m venv venv
source venv/bin/activate
pip install gitpython
python -c "import git; print('GitPython успешно установлен!')"
```
`# После окончания работы Деактивируем окружение и Удаляем папку окружения`
```bash
deactivate
rm venv
```

## Работа с импортом
1. Установить GitPython через виртуальное окружение
```bash
python3 -m venv venv
source venv/bin/activate
pip install gitpython
python -c "import git; print('GitPython успешно установлен!')"
```
2. Установить путь на папку содержащую в корне скрипты для импорта `Importer` и скрипт для запуска `RunImport.py`
3. Прописать пути к папкам приватных проектов где находится git `repo1 = git.Repo("Path/PrivateProject1/.git")` и указать их в массиве `importer = ImporterFromRepository([repo1, repo2], mock_repo)`
4. Прописать путь где находится пустой  git для сохранения вклада `mock_repo = git.Repo("Path/MockProjects/.git")`
5. Прописать почты для захвата избранных коммитов `importer.set_author(['work@email.ru', 'personal@email.ru'])`
6. Запустить скрипт импорта вклада
```bash
python RunImport.py
```
7. Деактивируем виртуальное окружение и Удаляем папку
```bash
deactivate
rm venv
```

## Примечания
Все команды выполняются в терминале\
Используйте python3 и pip3 вместо python/pip, чтобы избежать конфликтов со старыми версиями Python\
Если возникают ошибки прав
```bash
pip3 install --user gitpython
```
