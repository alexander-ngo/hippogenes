.. _installation:

Installation
============
 
Basic installation
------------------

.. note::

    ``hippogenes`` is not yet published on PyPI. Until it is, install it directly from Github using the instructions below. The `pip install hippogenes` command will be enabled here as soon as a release is published
    
Install the latest development version directly from GitHubL
 
.. code-block:: bash

    git clone https://github.com/alexander-ngo/hippogenes.git
    cd hippogenes
    pip install -e .


After installation, you can verify everything is working correctly by running the following in a Python interpreter:
 
.. code-block:: python

    import hippogenes
    print(hippogenes.__version__)
 
Or from the command line:

.. code-block:: bash
 
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