.. _installation:
 
Installation
============
 
Requirements
------------
 
hippogenes requires:
 
- Python 3.9 or later
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
 
Installing from PyPI
--------------------
 
The recommended way to install hippogenes is via ``pip``::
 
    pip install hippogenes
 
Installing from source
----------------------
 
To install the latest development version directly from GitHub::
 
    git clone https://github.com/alexander-ngo/hippogenes.git
    cd hippogenes
    pip install -e .
 
The ``-e`` flag installs the package in *editable* mode, which means changes
to the source code are reflected immediately without reinstalling.
 
Verifying your installation
---------------------------
 
After installation, you can verify everything is working correctly by running
the following in a Python interpreter::
 
    import hippogenes
    print(hippogenes.__version__)
 
Or from the command line::
 
    python -c "import hippogenes; print(hippogenes.__version__)"
 
Virtual environments
--------------------
 
We recommend installing hippogenes inside a virtual environment to avoid
conflicts with other packages. For example, using ``venv``::
 
    python -m venv hippo-env
    source hippo-env/bin/activate   # On Windows: hippo-env\Scripts\activate
    pip install hippogenes
 
Or using ``conda``::
 
    conda create -n hippo-env python=3.9
    conda activate hippo-env
    pip install hippogenes
 
Troubleshooting
---------------
 
**ImportError after installation**
 
Make sure you are running Python from the same environment where hippogenes
was installed. If you are using Jupyter, install the package inside the kernel
environment::
 
    pip install hippogenes
 
and then restart the kernel.
 
**Network / firewall issues**
 
``load_expression()`` downloads atlas data on first use. If you are working
behind a firewall, ensure outbound HTTPS connections are permitted, or contact
your system administrator about caching the data locally.