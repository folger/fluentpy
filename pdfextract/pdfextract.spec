# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:/folscode/fluentpy/pdfextract/pdfextract.py'],
             pathex=['D:\\fluentpy'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['tk', 'tcl', 'unicodedata', 'ssl'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries - TOC([
              ('libcrypto-1_1.dll', None, None),
          ]),
          a.zipfiles,
          a.datas,
          [],
          name='pdfextract',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
