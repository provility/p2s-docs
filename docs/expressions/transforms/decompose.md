---
title: decompose
sidebar_label: decompose
---

# decompose

Decomposes a vector into its parallel or perpendicular component relative to a reference direction.

**Utility:** Decompose a vector into parallel or perpendicular component relative to another vector

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The graph container |
| `vecSource` | `vector` | Yes | The vector to decompose |
| `vecReference` | `vector` | Yes | The reference vector to decompose along |
| `mode` | `"perp"` | No | Pass "perp" for perpendicular component (default: parallel) |

## Variants

### Parallel component (default)

```js
decompose(G, vecSource, vecReference)
```

Get the parallel (projection) component of vecSource along vecReference

### Perpendicular component

```js
decompose(G, vecSource, vecReference, "perp")
```

Get the perpendicular component of vecSource relative to vecReference

## Examples

### Get parallel component of a force vector

```js
F = vector(G, 0, 0, 3, 4)
D = vector(G, 0, 0, 5, 0)
F_par = decompose(G, F, D)
```

### Get perpendicular component of a force vector

```js
F = vector(G, 0, 0, 3, 4)
D = vector(G, 0, 0, 5, 0)
F_perp = decompose(G, F, D, "perp")
```

### Decompose a vector into both components

```js
V = vector(G, 0, 0, 4, 3)
Ref = vector(G, 0, 0, 5, 1)
V_par = decompose(G, V, Ref)
V_perp = decompose(G, V, Ref, "perp")
```

### Visualize force decomposition along an incline

```js
gravity = vector(G, 3, 5, 3, 0)
incline = vector(G, 0, 0, 5, 3)
g_along = decompose(G, gravity, incline)
g_normal = decompose(G, gravity, incline, "perp")
```
