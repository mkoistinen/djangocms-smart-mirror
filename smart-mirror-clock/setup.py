from setuptools import setup, find_packages

from smart_mirror_clock import __version__

setup(
    name="smart-mirror-clock",
    version=__version__,
    url='',
    license='MIT',
    description="Simple clock for a smart mirror",
    long_description=open('README.rst').read(),
    author='Martin Koistinen',
    author_email='mkoistinen@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "Django >= 1.7",
        "django-cms >= 3.1",
    ],
    include_package_data=True,
    zip_safe=False,
)
