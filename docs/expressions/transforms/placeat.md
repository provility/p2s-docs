---
title: placeat
sidebar_label: placeat
---

# placeat

Copies a vector or line to a new starting point, preserving its direction and magnitude.

**Utility:** Copy a vector to start at a new position while preserving direction and magnitude

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The graph container |
| `vector` | `vector \| line` | Yes | The vector or line to copy |
| `point` | `point` | Yes | The new starting point for the copied vector |

## Variants

### Place at a point expression

```js
placeat(G, vec, point)
```

Copy vector to start at the given point

### Place at coordinates

```js
placeat(G, vec, x, y)
```

Copy vector to start at (x, y)

### Place a line as vector

```js
placeat(G, line, point)
```

Copy line as a vector starting at the given point

## Examples

### Copy a vector to a new starting point

```js
V = vector(G, 0, 0, 3, 2)
V2 = placeat(G, V, point(G, 1, 1))
```

### Copy a vector to explicit coordinates

```js
V = vector(G, 0, 0, 3, 2)
V2 = placeat(G, V, 2, 3)
```

### Build a parallelogram by placing vectors at tips

```js
A = vector(G, 0, 0, 4, 0)
B = vector(G, 0, 0, 1, 3)
A2 = placeat(G, A, point(G, 1, 3))
B2 = placeat(G, B, point(G, 4, 0))
```

### Place a line as a vector at a new position

```js
L = line(G, 0, 0, 3, 0)
V = placeat(G, L, point(G, 0, 4))
```

### Compare equivalent vectors at different positions

```js
V = vector(G, 0, 0, 2, 3)
V1 = placeat(G, V, point(G, 3, 0))
V2 = placeat(G, V, point(G, 6, 0))
```
