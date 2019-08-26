.. _snippet_jira:

Get metrics from JIRA
=====================

The below example gets issues for an empty jql of a cloud-based JIRA system.

Empty jql string means that all issues are taken as result.

As no user/password are provided and this JIRA system as no free-accessible projects, the result should be **0**.

.. hint::
   You may need to create a API-token for JIRA-cloud, because using your password in JIRA-cloud is not allowed.
   In this case, simply use the token for the **password** field.

   See `JIRA api token docs <https://confluence.atlassian.com/cloud/api-tokens-938839638.html>`_.

.. literalinclude:: ../../tests/farmer_files/rest/jira.farm

