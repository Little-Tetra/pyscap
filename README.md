# Pyscap

Python package for handling Security Content Automation Protocol.

*Warning: This project is still in the development stage, please do not use it in a production environment*

## Installing

Install and update using pip:

    pip install pyscap

## Features

* Load and dump files related to SCAP.

Currently only supports:

* XCCDF
* OVAL

The following specs are still in work:

* OCIL
* DS
* ARF

## Usage

    from pyscap.xccdf import Benchmark
    
    my_benchmark = Benchmark.load("my_benchmark.xml")
    print(my_benchmark.title)
