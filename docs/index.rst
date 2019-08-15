.. metric-farmer documentation master file, created by
   sphinx-quickstart on Sun Jun 30 21:37:21 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Metric-Farmer
=============

**Cares about your project metrics**

Metric-Farmer is a Python based command line application to collect and store metrics from different sources
to different targets.

The configuration is completely done by JSON-based ``farm``-files in a project folder called ``.farmer``.

Features
---------
Metric-Farmer is capable to collect metrics from following sources:

* static values
* random values
* file count

And sends them on the following targets:

* print output (text or json)
* file output (text or json)

Sources and targets can be easily extended by registering own configurations to the Metric-Farmer entry-point.

Quick start
-----------

Metric-Farmer is controlled mostly via file-based configurations. For a quick start, create the following elements:

1. Create a folder ``.farmer`` on your project root folder
2. Create a file inside ``.farmer`` called ``my_metrics.farm``
3. Add the following content to the file:

.. code-block:: json

   {
      "metrics": {
         "my_metric": {
            "source": {
               "type": "random",
            }
         }
      }
   }

4. On your project root level execute ``metricfarmer print``.


Motivation
----------


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   sources/index.rst
   targets/index.rst
   settings.rst
   extensions.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
