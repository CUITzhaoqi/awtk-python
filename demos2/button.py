
import os
import sys

from src.python.awtk import *

s_preload_nr = 0
s_preload_res = ["earth", "dialog_title", "rgb", "rgba"]

def on_clicked(win, e):
    evt = TEvent.cast(e)
    btn = TWidget.cast(evt.target)
    p = TPointerEvent.cast(e)

    print('click at x=' + str(p.x) + " y=" + str(p.y))
    print('click:' + btn.get_text() + ' in ' + win.name)
    TGlobal.quit()

    return TRet.OK

def on_window_to_background(win, e):
    evt = TEvent.cast(e)
    win = TWidget.cast(evt.target)
    print('%s, to_background' % win.name)

    return TRet.OK

def on_window_to_foreground(win, e):
    evt = TEvent.cast(e)
    win = TWidget.cast(evt.target)
    print('%s, to_foreground' % win.name)

    return TRet.OK


def windows_open(name, to_close):
    if to_close is None:
        win = TWindow.open(name)
    else:
        win = TWindow.open_and_close(name, to_close)
    win.on(TEventType.WINDOW_TO_BACKGROUND, on_window_to_background, win)
    win.on(TEventType.WINDOW_TO_FOREGROUND, on_window_to_foreground, win)
    install_click_hander(win)

    return TRet.OK

def on_context_menu(ctx, e) :
    windows_open(ctx, None);
    return TRet.OK

def on_open_window(ctx, e) :
    print(ctx)
    windows_open(ctx, None);
    return TRet.OK


def on_paint_vgcanvas(ctx, e) :
    tp = TPaintEvent.cast(e)
    c = tp.c
    vg = c.get_vgcanvas()
    # vg.save()
    # vg.translate(c.ox, c.oy)
    # vg.set_line_width(1)
    # tc = TColor.create(0, 0xff, 0, 0xff)
    # vg.set_stroke_color(tc.color)
    # vg.set_fill_color(tc.color)
    #
    # vg.translate(5, 5)
    # vg.rounded_rect(0, 0, 60, 40, 1)
    # vg.fill()
    #
    # vg.restore()
    return TRet.OK


def install_one(win, iter):
    print(win.name)
    widget = TWidget.cast(iter)
    name = str(widget.name)
    print(name)
    index = name.find("open:")
    if index >= 0:
        print(name[5:len(name)])
        widget.on(TEventType.CLICK, on_open_window, name[5:len(name)])
        widget.on(TEventType.LONG_PRESS, on_open_window, name[5:len(name)])
        if name == "open:menu_point":
            widget.on(TEventType.CONTEXT_MENU, on_context_menu, widget)
    else:
        if name == "paint_linear_gradient":
            pass
        elif name == "paint_radial_gradient":
            pass
        elif name == "paint_stroke_gradient":
            pass
        elif name == "paint_vgcanvas":
            widget.on(TEventType.PAINT, on_paint_vgcanvas, widget)
            pass
        elif name == "snapshot":
            pass
        elif name == "memtest":
            pass
        elif name == "reload_theme":
            pass
        elif name == "show_fps":
            pass
        elif name == "clone_self":
            pass
        elif name == "clone_tab":
            pass
        elif name == "remove_self":
            pass
        elif name == "chinese":
            pass
        elif name == "english":
            pass
        elif name == "font_small" or name == "font_normal" or name == "font_big":
            pass
        elif name == "inc_value":
            pass
        elif name == "dec_value":
            pass
        elif name == "close":
            pass
        elif name == "fullscreen":
            pass
        elif name == "start":
            pass
        elif name == "pause":
            pass
        elif name == "stop":
            pass
        elif name == "key":
            pass
        elif name == "backspace":
            pass
        elif name == "quit":
            pass
        elif name == "back_to_home":
            pass
        elif name == "exit":
            pass
        elif name == "pages":
            pass
        elif name == "combo_box":
            pass
        pass
    return TRet.OK


def install_click_hander(win):
    win.foreach(install_one, win)
    return TRet.OK


def on_timer(win, e):
    evt = TTimerInfo.cast(e)
    print("id = " + str(evt.id))
    print(str(evt.now))
    print(str(evt.ctx))
    # test = TWidget.cast(evt.ctx)
    # print(test.name)
    bar = win.lookup("bar", True)
    status = win.lookup("status", True)

    global s_preload_nr
    if s_preload_nr == len(s_preload_res) - 1:
        TWindow.open("system_bar")
        windows_open("main", win)
        print("main")
        return TRet.OK
    else:
        print(s_preload_res[s_preload_nr])
        TImageManager.preload(TImageManager.instance(), s_preload_res[s_preload_nr])
        s_preload_nr = s_preload_nr + 1
        value = (s_preload_nr * 100) / len(s_preload_res)
        text = 'Load, %s(%u/%u)' % (s_preload_res[s_preload_nr], s_preload_nr, len(s_preload_res))
        bar.set_value(int(value))
        status.set_text(text)

    return TRet.REPEAT



def application_init():
    # win = TWindow.create_default()
    # btn = TButton.create(win, 0, 0, 0, 0)
    #
    # win.set_name("main")
    # btn.set_name("close")
    # btn.set_text("Close")
    # btn.set_self_layout_params("center", "middle", "50%", "30")
    #
    # btn1 = TButton.create(win, 0, 0, 0, 0)
    # btn1.set_name("test")
    # btn1.set_text("Test")
    # btn1.set_self_layout_params("center", "middle:50", "50%", "30")
    # btn1.on(TEventType.CLICK, on_test_add, win)
    #
    # print(win.lookup("close", 100).name)
    # win.layout()
    win = TWindow.open("preload")
    id = TTimer.add(on_timer, win, 100);
    print("id = " + str(id))
    # win.lookup("close", True).on(TEventType.CLICK, on_close_clicked, win);
    # win.lookup("inc_value", True).on(TEventType.CLICK, on_inc_clicked, win);
    # win.lookup("dec_value", True).on(TEventType.CLICK, on_dec_clicked, win);

    win.layout();


