import setuptools
import io
import os


package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, 'README.rst')
with io.open(readme_filename, encoding='utf-8') as readme_file:
    readme = readme_file.read()


setuptools.setup(
    name="django-gcp-log-groups",
    version="0.1.3",
    author="Christie Grinham",
    author_email="christiegrinham@gmail.com",
    description="Python Django logging middleware to group messages on Google Cloud Platform",
    long_description=readme,
    url="https://github.com/christophski/django-gcp-log-groups",
    install_requires=[
          'google-cloud-logging',
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',

        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",

        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging",
    ],
)
