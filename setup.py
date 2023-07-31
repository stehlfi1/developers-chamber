from setuptools import find_packages, setup

setup(
    name='skip-developers-chamber',
    version='0.0.70.2',
    description='A small plugin which help with development, deployment, git',
    keywords='django, skripts, easy live, git, bitbucket, Jira',
    author='Druids team',
    author_email='matllubos@gmail.com',
    url='https://github.com/skip-pay/developers-chamber',
    license='MIT',
    package_dir={'developers_chamber': 'developers_chamber'},
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'boto3<2',
        'click>=7.0',
        'click-completion==0.5.2',
        'coloredlogs==10.0',
        'gitpython==3.1.30',
        'isort>=5.12.0',
        'jira==2.0.0',
        'oauthlib==3.1.0',
        'pip-tools==6.13.0',
        'python-dotenv==0.14.0',
        'python-hosts==0.4.6',
        'requests>=2.23.0',
        'slack-sdk==3.21.3',
        'TogglPy==0.1.2',
        'unidecode==1.1.1',
    ],
    entry_points={'console_scripts': [
        'pydev=developers_chamber.bin.pydev:cli',
    ]},
    zip_safe=False,
)
