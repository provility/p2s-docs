---
title: hatch
sidebar_label: hatch
---

# hatch

Fills a polygon interior with a repeating line pattern in diagonal, vertical, or horizontal directions with adjustable spacing.

**Utility:** Create hatched shading pattern inside a polygon

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `polygon` | `polygon \| triangle \| rect \| square` | Yes | Polygon variable to fill with hatch pattern |
| `spacing` | `number` | No | Distance between hatch lines in model units (default 0.5) |
| `direction` | `string: "/" \| "\\" \| "\|" \| "-"` | No | Hatch line direction: / (diagonal), \\ (reverse), | (vertical), - (horizontal) |

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

Closer hatch lines

### Diagonal direction

```
hatch(G, polygon, 0.5, "/")
```

Explicit diagonal direction

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

Blue hatch lines

## Examples

### Hatch a triangle for area visualization

```
hatch_1 = hatch(graph_1, triangle_1)
```

### Dense diagonal hatching

```
hatch_2 = hatch(graph_1, triangle_1, 0.3, "/")
```

### Vertical stripes on rectangle

```
hatch_3 = hatch(graph_1, rect_1, 0.5, "|", c(blue))
```

### Horizontal stripes on square

```
hatch_4 = hatch(graph_1, square_1, 0.4, "-")
```

### Hatch right triangle for area proof

```
hatch_rt = hatch(graph_1, sss_triangle, 0.3, "/", c(red))
```

### Hatch polygon region

```
hatch_poly = hatch(graph_1, polygon_1, 0.5, "/")
```
