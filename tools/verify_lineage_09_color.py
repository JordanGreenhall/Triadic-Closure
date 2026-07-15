#!/usr/bin/env python3
"""Independent verification for Frontier Lineage 9.

Builds H=sum_{i<j,a} T_i^a T_j^a on (C^3)^tensor3 using
T^a=lambda^a/2. Verifies the spectrum and tests two independently
specified spectral flows from seeded random starts.
"""
import numpy as np

I = np.eye(3, dtype=complex)
lam = [
    np.array([[0,1,0],[1,0,0],[0,0,0]], complex),
    np.array([[0,-1j,0],[1j,0,0],[0,0,0]], complex),
    np.array([[1,0,0],[0,-1,0],[0,0,0]], complex),
    np.array([[0,0,1],[0,0,0],[1,0,0]], complex),
    np.array([[0,0,-1j],[0,0,0],[1j,0,0]], complex),
    np.array([[0,0,0],[0,0,1],[0,1,0]], complex),
    np.array([[0,0,0],[0,0,-1j],[0,1j,0]], complex),
    np.diag([1,1,-2]).astype(complex)/np.sqrt(3),
]
T = [x/2 for x in lam]
H = np.zeros((27,27), complex)
for A in T:
    H += np.kron(np.kron(A,A),I)
    H += np.kron(np.kron(A,I),A)
    H += np.kron(np.kron(I,A),A)

assert np.linalg.norm(H-H.conj().T) < 1e-12
w, V = np.linalg.eigh(H)
expected = np.array([-2.0] + [-0.5]*16 + [1.0]*10)
assert np.max(np.abs(w-expected)) < 1e-12, w

P = np.outer(V[:,0], V[:,0].conj())
rng = np.random.default_rng(20260715)
minimum = [1.0, 1.0]
for _ in range(200):
    z = rng.normal(size=27) + 1j*rng.normal(size=27)
    z /= np.linalg.norm(z)
    coeff = V.conj().T @ z
    # Binding-coherence: normalized exp(-tau H).
    y1 = V @ (np.exp(-12*w)*coeff)
    # Conditioning-degree: normalized exp(+tau H^2).
    y2 = V @ (np.exp(12*w*w)*coeff)
    for j, y in enumerate((y1,y2)):
        y /= np.linalg.norm(y)
        fidelity = float(np.real(y.conj() @ (P @ y)))
        minimum[j] = min(minimum[j], fidelity)

assert min(minimum) > 0.999999999, minimum
print("spectrum: -2 (1), -1/2 (16), +1 (10)")
print("minimum singlet fidelity over 200 starts:", minimum)
