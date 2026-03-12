---
title: backward
sidebar_label: backward
---

# backward

Shifts a vector or line backward by a specified distance opposite to its direction, preserving orientation and magnitude.

**Utility:** Shift a vector backward (opposite direction) by a given distance

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The graph container |
| `vector` | `vector \| line` | Yes | The vector or line to shift backward |
| `distance` | `number` | Yes | Distance to shift backward (opposite to vector direction) |

## Variants

### Backward shift vector

```
backward(G, vec, distance)
```

Shift vector backward by distance opposite to its direction

### Backward shift line

```
backward(G, line, distance)
```

Shift line backward by distance (returns vector)

## Examples

### Shift a vector backward by 2 units

```
V = vector(G, 3, 2, 6, 4)
B = backward(G, V, 2)
```

### Create forward and backward copies of a vector

```
V = vector(G, 0, 0, 3, 0)
F = forward(G, V, 2)
B = backward(G, V, 2)
```

### Shift a line backward as a vector

```
L = line(G, 2, 0, 5, 0)
B = backward(G, L, 3)
```

### Backward with default distance

```
V = vector(G, 1, 1, 4, 3)
bwd1 = backward(G, V, 1)
```
