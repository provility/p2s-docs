---
title: property
sidebar_label: property
---

# property

Extract geometric properties from shapes such as centroid, circumcenter, incenter, orthocenter, circumradius, and inradius. Returns point coordinates or numeric values depending on the requested property.

**Utility:** Extract geometric properties (points, values) from shapes

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `shape` | `triangle \| polygon \| rect \| square \| circle \| line` | Yes | Shape variable to extract property from |
| `propertyName` | `type(property_name)` | Yes | Property to extract using type() expression |
| `param` | `number` | No | Optional parameter for indexed properties like corner(i) |

## Variants

### Triangle centroid

```
property(triangle, type(centroid))
```

Get triangle centroid point

### Triangle incenter

```
property(triangle, type(incenter))
```

Get inscribed circle center

### Triangle circumcenter

```
property(triangle, type(circumcenter))
```

Get circumscribed circle center

### Triangle orthocenter

```
property(triangle, type(orthocenter))
```

Get altitudes intersection point

### Triangle inradius

```
property(triangle, type(in_radius))
```

Get inscribed circle radius

### Triangle circumradius

```
property(triangle, type(circum_radius))
```

Get circumscribed circle radius

### Triangle area

```
property(triangle, type(area))
```

Get triangle area

### Polygon perimeter

```
property(polygon, type(perimeter))
```

Get polygon perimeter

### Polygon corner

```
property(polygon, type(corner), 1)
```

Get first corner point

### Rectangle diagonal

```
property(rect, type(diagonal))
```

Get rectangle diagonal length

## Examples

### Get and draw triangle centroid

```
centroid_point = point(graph_1, property(triangle_1, type(centroid)), c(red))
```

### Get and draw triangle incenter

```
incenter_point = point(graph_1, property(triangle_1, type(incenter)), c(blue))
```

### Get and draw circumcenter

```
circumcenter_point = point(graph_1, property(triangle_1, type(circumcenter)), c(green))
```

### Get and draw orthocenter

```
orthocenter_point = point(graph_1, property(triangle_1, type(orthocenter)), c(purple))
```

### Get inradius for inscribed circle

```
r_in = property(triangle_1, type(in_radius))
```

### Draw inscribed circle

```
inscribed = circle(graph_1, property(triangle_1, type(incenter)), r_in)
```

### Get circumradius for circumscribed circle

```
r_circ = property(triangle_1, type(circum_radius))
```

### Get rectangle diagonal length

```
diag_len = property(rect_1, type(diagonal))
```

### Get polygon perimeter

```
perim = property(polygon_1, type(perimeter))
```
