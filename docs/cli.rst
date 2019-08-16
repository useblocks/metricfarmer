Cli
===

This pages describes the command line interface (cli) of Metric-Farmer and its options and arguments.

.. contents::
   :local:

For a quick help, you can execute::

   metricfarmer --help

As output you will get::

   Usage: metricfarmer [OPTIONS] [TARGETS]...

     Measure metrics and execute TARGETS

   Options:
     -f, --farmer TEXT   Only uses the given farm folder
     -m, --metrics TEXT  Filter metrics for specific name
     -t, --tags TEXT     Filter metrics for tags
     --list              Show configuration information only
     --help              Show this message and exit.

Targets argument
----------------

Set one or multiple ``TARGETS`` to get the wished result handling after measurement.

Example::

   metricfarmer print file_json

You also can set no ``TARGETS`` argument, if you only want the measurement to be executed::

   metricfarmer


Options
-------

farmer
~~~~~~

Use ``-f`` or ``--farmer`` to define a single folder, which contains your farm files.

All other locations will **not** be loaded.

So predefined farm-files from Metric-Farmer, from user/home directory and from the current working directory will
be ignored.

Example::

   metricfarmer --farmer /temp/farmer_folder/ print

.. _option_metrics:

metrics
~~~~~~~

Use ``-f`` or ``--metrics`` to define a comma separated list of metric names, which shall get measured.
All other metrics will be ignored, if not also part of a :ref:`tag-filter <option_tags>`.

Example::

   metricfarmer --metrics my_metric,another_metric print

.. _option_tags:

tags
~~~~

Use ``-t`` or ``--tags`` to define a comma separated list of tags, which metrics must have to get measured.

A metric needs only to match **one** tag of the complete list to be taken into account for measurement.

Can be combined with a :ref:`metric name filter <option_metrics>`.

Example::

   metricfarmer --tags mf_examples,my_tag print


list
~~~~

Use ``--list`` to get detailed information of loaded extension and configurations files.

You also get lists of available metrics, tags, sources and targets.

Can **not** be combined with other options.

Example::

   metricfarmer --list

help
~~~~

Use ``--help`` to get the default help message.

Example::

   metricfarmer --help

