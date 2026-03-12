---
title: cross
sidebar_label: cross
---

# cross

Computes the cross product of two vectors, returning a scalar (signed parallelogram area) in 2D or a perpendicular vector in 3D.

**Utility:** Calculate the cross product of two vectors (scalar in 2D, vector in 3D)

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `vectorA` | `vector` | Yes | First vector |
| `vectorB` | `vector` | Yes | Second vector |
| `position` | `point` | No | Optional start position for 3D result vector |

## Variants

### 2D cross product

```js
cross(vecA, vecB)
```

Cross product of two 2D vectors, returns scalar (z-component)

### 3D cross product

```js
cross(vec3dA, vec3dB)
```

Cross product of two 3D vectors, returns a vector

### 3D cross at position

```js
cross(vec3dA, vec3dB, point)
```

3D cross product result placed at given point

## Examples

### Create graph and two vectors

```js
G = g2d(at(8, 0), 20, 20)
```

### Vector along x-axis

```js
A = vector(G, 0, 0, 3, 0)
```

### Vector along y-axis

```js
B = vector(G, 0, 0, 0, 4)
```

### Cross product (returns 12, the area of the parallelogram)

```js
c1 = cross(A, B)
```

### Two general vectors

```js
C = vector(G, 0, 0, 2, 3)
```

### Cross product of A and C

```js
c2 = cross(A, C)
```
