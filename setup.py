import re

from setuptools import setup


version = ''
with open('nextcord/ext/lava/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Version is not set')

setup(
    name='nextcord-ext-lava',
    packages=['nextcord.ext.lava'],
    version=version,
    description='A fork of lavalink.py built for nextcord',
    author='nextcord-ext',
    author_email='VincentRPS@gmail.com',
    url='https://github.com/nextcord-ext/lava',
    download_url='https://github.com/nextcord-ext/lava/archive/{}.tar.gz'.format(version),
    keywords=['lavalink'],
    include_package_data=True,
    install_requires=['aiohttp>=3.6.0,<3.7.0'],
    extras_require={'docs': ['sphinx',
                             'pygments',
                             'guzzle_sphinx_theme'],
                    'development': ['pylint',
                                    'flake8']}
)
