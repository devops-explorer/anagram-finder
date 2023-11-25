from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='Multiword Anagram Finder',
    version='1.0',
    author='Emre Gozutok',
    author_email='emre.gozutok@yandex.com',
    description='Description of your package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        "requests"
        # Add your dependencies here
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
