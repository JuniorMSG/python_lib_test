# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: C:\Users\tures\AppData\Local\Programs\Python\Python38\Lib\site-packages\_pyinstaller_hooks_contrib\hooks\rthooks\pyi_rth_certifi.py
import os, ssl, sys
if ssl.get_default_verify_paths().cafile is None:
    os.environ['SSL_CERT_FILE'] = os.path.join(sys._MEIPASS, 'certifi', 'cacert.pem')
# okay decompiling pyi_rth_certifi.pyc
