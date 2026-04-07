.. _api:

API Reference
=============

This page documents all public functions in hippogenes.

.. contents:: On this page
   :local:
   :depth: 2

----

hippogenes.load_expression
--------------------------

.. py:function:: hippogenes.load_expression(genes=None, data_dir=None, force_download=False)

   :param genes: Official HGNC gene symbol (e.g. ``"BDNF"``, ``"APOE"``).
       The lookup is case-sensitive.
   :type gene: str, list[str] or None

   :param data_dir: Directory used to cache the dataset.  Defaults to ``~/.hippogenes/``.
   :type data_dir: str or None

   :param force_download: Re-download the file even if a local copy already exists.
   :type force_download: bool

Returns
    -------
    pandas.DataFrame
        Gene expression matrix, or a subset when ``genes`` is specified.

    Raises
    ------
    ValueError
        If any of the requested gene names are not present in the dataset.

    Examples
    --------
    Load the full matrix:
    >>> df = load_expression()

    Load a single gene:
    >>> bdnf = load_expression("SCN1A")

    Load several genes without downloading the full matrix:
    >>> subset = load_expression(["SCN1A", "APOE", "MAPT"])

    Use a project-specific cache directory:
    >>> df = load_expression(data_dir="./data")
    """
    data_dir = _resolve_data_dir(data_dir)
    local_path = data_dir / _GENE_EXPRESSION_FILENAME

    if force_download or not local_path.exists():
        _download(
            url=_GENE_EXPRESSION_URL,
            dest=local_path,
        )

    return _read_parquet(local_path, genes=genes)

   :returns: A pandas DataFrame of expression values for all genes or a subset when ``genes`` is specified. The vertex ordering 
       matches the hippocampal surface mesh bundled with the atlas.
   :rtype: pandas.DataFrame

   :raises ValueError: If *gene* is not found in the atlas.
   :raises ConnectionError: If the atlas data cannot be downloaded and is not
       present in *cache_dir*.

   **Examples**::

       import hippogenes as hg

       # Load all genes
       expr = hg.load_expression()
       print(expr.shape)   # (7262, 15630)  

       # Load a single gene
       expr = hg.load_expression("BDNF")

       # Load several genes
       subset = hg.load_expression(["SCN1A", "APOE", "MAPT"])

       # Custom cache location
       expr = hg.load_expression("HTR1A", data_dir="/scratch/hippo_cache")

----