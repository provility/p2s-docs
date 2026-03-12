---
title: chain
sidebar_label: chain
---

# chain

Positions one vector so its tail starts at another vector's tip, implementing tail-to-tip graphical vector addition.

**Utility:** Position a vector's tail at another vector's tip for tail-to-tip addition

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The graph container |
| `vecA` | `vector` | Yes | The target vector (chain attaches to its tip) |
| `vecB` | `vector` | Yes | The source vector (moved to start at vecA's tip) |

## Variants

### Chain two vectors

```js
chain(G, vecA, vecB)
```

Place vecB's tail at vecA's tip

## Examples

### Chain a vertical vector to a horizontal one (vector addition)

```js
A = vector(G, 0, 0, 3, 0)
B = vector(G, 0, 0, 0, 2)
C = chain(G, A, B)
```

### Chain multiple vectors in sequence

```js
V1 = vector(G, 0, 0, 3, 0)
V2 = vector(G, 0, 0, 1, 2)
V3 = vector(G, 0, 0, -1, 1)
C1 = chain(G, V1, V2)
C2 = chain(G, C1, V3)
```

### Visualize vector addition with resultant

```js
A = vector(G, 0, 0, 4, 1)
B = vector(G, 0, 0, 1, 3)
chained = chain(G, A, B)
resultant = vector(G, 0, 0, 5, 4, c(red))
```

### Chain two force vectors for equilibrium analysis

```js
F1 = vector(G, 0, 0, 3, 4)
F2 = vector(G, 0, 0, -2, 1)
F_sum = chain(G, F1, F2)
```
