---
title: zoom
sidebar_label: zoom
---

# zoom

Zooms the 2D graph viewport in, out, or to fit specific shapes, with animated transitions and configurable scale and duration.

**Utility:** Zoom in, zoom out, or zoom to fit shapes on a g2d graph with animated transitions

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d variable` | Yes | The g2d graph to zoom |
| `target` | `x, y \| point \| object \| x1, y1, x2, y2` | Yes | For zoomin: coordinates, point, object, or bounding box. For zoomfit: one or more shape variables. |
| `scale` | `number` | No | Zoom scale for zoomin (default 0.5 = zoom to 50% of range) |
| `duration` | `number` | No | Animation duration in seconds (default 1 for zoomin, 0.5 for zoomfit) |

## Variants

### Zoom in to coordinates

```
zoomin(graph, x, y)
```

Zoom into a specific point with default scale

### Zoom in with scale

```
zoomin(graph, x, y, scale)
```

Zoom into a point with custom scale factor

### Zoom in with scale and duration

```
zoomin(graph, x, y, scale, duration)
```

Zoom into a point with custom scale and animation duration

### Zoom in to point variable

```
zoomin(graph, pointVar)
```

Zoom into a previously defined point

### Zoom in to object

```
zoomin(graph, objectVar)
```

Zoom into the center of a circle, polygon, or other object

### Zoom in to bounding box

```
zoomin(graph, x1, y1, x2, y2)
```

Zoom to fit a rectangular region defined by two corners

### Zoom out (reset)

```
zoomout(graph)
```

Reset zoom to original view with default 1s duration

### Zoom out with duration

```
zoomout(graph, duration)
```

Reset zoom with custom animation duration

### Zoom fit single shape

```
zoomfit(graph, shape)
```

Zoom to fit a single shape with padding

### Zoom fit multiple shapes

```
zoomfit(graph, shape1, shape2, ...)
```

Zoom to fit all given shapes

### Zoom fit with duration

```
zoomfit(graph, shape1, shape2, duration)
```

Zoom to fit shapes with custom animation duration

## Examples

### Zoom in to a polygon region

```
G = g2d(at(2, 2), 20, 30, range(-1, 10))
P = polygon(G, point(G, 0, 0), point(G, 4, 0), point(G, 0, 3))
zoomin(G, P)
```

### Zoom in to specific coordinates

```
zoomin(G, 3, 4)
```

### Zoom in to a bounding box

```
zoomin(G, 0, 0, 5, 5)
```

### Zoom out to reset view

```
zoomout(G)
```

### Zoom out with fast animation

```
zoomout(G, 0.5)
```

### Zoom to fit two points

```
A = point(G, 1, 1)
B = point(G, 8, 6)
zoomfit(G, A, B)
```

### Zoom to fit a circle

```
C = circle(G, 3, point(G, 5, 5))
zoomfit(G, C)
```
