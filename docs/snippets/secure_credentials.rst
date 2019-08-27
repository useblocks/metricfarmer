Secure credentials
==================

Nearly all web-services need valid credentials for authentication.

Instead of storing this security related information inside ``.farm`` -files, you should
store them on local `Environment variables <https://en.wikipedia.org/wiki/Environment_variable>`_ , which
are normally not available for other users.

Use the helper function :ref:`helper_mf_env` to get this data into your configuration during runtime of
Metric-Farmer.


.. code-block:: json
   :linenos:
   :emphasize-lines: 16,17

   {
     "metrics": {
       "open_issues": {
         "description": "Measure open jira issues",
         "source": {
           "type": "jira",
           "jql": "status = Open"
         }
       },
     },

     "sources": {
       "jira": {
         "class": "mf.rest",
         "url": "https://my_jira.com",
         "user": ":MF_ENV:JIRA_USER",
         "password": ":MF_ENV:JIRA_PASSWORD",
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

