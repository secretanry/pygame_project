# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['E:\\misha\\PycharmProjects\\pygame\\pygame_project'],
             binaries=[],
             datas=[
		("res_cube.png","."),
		("res_die.png","."),
		("res_red_door.png","."),
		("res_fire.png","."),
		("res_flat.png","."),
		("res_down.png","."),
		("res_green_button.png","."),
		("res_green_door.png","."),
		("res_life.png","."),
		("res_red_door.png","."),
		("back.png","."),
		("you_win.png","."),
		("res_red_button.png","."),
		("res_shadow_block.png","."),
		("res_start.png","."),
		("res_unit.png", ".")
	     ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)     win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='mygame',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False)
