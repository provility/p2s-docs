---
title: dot
sidebar_label: dot
---

# dot

Computes the dot product of two vectors, returning a scalar value that measures their directional alignment.

**Utility:** Calculate the dot product (scalar) of two vectors

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `vectorA` | `vector` | Yes | First vector |
| `vectorB` | `vector` | Yes | Second vector |

## Variants

### 2D dot product

```js
dot(vecA, vecB)
```

Dot product of two 2D vectors, returns scalar

### 3D dot product

```js
dot(vec3dA, vec3dB)
```

Dot product of two 3D vectors, returns scalar

## Examples

### Create graph and two vectors

```js
G = g2d(at(8, 0), 20, 20)
```

### First vector along x-axis

```js
A = vector(G, 0, 0, 3, 0)
```

### Second vector along y-axis

```js
B = vector(G, 0, 0, 0, 4)
```

### Dot product of perpendicular vectors (returns 0)

```js
d1 = dot(A, B)
```

### Vectors at an angle

```js
C = vector(G, 0, 0, 3, 4)
```

### Dot product of A and C (returns 9)

```js
d2 = dot(A, C)
```
