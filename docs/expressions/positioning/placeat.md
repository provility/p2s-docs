---
title: placeat
sidebar_label: placeat
---

# placeat

Duplicate a vector or line segment at a new starting point, preserving its original direction and magnitude.

**Utility:** Copy vector/line to new starting point preserving direction and magnitude

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container |
| `source` | `vector \| line` | Yes | Vector or line to copy |
| `point` | `point \| (x, y)` | Yes | New starting point - either a point expression or x, y coordinates |

## Variants

### Copy vector to a point

```js
placeat(G, vec, point(G, x, y))
```

Copy vector to start at a point expression

### Copy vector to coordinates

```js
placeat(G, vec, x, y)
```

Copy vector to start at (x, y) coordinates

### Copy line as vector

```js
placeat(G, line, point)
```

Copy line segment as vector to new start point

## Examples

### Copy vector to a new starting point

```js
V = vector(G, 0, 0, 3, 2)
V2 = placeat(G, V, point(G, 1, 1))
```

### Copy vector using coordinates

```js
V = vector(G, 0, 0, 3, 2)
V2 = placeat(G, V, 2, 3)
```

### Build a parallelogram with vector placement

```js
A = point(G, 0, 0)
B = point(G, 4, 0)
V1 = vector(G, 0, 0, 4, 0)
V2 = vector(G, 0, 0, 1, 3)
V3 = placeat(G, V1, point(G, 1, 3))
V4 = placeat(G, V2, point(G, 4, 0))
```

### Copy line segment as vector to new position

```js
L = line(G, 0, 0, 3, 4)
V = placeat(G, L, point(G, 5, 0))
```
