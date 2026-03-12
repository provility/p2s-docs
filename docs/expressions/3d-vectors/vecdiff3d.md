---
title: vecdiff3d
sidebar_label: vecdiff3d
---

# vecdiff3d

Subtracts two 3D vectors component-wise, returning the difference vector A minus B. Only the displacement of each input is used, not its position.

**Utility:** Subtract two 3D vectors and return the difference vector

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `vecA` | `vector3d \| line3d` | Yes | Vector to subtract from (minuend) |
| `vecB` | `vector3d \| line3d` | Yes | Vector to subtract (subtrahend) |
| `startPoint` | `point3d \| x, y, z` | No | Optional start position for the result vector (defaults to origin) |

## Variants

### Basic subtraction from origin

```js
vecdiff3d(A, B)
```

Difference A - B, result starts at origin (0,0,0)

### Subtraction with point3d start

```js
vecdiff3d(A, B, point3d(G, 1, 1, 1))
```

Difference A - B, result starts at point (1,1,1)

### Subtraction with coordinate start

```js
vecdiff3d(A, B, 2, 3, 4)
```

Difference A - B, result starts at (2,3,4)

## Examples

### Subtract two vectors, result at origin

```js
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 3, 2, 1)
B = vector3d(G, 0, 0, 0, 1, 1, 0)
D = vecdiff3d(A, B)
```

### Subtract two vectors with result placed at a point

```js
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 5, 3, 2)
B = vector3d(G, 0, 0, 0, 2, 1, 1)
P = point3d(G, 1, 1, 1)
D = vecdiff3d(A, B, P)
```

### Visualize relative displacement between two direction vectors

```js
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 4, 0, 0, c(red))
B = vector3d(G, 0, 0, 0, 1, 3, 0, c(blue))
D = vecdiff3d(A, B, c(orange))
```
