<h1 align="center">
  <img src="./doc/img/logo.png" alt="AWTK" width="200">
  <br>
  AWTK
  <br>
</h1>

# awtk-python

ZLG 开源 GUI 引擎 [awtk](https://github.com/zlgopen/awtk) 针对 Python [Python](https://python.org) 的绑定。

[![Build status](https://travis-ci.com/CUITzhaoqi/awtk-python.svg?branch=master)](https://travis-ci.com/github/CUITzhaoqi/awtk-python/)
[![License](https://img.shields.io/badge/license-GPL%20V2-blue.svg?longCache=true)](https://www.gnu.org/licenses/gpl-2.1.en.html)
[![License](https://img.shields.io/badge/platform-linux--64%20%7C%20win--32%20%7C%20osx--64%20%7C%20win--64-lightgrey)]()


## 准备

> 请先安装 Python [Python](https://python.org)

### 方式一

1. 获取 awtk 并编译

```
git clone https://github.com/zlgopen/awtk.git
cd awtk; scons; cd -
```

> AWTK 的编译环境请参考 AWTK 的文档。

2. 获取 awtk-python 并编译

```
git clone https://github.com/zlgopen/awtk-python.git
cd awtk-python
scons
```

### 方式二

1. 获取 awtk 并编译

```
git clone https://github.com/zlgopen/awtk.git build/awtk
cd awtk; scons; cd -
```

> AWTK 的编译环境请参考 AWTK 的文档。

```
git clone https://github.com/CUITzhaoqi/awtk-python.git
cd awtk-python
python setup.py install
```

## 运行

### 方式一

```
./bin/awtkRun demos/button.py
```

> 请把 xxxx.py 换成具体的 py 文件。

```
./bin/awtkRun demos/button.py
```

### 方式二

```
python demos/button.py
```

## 更新绑定(由本项目的维护人员完成)

```
./sync.sh
```

> 在非 bash 终端（如 Windows 平台的 cmd.exe)，需要根据 sync.sh 的内容手工执行相应的命令。

## 文档

* [AWTK 脚本绑定原理](https://github.com/zlgopen/awtk/blob/master/docs/script_binding.md)


> 本文以 Linux/MacOS 为例，Windows 可能会微妙差异，请酌情处理。

## 注意事项

* 编译 PC 版本，请把 src/c/main.c 中的APP\_SIMULATOR 改成 APP\_DESKTOP，并重新编译。

## 示例

### 方式一

```python
from awtk import *

def on_clicked(win, e): 
    evt = TEvent.cast(e);
    btn = TWidget.cast(evt.target);
    p = TPointerEvent.cast(e);

    print('click at x=' + str(p.x) + " y=" + str(p.y));
    print('click:' + btn.get_text() + ' in ' + win.name);
    TGlobal.quit()

    return TRet.OK;

def application_init():
    win = TWindow.create_default()
    btn = TButton.create(win, 0, 0, 0, 0); 

    win.set_name("main");
    btn.set_name("close");
    btn.set_text("Close");
    btn.set_self_layout_params("center", "middle", "50%", "30");
    btn.on(TEventType.CLICK, on_clicked, win);

    win.layout();

application_init()
```

### 方式二

```python
import os
import sys
CWD=os.getcwd()
print(CWD)
AWTK_PYTHON_ROOT=os.path.normpath(os.path.join(CWD, '../src/python'))
sys.path.insert(0, CWD)
sys.path.insert(0, './demos')
sys.path.insert(0, './')
sys.path.insert(0, AWTK_PYTHON_ROOT)
from awtk import *
from basic import *

def on_clicked(win, e):
    evt = TEvent.cast(e)
    btn = TWidget.cast(evt.target)
    p = TPointerEvent.cast(e)

    print('click at x=' + str(p.x) + " y=" + str(p.y))
    print('click:' + btn.get_text() + ' in ' + win.name)
    TGlobal.quit()

    return TRet.OK

def on_test_add(win, e):
    evt = TEvent.cast(e)
    btn = TWidget.cast(evt.target)
    p = TPointerEvent.cast(e)

    print('click at x=' + str(p.x) + " y=" + str(p.y))
    print('click:' + btn.get_text() + ' in ' + win.name)
    btn.set_text("click")

    return TRet.OK

def application_init():
    win = TWindow.create_default()
    btn = TButton.create(win, 0, 0, 0, 0)

    win.set_name("main")
    btn.set_name("close")
    btn.set_text("Close")
    btn.set_self_layout_params("center", "middle", "50%", "30")

    btn1 = TButton.create(win, 0, 0, 0, 0)
    btn1.set_name("test")
    btn1.set_text("Test")
    btn1.set_self_layout_params("center", "middle:50", "50%", "30")
    btn1.on(TEventType.CLICK, on_test_add, win)

    print(win.lookup("close", 100).name)
    win.layout()


TGlobal.init(800, 480, TAppType.DESKTOP, "button_test", "../")
TAssetsManager.set_theme(TAssetsManager.instance(), theme="default")
TGlobal.assets_init()
application_init()
TGlobal.run()
```

## 使用限制

### 方式一

- 目前不能进行调试
- 适合开发完成之后，发布应用

### 方式一

- 可以进行调试
- 目前不太完善