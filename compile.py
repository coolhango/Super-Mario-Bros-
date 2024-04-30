from distutils.core import setup

import py2exe
import glob

setup(
    console=["main.py"],
    data_files=[
        ("sprites", glob.glob("sprites\\*.json")),
        ("sfx", glob.glob("sfx\\*.ogg") + glob.glob("sfx\\*.wav")),
        ("levels", glob.glob("levels\\*.json")),
        ("img", glob.glob("img\\*.gif") + glob.glob("img\\*.png")),
        ("", ["settings.json"]),
    ],
)
