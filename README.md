# 🎓 Empirical Trace Moments and Eigenvalue Distributions of the Wishart Ensemble

This project numerically investigates two foundational results in random matrix theory:

1. **Normalized Trace Moments**  
   We compute empirical estimates of  
   \[
   \frac{1}{N} \mathbb{E}[\mathrm{Tr}(S^k)] \quad \text{where} \quad S = X X^\dagger
   \]  
   for a complex Ginibre matrix \( X \). As \( N \to \infty \), these moments converge to the **Catalan numbers**, a key result derived in my thesis.

2. **Empirical Eigenvalue Distributions**  
   We simulate the eigenvalues of the Wishart matrix \( S = X X^\dagger \) for various \( N \) and overlay their empirical density against the **Marchenko–Pastur law** for \( c = 1 \), given by:
   \[
   d\text{MP}_1(x) = \frac{\sqrt{4x - x^2}}{2\pi x} \, \mathbf{1}_{[0,4]}(x) \, dx
   \]

---

## 📁 Files

- `trace_vs_catalan.ipynb`  
  Simulates trace moments and compares against Catalan numbers  
  **→ See rendered version in `trace_vs_catalan.html`**

- `empirical_eigenvalues.ipynb`  
  Simulates eigenvalue histograms for various values of \( N \), overlaid with the Marchenko–Pastur distribution

---

## 💻 Setup

Install requirements:

```bash
pip install -r requirements.txt
