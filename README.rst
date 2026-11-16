======
pascal
======

the French mathematician and philosopher whose 1640 broadside Essay pour les Coniques unveiled the Mystic Hexagram theorem for any conic section

Edition Overview
----------------

- **Treatise**: *Essay pour les Coniques*
- **Author**: Blaise Pascal
- **Primary Edition Track**: ``docsrc/essay_coniques_1640/`` (``:layout: book``)
- **Apparatus**: ``resources/persons.json``, ``resources/citations.json``, ``resources/glossary.json``
Installation & Verification
---------------------------

Managed with ``uv`` on Python 3.13:

.. code-block:: bash

   uv run --no-sync pytest
   ruff check src tests demos
   publish build

Usage
-----

.. code-block:: bash

   pascal --help

Links
-----

- **Documentation**: https://geometor.github.io/pascal
- **Repository**: https://github.com/geometor/pascal
- **Issues**: https://github.com/geometor/pascal/issues

License
-------

Licensed under the MIT License. See ``LICENSE`` for details.
