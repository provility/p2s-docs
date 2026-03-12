---
title: circle
sidebar_label: circle
---

# circle

Creates a circle on a 2D graph using center-and-radius, two-point, diameter, or three-point circumscribed construction. Supports property extraction for center, radius, diameter, circumference, and area.

**Utility:** Draw a circle from center+radius, two points, or three points

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `center or P1 or radius` | `point \| number` | Yes | Center point, first defining point, or radius value (when using radius, cx, cy form) |
| `P2 or radius() or cx` | `point \| radius(r) \| number` | Yes | Through-point, radius modifier, or center-x coordinate |
| `P3 or cy or type` | `point \| number \| type(diameter)` | No | Third point for circumcircle, center-y coordinate, or diameter type |
| `options` | `c(color) \| fo(opacity) \| type(diameter)` | No | Color, fill opacity, or construction type modifier |

## Variants

### Center point + radius

```
circle(G, center, radius(r))
```

Circle with center at point variable and given radius

### Radius + center coordinates

```
circle(G, r, cx, cy)
```

Circle with radius r centered at (cx, cy)

### Center + through point

```
circle(G, P1, P2)
```

Circle centered at P1 passing through P2

### Diameter from two points

```
circle(G, P1, P2, type(diameter))
```

Circle with P1 and P2 as diameter endpoints

### Circumcircle through three points

```
circle(G, P1, P2, P3)
```

Unique circle passing through all three points

### Colored circle

```
circle(G, center, radius(r), c(red))
```

Circle rendered in specified color

### Circle with fill opacity

```
circle(G, r, cx, cy, fo(0.3))
```

Semi-transparent filled circle

## Examples

### Circle at center point with explicit radius

```
circle_1 = circle(graph_1, point(graph_1, 1.4, 1.6), radius(2))
```

### Second circle for intersection test

```
circle_2 = circle(graph_1, point(graph_1, 3.1, 2.8), radius(2))
```

### Red circle for Venn diagram

```
C1 = circle(G, 3, -2, 0, c(red))
```

### Green circle for Venn diagram

```
C2 = circle(G, 3, 2, 0, c(green))
```

### Plain circle at origin for set operations

```
C4 = circle(H, 2, -4, 0)
```

### Circle from point menu with center variable

```
circle_1 = circle(G, point_1, radius(2))
```

### Find intersection of two circles

```
point_1 = intersect(graph_1, circle_1, circle_2)
```

### Venn diagram overlap using boolean and

```
Overlap = and(G, C1, C2, c(yellow))
```

### Trace sine on unit circle

```
trace_1 = trace(G, circle_1, type(sin), 0, 90, buff(-1, -1))
```

### Extract center point from circle

```
center_pt = point(G, property(circle_1, type(center)))
```
