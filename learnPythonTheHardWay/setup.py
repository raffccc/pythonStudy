try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup
    
config = {
    'description': 'My Project',
    'author': 'Rafael Figueiredo',
    'url': 'www.teste.com.br',
    'download_url': 'blablabla',
    'author_email': 'rafaelfigueiredoc@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['classStudy'],
    'scripts': [],
    'name': 'Estudo'
}

setup(**config)