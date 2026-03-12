---
title: cross
sidebar_label: cross
---

# cross

Computes the 3D cross product of two vectors, returning a new vector perpendicular to both inputs according to the right-hand rule.

**Utility:** Compute cross product of two 3D vectors, returning a perpendicular vector

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `vecA` | `vector3d \| line3d` | Yes | First vector operand |
| `vecB` | `vector3d \| line3d` | Yes | Second vector operand |
| `startPoint` | `point3d \| x, y, z` | No | Optional start position for the result vector (defaults to origin) |

## Variants

### Basic 3D cross product

```js
cross(A, B)
```

Cross product A x B, result starts at origin

### Cross product placed at a point

```js
cross(A, B, point3d(G, 1, 1, 1))
```

Cross product A x B, result starts at point (1,1,1)

### Cross product placed at coordinates

```js
cross(A, B, 2, 3, 4)
```

Cross product A x B, result starts at (2,3,4)

## Examples

### Cross product of x-axis and y-axis unit vectors gives z-axis

```js
G = g3d(at(0, 0), 30, 30)
i = vector3d(G, 0, 0, 0, 1, 0, 0, c(red))
j = vector3d(G, 0, 0, 0, 0, 1, 0, c(green))
k = cross(i, j, c(blue))
```

### Find normal vector to two direction vectors

```js
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 2, 1, 0)
B = vector3d(G, 0, 0, 0, 0, 1, 3)
N = cross(A, B, c(purple))
```

### Cross product placed at a specific point

```js
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 3, 0, 0)
B = vector3d(G, 0, 0, 0, 0, 4, 0)
P = point3d(G, 1, 1, 0)
N = cross(A, B, P)
```
