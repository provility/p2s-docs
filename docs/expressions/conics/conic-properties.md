---
title: property (conics)
sidebar_label: property (conics)
---

# property (conics)

Extracts geometric properties from a conic section, including foci, vertices, co-vertices, directrices, eccentricity, and latus rectum. Uses 1-based indexing for multi-valued properties.

**Utility:** Extract foci, vertices, directrices, eccentricity, and latus rectum from conic sections

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `conic` | `ellipse \| parabola \| hyperbola` | Yes | Conic section variable to extract property from |
| `propertyType` | `type(foci, n) \| type(vertex, n) \| type(covertex, n) \| type(directrix, n) \| type(eccentricity) \| type(latus_rectum)` | Yes | Property to extract using type() expression with optional 1-based index |

## Variants

### Ellipse focus (point)

```
property(ellipse, type(foci, n))
```

Get nth focus of ellipse (n = 1 or 2)

### Ellipse vertex (point)

```
property(ellipse, type(vertex, n))
```

Get nth vertex of ellipse

### Ellipse co-vertex (point)

```
property(ellipse, type(covertex, n))
```

Get nth co-vertex of ellipse (n = 1 or 2)

### Ellipse directrix (line)

```
property(ellipse, type(directrix, n))
```

Get nth directrix line of ellipse

### Parabola focus (point)

```
property(parabola, type(foci, 1))
```

Get the single focus of parabola

### Parabola vertex (point)

```
property(parabola, type(vertex, 1))
```

Get the vertex of parabola

### Parabola directrix (line)

```
property(parabola, type(directrix, 1))
```

Get the directrix line of parabola

### Hyperbola focus (point)

```
property(hyperbola, type(foci, n))
```

Get nth focus of hyperbola (n = 1 or 2)

### Hyperbola vertex (point)

```
property(hyperbola, type(vertex, n))
```

Get nth vertex of hyperbola

### Hyperbola directrix (line)

```
property(hyperbola, type(directrix, n))
```

Get nth directrix line of hyperbola

### Eccentricity (any conic)

```
property(conic, type(eccentricity))
```

Get eccentricity value (0&lt;e&lt;1 ellipse, e=1 parabola, e&gt;1 hyperbola)

### Latus rectum (any conic)

```
property(conic, type(latus_rectum))
```

Get latus rectum length

## Examples

### Draw both foci of an ellipse in red

```
F1 = point(G, property(E, type(foci, 1)), c(red))
```

### Draw second focus of an ellipse

```
F2 = point(G, property(E, type(foci, 2)), c(red))
```

### Draw first vertex of an ellipse in green

```
V1 = point(G, property(E, type(vertex, 1)), c(green))
```

### Draw co-vertex of an ellipse

```
CV1 = point(G, property(E, type(covertex, 1)), c(blue))
```

### Draw directrix of an ellipse

```
D1 = line(G, property(E, type(directrix, 1)))
```

### Get eccentricity of an ellipse

```
ecc = property(E, type(eccentricity))
```

### Get latus rectum of an ellipse

```
lr = property(E, type(latus_rectum))
```

### Draw focus of a parabola

```
F = point(G, property(parabola_1, type(foci, 1)), c(red))
```

### Draw directrix of a parabola

```
D = line(G, property(parabola_1, type(directrix, 1)))
```

### Draw both foci of a hyperbola

```
F1 = point(G, property(H, type(foci, 1)), c(red))
```

### Get eccentricity of a hyperbola

```
ecc = property(H, type(eccentricity))
```

### Draw directrix of a hyperbola

```
D1 = line(G, property(H, type(directrix, 1)))
```
