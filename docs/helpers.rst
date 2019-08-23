Helpers
=======

**Helpers** are little functions or definitions, which bring some helpful functions into the json-format of
the ``.farm``-files

All helpers are defined and configured as a string value and start with ``:MF_`` + helper name.


Current helpers are:

.. contents::
   :local:


MF_REPLACE
----------

MF_REPLACE replaces the value, where it is defined, with a value taken from another parameter.
Short example: ``:MF_REPLACE:my_name:`` will search for ``my_name`` in the source definition of the current metric.

This helper is mainly used in source definitions, where single values need to be replaced by values from the metric
definition.

**Example use case**

Imagine you need to perform a REST call on a webservice and the webservice needs a complex payload.
Most parts of the payload are the same for all calls, but 1 option is specific for each metric.

In the below example we want to measure the amount of tickets in a ticket-system called `Jira <https://www.atlassian.com/software/jira>`_.
Most important parameter is the jql-parameter (search string), which differs for each metric.
But the rest of the needed configuration: data to get, amount of data to get, ... needs to be the same for each metric.

So instead a letting each metric definition contain the whole complex payload, it shall only define the **jql**.
The complex payload is only defined once in the source definition and the nested jql-parameter gets replaced by
the jql-data from the metric definition.

.. code-block:: json
   :linenos:
   :emphasize-lines: 7,14,28

   {
     "metrics": {
       "open_issues": {
         "description": "Measure open jira issues",
         "source": {
           "type": "jira",
           "jql": "status = Open"
         }
       },
       "closed_issues": {
         "description": "Measure closed jira issues",
         "source": {
           "type": "jira",
           "jql": "status in ('Closed','Done')"
         }
       },
     },

     "sources": {
       "jira": {
         "class": "mf.rest",
         "url": "https://my_jira.com",
         "payload": {
           "fields": [
             "status"
           ],
           "maxResults": 1,
           "jql": ":MF_REPLACE:jql"
         },
       }
     }
   }

