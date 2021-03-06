===============
masakari-status
===============

------------------------------------------
CLI interface for Masakari status commands
------------------------------------------

Synopsis
========

::

  masakari-status <category> <command> [<args>]

Description
===========

:program:`masakari-status` is a tool that provides routines for checking the
status of a Masakari deployment.

Options
=======

The standard pattern for executing a :program:`masakari-status` command is::

    masakari-status <category> <command> [<args>]

Run without arguments to see a list of available command categories::

    masakari-status

Categories are:

* ``upgrade``

Detailed descriptions are below:

You can also run with a category argument such as ``upgrade`` to see a list of
all commands in that category::

    masakari-status upgrade

These sections describe the available categories and arguments for
:program:`masakari-status`.

Upgrade
~~~~~~~

.. _masakari-status-checks:

``masakari-status upgrade check``
  Performs a release-specific readiness check before restarting services with
  new code. For example, missing or changed configuration options,
  incompatible object states, or other conditions that could lead to
  failures while upgrading.

  **Return Codes**

  .. list-table::
     :widths: 20 80
     :header-rows: 1

     * - Return code
       - Description
     * - 0
       - All upgrade readiness checks passed successfully and there is nothing
         to do.
     * - 1
       - At least one check encountered an issue and requires further
         investigation. This is considered a warning but the upgrade may be OK.
     * - 2
       - There was an upgrade status check failure that needs to be
         investigated. This should be considered something that stops an
         upgrade.
     * - 255
       - An unexpected error occurred.

  **History of Checks**

  **7.0.0 (Stein)**

  * Sample check to be filled in with checks as they are added in Stein.
