---
title: pan
sidebar_label: pan
---

# pan

Pans the 2D graph viewport to center on a coordinate, point, or geometric object with an animated transition.

**Utility:** Pan the graph viewport to center on a point or object while maintaining zoom level

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d variable` | Yes | The g2d graph to pan |
| `target` | `x, y \| point \| object` | Yes | Target to center on: x,y coordinates, a point variable, or an object with a center (circle, polygon) |
| `duration` | `number` | No | Animation duration in seconds (default 0.5) |

## Variants

### Pan to coordinates

```
pan(graph, x, y)
```

Pan to center on the given x, y coordinates

### Pan to coordinates with duration

```
pan(graph, x, y, duration)
```

Pan to coordinates with custom animation duration

### Pan to point variable

```
pan(graph, pointVar)
```

Pan to center on a previously defined point

### Pan to object center

```
pan(graph, objectVar)
```

Pan to center on a circle, polygon, or other object

## Examples

### Pan to specific coordinates

```
G = g2d(at(2, 2), 20, 20, range(-10, 10), range(-10, 10))
pan(G, 5, 5)
```

### Pan to a point variable

```
G = g2d(at(2, 2), 20, 20)
P = point(G, 7, 3)
pan(G, P)
```

### Pan with custom duration

```
pan(G, -3, 2, 0.5)
```

### Pan to center on a circle

```
C = circle(G, 3, point(G, 5, 5))
pan(G, C)
```
