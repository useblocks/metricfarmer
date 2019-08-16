Metrics
=======

Metrics can be defined inside any ``.farm``-file and must contain a unique name and a source configuration, which
describes how to measure the metric.

.. literalinclude:: ../tests/farmer_files/simple/my_metrics.farm
   :language: json
   :linenos:
   :emphasize-lines: 2,3,8

Metrics must be defined in the **metrics** section, which stores a dictionary for specific metrics  (line 2).

Each metric must be registered as element of this dictionary with an unique name (line 3 and 8).
The name must be unique in all used ``.farm``-files.

Parameters
----------
A metric can contain multiple parameters, which can be simple numbers or strings or list and complex dictionaries.

description
~~~~~~~~~~~
A ``description`` can be set to simplify the understanding and maintenance of your metrics for other users.

.. code-block:: json

   {
     "metrics": {
        "my_metric": {
           "description": "An awesome metric to measure awesome stuff",
           "source": {
             "type": "static"
           }
        }
     }
   }

source
~~~~~~

``source`` is the most important section of a metric, as it defines what gets measured and how.

.. literalinclude:: ../tests/farmer_files/simple/my_metrics.farm
   :language: json
   :linenos:
   :lines: 1-2,8-
   :emphasize-lines: 4-6

``source`` must be a dictionary and contain at least the parameter ``type`` (line 5).

``type`` must be a string and reference an existing and loaded :ref:`source type <sources>`.

The used ``source type`` defines what other parameters can be set and are used during measurement.
These parameters differs a lot between the different source types.
So take a look into the related source type documentation.

However, there aren't any checks, if additional parameters are really supported by the referenced ``source type``.
So you are free to set as many parameters as you like.


