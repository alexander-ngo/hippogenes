"""
HippoGenes - Gene expression data loading utilities.
"""

from __future__ import annotations

import os
from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_DEFAULT_DATA_DIR = Path.home() / ".hippogenes"

_GENE_EXPRESSION_URL = "https://osf.io/download/f6wxm/"
_GENE_EXPRESSION_FILENAME = "gene_expression.parquet"


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def load_expression(
    genes: str | list[str] | None = None,
    data_dir: str | os.PathLike | None = None,
    *,
    force_download: bool = False,
) -> pd.DataFrame:
    """Load the HippoGenes gene expression dataset.

    The full matrix (~2.2 GB) is downloaded from OSF on the first call and
    cached locally.  Subsequent calls read from the cache.  When ``genes`` is
    specified only those columns are read from disk — much faster than loading
    the entire matrix.

    Parameters
    ----------
    genes:
        Gene name or list of gene names to load (e.g. ``"BDNF"`` or
        ``["BDNF", "APOE", "MAPT"]``).  If *None* (default) the full matrix
        is returned.
    data_dir:
        Directory used to cache the dataset.  Defaults to ``~/.hippogenes/``.
    force_download:
        Re-download the file even if a local copy already exists.

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


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _resolve_data_dir(data_dir: str | os.PathLike | None) -> Path:
    """Resolve and create the data directory if it does not exist."""
    path = Path(data_dir) if data_dir is not None else _DEFAULT_DATA_DIR
    path.mkdir(parents=True, exist_ok=True)
    return path


def _read_parquet(
    path: Path,
    genes: str | list[str] | None,
) -> pd.DataFrame:
    """Read a Parquet file, optionally loading only requested gene columns."""
    if genes is None:
        return pd.read_parquet(path)

    gene_list = [genes] if isinstance(genes, str) else list(genes)

    # Validate before reading to give a clear error message.
    # Reading with columns=[] fetches only metadata — very fast.
    all_columns = pd.read_parquet(path, columns=[]).columns.tolist()
    missing = sorted(set(gene_list) - set(all_columns))
    if missing:
        raise ValueError(
            f"The following genes were not found in the dataset: {missing}\n"
            "Call load_expression() with no arguments to inspect all "
            "available genes."
        )

    return pd.read_parquet(path, columns=gene_list)


def _download(url: str, dest: Path) -> None:
    """Download *url* to *dest* with a progress bar."""
    print("Downloading gene expression data from OSF ...")
    print(f"  URL : {url}")
    print(f"  Dest: {dest}")

    try:
        urlretrieve(url, dest, reporthook=_progress_hook)
    except Exception as exc:
        if dest.exists():
            dest.unlink()
        raise RuntimeError(
            "Failed to download gene expression data.\n"
            f"URL: {url}\n"
            f"Reason: {exc}\n\n"
            "Check your internet connection or download the file manually and "
            f"place it at:\n  {dest}"
        ) from exc

    print(f"\nSaved to {dest}")


def _progress_hook(block_num: int, block_size: int, total_size: int) -> None:
    """Simple progress indicator for urlretrieve."""
    if total_size <= 0:
        return
    downloaded = min(block_num * block_size, total_size)
    pct = downloaded / total_size * 100
    bar_len = 30
    filled = int(bar_len * downloaded / total_size)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"\r  [{bar}] {pct:5.1f}%", end="", flush=True)
