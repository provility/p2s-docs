---
title: point (from vertex)
sidebar_label: point (from vertex)
---

# point (from vertex)

Creates a visible point marker from vertex data extracted from a polygon or triangle. Renders the vertex as a drawable point with optional color and radius styling for marking corners in geometric constructions.

**Utility:** Draw visible point from polygon vertex extraction

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `vertex_data` | `item(polygon, type(vertex), index)` | Yes | Vertex data extracted from polygon using item() |

## Variants

### Point from vertex

```js
point(G, item(triangle, type(vertex), 1))
```

Point at first vertex of triangle

### Colored vertex point

```js
point(G, item(triangle, type(vertex), 1), c(red))
```

Red point at vertex

### Large vertex marker

```js
point(G, item(triangle, type(vertex), 1), c(blue), r(0.15))
```

Larger blue point at vertex

## Examples

### Create triangle and extract vertices

```js
triangle_1 = sas(graph_1, 5, 40, 6, point(graph_1, 0, 0))
```

### Draw point at vertex A (first vertex)

```js
point_A = point(graph_1, item(triangle_1, type(vertex), 1), c(red))
```

### Draw point at vertex B (second vertex)

```js
point_B = point(graph_1, item(triangle_1, type(vertex), 2), c(red))
```

### Draw point at vertex C (third vertex)

```js
point_C = point(graph_1, item(triangle_1, type(vertex), 3), c(red))
```

### Extract vertex for projection

```js
point_c = item(triangle_1, type(vertex), 3)
```

### Project vertex onto opposite edge

```js
point_projected_d = project(graph_1, line_c, point_c, s(0), fo(0), t(0))
```

### Label the vertex point

```js
label_A = label(graph_1, at(point_A), "A", buff(0.5, 0.5))
```

### Use vertex in polygon construction

```js
polygon_1 = polygon(graph_1, point_A, point_c, point_projected_d, s(0))
```
