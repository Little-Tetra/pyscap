Pyscap
======

Python package for handling Security Content Automation Protocol.

**Warning: This project is still under development, please do not use it in a production environment.**

Installing
----------

Install and update using pip:

.. code-block:: text

  $ pip install pyscap

Features
--------

* Load and dump SCAP strings or files as pythonic objects.

  * XCCDF(WIP)
  * OVAL(WIP)
  * OCIL(WIP)
  * CPE(WIP)
  * SWID(WIP)
  * CCE(WIP)
  * CVE(WIP)
  * CVSS(WIP)
  * CCSS(WIP)
  * DS(WIP)
  * ARF(WIP)

* Load and dump SCAP objects in JSON format(unofficial).

* Provide SCAP-related utils.


Usage
-----

.. code-block:: python

  from pyscap import xccdf

  with open("my_benchmark.xml", "r") as f:
    my_benchmark = xccdf.Benchmark.load(f)
    print(my_benchmark.title)
