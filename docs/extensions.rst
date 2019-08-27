.. _extensions:

Extensions
==========

Metric-Farmer can be easily extended by developers with own solutions for source and target types.

The reasons for this are the measurement from not yet supported sources (e.g. a department specific Excel list)
or the storage of measurement results on not yet supported targets (e.g. a specific company metric system like
`Prometheus <https://prometheus.io/>`_)

Concept
-------

Metric-Farmer can be extend by using the `entry-point <https://amir.rachum.com/blog/2017/07/28/python-entry-points/>`_
mechanism of `setuptools <https://setuptools.readthedocs.io/en/latest/>`_.

So a Metric-Farmer extension must be a valid Python package, which contains a ``setup.py`` file.

.. code-block:: python


   import os
   from setuptools import setup

   setup(
       name='Your extension',
         # ... More, but not for us important configurations
       entry_points={
           'metricfarmer': ['unimportant_name=your_package.your_modul:ExtensionClass']
       }
   )

During installation of this package, the ``entry_point`` content gets registered on the used Python environment.

For Metric-Farmer the entry-point entry must be a class, which inherits from
``metricfarmer.extensions.MetricFarmerExtension`` and must have common variables, which define sources and target types.

Metric-Farmer creates an instance of this class during startup.
From this point all defined sources and targets types of the extension are available.

A single Python package can register as many Metric-Farmer extensions as it likes.

Step by step introductions
--------------------------

1. Create a new folder ``my_project``
2. Create a ``setup.py`` file and a ``my_mf_extension.py`` inside the above folder.
3. For ``mf_my_extension.py`` use the following content.

.. code-block:: python

   from metricfarmer.extensions import MetricFarmerExtension

   def my_source_a(**kwargs):
      return 100

   def my_target_a(metrics, **kwargs):
      for metric in metrics.keys():
         print metric

   class MyExtension(MetricFarmerExtension):
       def __init__(self, app):
           self.app = app

           self.name = "My Extension"
           self.namespace = 'me'
           self.author = 'Awesome guy'
           self.description = 'Metric-Farmer extension...'

           self.source_classes = {
               'my_source': my_source_a
           }

           self.target_classes = {
               'my_target': my_target_a
           }

4. Then register this class inside your ``setup.py`` file:

.. code-block:: python
   :emphasize-lines: 14,15

   import os
   from setuptools import setup, find_packages

   setup(
       name='My extension project',
       version='0.0.1',
       license='MIT',
       author='Me',
       author_email='me@me.com',
       description='Collects and stores metrics for my project.',
       platforms='any',
       packages=find_packages(),
       install_requires=['metricfarmer'],
       entry_points={
           'metricfarmer': ['my_extension=my_project.mf_my_extension:MyExtension']
       }
   )

5. After that you need to install your package, so that Python is aware of the new entry_point entry:

.. code-block:: bash

   pip install -e .

6. Finally you should be able to address your source class with ``me.my_source`` and the target class
with ``me.my_target`` in the related ``class`` parameters of source/target type definitions.


Example
-------

Take a look into the source code of Metric Farmer, as it is using the entry-point mechanism to register all
available sources and targets.

Visit https://github.com/useblocks/metricfarmer/tree/master/metricfarmer/extensions to get an overview about all folders
and files.

The most important stuff is happening in file
`mf_extension.py <https://github.com/useblocks/metricfarmer/blob/master/metricfarmer/extensions/mf/mf_extension.py>`_.
There the needed class gets defined.

This class is then used in the `setup.py <https://github.com/useblocks/metricfarmer/blob/master/setup.py>`_ file as
value for the ``metricfarmer`` entry-point.





