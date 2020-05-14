from demos2.button import *

TGlobal.init(800, 480, TAppType.DESKTOP, "AWTK_PYTHON_DEMO", "../")
TAssetsManager.set_theme(TAssetsManager.instance(), theme="default")
TGlobal.ext_widgets_init()
TGlobal.assets_init()
application_init()
TGlobal.run()