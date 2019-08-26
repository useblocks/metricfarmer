.. _snippet_github:

Get metrics from GitHub
=======================

The below example gets the amount of issues from `GitHub <https://github.com>`_.

For the **GitHub api v3** please set ``"no_escape": true`` so that the filter string does not get escaped and is
used as it is in the GET call against GitHub.

The used ``filter`` itself is using a not existing github account for the assignee field. So the result should
always be **0**.

GitHub API documentation: https://developer.github.com/v3/search/

.. literalinclude:: ../../tests/farmer_files/rest/github.farm

