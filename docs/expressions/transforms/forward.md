---
title: forward
sidebar_label: forward
---

# forward

Shifts a vector or line forward along its own direction by a specified distance, preserving orientation and magnitude.

**Utility:** Shift a vector forward along its direction by a given distance

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The graph container |
| `vector` | `vector \| line` | Yes | The vector or line to shift forward |
| `distance` | `number` | Yes | Distance to shift forward along the vector direction |

## Variants

### Forward shift vector

```js
forward(G, vec, distance)
```

Shift vector forward by distance along its direction

### Forward shift line

```js
forward(G, line, distance)
```

Shift line forward by distance (returns vector)

## Examples

### Shift a vector forward by 2 units

```js
V = vector(G, 0, 0, 3, 2)
F = forward(G, V, 2)
```

### Create a stepped progression of vectors

```js
V = vector(G, 0, 0, 1, 1)
F1 = forward(G, V, 1)
F2 = forward(G, V, 2)
F3 = forward(G, V, 3)
```

### Shift a line forward as a vector

```js
L = line(G, 0, 0, 4, 0)
F = forward(G, L, 3)
```

### Forward with default distance

```js
V = vector(G, 1, 1, 4, 3)
fwd1 = forward(G, V, 1)
```
