---
title: vecsum3d
sidebar_label: vecsum3d
---

# vecsum3d

Adds two 3D vectors component-wise, returning the resultant sum vector. Only the displacement of each input is used, not its position.

**Utility:** Add two 3D vectors and return the resultant vector

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `vecA` | `vector3d \| line3d` | Yes | First vector operand |
| `vecB` | `vector3d \| line3d` | Yes | Second vector operand |
| `startPoint` | `point3d \| x, y, z` | No | Optional start position for the result vector (defaults to origin) |

## Variants

### Basic addition from origin

```js
vecsum3d(A, B)
```

Sum of A + B, result starts at origin (0,0,0)

### Addition with point3d start

```js
vecsum3d(A, B, point3d(G, 1, 1, 1))
```

Sum of A + B, result starts at point (1,1,1)

### Addition with coordinate start

```js
vecsum3d(A, B, 2, 3, 4)
```

Sum of A + B, result starts at (2,3,4)

## Examples

### Add two vectors from origin, result at origin

```js
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 3, 0, 0)
B = vector3d(G, 0, 0, 0, 0, 2, 0)
S = vecsum3d(A, B)
```

### Add two vectors with result placed at a point

```js
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 3, 0, 0)
B = vector3d(G, 0, 0, 0, 0, 2, 0)
P = point3d(G, 1, 1, 1)
S = vecsum3d(A, B, P)
```

### Visualize parallelogram law of addition

```js
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 2, 1, 0, c(red))
B = vector3d(G, 0, 0, 0, 0, 1, 2, c(blue))
S = vecsum3d(A, B, c(green))
```
