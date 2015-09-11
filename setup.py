try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

    config = {
                'description': 'Create RSS feed based on mp3 files',
                'author': 'Josh Wheeler',
                'url': 'https://github.com/mantlepro/pypodcaster',
                'download_url': 'https://github.com/mantlepro/pypodcaster/archive/master.zip',
                'author_email': 'mantlepro@gmail.com',
                'version': '0.1',
                'install_requires': ['Jinja2','eyeD3','pyyaml','validators'],
                'packages': ['pypodcaster'],
                'scripts': [],
                'name': 'pypodcaster'
                }

    setup(**config)