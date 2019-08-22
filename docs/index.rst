.. metric-farmer documentation master file, created by
   sphinx-quickstart on Sun Jun 30 21:37:21 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Metric-Farmer
=============

**Cares about your project metrics**

Metric-Farmer is a Python based command line application to collect and store metrics from different sources
to different targets.

It is designed to easily create and maintain complex metric measurements and to painless integrate its functions into
continuous integration systems (CI/CD) or local task executions (cron jobs).

The configuration is completely done by JSON-based ``farm``-files in a project folder called ``.farmer``.
And no development skills are needed to use Metric-Farmer.

Developers can easily create own Metric-Farmer extensions to provide custom solutions for sources and targets.
For instance to measure a company-internal service.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   cli
   metrics
   sources/index
   targets/index
   settings
   extensions

Features
---------
Metric-Farmer is capable to collect metrics from following :ref:`sources`:

* static values
* random values
* file count

And sends the results to the following :ref:`targets`:

* print output (text or json)
* file output (text or json)
* database output (sqlite)

Workflow
--------

.. uml::

   @startuml
   skinparam defaultTextAlignment center
   left to right direction

   skinparam cloud {
      FontColor #fff
      Backgroundcolor #483e37
   }

   node "**User**\ndefines metrics\n in //.farm files//" as dm #ffcc00
   node "**User/CI**\nexecutes Metric-Farmer" as em #ffcc00

   node "**Metric-Farmer**\nprepares measurments\nbased on //.farm files// " as pm #abc837
   node "**Metric-Farmer**\nmeasures metrics\n from  //sources// " as mm #abc837
   node "**Metric-Farmer**\nstores results\n on //targets//" as sr #abc837
   node "**User**\nanalyses results" as ar_user #ffcc00
   node "**CI**\nanalyses results" as ar_ci #ffcc00

   artifact ".farm files" as ff #ffcc00

   cloud "Source A" as src_a
   cloud "Source B" as src_b

   cloud "Target A" as target_a
   cloud "Target B" as target_b

   dm --> ff
   ff --> pm
   em -> pm

   pm -> mm
   mm -> sr

   src_a --> mm
   src_b --> mm

   sr --> target_a
   sr --> target_b

   target_a --> ar_user
   target_b --> ar_ci


   @enduml


Quick start
-----------

Installation
~~~~~~~~~~~~
You need to have an installed  Python 3.5 or above environment.

Then install Metric-Farmer by executing ``pip install metricfarmer``. A working internet connection is needed!

First measurements
~~~~~~~~~~~~~~~~~~
Execute metricfarmer by following command on your command prompt::

   metricfarmer

You will see that extensions and configurations got loaded, but no metrics have been measured.
That's because you haven't defined them yet.

Luckily Metric-Farmer comes with some metric examples,
which can be used by asking for all metrics with the tag ``mf_examples``.

So simply execute::

   metricfarmer --tags mf_examples print

``print`` is a predefined target and prints out the results of all measured metrics.

Playing with targets
~~~~~~~~~~~~~~~~~~~~
Targets define what shall happen with the measured metric results.

A very basic target is the ``print`` target. Other predefined targets are ``print_json``, ``file_text``
and ``file_json``.

You are free to combine them during your call::

   metricfarmer -t mf_examples print file_json

``-t`` is an abbreviation of ``--tags`` and ``file_json`` will print the results in a file called
``metric_results.json`` on your current working directory.

Take a look into :ref:`targets` to know how to define easily own, custom targets for your special use cases.

Knowing what is possible
~~~~~~~~~~~~~~~~~~~~~~~~
To get a list of all available metrics, tags, sources, targets and more, simply execute::

   metricfarmer --list


Own metrics
~~~~~~~~~~~
Metric-Farmer is controlled completely by file-based configurations.
Therefore it looks for ``.farm`` files at the following locations:

1. Metric-Farmer installation folder (for basic and example configs)
2. ``.farmer`` folder in user/home directory (e.g. ~/.farmer)
3. ``.farmer`` folder in current working directory (normally your project root)

Metric-Farmer reads in **all** found ``.farm``-files and combines them to a single configuration object.

Later read configuration parameters overrides previous read configurations.
So a project-configuration overrides always configurations coming from the user/home folder.

For a simple example, execute the following steps:

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

Congratulations, you have created and measured your first own metric.
As we have used the predefined ``random`` source-type, new measurements should provide random numbers as result.

Metric-Farmer provides the following predefined source types: ``static``, ``random`` and ``file_count``

Take a look into :ref:`sources` to get details about them or to get information about
how to define your own source types for your special needs.

Motivation
----------
Metric-Farmer is based on the needs of a software development team inside a german automotive company.

The project team was searching for a small and practical way of measuring and analysing metrics related
to the `ISO 26262 <https://en.wikipedia.org/wiki/ISO_26262>`_ standard for safety critical software.

Metric-Farmer is part of a software bundle, which was designed to support the development of
`ISO 26262 <https://en.wikipedia.org/wiki/ISO_26262>`_ compliant software.
Other tools are: `sphinx-needs <https://sphinxcontrib-needs.readthedocs.io/en/latest/>`_,
`sphinx-test-reports <https://sphinx-test-reports.readthedocs.io/en/latest/>`_ and
`tox-envreport <https://tox-envreport.readthedocs.io/en/latest/>`_.
