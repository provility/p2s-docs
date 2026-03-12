---
title: pll
sidebar_label: pll
---

# pll

Constructs a parallel line through a given point, preserving the direction of a reference line or vector. Supports an optional custom length.

**Utility:** Create a parallel line or vector through a point relative to a reference line/vector

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container |
| `line_or_vec` | `line \| vector` | Yes | Reference line or vector to be parallel to |
| `point` | `point` | Yes | Point through which the parallel passes |
| `length` | `number` | No | Custom length for the parallel (defaults to reference length) |

## Variants

### Parallel through point (default length)

```
pll(G, L, P)
```

Line through P parallel to L, same length as L

### Parallel with custom length

```
pll(G, L, P, 8)
```

Parallel through P with length 8

### Parallel to a vector

```
pll(G, V, P)
```

Vector through P parallel to vector V

## Examples

### Set up graph and reference line

```
graph_1 = g2d(at(10, 10), 20, 20)
```

### Define a reference line

```
L = line(graph_1, point(graph_1, -4, -2), point(graph_1, 4, 2))
```

### Define a point above the line

```
P = point(graph_1, 0, 3)
```

### Draw parallel through P

```
pll_1 = pll(graph_1, L, P)
```

### Draw parallel with custom length 6

```
pll_2 = pll(graph_1, L, P, 6)
```

### Color the parallel line blue

```
pll_3 = pll(graph_1, L, P, c(blue))
```
