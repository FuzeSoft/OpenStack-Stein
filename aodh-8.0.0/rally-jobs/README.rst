Rally job related files
=======================

This directory contains rally tasks and plugins that are run by OpenStack CI.

Structure
---------

* plugins - directory where you can add rally plugins. Almost everything in
  Rally is a plugin. Benchmark context, Benchmark scenario, SLA checks, Generic
  cleanup resources, ....

* extra - all files from this directory will be copy pasted to gates, so you
  are able to use absolute paths in rally tasks.
  Files will be located in ~/.rally/extra/*

* aodh is a task that is run in gates against aodh


Useful links
------------

* More about Rally: https://rally.readthedocs.org/en/latest/

* How to add rally-gates: https://rally.readthedocs.io/en/latest/quick_start/gates.html

* About plugins:  https://rally.readthedocs.io/en/latest/plugins/index.html

* Plugin samples: https://github.com/openstack/rally/tree/master/samples/plugins
