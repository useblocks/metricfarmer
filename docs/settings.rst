Settings
========

``Settings`` are used to configure the Metric-Farmer Application.

They can be part of any ``.farm``-file::

   {
      "settings": {
         "setting_A": true,
         "setting_B": ["my_list"]
         }
   }

All settings are defined by Metric-Farmer, as their usage is hardly coded in its source code.

Extensions have access to it, but should normally not use them.
Instead their configuration should be stored in the parameters of their ``sources`` and ``targets``.

Available settings
------------------

.. contents::
   :local:

targets_default
~~~~~~~~~~~~~~~
List of default targets, which shall be used, if the user is using Metric-Farmer without any target.

Has no effect, if the user provides own targets in its call.

Example::

  {
    "settings": {
      "targets_default": ["print"]
    }
  }

Calling just ``metricfarmer`` will automatically execute the target ``print``, if the above configuration is given.


targets_always
~~~~~~~~~~~~~~
List of targets, which shall always get executed. No matter what the user has defined.

This targets will get executed first, then the user defined targets get executed.

Example::

  {
    "settings": {
      "targets_always": ["print_json"]
    }
  }

If the user runs ``metricfarmer print`` with the above configuration, the two targets ``print_json`` and ``print``
will get executed.
