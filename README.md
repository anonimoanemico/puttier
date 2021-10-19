# puttier
Change colors to putty sessions.

It is possible to use the command line tool, example:

```sh
py.exe -m puttier.nogui
```

or the GUI:

```sh
py.exe -m puttier
```

Below a screenshot of the UI

![Alt text](example.png?raw=true "Example")

 Note: the terminal displayed in the UI is a reproduction.

# Build and install
Otherwise you can build the egg package and run the executable, with the following steps:
## Build
```sh
git clone git@github.com:anonimoanemico/puttier.git
cd puttier
py -m build
```

## Install
Using pip3 or another pip version

```sh
pip3 install .\dist\puttier-0.0.2-py3-none-any.whl
```
## Run
```sh
puttier
```


# Credits

Color schemas are kindly provided:
- mbadolato project: https://github.com/mbadolato repository https://github.com/mbadolato/iTerm2-Color-Schemes
- jacektrocinski https://github.com/jacektrocinski repository https://github.com/jacektrocinski/pretty-putty
- teeli https://github.com/teeli repository https://raw.githubusercontent.com/teeli/dracula-putty

Thanks all contributors for sharing those files!
