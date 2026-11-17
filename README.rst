GEOMETOR • pascal
=================

**Visit the Online Archive:** https://geometor.github.io/pascal/

.. image:: docsrc/_static/constructions/golden_pascal.svg
   :alt: GEOMETOR • pascal featured geometric construction
   :target: https://geometor.github.io/pascal/
   :align: center

**Blaise Pascal • Essay pour les Coniques • semantic digital archive**

Mission
-------

``geometor/pascal`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It preserves and formalizes Blaise Pascal's landmark 1640 broadsheet *Essay pour les Coniques*, which unveiled the *hexagrammum mysticum* theorem showing that opposite side intersections of a hexagon inscribed in any conic are collinear. Through addressable semantic units, calibrated theme-adaptive vector diagrams, primary-source folio provenance, and exact SymPy symbolic projective engines, Pascal's foundational projective theorem connects ancient conics directly to modern synthetic geometry across the GEOMETOR corpus.

Books in This Archive
---------------------

- **`Essay on Conics <https://geometor.github.io/pascal/essay_coniques_1640/>`_** — *Essay pour les Coniques* (Paris, 1640), Pascal's landmark broadsheet introducing the *hexagrammum mysticum* and the foundations of modern projective geometry.

Repository Contents
-------------------

- ``docsrc/`` — RST documentation source, book codex, and Sphinx docs compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Primary-source folios, 1640 broadsheet facsimile page images, and archival apparatus registries.
- ``src/geometor/pascal/`` — Exact SymPy symbolic implementations of the Pascal line, hexagram configurations, and projective conics.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
