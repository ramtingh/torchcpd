from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='torchcpd',
      version='1.0.1',
      description='PyTorch Implementation of the Coherent Point Drift Algorithm',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/ramtingh/torchcpd',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering',
      ],
      keywords='image processing, point cloud, registration, mesh, surface',
      author='Ramtin Gharleghi',
      author_email='ramtin@ramt.in',
      license='MIT',
      packages=['torchcpd'],
      install_requires=['numpy'],
      zip_safe=False)
