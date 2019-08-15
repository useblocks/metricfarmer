Sources
=======

A **metric source** defines and configures the way a metric shall get measured.

It normally contains a set of parameters, which are shared between all metrics, which use this source.
But each metric can override specific parameters for its own measurement.

**Sources** get defined by the user in a **farm-file** and can the be referenced by metrics in the same file
or in other farm-files.

Exampel::

   # .farmer/my_sources.farm


   # .farmer/my_metrics.farm






.. _own_sources:

Create own sources
------------------

.. _predefined_sources:

Use predefined sources
----------------------

The following predefined sources are coming with Metric-Farmer:

.. contents::
   :local:





static
~~~~~~

Measures a single, static value.

Set parameters:

   * **value**: 0

random
~~~~~~

Measure a single, random float number.

Set parameters:

   * **min**: 0
   * **max**: 10
   * **digits**: 2


file_count
~~~~~~~~~~

Counts a files in the current working directory.

Set parameters: None


Classes
-------
