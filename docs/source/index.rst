.. hippogenes documentation master file
 
.. image:: logo.png
   :alt: Hippocampal gene expression map
   :align: center
 
**HippoGenes** is a Python toolbox providing a vertex-wise gene expression atlas
for the hippocampus. It maps gene expression data onto hippocampal surface
vertices, enabling researchers to explore the spatial transcriptomic landscape
of the hippocampus directly within their analysis workflows.


Overview
--------
 
The hippocampus plays a critical role in memory, spatial navigation, and
affective processing, yet its transcriptomic organisation along the
longitudinal and transverse axes has been difficult to explore at the vertex
level. **HippoGenes** bridges that gap by providing pre-computed, surface-mapped
gene expression data that can be fetched with a single function call and
immediately integrated into neuroimaging pipelines.
 
Key features
~~~~~~~~~~~~
 
- **Single-function API** — retrieve vertex-wise expression maps with
  ``load_expression()``.
- **Surface-native format** — outputs align directly to hippocampal surface
  meshes (compatible with common neuroimaging toolboxes).
- **Researcher-friendly** — minimal dependencies, straightforward installation,
  and rich tutorial notebooks.

Core development team
---------------------

HippoGenes is developed by members of the MICA-lab (https://mica-mni.github.io) and collaborators from around the world:

- **Alexander Ngo**, *Montreal Neurological Institute*
- **Lang Liu**, *Montreal Neurological Institute*
- **Ziv Gan-Or**, *Montreal Neurological Institute*
- **Jordan DeKraker**, *Montreal Neurological Institute*
- **Boris Bernhardt**, *Montreal Neurological Institute*


