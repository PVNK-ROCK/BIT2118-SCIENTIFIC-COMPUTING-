# Task 9: Eigenvalues and Eigenvectors

**Concept:** An eigenvector v of A satisfies Av = λv: the transformation only stretches it by the eigenvalue λ. The dominant eigenvector of a network's adjacency matrix measures node importance (eigenvector centrality).

**Files:** [`code/Task_09_eigenvalues.py`](../code/Task_09_eigenvalues.py) (given program) · [`code/Task_09_extension.py`](../code/Task_09_extension.py) (parameter change + new real-world case)

---

## 1. Inputs and mathematical operation

- **Input values:** a 4 × 4 adjacency matrix of a network (A–B, A–C, B–C, B–D, C–D).
- **Mathematical operations:** `np.linalg.eig`, picking the largest eigenvalue, normalising its eigenvector, and checking ‖Av − λv‖.

## 2. Output of the program

```text
All eigenvalues: [ 2.5616  0.     -1.5616 -1.    ]
Dominant eigenvalue: 2.5615528128088285
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 1.9357399876532506e-15
```

## 3. Interpretation of the output

The dominant eigenvalue is **2.5616**. Nodes **B and C (0.2808 each)** are more influential than **A and D (0.2192 each)** because they have three connections and are connected to each other and to the other well-connected nodes. The verification error ≈ 2 × 10⁻¹⁵ confirms Av = λv. There is no graph in this task.

## 4. Changing an input / parameter

**Change made:** a new link between A and D was added.

```text
Original: dominant eigenvalue=2.5616, importance (A,B,C,D)=[0.2192 0.2808 0.2808 0.2192]
With A-D link: dominant eigenvalue=3.0000, importance (A,B,C,D)=[0.25 0.25 0.25 0.25]
```

**How the result changes:** Every node now has three connections (all nodes are mutually connected), so the dominant eigenvalue rises to exactly **3.0** and all four nodes have the same importance of **0.25**. Adding one link removed the difference in influence between the nodes.

## 5. Modified program for a different but related real-world case

**Case:** PageRank of a 5-page website

**New assumptions**

- Links: Home → Products, Blog; Products → Home, Contact; Blog → Home, Products, About; About → Home, Contact; Contact → Home, About.
- A visitor follows a random link with probability d = 0.85 and jumps to a random page with probability 0.15 (damping).
- The Google matrix is G = d·M + (1−d)/5·J, M being the column-normalised link matrix.

**Input data:** `links` matrix in `code/Task_09_extension.py`.

**Output**

```text
Dominant eigenvalue of Google matrix: 1.0
Home     : 0.3035
Products : 0.2040
Contact  : 0.1814
Blog     : 0.1590
About    : 0.1521
```

**Interpretation:** The dominant eigenvalue of G is exactly 1 (it is a probability matrix), and its eigenvector, normalised to sum to 1, gives the page ranks. **Home (0.3035)** ranks highest because every other page links to it. Products is second since two pages link to it; About is lowest. This is the idea behind Google's original PageRank algorithm.
