from setuptools import setup

setup(name='MarconiDashboard',
      version='0.1',
      description='Simple dashboard for Marconi',
      author='Flavio Percoco',
      author_email='flaper87@flaper87.org',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['pbr', 'setuptools-git',
                        'Flask==0.10.1', 'Flask-Bootstrap',
                        'flask-appconfig', 'flask-wtf',
                        'python-marconiclient>=0.0.1a1'])
