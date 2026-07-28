.. _api:

Reference API
=============

This page documents all public functions in hippogenes.


hippogenes.load_expression
--------------------------

.. py:function:: hippogenes.load_expression(genes=None, data_dir=None, force_download=False)

   :param genes: Official HGNC gene symbol (e.g. ``"BDNF"``, ``"APOE"``).
   The lookup is case-sensitive.
   :type genes: str, list[str] or None

   :param data_dir: Directory used to cache the dataset.  Defaults to ``~/.hippogenes/``.
   :type data_dir: str or None

   :param force_download: Re-download the file even if a local copy already exists.
   :type force_download: bool
   
   :returns: expression: A pandas DataFrame containing gene expression values. If
   genes is specified, only the requested genes are returned. The row
   ordering matches the hippocampal surface mesh bundled with the atlas.
   :type expression: pandas.DataFrame
   
   :returns ValueError: If one or more gene names are not present in the atlas
   :returns ConnectionError: If the atlas data cannot be downloaded and is not 
   available in the local cache

----