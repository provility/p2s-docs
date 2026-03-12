---
title: reverse
sidebar_label: reverse
---

# reverse

Creates a direction-reversed copy of a vector or line, flipping tip and tail while preserving magnitude, placed at a specified starting point.

**Utility:** Create a direction-reversed copy of a vector placed at a new point

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The graph container |
| `vector` | `vector \| line` | Yes | The vector or line to reverse |
| `point` | `point` | Yes | The new starting point for the reversed vector |

## Variants

### Reverse at a point expression

```
reverse(G, vec, point)
```

Reverse vector direction and place at the given point

### Reverse at coordinates

```
reverse(G, vec, x, y)
```

Reverse vector direction and place at (x, y)

### Reverse a line

```
reverse(G, line, point)
```

Reverse a line direction as a vector at the given point

## Examples

### Reverse a vector at the origin

```
V = vector(G, 1, 1, 4, 3)
R = reverse(G, V, point(G, 0, 0))
```

### Reverse a vector at its own tip (tail-to-tail)

```
V = vector(G, 0, 0, 3, 2)
R = reverse(G, V, point(G, 3, 2))
```

### Reverse a vector at explicit coordinates

```
V = vector(G, 0, 0, 3, 2)
R = reverse(G, V, 5, 5)
```

### Reverse a line as a vector

```
L = line(G, 0, 0, 4, 3)
R = reverse(G, L, point(G, 0, 0))
```
