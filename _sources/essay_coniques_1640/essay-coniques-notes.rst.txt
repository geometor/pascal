:navigation: header
:order: 4
:type: section
:nav_title: Scholarly Notes
:breadcrumb_title: Scholarly Notes

.. _essay-coniques-notes:

====================================
Scholarly Notes & Historical Context
====================================

.. rubric:: The 1640 Broadside, Desargues's Influence & the Evolution of the Hexagram Web

The February 1640 Broadside
---------------------------

In February 1640, sixteen-year-old :person:`Blaise Pascal <pascal>` printed approximately fifty copies of a single large folio sheet titled **ESSAY POUR LES CONIQUES. Par B. P.** in Paris. Only two original exemplars are known to survive today: one preserved in the Bibliothèque nationale de France in Paris, and one in the Gottfried Wilhelm Leibniz collection in Hannover.

The broadside was not intended as a complete treatise, but as a prospectus and announcement of a comprehensive forthcoming work on conic sections (*Genera Conicorum* or *Traité complet des coniques*). In just under 1,500 words, young Pascal introduced the fundamental concepts of projective collineation, defined pencils of concurrent and parallel lines (*ordonnances de lignes*), established three preliminary lemmas, and announced his celebrated **Hexagrammum Mysticum** theorem.

The Debt to Girard Desargues
----------------------------

At the conclusion of the broadsheet, Pascal paid an extraordinary public tribute to :person:`Girard Desargues <desargues>`:

   *"We will also demonstrate this property, whose first inventor is M. Desargues Lyonnais, one of the great spirits of this time, and of those most versed in mathematics, and among others in conics... and I am very willing to confess that I owe the little that I have found on this matter to the examples of his writings, and that I have tried to imitate, as far as possible, his method on this subject, which treats of conic sections without using the cone."*

In his 1639 *Brouillon project d'une atteinte aux événemens des rencontres du cône avec un plan*, Desargues had revolutionized geometry by introducing points at infinity, projective involutions, and the principle that parallel lines meet at an ideal point. While contemporaries found Desargues's specialized botanical vocabulary obscure and off-putting, the young Pascal recognized the sheer conceptual power of Desargues's perspective methods.

Descartes's Skepticism
----------------------

When Father :person:`Marin Mersenne <mersenne>` sent a copy of Pascal's broadside to :person:`René Descartes <descartes>` in the Netherlands, Descartes initially refused to believe that a sixteen-year-old boy had produced it, suspecting instead that Étienne Pascal (Blaise's father, an accomplished mathematician) or Girard Desargues was the true author. Mersenne reassured Descartes of Blaise's authentic authorship, marking Pascal's sensational entrance into the European Republic of Letters.

The Lost Treatise (*Genera Conicorum*)
---------------------------------------

Pascal went on to compose a massive, multi-part work on conic sections based on the Hexagrammum Mysticum, titled variously *Genera Conicorum* or *Traité des coniques*. The completed manuscript, consisting of several hundred pages, was read and admired by Mersenne and members of the Paris academy in the 1640s and 1650s.

In 1676—fourteen years after Pascal's death—:person:`Gottfried Wilhelm Leibniz <leibniz>`, visiting Paris, was given access to Pascal's mathematical papers by Pascal's nephew, Louis Périer. Leibniz recognized the masterpiece and copied extensive extracts and outlines, recommending its immediate publication. Tragically, the Pascal family failed to print it, and the manuscript subsequently disappeared. Our knowledge of the full extent of Pascal's work rests on the 1640 broadside, Leibniz's copied notes, and the accounts of Mersenne.

Nineteenth-Century Flowering: The 60-Line Web
---------------------------------------------

Pascal proved that six points on a conic yield a Pascal line. But six points can be ordered into a cyclic hexagon in :math:`\frac{6!}{2 \cdot 6} = 60` distinct ways! Does each ordering yield a different line?

In the early nineteenth century, the rebirth of synthetic projective geometry led to an explosion of discoveries surrounding this 60-line web:

1. **Charles Julien Brianchon (1806)**: Discovered :person:`Brianchon's theorem <brianchon>`, the projective dual of Pascal's theorem: the three principal diagonals of a hexagon circumscribed about a conic section concur at a single point.
2. **Jakob Steiner (1828)**: Proved in *Systematische Entwicklung* (:cite:`steiner:1832`) that the 60 Pascal lines concur three-by-three in **20 Steiner points** (:math:`G`). Steiner showed that these correspond to the ten ways of partitioning the six conic points into two complementary triangles :math:`\triangle_A` and :math:`\triangle_B`, with each partition generating two Steiner points (associated with the alternating group :math:`A_3` and coset :math:`S_3 \setminus A_3`).
3. **Julius Plücker (1830)**: Proved (:cite:`pluecker:1830`) that the 20 Steiner points lie four-by-four on **15 Plücker lines**.
4. **Thomas Penyngton Kirkman (1850)**: Discovered (:cite:`kirkman:1850`) that the 60 Pascal lines concur three-by-three in a *second*, distinct way at **60 Kirkman points** (:math:`K`), with three Kirkman points lying on every Pascal line.
5. **George Salmon & Arthur Cayley (1850s)**: Unified the Steiner and Kirkman configurations into the complete self-dual incidence structure of the *Hexagrammum Mysticum*, showing that the 60 Kirkman points lie three-by-three on 20 Cayley–Salmon lines.

Relation to Pappus of Alexandria
--------------------------------

The archetype of Pascal's theorem is :person:`Pappus of Alexandria's <pappus>` Hexagon Theorem (*Synagoge* VII.139, c. 340 CE). Pappus established collinearity for six points distributed three-and-three along two straight lines :math:`a` and :math:`b`.

In projective geometry, two intersecting lines form a **degenerate conic section** :math:`L_a(x, y) \cdot L_b(x, y) = 0`. When the conic is smooth (circle or ellipse), all 60 hexagons are non-degenerate, producing 60 Pascal lines and 20 Steiner points. When the conic degenerates into two lines :math:`a \cup b`, 54 of the 60 orderings degenerate or collapse onto the carrier lines, leaving exactly the **6 Pappus lines** and **2 Steiner Star points** :math:`(S_+, S_-)` of the Pappus–Steiner theorem.
