# Transformer Forward and Backward Pass

## Forward Pass

### 1. Input Embedding
- **Shape**: `(batch_size, seq_length, embedding_dim) = (2, 5, 8)`
- **Example**: 2 sentences, each with 5 tokens, and each token has an 8-dimensional embedding.

### 2. Adding Positional Embeddings
- **Shape remains**: `(2, 5, 8)`
- Positional embeddings are added to input token embeddings to encode sequence order.

### 3. Multi-Head Self-Attention

#### a. Linear Projections (Q, K, V)
- We project the input embeddings into **queries (Q)**, **keys (K)**, and **values (V)** using **learned weight matrices**.
- For **2 attention heads**, each head projects the 8-dimensional input to a **4-dimensional space** using different learned matrices.
  - **Projection matrices**: `W_Q`, `W_K`, and `W_V` (shape: `(embedding_dim, head_dim) = (8, 4)`).
  
- **Shape after projection for each head**: `(batch_size, seq_length, head_dim) = (2, 5, 4)` for Q, K, V.

#### b. Attention Calculation
- For each head, compute **attention scores** by:
  - Dot product of `Q` and `K^T`: `Q x K^T`
  - Apply softmax to get attention weights.
  - Multiply attention weights with `V` to get the output for each head.
  
- **Result per head**: `(2, 5, 4)` (for each head).

#### c. Concatenating Heads
- The outputs of the 2 heads are concatenated, restoring the original embedding dimension.
- **Shape after concatenation**: `(2, 5, 8)`.

### 4. Feed-Forward Network (FFN)
- Apply a feed-forward network (2 linear layers) independently to each token.
  - First layer: Projects from 8D to 16D.
  - Second layer: Projects back from 16D to 8D.
  
- **Output shape**: `(2, 5, 8)`.

---

## Backward Pass

### 1. Compute Loss
- Use a loss function (e.g., cross-entropy) to compute the error between predicted outputs and true labels.
- **Shape of predictions**: `(2, 5, num_classes)`.

### 2. Backpropagation

#### a. Backprop through Feed-Forward Network (FFN)
- Compute gradients of the loss with respect to the weights of the FFN layers and update them using an optimizer (e.g., Adam).

#### b. Backprop through Multi-Head Attention
- Gradients are backpropagated through each attention head:
  - **Gradients for Q, K, V projections**: Update the learned matrices `W_Q`, `W_K`, and `W_V` based on gradients computed during backprop.
  - Each head updates its projection matrices independently, allowing parallelization.

### 3. Gradient Update
- The optimizer updates all weights based on computed gradients, adjusting the transformer parameters to minimize the loss in the next forward pass.

---

## Key Points
- **Multi-Head Attention**: We project the input into **lower dimensions** for each head using learned matrices. These projections are **independent** for each head, allowing **parallelization**.
- **After Attention**: The heads' outputs are concatenated, and the model continues with feed-forward layers.
- **Backpropagation**: The gradients are computed for each head separately, and updates to the weights are applied accordingly.
