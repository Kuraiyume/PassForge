from setuptools import setup, find_packages

setup(
    name='passforge',
    version='0.2',
    description='PassForge is an advanced password generation tool designed to provide users with highly customizable and secure password options. It blends sophistication with flexibility, allowing users to craft passwords tailored to their specific needs, enhancing both security and usability in a user-friendly manner.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='veilwr4ith',
    author_email='hidetheveil@gmail.com',
    url='https://github.com/veilwr4ith/PassForge',
    packages=find_packages(),  # This will include the `passforge` package
    install_requires=[],
    entry_points={
        'console_scripts': [
            'passforge=passforge.passforge:main',  # Adjust 'main_function' to your entry point function
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


