---
title: hatch
sidebar_label: hatch
---

# hatch

Fill a polygon region with parallel line shading in diagonal, vertical, or horizontal patterns. Supports adjustable line spacing, direction, and color for visualizing areas, feasible regions, or distinguishing overlapping geometric regions.

**Utility:** Create hatched shading pattern inside a polygon region

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `polygon` | `polygon \| triangle \| rect \| square` | Yes | Polygon variable to fill with hatch pattern |
| `spacing` | `number` | No | Distance between hatch lines in model units (default: 0.5) |
| `direction` | `string: "/" \| "\\" \| "\|" \| "-"` | No | Hatch line direction: / (diagonal), \\ (reverse diagonal), | (vertical), - (horizontal) |
| `color` | `c(colorName)` | No | Color for hatch lines - e.g., c(blue), c(red) |

## Variants

### Default diagonal hatch

```
hatch(G, polygon)
```

Diagonal hatching with default spacing

### Custom spacing

```
hatch(G, polygon, 0.3)
```

Denser hatch lines

### Explicit direction

```
hatch(G, polygon, 0.5, "/")
```

Diagonal direction with spacing

### Vertical stripes

```
hatch(G, polygon, 0.5, "|")
```

Vertical hatch lines

### Horizontal stripes

```
hatch(G, polygon, 0.5, "-")
```

Horizontal hatch lines

### Colored hatch

```
hatch(G, polygon, 0.3, "/", c(blue))
```

Blue diagonal hatch lines

## Examples

### Hatch feasible region in linear programming (from linear-programming lesson)

```
G = g2d(at(2, 2), 20, 30, range(-1, 10))
L1 = line(G, point(G, 0, 0), point(G, 5, 0))
L2 = line(G, point(G, 0, 0), point(G, 0, 4))
L3 = line(G, point(G, 0, 3), point(G, 4, 0))
A = intersect(G, L1, L3)
B = intersect(G, L2, L3)
P = polygon(G, point(G, 0, 0), A, B, fo(0.1))
hatch(G, P, 0.3, "/", c(blue))
```

### Default diagonal hatching on triangle

```
hatch_1 = hatch(graph_1, triangle_1)
```

### Dense diagonal hatching

```
hatch_2 = hatch(graph_1, triangle_1, 0.3, "/")
```

### Vertical blue stripes on rectangle

```
hatch_3 = hatch(graph_1, rect_1, 0.5, "|", c(blue))
```

### Horizontal stripes on square

```
hatch_4 = hatch(graph_1, square_1, 0.4, "-")
```

### Red hatching for area proof

```
hatch_rt = hatch(graph_1, sss_triangle, 0.3, "/", c(red))
```
