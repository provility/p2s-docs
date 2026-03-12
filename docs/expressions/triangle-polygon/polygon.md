---
title: polygon
sidebar_label: polygon
---

# polygon

Creates a closed polygon from three or more vertex points, automatically connecting consecutive vertices with edges and closing the shape.

**Utility:** Create closed polygon from three or more points

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `points` | `point \| point(G, x, y) \| x, y pairs` | Yes | Three or more points defining polygon vertices (can be point variables, inline points, or x,y coordinate pairs) |

## Variants

### From point variables

```
polygon(G, P1, P2, P3)
```

Polygon using existing point variables

### From inline points

```
polygon(G, point(G, 0, 0), point(G, 3, 0), point(G, 1.5, 2))
```

Polygon with inline point definitions

### From coordinates

```
polygon(G, 0, 0, 3, 0, 1.5, 2)
```

Polygon from x,y coordinate pairs

### With color styling

```
polygon(G, P1, P2, P3, P4, c(blue), f(lightblue))
```

Colored polygon with stroke and fill

### Hidden stroke

```
polygon(G, P1, P2, P3, so(0))
```

Polygon structure without visible outline

## Examples

### Triangle from three existing points

```
triangle_1 = polygon(graph_1, point_A, point_B, point_C)
```

### Quadrilateral with coordinates

```
quad_1 = polygon(graph_1, 0, 0, 4, 0, 4, 3, 0, 3)
```

### Extract edge as line for measurement

```
edge_1 = line(graph_1, item(quad_1, type(edge), 1), type(segment))
```

### Extract vertex for labeling

```
vertex_A = point(graph_1, item(quad_1, type(vertex), 1))
```

### Pentagon with fill color

```
pentagon_1 = polygon(graph_1, P1, P2, P3, P4, P5, c(blue), f(lightblue))
```
