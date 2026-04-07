.. _usage:
 
Usage Guide
===========
 
This page describes how to use HippoGenes in detail, covering all parameters
of ``load_expression()`` and common patterns for integrating the toolbox into
research workflows.
 
Importing HippoGenes
--------------------
 
::
 
    import hippogenes as hg
 
    # Or import the function directly
    from hippogenes import load_expression
 
The ``load_expression()`` function
----------------------------------
 
``load_expression()`` is the primary (and currently sole) public function in
hippogenes. It retrieves vertex-wise gene expression values mapped onto the
hippocampal surface atlas.
 
Signature
~~~~~~~~~
 
::
 
    hippogenes.load_expression(
        gene,
        hemisphere="both",
        normalise=True,
        cache_dir=None,
    )
 
Parameters
~~~~~~~~~~
 
.. list-table::
   :header-rows: 1
   :widths: 20 15 65
 
   * - Parameter
     - Type
     - Description
   * - ``genes``
     - ``None`` or ``str`` or list of ``str``
     - Official gene symbol (e.g. ``"BDNF"``, ``"APOE"``). Case-sensitive.
   * - ``data_dir``
     - ``str`` or ``None``
     - Path to the directory used for caching downloaded atlas files.
       Defaults to ``~/.hippogenes/``.
   * - ``force_download``
     - ``bool``
     - If *True*, forces re-download of the atlas file even if a local copy
       already exists.  Use this to refresh the cache if you suspect the local
       file is corrupted or outdated.

Returns
~~~~~~~
 
A :class:`pandas.DataFrame` of shape ``(n_vertices, n_genes)`` containing expression
values for all genes or a subset when ``genes`` is specified. The vertex ordering 
matches the hippocampal surface mesh bundled with the atlas.
 
Raises
~~~~~~
 
.. list-table::
   :header-rows: 1
   :widths: 30 70
 
   * - Exception
     - Condition
   * - ``ValueError``
     - The requested gene symbol is not found in the atlas.
   * - ``ConnectionError``
     - The atlas could not be downloaded and is not cached locally.

 
Examples
--------
 
Basic usage
~~~~~~~~~~~
 
::
 
    import hippogenes as hg
 
    expr = hg.load_expression()
    print(expr.shape)   # (7262, 15630) 

    expr = hg.load_expression(genes="BDNF")
    print(expr.shape)   # (7262, 1) 

    expr = hg.load_expression(["BDNF", "APOE", "HTR1A", "NR3C1"])
    print(expr.shape)   # (7262, 4) 
 
Using a custom cache directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
Useful on shared HPC clusters where the home directory has limited quota::
 
    expr = hg.load_expression("BDNF", data_dir="/scratch/my_project/hippo_cache")
 
Checking gene availability
---------------------------
 
Before running a large batch, you may want to verify that all genes of
interest are present in the atlas::
 
    import hippogenes as hg
 
    genes_of_interest = ["BDNF", "APOE", "HTR1A", "NR3C1"]
 
    for gene in genes_of_interest:
        try:
            _ = hg.load_expression(gene)
            print(f"{gene}: available")
        except ValueError:
            print(f"{gene}: NOT found in atlas")

 
Integration with neuroimaging tools
------------------------------------
 
The output of ``load_expression()`` is a plain NumPy array and is therefore
compatible with any library that accepts vertex-wise surface data, including
``nibabel``, ``nilearn``, ``brainspace``, ``hippomaps``, and ``surfplot``.
 
Example — saving as a GIFTI metric file with nibabel::
 
    import hippomaps as hm
    import hippogenes as hg
 
    expr = hg.load_expression("BDNF").to_numpy().flatten()
    
    hm.plotting.surfplot_canonical_foldunfold(expr, cmap="viridis", hemis=['L'], 
                                              labels=['hipp'], unfoldAPrescale=True, share='row',
                                              tighten_cwindow=True, embed_nb=True)
 
Data and atlas details
-----------------------
 
The hippogenes atlas is derived from publicly available transcriptomic data
sources. Vertex coordinates correspond to the hippocampal surface mesh
included with the atlas download. Please cite the relevant data source as well
as hippogenes itself in any publication — see :doc:`contributing` for citation
guidance.