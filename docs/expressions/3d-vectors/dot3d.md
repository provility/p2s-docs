---
title: dot
sidebar_label: dot
---

# dot

Computes the dot product (scalar product) of two vectors, returning a single numeric value equal to the product of their magnitudes times the cosine of the angle between them.

**Utility:** Compute dot product of two vectors, returning a scalar value

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `vecA` | `vector3d \| line3d \| vector \| line` | Yes | First vector operand |
| `vecB` | `vector3d \| line3d \| vector \| line` | Yes | Second vector operand |

## Variants

### Dot product of two 3D vectors

```
dot(A, B)
```

Returns scalar a*b = ax*bx + ay*by + az*bz

### Assigned to variable for reuse

```
d = dot(A, B)
```

Store the scalar result for use in further expressions

## Examples

### Dot product of two 3D vectors

```
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 1, 2, 3)
B = vector3d(G, 0, 0, 0, 4, 5, 6)
d = dot(A, B)
```

### Check orthogonality - dot product is zero for perpendicular vectors

```
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 1, 0, 0)
B = vector3d(G, 0, 0, 0, 0, 1, 0)
d = dot(A, B)
```

### Dot product of parallel vectors equals product of magnitudes

```
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 2, 0, 0)
B = vector3d(G, 0, 0, 0, 5, 0, 0)
d = dot(A, B)
```
