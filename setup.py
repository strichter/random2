from setuptools import setup

setup (
    name='random2',
    version='1.0.2',
    author = "PSF",
    description = "Python 3 compatible Python 2 `random` Module.",
    long_description = (
        open('CHANGES.rst').read()
        + '\n\n' +
        open('README.rst').read()
        ),
    license = "Python 2.1.1",
    keywords = "roman",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent'],
    url = 'http://pypi.python.org/pypi/random2',
    package_dir={"": "src"},
    py_modules=['random2'],
    include_package_data = True,
    test_suite = 'tests.test_suite',
    zip_safe = True,
    )
