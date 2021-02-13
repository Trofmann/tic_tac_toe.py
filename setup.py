from cx_Freeze import setup, Executable

executables = [Executable('tic_tac_toe.py', base='Win32GUI')]

includes = ['pygame', 'settings', 'button', 'game_functions', 'entry_pole']

options = {
    'build_exe': {
        'includes': includes,
        'build_exe': 'Tic-Tac-Toe'
    }
}

setup(name='tic_tac_toe',
      version='1.0.0',
      description='My app',
      executables=executables,
      options=options)
