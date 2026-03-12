---
title: intersect
sidebar_label: intersect
---

# intersect

Computes the intersection point between two geometric objects such as lines, circles, or polygons, with a 1-based index to select among multiple intersections.

**Utility:** Find intersection point between two geometric objects

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `object1` | `line \| circle \| polygon \| plot` | Yes | First geometric object |
| `object2` | `line \| circle \| polygon \| plot` | Yes | Second geometric object |
| `index` | `number (1-based)` | No | Which intersection point to return (1 = first, 2 = second, etc.) |

## Variants

### Two lines

```js
intersect(G, line1, line2)
```

Find where two lines cross

### Line and polygon

```js
intersect(G, line, polygon, 1)
```

First intersection of line with polygon edge

### Circle and line

```js
intersect(G, circle, line, 2)
```

Second intersection of circle with line

### Two circles

```js
intersect(G, circle1, circle2, 1)
```

First intersection of two circles

## Examples

### Find where altitude meets base (perpendicular foot)

```js
foot = intersect(graph_1, line_base, line_altitude)
```

### Draw the intersection point

```js
point_int = point(graph_1, foot, c(red))
```

### Intersection of two triangle edges extended

```js
crossing = intersect(graph_1, line_a, line_b)
```

### Line intersecting polygon (first intersection)

```js
int_1 = intersect(graph_1, diagonal_line, triangle_1, 1)
```

### Line intersecting polygon (second intersection)

```js
int_2 = intersect(graph_1, diagonal_line, triangle_1, 2)
```

### Circle and line intersection

```js
tangent_point = intersect(graph_1, circle_1, line_1, 1)
```
