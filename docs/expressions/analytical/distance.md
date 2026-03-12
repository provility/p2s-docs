---
title: distance
sidebar_label: distance
---

# distance

Computes the Euclidean distance between two points, the length of a segment, or the magnitude of a 2D component pair. Returns a scalar numeric value.

**Utility:** Calculate distance between points or length of a line/vector

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `source` | `line \| vector \| arc` | No | Single shape to measure length of (mode 1) |
| `p1` | `point \| number` | No | First point or x-component (modes 2 and 3) |
| `p2` | `point \| number` | No | Second point or y-component (modes 2 and 3) |

## Variants

### Length of a line/vector

```js
distance(L)
```

Returns the length of line or vector L

### Distance between two points

```js
distance(A, B)
```

Euclidean distance between points A and B

### Vector magnitude

```js
distance(3, 4)
```

Magnitude of vector (3,4) = 5

## Examples

### Set up graph and create a line

```js
graph_1 = g2d(at(10, 10), 20, 20)
```

### Create a line with known length (3-4-5 triangle)

```js
L = line(graph_1, 0, 0, 3, 4)
```

### Get length of the line (returns 5)

```js
d1 = distance(L)
```

### Create two points

```js
A = point(graph_1, 1, 1)
```

### Second point

```js
B = point(graph_1, 4, 5)
```

### Distance between two points

```js
d2 = distance(A, B)
```

### Vector magnitude (returns 5)

```js
d3 = distance(3, 4)
```
