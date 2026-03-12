---
title: rect
sidebar_label: rect
---

# rect

Create a rectangle from a top-left corner point, width, and height. Automatically generates four vertices and four edges accessible by index.

**Utility:** Create rectangle from top-left corner, width, and height

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `topLeft` | `point \| x, y` | Yes | Top-left corner (point variable or x,y coordinates) |
| `width` | `number` | Yes | Width of rectangle (extends right from topLeft) |
| `height` | `number` | Yes | Height of rectangle (extends down from topLeft) |

## Variants

### From point variable

```
rect(G, P, width, height)
```

Rectangle with corner at point variable P

### From coordinates

```
rect(G, x, y, width, height)
```

Rectangle with corner at coordinates

### From inline point

```
rect(G, point(G, 1, 5), 4, 3)
```

Rectangle with inline point definition

### With styling

```
rect(G, P, 4, 3, c(blue), f(lightblue))
```

Colored rectangle with stroke and fill

## Examples

### Basic rectangle at origin

```
rect_1 = rect(graph_1, point(graph_1, 0, 4), 4, 3)
```

### Rectangle with coordinates

```
rect_2 = rect(graph_1, 1, 5, 6, 4)
```

### Extract top edge

```
top_edge = line(graph_1, item(rect_1, type(edge), 1), type(segment))
```

### Extract corner vertex

```
corner = point(graph_1, item(rect_1, type(vertex), 1))
```

### Get rectangle diagonal length

```
diag = property(rect_1, type(diagonal))
```
