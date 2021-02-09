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

* Load and dump SCAP files.

  * OVAL
  * OCIL
  * XCCDF
  * DS
  * ARF

Usage
-----

.. code-block:: python

  import pyscap

  my_benchmark = pyscap.xccdf.Benchmark.parse("my_benchmark.xml")
  print(my_benchmark.title)
