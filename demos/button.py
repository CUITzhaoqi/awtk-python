
import os
import sys
CWD=os.getcwd()
print(CWD)
AWTK_PYTHON_ROOT=os.path.normpath(os.path.join(CWD, '../src/python'));
sys.path.insert(0, CWD);
sys.path.insert(0, './demos');
sys.path.insert(0, AWTK_PYTHON_ROOT);
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

    # as = TAssetsManager.instance();

    print(win.lookup("close", 100).name)
    win.layout();


# TGlobal.init(800, 480, TAppType.DESKTOP, "test", "../")
TAssetsManager.set_theme(TAssetsManager.instance(), theme="default")
# TAssetsManager.add(TAssetsManager.instance(),info="test")
application_init()
TGlobal.run()