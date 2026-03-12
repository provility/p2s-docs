---
title: norm
sidebar_label: norm
---

# norm

Computes the unit vector of a given vector, line, or pair of points, returning a direction with magnitude 1.

**Utility:** Calculate the normalized direction (unit vector) of a line or vector

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source` | `line \| vector` | Yes | Line or vector to normalize (single argument form) |
| `point1` | `point \| number` | No | First point or x-component (two argument form) |
| `point2` | `point \| number` | No | Second point or y-component (two argument form) |

## Variants

### From line or vector

```js
norm(line)
```

Normalized direction of a line or vector

### From two points

```js
norm(P1, P2)
```

Normalized direction from point P1 to point P2

### From coordinates

```js
norm(x, y)
```

Normalized direction of the vector (x, y)

## Examples

### Create graph and a vector

```js
G = g2d(at(8, 0), 20, 20)
```

### A 3-4-5 vector

```js
V1 = vector(G, 0, 0, 3, 4)
```

### Normalize the vector (returns direction 0.6, 0.8)

```js
n1 = norm(V1)
```

### Normalize direction between two points

```js
n2 = norm(point(G, 1, 1), point(G, 4, 5))
```

### Normalize from raw coordinates

```js
n3 = norm(3, 4)
```
