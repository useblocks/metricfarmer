.. _sources:

Sources
=======

A **source** defines and configures the way a metric shall get measured.

It normally contains a set of parameters, which are shared between all metrics, which use this source.
But each metric can override specific parameters for its own measurement.

A metric must reference a ``source type`` defined in a ``.farm``-file.
And a ``source type`` needs to reference a ``source class``, which is provided by Metric-Farmer extensions and defined
as a function in a Python file.

**Context example**

Image you are working for a company. This company is using **Jira** for their issue systems.
Two different Jira installation exist: One for development tasks and one for product requirements.

The needed functions to access this Jira systems and measure metrics are the same, therefore only one ``source class``
is needed, which must be provided by an Metric-Farmer extension.

But both systems are available on different URLs and use different credentials.
So two ``source types`` are needed, to store the different urls and credentials as parameters.
These ``source types`` must be configured by the user in a ``.farm``-file.

The needed metrics can then measure the needed JIRA system by referencing the correct ``source type``.
The metrics itself are only setting a filter parameter to get the needed data.


.. uml::

   @startuml
      hide stereotype
      skinparam defaultTextAlignment center
      skinparam nodeFontColor<<jira_style>> #fff

      node "**Open tasks user A**\n(metric)" as ma #ffcc00
      node "**Open tasks user B**\n(metric)" as mb #ffcc00
      node "**Open requirements user A**\n(metric)" as mc #ffcc00

      node "**Task Jira system**\n(source type)" as ta #abc837
      node "**Requirement Jira system**\n(source type)" as tb #abc837


      node "**Jira**\n(source class)" <<jira_style>> as c #483e37

      ma --> ta
      mb --> ta

      mc --> tb

      ta --> c
      tb --> c

   @enduml

.. contents::
   :local:

Source types
------------

``Source types`` are referenced by metrics and add a use-case specific configuration to a normally
not configured ``source class``.

**Example**: Referenced source in a metric definition

.. literalinclude:: ../../tests/farmer_files/simple/my_metrics.farm

Both metrics use the same source ``html_file_count``, but the last metric also overrides the ``path`` parameter.

**Example**: Referenced source class in a source definition

.. literalinclude:: ../../tests/farmer_files/simple/my_sources.farm

This source references the source class ``mf.file_count``.
``mf`` is the namespace of the extension (here Metric-Farmer) and ``file_count`` is the source function to call.

.. _own_sources:

Create own sources
~~~~~~~~~~~~~~~~~~

Sources get defined in the ``sources`` section of a ``.farm``-file.

Example::

   {
      "metrics": {}
      "sources": {
         "my_source": {
            "class": "mf.file_count",
            "description": "Counts all c-files in all subfolders"
            "pattern": "**/*.c"
         }
      }
      "targets": {}
   }

They must have a ``class`` parameter, which must contain a string to reference a ``source class``
from a Metric-Farmer extension. Run ``metricfarmer --list`` to sell all available source classes.

They should also have a ``description`` parameter for documentation.

All other needed parameters are based on the selected ``source class``.
So please take a look into their documentation to find out which parameters are available and are mandatory.

Defined ``sources`` can be used and referenced in all other ``.farm``-files.

.. _predefined_sources:

Use predefined sources
~~~~~~~~~~~~~~~~~~~~~~

Metric-Farmer provides the predefined sources ``static``, ``random`` and ``file_count``.
They are used mainly for examples and simple use cases.

This is the content of the ``.farm``-file, which defines the predefined sources:

.. literalinclude:: ../../metricfarmer/basics/sources.farm
   :language: json

**Usage example**:

.. literalinclude:: ../../tests/farmer_files/predefined/metrics.farm
   :language: json


Source classes
--------------

A ``source class`` is the link to a python function, which does the specific measurement work.
They are provided by Metric-Farmer extensions.

For all available source classes on your installation, please execute ``metricfarmer --list``.

If you wish to create your own ``source class`` please take a look into :ref:`extensions`.

