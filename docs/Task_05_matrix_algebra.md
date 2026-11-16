# Task 5: Matrix Algebra and Matrix Operations

**Concept:** A matrix is a rectangular array of numbers; multiplying a coordinate vector by a matrix rotates, scales or otherwise transforms it. The determinant measures how much the transformation scales area.

**Files:** [`code/Task_05_matrix_algebra.py`](../code/Task_05_matrix_algebra.py) (given program) · [`code/Task_05_extension.py`](../code/Task_05_extension.py) (parameter change + new real-world case)

---

## 1. Inputs and mathematical operation

- **Input values:** the corners of a unit square, a 45° rotation matrix R and a scaling matrix S = diag(2, 1.5).
- **Mathematical operations:** matrix multiplication T = R·S, transforming every point (`points @ T.T`), and the determinant det(T).

## 2. Output of the program

```text
Original points:
 [[0. 0.]
 [1. 0.]
 [1. 1.]
 [0. 1.]]
Transformation matrix:
 [[ 1.41421356 -1.06066017]
 [ 1.41421356  1.06066017]]
Transformed points:
 [[ 0.          0.        ]
 [ 1.41421356  1.41421356]
 [ 0.35355339  2.47487373]
 [-1.06066017  1.06066017]]
Determinant: 2.9999999999999996
```

## 3. Interpretation of the output

- The corner (1, 0) is first stretched to (2, 0) by S, then rotated 45° by R to (1.414, 1.414), exactly the second transformed point. The origin stays at (0, 0).
- The **determinant is 3.0 = 2 × 1.5**: the unit-area square becomes a parallelogram of area 3. Rotation does not change area, so the area change is caused only by scaling.
- There is no graph in this task.

## 4. Changing an input / parameter

**Change made:** rotation angle 45° → **90°** and scale (2, 1.5) → **(3, 1)**.

```text
Transformation matrix:
 [[ 0. -1.]
 [ 3.  0.]]
Transformed points:
 [[ 0.  0.]
 [ 0.  3.]
 [-1.  3.]
 [-1.  0.]]
Determinant (area scale factor): 3.0
```

**How the result changes:** The square is now rotated a quarter-turn and stretched only in the original x-direction: the corners become (0,0), (0,3), (−1,3), (−1,0), a 1 × 3 rectangle standing upright. The determinant is again 3 (3 × 1), so the area is the same as before even though the shape is different. The determinant depends only on the scale factors, not on the angle.

## 5. Modified program for a different but related real-world case

**Case:** Forward kinematics of a 2-link robot arm

**New assumptions**

- Link 1 = 0.40 m, link 2 = 0.30 m; joint angles measured anticlockwise; the base is at the origin.
- The elbow position is R(θ₁)·[L₁, 0]ᵀ and the tip is the elbow plus R(θ₁+θ₂)·[L₂, 0]ᵀ.

**Input data:** Four joint-angle pairs (θ₁, θ₂): (0,0), (30,45), (90,−90), (45,90), in degrees.

**Output**

```text
theta1=  0, theta2=  0: elbow=[0.4 0. ], tip=[0.7 0. ], reach=0.700 m
theta1= 30, theta2= 45: elbow=[0.346 0.2  ], tip=[0.424 0.49 ], reach=0.648 m
theta1= 90, theta2=-90: elbow=[0.  0.4], tip=[0.3 0.4], reach=0.500 m
theta1= 45, theta2= 90: elbow=[0.283 0.283], tip=[0.071 0.495], reach=0.500 m
```

**Interpretation:** Rotation matrices convert joint angles into positions. With both joints straight the arm reaches its maximum of **0.700 m** (0.4 + 0.3). Bending the elbow shortens the reach: 0.648 m for (30°, 45°) and 0.500 m for the two bent poses. For θ₁ = 90°, θ₂ = −90° the tip is at (0.3, 0.4): the first link points up and the second points right. A robot controller multiplies matrices in exactly this way for every pose.
