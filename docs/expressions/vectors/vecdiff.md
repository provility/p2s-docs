---
title: vecdiff
sidebar_label: vecdiff
---

# vecdiff

Subtracts one vector from another (A minus B) to produce a difference vector, optionally placed at a specified starting point.

**Utility:** Subtract two vectors to produce a difference vector (A - B)

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `vectorA` | `vector \| line` | Yes | Vector to subtract from (minuend) |
| `vectorB` | `vector \| line` | Yes | Vector to subtract (subtrahend) |
| `startPoint` | `point` | No | Optional point where the result vector starts |

## Variants

### Basic difference at origin

```js
vecdiff(G, vecA, vecB)
```

Subtract vectors (A - B), result starts at origin

### Difference placed at a point

```js
vecdiff(G, vecA, vecB, point)
```

Subtract vectors, result starts at the given point

## Examples

### Create graph and two vectors

```js
G = g2d(at(8, 0), 20, 20)
```

### First vector

```js
V1 = vector(G, 0, 0, 5, 3)
```

### Second vector

```js
V2 = vector(G, 0, 0, 2, 1)
```

### Difference V1 - V2 at origin

```js
diff_1 = vecdiff(G, V1, V2)
```

### Difference placed at a point

```js
diff_2 = vecdiff(G, V1, V2, point(G, -3, 0))
```

### Styled difference vector in orange

```js
diff_3 = vecdiff(G, V1, V2, c(orange))
```
