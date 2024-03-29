# puttier
Change colors to putty sessions or export a theme to the clipboard in json for Visual Studio Code.
# Description
It is possible to use the command line tool, example:

```sh
py.exe -m puttier.nogui
```

or the GUI:

```sh
py.exe -m puttier
```
put
Below a screenshot of the UI

![Alt text](example.png?raw=true "Example")

 Note: the terminal displayed in the UI is a reproduction.

# Quick how to
Donwload release 1.0 from https://github.com/anonimoanemico/puttier/archive/refs/tags/v.1.0.0.zip
Unzip in a folder
Select file name ```gui.py```
Right click to ```open with Python3```
![image](https://github.com/anonimoanemico/puttier/assets/19540260/bb3b4213-7eac-44cb-9fea-f53daa937244)

# Build and install
Otherwise you can build the egg package and run the executable, with the following steps:

## Prerequisits
If you don't have build
```sh
py -m pip install build
```

## Build
```sh
git clone https://github.com/anonimoanemico/puttier.git
cd puttier
py -m build
```

## Install
Using pip3 or another pip version

```sh
py -m pip install .\dist\puttier-0.0.4-py3-none-any.whl
```

## Run
If your PATH variable contains the path to your Python script folder than you can simply execute:

```sh
puttier
```

Otherwise locate  where Scripts are installed (normally in Scripts folder inside your local Python install dir) and do:
```sh
cd C:\Users\MYUSER\AppData\Local\Programs\Python\Python39\Scripts
puttier
```


# Credits

Color schemas are kindly provided:
- mbadolato project: https://github.com/mbadolato repository https://github.com/mbadolato/iTerm2-Color-Schemes
- jacektrocinski https://github.com/jacektrocinski repository https://github.com/jacektrocinski/pretty-putty
- teeli https://github.com/teeli repository https://raw.githubusercontent.com/teeli/dracula-putty

Thanks all contributors for sharing those files!
