---
title: point
sidebar_label: point
---

# point

Places a point on a 2D graph at Cartesian coordinates, polar coordinates, or at a parametric ratio on an existing shape. Supports invisible reference points and coordinate extraction.

**Utility:** Place a visible or invisible point at Cartesian, polar, or shape-relative coordinates

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `x` | `number \| shape \| property` | Yes | X coordinate, or shape reference for point-on-shape, or property() for extraction |
| `y` | `number \| ratio` | No | Y coordinate, or parametric ratio (0-1) for point-on-shape |
| `type` | `type(polar) \| type(ratio)` | No | type(polar) for polar coordinates (r, theta), type(ratio) for point on shape at ratio |
| `options` | `c(color) \| nodraw() \| fi("name", size)` | No | Color, visibility, or fill-image modifiers |

## Variants

### Cartesian point

```js
point(G, x, y)
```

Point at (x, y) coordinates

### Polar point

```js
point(G, r, theta, type(polar))
```

Point at polar coordinates (radius, angle in degrees)

### Point on shape at ratio

```js
point(G, shape, t, type(ratio))
```

Point on line/curve at parametric position t (0 to 1)

### Invisible reference point

```js
point(G, x, y, nodraw())
```

Creates a point used for computation but not rendered

### Colored point

```js
point(G, x, y, c(red))
```

Point rendered in specified color

### Start point of line

```js
point(G, property(L, type(start)))
```

Extract start point from a line

### End point of line

```js
point(G, property(L, type(end)))
```

Extract end point from a line

### Center of circle

```js
point(G, property(C, type(center)))
```

Extract center point from a circle

### Midpoint of line

```js
point(G, property(L, type(center)))
```

Extract midpoint of a line segment

### Midpoint between two points

```js
midpoint(G, P1, P2)
```

Point at midpoint between two existing points

### Vertex from polygon/triangle

```js
point(G, item(polygon, type(vertex), n))
```

Extract nth vertex (1-based) from polygon, sss, sas, asa, aas, rect, square

### Point from intersection

```js
intersect(G, obj1, obj2)
```

Point at intersection of two lines, curves, circles, or plots

### Point from projection

```js
project(G, line, point)
```

Foot of perpendicular from point onto line

### Point from reflection

```js
reflect(G, line, point)
```

Mirror of point across a line

### Point from rotation

```js
rotate(G, point, angle)
```

Point rotated by angle degrees about origin (or optional center)

### Point from translation

```js
translate(G, point, dx, dy)
```

Point shifted by (dx, dy) offset

### Point from scaling

```js
scale(G, point, factor)
```

Point scaled by factor about origin (or optional center)

### Point at ratio on segment

```js
pointatratio(G, P1, P2, t)
```

Point at ratio t between P1 and P2 (t=0 gives P1, t=1 gives P2)

### Point at angle from point

```js
pointatangle(G, P, r, angle)
```

Point at distance r and angle degrees from point P

### Extract x coordinate

```js
x(point)
```

Get x-coordinate as numeric value for use in expressions

### Extract y coordinate

```js
y(point)
```

Get y-coordinate as numeric value for use in expressions

### Point on circle at ratio

```js
point(G, circle, t, type(ratio))
```

Point on circle circumference at parametric ratio t (0 to 1)

### Point from function evaluation

```js
point(G, x, fun(f, x))
```

Point on function curve at x, using fun() to evaluate

### Point with notes popup

```js
point(G, x, y, notes("text", c(black), fc(orange)))
```

Point with popup annotation on hover

## Examples

### Create two points for a line segment

```js
A = point(G, -2, 1)
```

### Second point at positive coordinates

```js
B = point(G, 3, 4)
```

### Focus point at origin for parabola lesson

```js
F = point(G, 0, 1)
```

### Multiple labeled points for geometry

```js
point_1 = point(graph_1, -3.1, 1.8)
```

### Invisible base point for triangle

```js
point_1 = point(graph_1, 0, 0, nodraw())
```

### Point on plot curve at parametric ratio

```js
point_5 = point(graph_2, parabola_1, 0.5, type(ratio))
```

### Point on line at midpoint ratio

```js
point_1 = point(G, L, 0.5, type(ratio))
```

### Point in polar coordinates

```js
point_1 = point(G, 3, 45, type(polar))
```

### Colored point on ellipse focus

```js
point_f = point(G, F1, c(red))
```

### Point computed from function value

```js
p = point(G, b, fun(eq, b))
```

### Point with fill image and notes

```js
P = point(G, L, 0.5, type(ratio), fi("tree", 1), notes("description"))
```
