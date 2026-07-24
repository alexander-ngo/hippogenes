.. _usage:
 
User Guide
===========
 
This page describes how to use HippoGenes in detail, covering all parameters
of ``load_expression()`` and common patterns for integrating the toolbox into
research workflows.
 
Importing HippoGenes
~~~~~~~~~~~~~~~~~~~~
 
::
 
    import hippogenes as hg
 
    # Or import the function directly
    from hippogenes import load_expression
 
Basic usage:
~~~~~~~~~~~~

.. tabs:: 
  .. tab:: All genes
    ::

        import hippogenes as hg
    
        expr = hg.load_expression()
        print(expr.shape)   # (7262, 15630) 

  .. tab:: Single gene
    ::

        import hippogenes as hg

        expr = hg.load_expression(genes="BDNF")
        print(expr.shape)   # (7262, 1) 

  .. tab:: Multiple genes
    ::

        import hippogenes as hg

        expr = hg.load_expression(genes=["BDNF", "APOE", "HTR1A", "NR3C1"])
        print(expr.shape)   # (7262, 4)
 
Using a custom cache directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
Useful when  home directory has limited quota::
 
    data_dir = "/scratch/my_project/hippogene_cache"
    expr = hg.load_expression(data_dir=data_dir)
 
Checking gene availability
~~~~~~~~~~~~~~~~~~~~~~~~~~
 
You may want to verify that all genes of
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
 
Example — plotting gene expression values using hippomaps::
 
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