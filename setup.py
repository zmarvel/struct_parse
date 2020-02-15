import setuptools

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='struct_parse',
    version='0.0.1',
    author='Zack Marvel',
    author_email='zpmarvel@gmail.com',
    description='Parse struct definitions like those used in the struct module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/zmarvel/struct_parse',
    project_urls={
        'Bug Tracker': 'https://github.com/zmarvel/struct_parse/issues',
        'Documentation': 'https://struct-parse.readthedocs.io/',
        'Source Code': 'https://github.com/zmarvel/struct_parse',
    },
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.6',
)
