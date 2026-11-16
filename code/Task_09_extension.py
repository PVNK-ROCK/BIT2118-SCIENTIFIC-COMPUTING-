"""Task 9 extension: (A) change the network, (B) PageRank of a 5-page website."""
import numpy as np

print("=== PART A: add a link between nodes A and D ===")
A = np.array([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]], dtype=float)
A2 = A.copy(); A2[0, 3] = A2[3, 0] = 1
for name, M in (("Original", A), ("With A-D link", A2)):
    vals, vecs = np.linalg.eig(M)
    i = np.argmax(vals.real); v = np.abs(vecs[:, i].real); v /= v.sum()
    print(f"{name}: dominant eigenvalue={vals[i].real:.4f}, importance (A,B,C,D)={np.round(v, 4)}")

print("\n=== PART B: PageRank for a 5-page website ===")
pages = ["Home", "Products", "Blog", "About", "Contact"]
# links[i][j] = 1 if page j links to page i  (columns = outgoing links)
links = np.array([
    [0, 1, 1, 1, 1],   # Home receives links from everyone
    [1, 0, 1, 0, 0],   # Products
    [1, 0, 0, 0, 0],   # Blog
    [0, 0, 1, 0, 1],   # About
    [0, 1, 0, 1, 0],   # Contact
], dtype=float)
M = links / links.sum(axis=0)                 # column-stochastic
d = 0.85                                      # damping factor (assumed)
G = d * M + (1 - d) / 5 * np.ones((5, 5))     # Google matrix
vals, vecs = np.linalg.eig(G)
i = np.argmax(vals.real)
rank = np.abs(vecs[:, i].real); rank /= rank.sum()
print("Dominant eigenvalue of Google matrix:", round(vals[i].real, 6))
for p, r in sorted(zip(pages, rank), key=lambda t: -t[1]):
    print(f"{p:9s}: {r:.4f}")
