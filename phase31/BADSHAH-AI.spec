# -*- mode: python ; coding: utf-8 -*-
a = Analysis(['main.py'], datas=[('.env.example','.'), ('README.md','.'), ('docs','docs')], hiddenimports=['dotenv','requests','rich','badshah_ai'], excludes=['pytest','streamlit','PyQt6'])
pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name='BADSHAH-AI', console=True)
coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas, name='BADSHAH-AI')
