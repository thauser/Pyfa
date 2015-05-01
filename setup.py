"""
Distribution builder for pyfa.

Windows executable: python setup.py build
Windows executable + installer: python setup.py bdist_msi
"""

import sys

from cx_Freeze import setup, Executable

import config


app_name = 'pyfa'
app_version = '{}'.format(config.version)
app_description = 'Python fitting assistant'


packages = ['eos', 'gui', 'service', 'utils']
include_files = ['icons', 'staticdata', 'gpl.txt']
includes = []
excludes = ['Tkinter']


# Windows-specific options
build_options_winexe = {
    'packages': packages,
    'include_files': include_files,
    'includes': includes,
    'excludes': excludes,
    'compressed': True,
    'optimize': 2,
    'include_msvcr': True,
}

build_options_winmsi = {
    'upgrade_code': '{E80885AC-31BA-4D9A-A04F-9E5915608A6C}',
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\{}'.format(app_name),
}


# Mac-specific options (untested)
build_options_macapp = {
    'iconfile': 'dist_assets/mac/pyfa.icns',
    'bundle_name': app_name,
}

build_options_macdmg = {
    'volume_label': app_name,
    'applications-shortcut': True,
}


# Generic executable options
executable_options = {
    'script': 'pyfa.py',
    # Following are windows-specific options, they are stored
    # on a per-executable basis
    'base': 'Win32GUI' if sys.platform=='win32' else None,
    'icon': 'dist_assets/win/pyfa.ico',
    'shortcutDir': 'DesktopFolder',
    'shortcutName': app_name,
}


setup(
    name=app_name,
    version=app_version,
    description=app_description,
    options = {
        'build_exe': build_options_winexe,
        'bdist_msi': build_options_winmsi,
        'bdist_mac': build_options_macapp,
        'bdist_dmg': build_options_macdmg,
    },
    executables=[Executable(**executable_options)]
)