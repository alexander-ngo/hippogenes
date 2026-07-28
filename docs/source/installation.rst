.. _installation:
 
Getting started
===============

Basic installation
------------------
 
The recommended way to install hippogenes is via ``pip``::
 
    pip install hippogenes
 
 
 You can also install the latest development version directly from GitHub::
 
    git clone https://github.com/alexander-ngo/hippogenes.git
    cd hippogenes
    pip install -e .


After installation, you can verify everything is working correctly by running
the following in a Python interpreter::
 
    import hippogenes
    print(hippogenes.__version__)
 
Or from the command line::
 
    python -c "import hippogenes; print(hippogenes.__version__)"
 
 
Requirements
------------
 
``hippogenes`` requires:
 
- Python 3.8 or later
- pip
 
The following packages are installed automatically as dependencies:
 
.. list-table::
   :header-rows: 1
   :widths: 30 70
 
   * - Package
     - Purpose
   * - ``numpy``
     - Array operations and data handling
   * - ``nibabel``
     - Reading and writing neuroimaging file formats
   * - ``pandas``
     - Tabular data handling for gene metadata
   * - ``pyarrows``
     - Columnar storage format handling