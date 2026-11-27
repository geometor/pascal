:navigation: header
:order: 3
:type: section
:nav_title: Mathematical Summary
:breadcrumb_title: Mathematical Summary

.. _essay-coniques-summary:

============================================
Mathematical Summary & Symbolic Architecture
============================================

.. rubric:: Exact Symbolic Projective Geometry, Veronese Invariants & 60-Line Web

From Two Straight Lines to Any Conic Section
--------------------------------------------

Thirteen centuries after :person:`Pappus of Alexandria <pappus>` proved his Hexagon Lemma (*Synagoge* VII.139) for six points distributed along **two straight lines** :math:`a` and :math:`b`, sixteen-year-old :person:`Blaise Pascal <pascal>` published a single printed broadsheet in February 1640—*Essai pour les coniques*—announcing a breathtaking generalization: **the two lines can be replaced by any conic section**.

Algebraically, Pappus's theorem and Pascal's theorem are **two faces of one projective law**. Six points :math:`P_k = (x_k, y_k)` lie on a planar curve of degree two—whether a **smooth conic** :math:`\mathcal{C}: A x^2 + B x y + C y^2 + D x + E y + F = 0` (circle, ellipse, parabola, or hyperbola) or a **degenerate conic** :math:`L_a(x, y) \cdot L_b(x, y) = 0` (Pappus's pair of lines)—if and only if their :math:`6 \times 6` **Veronese matrix** drops rank (:math:`\det V_6 = 0`):

.. math::

   \det \begin{bmatrix}
   x_0^2 & x_0 y_0 & y_0^2 & x_0 & y_0 & 1 \\
   x_1^2 & x_1 y_1 & y_1^2 & x_1 & y_1 & 1 \\
   \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
   x_5^2 & x_5 y_5 & y_5^2 & x_5 & y_5 & 1
   \end{bmatrix} = 0.

In ``geometor.pascal.projective.are_coconic``, this exact SymPy rank test unifies smooth circles and ellipses with degenerate configurations under a single algebraic predicate, while :person:`Colin Maclaurin <maclaurin>` (1720) and :person:`William Braikenridge <braikenridge>` (1733) proved the converse: if the three opposite-side intersections of a hexagon are collinear, its six vertices necessarily lie on a conic.

.. admonition:: Theorem (Pascal's *Hexagrammum Mysticum*, 1640)

   Let :math:`P_0, P_1, P_2, P_3, P_4, P_5` be any six distinct points on an irreducible conic :math:`\mathcal{C}` in :math:`\mathbb{P}^2`, ordered in a cyclic hexagon :math:`\langle P_{c_0}, P_{c_1}, P_{c_2}, P_{c_3}, P_{c_4}, P_{c_5} \rangle`. Then the three intersections of opposite sides,

   .. math::

      M_{03} = [P_{c_0} P_{c_1}] \cap [P_{c_3} P_{c_4}], \quad
      M_{14} = [P_{c_1} P_{c_2}] \cap [P_{c_4} P_{c_5}], \quad
      M_{25} = [P_{c_2} P_{c_3}] \cap [P_{c_5} P_{c_0}],

   are **collinear** along a single line :math:`p`—the **Pascal line** of the inscribed hexagram.

The Mystic Star Hexagram on the Pythagorean Circle
--------------------------------------------------

To explore Pascal's theorem in **100% exact rational arithmetic** (:math:`\mathbb{Q}^2`) without floating-point approximations, ``geometor.pascal.projective.circle_stereographic_point`` maps any rational parameter :math:`t \in \mathbb{Q}` onto the unit circle :math:`x^2 + y^2 = 1` via Weierstrass stereographic projection:

.. math::

   P(t) = \left(\frac{1 - t^2}{1 + t^2},\; \frac{2t}{1 + t^2}\right) \in \mathbb{Q}^2.

Seeding ``preset="hexagrammum"`` with :math:`t = \left(0,\, \frac{1}{3},\, 1,\, 3,\, -2,\, -\frac{1}{2}\right)` places six cardinal and :math:`3\text{-}4\text{-}5` Pythagorean vertices around all four quadrants of :math:`x^2 + y^2 = 1`:

.. math::

   P_0 = (1, 0),\quad P_1 = \left(\frac{4}{5}, \frac{3}{5}\right),\quad
   P_2 = (0, 1),\quad P_3 = \left(-\frac{4}{5}, \frac{3}{5}\right),\quad
   P_4 = \left(-\frac{3}{5}, -\frac{4}{5}\right),\quad P_5 = \left(\frac{3}{5}, -\frac{4}{5}\right).

Tracing the non-convex **mystic star cycle** :math:`\langle P_0, P_2, P_4, P_1, P_3, P_5 \rangle` produces two interior meets and one compact exterior meet, all strictly rational:

.. math::

   M_{03} = \left(\frac{2}{5},\, \frac{3}{5}\right), \qquad
   M_{14} = \left(-\frac{3}{10},\, \frac{1}{10}\right), \qquad
   M_{25} = \left(\frac{9}{5},\, \frac{8}{5}\right),

aligned along the exact Pascal line :math:`25x - 35y + 11 = 0`:

.. picture:: /_static/constructions/pascal_hexagrammum.svg
   :alt: Pascal's Hexagrammum Mysticum (1640) on the Pythagorean Unit Circle

.. step::

   Inscribe the six Pythagorean rational points :g:`P_0 <g1:P0>`, :g:`P_1 <g1:P1>`, :g:`P_2 <g1:P2>`, :g:`P_3 <g1:P3>`, :g:`P_4 <g1:P4>`, and :g:`P_5 <g1:P5>` around the unit circle :g:`𝒞 <g1:( O P0 )>` centered at :g:`O <g1:O>` :math:`= (0, 0)`.

.. step::

   Trace the self-intersecting star hexagram :g:`P_0 P_2 P_4 P_1 P_3 P_5 <g1:< P0 P2 P4 P1 P3 P5 >>` and intersect the first opposite side pair :g:`P_0 P_2 <g1:[ P0 P2 ]>` (:math:`x + y = 1`) with :g:`P_1 P_3 <g1:[ P1 P3 ]>` (:math:`y = \frac{3}{5}`) at :g:`M_{03} <g1:M03>` :math:`= \left(\frac{2}{5}, \frac{3}{5}\right)`.

.. step::

   Intersect the second opposite pair :g:`P_2 P_4 <g1:[ P2 P4 ]>` (:math:`3x - y + 1 = 0`) with :g:`P_3 P_5 <g1:[ P3 P5 ]>` (:math:`5x + 5y + 1 = 0`) inside the circle at :g:`M_{14} <g1:M14>` :math:`= \left(-\frac{3}{10}, \frac{1}{10}\right)`, and the third opposite pair :g:`P_4 P_1 <g1:[ P4 P1 ]>` (:math:`5x - 5y = 1`) with :g:`P_5 P_0 <g1:[ P5 P0 ]>` (:math:`2x - y = 2`) outside the circle at :g:`M_{25} <g1:M25>` :math:`= \left(\frac{9}{5}, \frac{8}{5}\right)`.

.. step::

   Draw the **Pascal line** :g:`p <g1:[ M03 M14 ]>` (:math:`25x - 35y + 11 = 0`):
   :math:`25\left(\frac{2}{5}\right) - 35\left(\frac{3}{5}\right) + 11 = 10 - 21 + 11 = 0`,
   :math:`25\left(-\frac{3}{10}\right) - 35\left(\frac{1}{10}\right) + 11 = -11 + 11 = 0`, and
   :math:`25\left(\frac{9}{5}\right) - 35\left(\frac{8}{5}\right) + 11 = 45 - 56 + 11 = 0`!

Universal Symbolic Proof & Conic Invariance
-------------------------------------------

Why did Pascal need only prove his lemma for the circle in order to establish it for **every** ellipse, parabola, and hyperbola? Because any non-degenerate conic is the central projection of a circle from the apex of Apollonius's cone, and incidence (:math:`P \in \ell`) is preserved under every projective collineation :math:`T \in \mathrm{PGL}_3(\mathbb{R})`.

1. **Universal 6-Parameter Proof**: ``verify_pascal_symbolic()`` parameterizes six generic points :math:`P_k = [1 - t_k^2 : 2 t_k : 1 + t_k^2]` over the polynomial ring :math:`\mathbb{Z}[t_0, t_1, t_2, t_3, t_4, t_5]`, computes :math:`M_{03}, M_{14}, M_{25}` via homogeneous 3D cross products, and expands :math:`\det[M_{03}, M_{14}, M_{25}]`—which cancels **identically to zero**.
2. **General Ellipse Verification**: Applying the affine transformation :math:`(x, y) \mapsto (2x, y)` in ``preset="ellipse"`` maps the Pythagorean hexagram onto the non-circular ellipse :math:`\mathcal{E}: \frac{x^2}{4} + y^2 = 1` (:math:`x^2 + 4y^2 - 4 = 0`), stretching the three Pascal intersections to :math:`M'_{03} = \left(\frac{4}{5}, \frac{3}{5}\right)`, :math:`M'_{14} = \left(-\frac{3}{5}, \frac{1}{10}\right)`, and :math:`M'_{25} = \left(\frac{18}{5}, \frac{8}{5}\right)` along :math:`25x - 70y + 22 = 0`:

.. picture:: /_static/constructions/pascal_ellipse.svg
   :alt: Pascal's Hexagrammum Mysticum on the General Ellipse x^2/4 + y^2 = 1

.. step::

   Compare the stretched ellipse :g:`ℰ <g2:( O P0 )>` (:math:`\frac{x^2}{4} + y^2 = 1`) with the unit circle above: every chord, opposite meet :g:`M'_{03} <g2:M03>`, :g:`M'_{14} <g2:M14>`, :g:`M'_{25} <g2:M25>`, and Pascal line :g:`p' <g2:[ M03 M14 ]>` transforms covariantly while preserving exact three-point collinearity.

The Complete 60-Line *Hexagrammum Mysticum* Web
-----------------------------------------------

On two lines (Pappus), permuting the vertices yields :math:`3! = 6` hexagons and **6 Pappus lines** concurring in **2 Steiner Star points**. On a smooth conic, however, **no three of the six vertices are collinear**, so **every cyclic ordering** of :math:`P_0, \dots, P_5` up to dihedral rotation and reversal (:math:`D_6`, order 12) inscribes a valid hexagon—producing:

.. math::

   \frac{6!}{2 \cdot 6} = \mathbf{60\text{ Pascal lines}}!

In the nineteenth century, :person:`Jakob Steiner <steiner>` (1828), :person:`Julius Plücker <pluecker>` (1830), :person:`Thomas Penyngton Kirkman <kirkman>` (1850), Arthur Cayley, and George Salmon uncovered an astonishing, self-dual incidence architecture hidden inside these 60 lines. Running ``enumerate_hexagrammum_mysticum(preset="hexagrammum")`` constructs and verifies every element of this web in exact homogeneous coordinates with **zero combinatorial degeneracies**:

.. list-table:: Exact Projective Census of Pascal's *Hexagrammum Mysticum* (``preset="hexagrammum"``)
   :header-rows: 1
   :widths: 26 12 62

   * - Geometric Stratum
     - Count
     - Incidence Law & Discoverer
   * - **Conic Chords** :math:`[P_i P_j]`
     - **15**
     - :math:`\binom{6}{2} = 15` secant lines joining pairs of the 6 conic vertices
   * - **Pascal Diagonal Points**
     - **45**
     - :math:`\frac{1}{2}\binom{6}{2}\binom{4}{2} = 45` intersections :math:`[P_i P_j] \cap [P_k P_l]`; 4 Pascal lines pass through each
   * - **Pascal Lines** :math:`p_H`
     - **60**
     - :math:`6! / 12 = 60` lines, each carrying 3 of the 45 diagonal points (:person:`Pascal <pascal>`, 1640)
   * - **Steiner Points** :math:`G`
     - **20**
     - 60 Pascal lines concur 3-by-3 at 20 Steiner points—2 per complementary triangle pair (:person:`Steiner <steiner>`, 1828)
   * - **Kirkman Points** :math:`K`
     - **60**
     - 60 Pascal lines also concur 3-by-3 in a **second** way at 60 Kirkman points—3 on each Pascal line (:person:`Kirkman <kirkman>`, 1850)
   * - **Plücker Lines** :math:`\ell_{\mathrm{Pl}}`
     - **15**
     - 20 Steiner points lie 4-by-4 along 15 Plücker lines—3 through each Steiner point (:person:`Plücker <pluecker>`, 1830)

Bi-Triangle :math:`S_3` Concurrency: How Pappus's Two Star Points Generalize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How do Steiner's **20 points** on a smooth conic relate to the **2 Star points** :math:`(S_+, S_-)` of the Pappus–Steiner theorem? Partition the six conic vertices into **two complementary inscribed triangles**—say :math:`\triangle_A = (P_0, P_2, P_4)` and :math:`\triangle_B = (P_1, P_3, P_5)`. There are :math:`\frac{1}{2}\binom{6}{3} = 10` such complementary triangle pairs.

Fixing :math:`\triangle_A` and permuting :math:`\triangle_B` by :math:`\sigma \in S_3` generates **6 alternating hexagons** :math:`\langle P_0, B_{\sigma_0}, P_2, B_{\sigma_1}, P_4, B_{\sigma_2} \rangle`—the exact smooth-conic counterpart of the six :math:`S_3` Pappus hexagons! Just as on two lines:

- The **3 even** (:math:`\sigma \in A_3`) Pascal lines concur at the even Steiner point :math:`G_+ = \left(\frac{78}{25},\; \frac{1}{25}\right)`.
- The **3 odd** (:math:`\sigma \in S_3 \setminus A_3`) Pascal lines concur at the odd Steiner point :math:`G_- = \left(\frac{498}{1565},\; \frac{281}{1565}\right)`.

Across all :math:`10` triangle partitions, :math:`10 \times 2 = \mathbf{20}` Steiner points arise; when the conic degenerates into two straight lines :math:`a \cup b`, only the single partition separating :math:`a` from :math:`b` survives without collapsing onto the carrier lines, leaving Pappus's two Star points :math:`(S_+, S_-)`!

.. picture:: /_static/constructions/pascal_steiner_family.svg
   :alt: Bi-Triangle S_3 Pascal Lines Concurring at Steiner Points G+ and G-

.. step::

   Partition the conic vertices on :g:`𝒞 <g3:( O P0 )>` into complementary triangles :math:`\triangle_A =` (:g:`P_0 <g3:P0>`, :g:`P_2 <g3:P2>`, :g:`P_4 <g3:P4>`) and :math:`\triangle_B =` (:g:`P_1 <g3:P1>`, :g:`P_3 <g3:P3>`, :g:`P_5 <g3:P5>`), joined by their nine cross-chords.

.. step::

   Trace the three **even** (:math:`A_3`) Pascal lines :g:`p_{012} <g3:[ M0143 M2145 ]>` (:math:`49x + 28y = 154`), :g:`p_{120} <g3:[ M0345 M2341 ]>` (:math:`15x + 5y = 47`), and :g:`p_{201} <g3:[ M0541 M2543 ]>` (:math:`39x + 33y = 123`), concurring at :g:`G_+ <g3:S1>` :math:`= \left(\frac{78}{25},\, \frac{1}{25}\right)`.

.. step::

   Trace the three **odd** (:math:`S_3 \setminus A_3`) Pascal lines :g:`p_{021} <g3:[ M0145 M2143 ]>`, :g:`p_{102} <g3:[ M0341 M2345 ]>` (:math:`5x - 20y + 2 = 0`), and :g:`p_{210} <g3:[ M0543 M2541 ]>` (:math:`83x - 19y = 23`), concurring inside the circle at :g:`G_- <g3:S2>` :math:`= \left(\frac{498}{1565},\, \frac{281}{1565}\right)`, and join the pair along :g:`G_+G_- <g3:[ S1 S2 ]>`.

Golden *Hexagrammum Mysticum* in :math:`\mathbb{Q}(\phi)`
---------------------------------------------------------

By **Michel Chasles's Theorem** (1865), four points :math:`P_0, P_1, P_2, P_3` on an irreducible conic :math:`\mathcal{C}` possess an intrinsic **conic cross-ratio** :math:`(P_0, P_1; P_2, P_3)_{\mathcal{C}}`: for any fifth observer point :math:`V \in \mathcal{C}`, the pencil of four rays :math:`[V P_0], [V P_1], [V P_2], [V P_3]` has the **exact same cross-ratio**, independent of :math:`V`.

Because Weierstrass stereographic projection is a birational isomorphism :math:`\mathbb{P}^1 \to \mathcal{C}`, seeding ``preset="golden_conic"`` with the golden stereographic chain :math:`t = (0,\, 1,\, \phi,\, \phi + 1,\, -1,\, -\phi)` inscribes six exact :math:`\mathbb{Q}(\sqrt{5})` points on :math:`x^2 + y^2 = 1`:

.. math::

   P_0 = (1, 0), \quad P_1 = (0, 1), \quad
   P_2 = \left(-\frac{\sqrt{5}}{5},\, \frac{2\sqrt{5}}{5}\right), \quad
   P_3 = \left(-\frac{\sqrt{5}}{3},\, \frac{2}{3}\right), \quad
   P_4 = (0, -1), \quad P_5 = \left(-\frac{\sqrt{5}}{5},\, -\frac{2\sqrt{5}}{5}\right).

1. **Chasles Golden Conic Cross-Ratio**: Calling ``conic_cross_ratio(P_0, P_1, P_2, P_3, V)`` from either :math:`V = P_4` or :math:`V = P_5` simplifies identically to the **Golden Ratio** :math:`\phi = \frac{1 + \sqrt{5}}{2}`!
2. **Emergent Golden Section on the Mystic Hexagram**: Constructing the inscribed hexagram on cycle :math:`\langle P_0, P_2, P_5, P_1, P_3, P_4 \rangle` yields exact opposite-side intersections:

   .. math::

      M_{03} = \left(\frac{5 - 4\sqrt{5}}{11},\; \frac{7 + \sqrt{5}}{11}\right), \qquad
      M_{14} = \left(-\frac{\sqrt{5}}{5},\; 0\right), \qquad
      M_{25} = \left(-\phi^{-1},\; -\phi\right) = \left(\frac{1 - \sqrt{5}}{2},\; -\frac{1 + \sqrt{5}}{2}\right).

   Running ``geometor.divine`` (``find_golden_sections``) on this model automatically discovers an **emergent golden section**: the Pascal intersection :math:`M_{25} = (-\phi^{-1}, -\phi)` extends the conic chord :math:`[P_4 P_0]` (:math:`y = x - 1`) in the **exact Divine Proportion**! Because :math:`x(P_0) - x(P_4) = 1 - 0 = 1` and :math:`x(P_4) - x(M_{25}) = 0 - (-\phi^{-1}) = \phi^{-1}` along the :math:`45^\circ` chord, :math:`|P_0 P_4| / |P_4 M_{25}| = |M_{25} P_0| / |P_0 P_4| = \phi` identically:

.. picture:: /_static/constructions/golden_pascal.svg
   :alt: Golden Hexagrammum Mysticum in Q(phi) — Emergent Section / M25 P4 P0 /

.. step::

   Project the golden parameter chain :math:`t = (0, 1, \phi, \phi + 1, -1, -\phi)` onto the unit circle :g:`𝒞 <g4:( O P0 )>` to obtain :g:`P_0 <g4:P0>`, :g:`P_1 <g4:P1>`, :g:`P_2 <g4:P2>`, :g:`P_3 <g4:P3>`, :g:`P_4 <g4:P4>`, and :g:`P_5 <g4:P5>`, where :math:`(P_0, P_1; P_2, P_3)_{\mathcal{C}} = \phi`.

.. step::

   Trace the hexagram :g:`P_0 P_2 P_5 P_1 P_3 P_4 <g4:< P0 P2 P5 P1 P3 P4 >>` and locate the three exact :math:`\mathbb{Q}(\sqrt{5})` opposite-side intersections :g:`M_{03} <g4:M03>`, :g:`M_{14} <g4:M14>`, and :g:`M_{25} <g4:M25>` :math:`= (-\phi^{-1}, -\phi)` on Pascal line :g:`p <g4:[ M03 M14 ]>`.

.. step::

   Inspect the emergent ``geometor.divine`` golden section :g:`M_{25} P_4 P_0 <g4:/ M25 P4 P0 />` along chord :g:`P_4 P_0 <g4:[ P4 P0 ]>`: :math:`|P_0 P_4| = \sqrt{2}` and :math:`|P_4 M_{25}| = \phi^{-1}\sqrt{2}`, dividing the extended conic chord in the exact Golden Ratio :math:`\phi = \frac{1 + \sqrt{5}}{2}`.
