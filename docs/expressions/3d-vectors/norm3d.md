---
title: norm3d
sidebar_label: norm3d
---

# norm3d

Normalizes a 3D vector to unit length (magnitude 1) while preserving its direction, dividing each component by the vector's magnitude.

**Utility:** Normalize a 3D vector to unit length (magnitude 1)

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `vector3d \| line3d \| point3d, point3d \| x, y, z` | Yes | A vector3d, a line3d, two point3d expressions, or three numeric values |

## Variants

### From a vector3d

```
norm3d(V)
```

Unit vector in the direction of V, starting at V's start point

### From a line3d

```
norm3d(L)
```

Unit direction vector of the line

### From two points

```
norm3d(P1, P2)
```

Unit vector from point P1 toward point P2

### From three numbers

```
norm3d(3, 4, 0)
```

Unit vector from origin in direction (3,4,0)

## Examples

### Normalize a 3D vector to unit length

```
G = g3d(at(0, 0), 30, 30)
V = vector3d(G, 0, 0, 0, 3, 4, 0)
U = norm3d(V)
```

### Get unit direction of a line segment

```
G = g3d(at(0, 0), 30, 30)
L = line3d(G, 1, 1, 1, 4, 5, 1)
U = norm3d(L)
```

### Unit vector from numeric components

```
G = g3d(at(0, 0), 30, 30)
U = norm3d(3, 4, 0)
```

### Unit vector between two points

```
G = g3d(at(0, 0), 30, 30)
P1 = point3d(G, 0, 0, 0)
P2 = point3d(G, 6, 0, 8)
U = norm3d(P1, P2)
```
