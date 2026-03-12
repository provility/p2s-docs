---
title: pos
sidebar_label: pos
---

# pos

Apply a relative row and column shift to one or more containers, moving them from their current position by the specified delta amounts.

**Utility:** Shift containers by delta row/col offset from current position

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `containers` | `variable references (g2d \| g3d \| mathtext)` | Yes | One or more container variables to reposition |
| `dRow` | `number` | Yes | Vertical shift in logical units (positive = down, negative = up) |
| `dCol` | `number` | Yes | Horizontal shift in logical units (positive = right, negative = left) |

## Variants

### Shift single container

```
pos(G, dRow, dCol)
```

Move one container by dRow, dCol

### Shift two containers together

```
pos(G, T, dRow, dCol)
```

Move two containers by the same offset

### Shift three containers together

```
pos(G, T, M, dRow, dCol)
```

Move three containers by the same offset

## Examples

### Shift a graph down by 2 rows and right by 3 cols

```
pos(G, 2, 3)
```

### Move a graph and text block together

```
G = g2d(at(2, 3), 14, 14)
T = write(at(18, 3), "f(x) = x^2", type(write))
pos(G, T, 5, 0)
```

### Shift graph left without vertical change

```
pos(G, 0, -5)
```

### Move three containers in unison

```
pos(G, T, M, 3, 2)
```
