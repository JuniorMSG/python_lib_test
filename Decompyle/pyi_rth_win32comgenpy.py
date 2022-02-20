# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\tures\AppData\Local\Programs\Python\Python38\Lib\site-packages\PyInstaller\hooks\rthooks\pyi_rth_win32comgenpy.py
import atexit, os, shutil, tempfile
supportdir = tempfile.mkdtemp()
genpydir = os.path.join(supportdir, 'gen_py')
try:
    os.makedirs(genpydir)
    atexit.register((shutil.rmtree), supportdir, ignore_errors=True)
except OSError:
    pass
else:
    import win32com
    win32com.__gen_path__ = genpydir
    if hasattr(win32com, '__loader__'):
        del win32com.__loader__
    import win32com.gen_py
    win32com.gen_py.__path__.insert(0, genpydir)
# okay decompiling pyi_rth_win32comgenpy.pyc
