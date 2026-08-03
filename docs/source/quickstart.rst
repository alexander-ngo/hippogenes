.. _quickstart:

Quickstart
==========

This page shows the fastest path from installation to a working gene expression
map. For more detailed examples, see the :ref:`tutorials`.

Fetch a gene expression map in three lines
------------------------------------------

.. code-block:: python

    import hippogenes as hg

    # Retrieve vertex-wise expression values for BDNF across the hippocampal surface
    expression = hg.load_expression("BDNF")

``expression`` is a Pandas DataFrame of shape ``(n_vertices, n_genes)`` containing
normalised expression values for each vertex on the hippocampal surface mesh.

Visualise the result
--------------------

You can plot the expression map with any surface-plotting library. Here is a
minimal example using ``hippomaps``:

.. code-block:: python

    import hippomap as hm
    import hippogenes as hg

    expression = hg.load_expression("BDNF")

    hm.plotting.surfplot_canonical_foldunfold(expression.to_numpy(), cmap="viridis", hemis=['L'], 
                                              labels=['hipp'], unfoldAPrescale=True, share='row',
                                              tighten_cwindow=True, embed_nb=True)

What happens on first run?
--------------------------

The first time ``load_expression()`` is called, hippogenes downloads the
pre-computed atlas from our data repository and caches it locally (typically
in ``~/.hippogenes/``). Subsequent calls use the cached data and return
almost instantly.