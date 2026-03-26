"""
HippoGenes: Transcriptomic mapping of the human hippocampus.

This package provides tools for :
- Processing and normalizing AHBA gene expression
- Mapping gene expression to hippocampal anatomy
- Running imaging-transcriptomic analyses (PLS and spatial correlations)
- Performing enrichment analyses
- Visualize imaging-transcriptomic analyses
"""

__version__ = "0.1.0"

# --- Import functions for top-level access ---

from .data import load_expression

__all__ = ["load_expression"]
