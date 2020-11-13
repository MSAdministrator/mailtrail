from setuptools import setup, find_packages

def parse_requirements(requirement_file):
    with open(requirement_file) as f:
        return f.readlines()

version = dict()
with open("./mailtrail/utils/version.py") as fp:
    exec(fp.read(), version)


setup(
    name='mailtrail',
    version=version['__version__'],
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Retrieve and forward Exchange or Office 365 mail messages to logging infrastructure.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=parse_requirements('./requirements.txt'),
    keywords=['carcass'],
    url='https://github.com/MSAdministrator/mailtrail',
    author='MSAdministrator',
    author_email='rickardja@live.com',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    entry_points={
          'console_scripts': [
              'mailtrail = mailtrail.__main__:main'
          ]
    }
)