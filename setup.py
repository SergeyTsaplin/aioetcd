from setuptools import find_packages, setup


with open('README.md') as fd:
    long_description = fd.read()


install_requires = [
    'aiohttp'
]

setup(
    name='aioetcd',
    version='0.1.0',
    author='Sergey Tsaplin',
    author_email='me@sergeytsaplin.com',
    description='etcd v2 client for AsyncIO',
    long_description=long_description,
    license='MIT',
    url='https://github.com/SergeyTsaplin/aioetcd',
    packages=find_packages(exclude=['test', 'examples']),
    install_requires=install_requires,
    include_package_data=True,
    python_requires='>=3.5.3',
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
