---
title: vecsum
sidebar_label: vecsum
---

# vecsum

Adds two vectors to produce a resultant sum vector, optionally placed at a specified starting point.

**Utility:** Add two vectors to produce a resultant sum vector

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `vectorA` | `vector \| line` | Yes | First vector to add |
| `vectorB` | `vector \| line` | Yes | Second vector to add |
| `startPoint` | `point` | No | Optional point where the result vector starts |

## Variants

### Basic sum at origin

```
vecsum(G, vecA, vecB)
```

Add vectors, result starts at origin

### Sum placed at a point

```
vecsum(G, vecA, vecB, point)
```

Add vectors, result starts at the given point

## Examples

### Create graph and two vectors

```
G = g2d(at(8, 0), 20, 20)
```

### First vector

```
V1 = vector(G, 0, 0, 3, 4)
```

### Second vector

```
V2 = vector(G, 0, 0, 2, -1)
```

### Sum of V1 and V2 at origin

```
sum_1 = vecsum(G, V1, V2)
```

### Sum placed at a specific point

```
sum_2 = vecsum(G, V1, V2, point(G, 1, 1))
```

### Styled sum vector in green

```
sum_3 = vecsum(G, V1, V2, c(green))
```
