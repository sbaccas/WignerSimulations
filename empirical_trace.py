import numpy as np

def generate_ginibre_matrix(N):
    """Generates an N x N complex Ginibre matrix with entries ~ CN(0, 1/N)."""
    real = np.random.normal(0, 1/np.sqrt(2*N), (N, N))
    imag = np.random.normal(0, 1/np.sqrt(2*N), (N, N))
    return real + 1j * imag

def compute_trace_moment(N, k, trials=1000):
    """Computes E[Tr(S^k)] where S = X X† over multiple trials."""
    trace_moments = []
    for _ in range(trials):
        X = generate_ginibre_matrix(N)
        S = X @ X.conj().T
        trace_moments.append(np.trace(np.linalg.matrix_power(S, k)).real)
    return np.mean(trace_moments)

# Example usage
if __name__ == "__main__":
    N = 100
    for k in range(1, 6):
        mk = compute_trace_moment(N, k)
        print(f"E[Tr(S^{k})] ≈ {mk:.4f}")
