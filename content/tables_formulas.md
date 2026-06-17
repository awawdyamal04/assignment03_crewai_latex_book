<!-- file: tables_formulas.md — offline technical asset, no LLM, no real data -->

# Technical Assets — Table and Formula

> Course-aligned technical content for course **203.3763 — Orchestration of
> AI Agents**. These assets are conceptual/definitional (textbook-level), not
> experimental results, and are generated offline without calling any LLM.

## 1. Comparison Table

<!-- TABLE-ASSET -->
| Model / System | Core mechanism | Sequence handling | Long-range dependencies | Parallelism |
|----------------|----------------|-------------------|-------------------------|-------------|
| **RNN** | Recurrent hidden state | Step-by-step (O(n) path) | Weak — vanishing/exploding gradients | Low (sequential) |
| **LSTM** | Gated cell state (input/forget/output) | Step-by-step (O(n) path) | Improved via gating + cell memory | Low (sequential) |
| **Transformer** | Scaled dot-product self-attention | All positions at once (O(1) path) | Strong — direct pairwise access | High (parallel) |
| **CrewAI agents** | Role-based agents + shared context | Sequential task hand-off | Carried by passed task context | Orchestrated (per process) |

*Table: conceptual comparison of recurrent models, the Transformer, and
CrewAI agent orchestration.*

## 2. Complex Formula — Scaled Dot-Product Attention

<!-- FORMULA-ASSET -->

$$
\operatorname{Attention}(Q, K, V) = \operatorname{softmax}\!\left(\frac{Q K^{T}}{\sqrt{d_k}}\right) V
$$

Plain-text form: `Attention(Q,K,V) = softmax((Q K^T) / sqrt(d_k)) V`.

## 3. Explanation

The scaled dot-product attention is the core operation of the Transformer
(Vaswani et al., 2017). For each query in $Q$, the dot products $Q K^{T}$
score how relevant every key in $K$ is. Dividing by $\sqrt{d_k}$ — the
square root of the key dimension — keeps those scores from growing too
large, which would otherwise push the `softmax` into regions with vanishing
gradients. The `softmax` turns the scaled scores into a probability
distribution (attention weights) that is then used to take a weighted sum of
the value vectors $V$. The result is a context-aware representation in which
every position can attend **directly** to every other position, removing the
long sequential dependency path that limits RNNs and LSTMs.

## 4. Note

<!-- COURSE-ALIGNED-NOTE -->
This table and formula are **course-aligned technical content**: they restate
established definitions from the course material and the cited literature and
contain no fabricated experimental data.
