---
title: vecproject3d
sidebar_label: vecproject3d
---

# vecproject3d

Projects one 3D vector onto another, returning the component of the first vector that lies along the direction of the second. The result is always parallel to the target vector.

**Utility:** Project one 3D vector onto another, returning the parallel component

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `vecToProject` | `vector3d \| line3d` | Yes | The vector being projected |
| `vecTarget` | `vector3d \| line3d` | Yes | The vector to project onto (defines the direction) |
| `startPoint` | `point3d \| x, y, z` | No | Optional start position for the result vector (defaults to origin) |

## Variants

### Basic projection from origin

```js
vecproject3d(A, B)
```

Project A onto B, result starts at origin

### Projection with point3d start

```js
vecproject3d(A, B, point3d(G, 1, 1, 1))
```

Project A onto B, result starts at point (1,1,1)

### Projection with coordinate start

```js
vecproject3d(A, B, 2, 3, 4)
```

Project A onto B, result starts at (2,3,4)

## Examples

### Project a vector onto the x-axis to extract the x-component

```js
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 3, 2, 1)
B = vector3d(G, 0, 0, 0, 1, 0, 0)
P = vecproject3d(A, B)
```

### Project one arbitrary vector onto another

```js
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 4, 3, 2, c(red))
B = vector3d(G, 0, 0, 0, 1, 1, 0, c(blue))
P = vecproject3d(A, B, c(green))
```

### Projection placed at a specific start point

```js
G = g3d(at(0, 0), 30, 30)
A = vector3d(G, 0, 0, 0, 5, 3, 1)
B = vector3d(G, 0, 0, 0, 0, 0, 1)
pt = point3d(G, 2, 2, 0)
P = vecproject3d(A, B, pt)
```
