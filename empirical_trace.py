import numpy as np
import matplotlib.pyplot as plt
from math import comb

def generate_ginibre_matrix(N):
    """Generates an N x N complex Ginibre matrix with entries ~ CN(0, 1/N)."""
    real = np.random.normal(0, 1/np.sqrt(2*N), (N, N))
    imag = np.random.normal(0, 1/np.sqrt(2*N), (N, N))
    return real + 1j * imag

def compute_trace_moment(N, k, trials=100):
    """Computes normalized E[Tr(S^k)] where S = X X† over multiple trials."""
    total = 0
    for _ in range(trials):
        X = generate_ginibre_matrix(N)
        S = X @ X.conj().T
        total += np.trace(np.linalg.matrix_power(S, k)).real
    return total / (trials * N)

def catalan_number(k):
    """Returns the k-th Catalan number."""
    return comb(2*k, k) // (k + 1)

if __name__ == "__main__":
    N_values = [10, 50, 100, 200]
    trials = 100
    max_k = 15
    ks = list(range(1, max_k + 1))
    catalan = [catalan_number(k) for k in ks]

    plt.figure(figsize=(10, 6))

    for N in N_values:
        simulated = [compute_trace_moment(N, k, trials) for k in ks]
        plt.plot(ks, simulated, marker='o', label=f"Simulated (N={N})")

    plt.plot(ks, catalan, 'k--', marker='x', label="Catalan $C_k$", linewidth=2)
    plt.xlabel("k")
    plt.ylabel("Moment Value")
    plt.title("Normalized Trace Moments vs Catalan Numbers (Varying N)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
