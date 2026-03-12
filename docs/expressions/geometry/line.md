---
title: line
sidebar_label: line
---

# line

Creates a line on a 2D graph as an infinite line, finite segment, or ray between two points or coordinates. Supports polar form, dashed styling, and property extraction for slope, angle, and endpoints.

**Utility:** Draw a line, segment, or ray between two points or through coordinates

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `P1 or x1` | `point \| number` | Yes | First point variable, or x-coordinate of first point |
| `P2 or y1` | `point \| number` | Yes | Second point variable, or y-coordinate of first point |
| `x2` | `number` | No | X-coordinate of second point (when using raw coordinates) |
| `y2` | `number` | No | Y-coordinate of second point (when using raw coordinates) |
| `lineType` | `type(line) \| type(segment) \| type(ray) \| type(polar)` | No | Line type: line (infinite, default), segment (finite), ray (half-infinite), polar (length + angle) |
| `options` | `c(color) \| dash() \| stroke(width)` | No | Color, dashed style, or stroke width |

## Variants

### Infinite line through two points

```
line(G, P1, P2)
```

Line extending infinitely through both points

### Line segment between two points

```
line(G, P1, P2, type(segment))
```

Finite segment from P1 to P2

### Ray from first through second point

```
line(G, P1, P2, type(ray))
```

Half-line starting at P1, passing through P2

### Line from raw coordinates

```
line(G, x1, y1, x2, y2)
```

Line from (x1,y1) to (x2,y2) using coordinate values

### Polar line

```
line(G, length, angle, type(polar))
```

Line through origin at given angle with given length

### Colored line

```
line(G, P1, P2, c(red))
```

Line rendered in specified color

### Dashed line

```
line(G, P1, P2, type(segment), dash())
```

Dashed line segment between points

### Line from edge data

```
line(G, item(polygon, type(edge), index), type(segment))
```

Line segment created from polygon edge extraction

### Vertical line through point

```
vline(G, point)
```

Vertical line passing through a point (or vline(G, x) for x-coordinate)

### Horizontal line through point

```
hline(G, point)
```

Horizontal line passing through a point (or hline(G, y) for y-coordinate)

### Perpendicular line

```
perp(G, line, point)
```

Line perpendicular to existing line through given point

### Parallel line

```
pll(G, line, point)
```

Line parallel to existing line through given point

### Reflected line

```
reflect(G, mirror_line, line)
```

Line reflected across another line

### Rotated line

```
rotate(G, line, angle)
```

Line rotated by angle degrees (optional center point)

### Translated line

```
translate(G, line, dx, dy)
```

Line shifted by (dx, dy) offset

### Tangent line to curve

```
tangent(G, plot, x)
```

Tangent line to a curve at x-coordinate

### Line property: start point

```
point(G, property(line, type(start)))
```

Extract start point of a line

### Line property: end point

```
point(G, property(line, type(end)))
```

Extract end point of a line

### Line property: midpoint

```
point(G, property(line, type(center)))
```

Extract midpoint of a line

### Line property: slope

```
property(line, type(slope))
```

Get numeric slope value

### Line property: angle

```
property(line, type(angle))
```

Get angle of line in degrees

### Line property: distance/length

```
measure(G, line)
```

Get length/distance measurement of line segment

### Point on line at ratio

```
point(G, line, t, type(ratio))
```

Point at parametric position t (0=start, 0.5=mid, 1=end)

## Examples

### Infinite line through two point variables

```
L = line(G, A, B)
```

### Line between inline points for linear programming

```
L1 = line(G, point(G, 0, 0), point(G, 5, 0))
```

### Constraint line through two inline points

```
L3 = line(G, point(G, 0, 3), point(G, 4, 0))
```

### Line from raw coordinates

```
L = line(G, -5, 0, 5, 7)
```

### Red secant line between two points in tangent-limit lesson

```
line(G, p, q, c(red))
```

### Line between inline points with color

```
line_2 = line(G, point(G, 2.6, 2.7), point(G, -3.4, 3.2))
```

### Ray from intersection in parabola simulation

```
line(G, -2, y_start, x(H1), y(H1))
```

### Reflected ray to focus point

```
line(G, H1, F)
```

### Colored segment from polygon edge

```
line_a = line(graph_1, item(triangle_1, type(edge), 1), type(segment), c(blue))
```
