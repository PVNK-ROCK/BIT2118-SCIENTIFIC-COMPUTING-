"""Task 5 extension: (A) change angle and scale, (B) 2-link robot arm kinematics."""
import numpy as np

def rot(deg):
    a = np.deg2rad(deg)
    return np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])

print("=== PART A: change rotation to 90 degrees and scale to (3, 1) ===")
square = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
T = rot(90) @ np.diag([3.0, 1.0])
print("Transformation matrix:\n", np.round(T, 4))
print("Transformed points:\n", np.round(square @ T.T, 4))
print("Determinant (area scale factor):", round(np.linalg.det(T), 4))

print("\n=== PART B: 2-link robot arm (forward kinematics) ===")
# Assumptions: link 1 = 0.40 m, link 2 = 0.30 m, joint angles measured anticlockwise
L1, L2 = 0.40, 0.30
def end_effector(theta1, theta2):
    elbow = rot(theta1) @ np.array([L1, 0.0])
    tip = elbow + rot(theta1 + theta2) @ np.array([L2, 0.0])
    return elbow, tip
for t1, t2 in [(0, 0), (30, 45), (90, -90), (45, 90)]:
    elbow, tip = end_effector(t1, t2)
    reach = np.linalg.norm(tip)
    print(f"theta1={t1:>3}, theta2={t2:>3}: elbow={np.round(elbow, 3)}, tip={np.round(tip, 3)}, reach={reach:.3f} m")
