import sys
import re
from distutils.core import setup, Extension

print(sys.executable)
sys.path.insert(0, '../awtk/')
import awtk_config as awtk

include_dirs = awtk.CPPPATH
extra_compile_args = awtk.CCFLAGS
print(extra_compile_args)

print (extra_compile_args.split( ))

extra_compile_args_list = extra_compile_args.split( )

for i in extra_compile_args_list:
    print(i)

    searchObj = re.match('\S[-D]', 'i')
    if searchObj :
        print(searchObj)
    else:
        print("Nothing found!!")



# # define_macros =
# extra_define_macros = [
# ("WIN32",None),
# ("_WIN32 ",None),
# ("WINDOWS ",None),
# ("WITH_ASSET_LOADER",None),
# ("WITH_FS_RES",None),
# ("WITH_ASSET_LOADER_ZIP",None),
# ("STBTT_STATIC",None),
# ("STB_IMAGE_STATIC",None),
# ("WITH_STB_IMAGE",None),
# ("WITH_VGCANVAS",None),
# ("WITH_UNICODE_BREAK",None),
# ("WITH_DESKTOP_STYLE",None),
# ("SDL2",None),
# ("HAS_STD_MALLOC",None),
# ("WITH_SDL",None),
# ("HAS_STDIO",None),
# ("HAVE_STDIO_H",None),
# ("WITH_IME_PINYIN",None),
# ("WITH_NANOVG_GPU",None),
# ("WITH_VGCANVAS_LCD",None),
# ("WITH_STB_FONT",None),
# ("WITH_NANOVG_GLES2",None),
# ("WITH_NANOVG_GL",None),
# ("_WIN64",None),
# ("SDL_REAL_API",None),
# ("SDL_HAPTIC_DISABLED",None),
# ("SDL_SENSOR_DISABLED",None),
# ("SDL_JOYSTICK_DISABLED",None),
# ("__STDC_LIMIT_MACROS",None),
# ("__STDC_FORMAT_MACROS",None),
# ("__STDC_CONSTANT_MACROS",None),
# ("_HAS_EXCEPTIONS","0"),
# ("_HAS_ITERATOR_DEBUGGING","0"),
# ("_ITERATOR_DEBUG_LEVEL","0"),
# ("_SCL_SECURE","0"),
# ("_SECURE_SCL","0"),
# ("_SCL_SECURE_NO_WARNINGS",None),
# ("_CRT_SECURE_NO_WARNINGS",None),
# ("_CRT_SECURE_NO_DEPRECATE",None),
#                        ]
#
# library_dirs=awtk.LIBPATH
# print(library_dirs)
# libraries=awtk.LIBS
# # libraries.remove("winmm.lib")
# # libraries.remove("imm32.lib")
# # libraries.remove("version.lib")
# # libraries.remove("shell32.lib")
# # libraries.remove("ole32.lib")
# # libraries.remove("Oleaut32.lib")
# # libraries.remove("Advapi32.lib")
# # libraries.remove("DelayImp.lib")
# # libraries.remove("psapi.lib")
#
# print(libraries)
#
# setup(name="awtk", version="0.0.1",
#       ext_modules=[Extension("awtk_native",
#                              ["src/c/awtk_native.c",
#                               "src/assets.c"],
#                              include_dirs=include_dirs,
#                              # extra_compile_args=extra_compile_args,
#                              define_macros=extra_define_macros,
#                              library_dirs=library_dirs,
#                              libraries=libraries,
#                              )])
