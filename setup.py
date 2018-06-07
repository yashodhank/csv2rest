import setuptools


setuptools.setup(name='csv2rest',
                 version='0.0.1',
                 description="CSV to REST API",
                 long_description=open('README.md').read().strip(),
                 author="David Côté-Tremblay",
                 author_email="imdc.technologies@gmail.com",
                 url='https://github.com/dctremblay/csv2rest',
                 py_modules=['csv2rest'],
                 install_requires=[],
                 license='Apache License 2.0',
                 zip_safe=False,
                 keywords='rest api csv',
                 classifiers=['Packages'])
