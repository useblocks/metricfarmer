.. _targets:

Targets
=======

Targets care about the final handling of metric results, after all measurements have been executed.

They are normally storing the results in a specific format on a specific system. E.g. locally as csv file or
as entry on a metric system like `Prometheus <https://prometheus.io>`_.


There is no direct link between a metric and a target, as a metric does not need to know, how its result
get handled.

Targets get selected by the user during the call of Metric-Farmer, e.g. ``metricfarmer print``, or by using the related
:ref:`settings`: :ref:`target_default` or :ref:`target_always`.

.. contents::
   :local:

Define own targets
------------------
Targets can be defined in each ``.farm``-file. After definition they can directly be selected and used by the user.

Example:

.. code-block:: json

   {
     "targets": {
       "file_csv": {
         "class": "mf.file_csv",
         "description": "Stores metric results in a csv file.",
         "path": "metric_results.csv",
         "override": false,
         "delimiter": ","
       }
     }
   }

Targets must have an unique name, which is used only once in all loaded ``.farm``-files.

They also need to reference a ``target class`` of a loaded extension::

   "file_csv": {
     "class": "mf.file_csv"
   }

The ``target class`` defines what other parameters are needed.
So please take a look into the related documentation of target classes.

Run ``metricfarmer --list`` to get a list off all extension and their provided target classes.


Available target classes
------------------------

This list shows only  target classes provided by Metric-Farmer. If you have installed some extensions, this list might
be much bigger. Please run ``metricfarmer --list`` to see what is really available on your system.

mf.print
~~~~~~~~
Prints the result on the command line.

Does not support any parameters.

mf.print_json
~~~~~~~~~~~~~

Prints the result as json format on the command line.

Does not support any parameters.

mf.file_text
~~~~~~~~~~~~

Writes the results to a text file.

.. list-table:: Parameters
   :widths: 20 50 20 10
   :header-rows: 1
   :stub-columns: 1

   * - Parameter
     - Description
     - Default
     - Required
   * - path
     - File path to use
     - metric_results.txt
     - No
   * - override
     - If true, existing file gets replace, otherwise an error is thrown
     - False
     - No

mf.file_json
~~~~~~~~~~~~
Writes the results to a json file.

Same out put as target ``print_json``.

.. list-table:: Parameters
   :widths: 20 50 20 10
   :header-rows: 1
   :stub-columns: 1

   * - Parameter
     - Description
     - Default
     - Required
   * - path
     - File path to use
     - metric_results.txt
     - No
   * - override
     - If true, existing file gets replace, otherwise an error is thrown
     - False
     - No

mf.file_csv
~~~~~~~~~~~
Writes the results to a csv file.

If ``override`` is set to false and a csv file already exists, new results with get added.


.. list-table:: Parameters
   :widths: 20 50 20 10
   :header-rows: 1
   :stub-columns: 1

   * - Parameter
     - Description
     - Default
     - Required
   * - path
     - File path to use
     - metric_results.txt
     - No
   * - override
     - If true, existing file gets replace, otherwise an error is thrown
     - False
     - No
   * - delimiter
     - Character to use as delimiter in csv file
     - ,
     - No

