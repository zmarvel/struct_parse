import setuptools

with open('README.md', 'r') as fh:
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
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)