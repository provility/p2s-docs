---
title: parabola
sidebar_label: parabola
---

# parabola

Draws a parabola on a 2D graph from a vertex and focal parameter, or from an equation string. Supports optional rotation in radians.

**Utility:** Draw a parabola on a 2D graph by vertex+focal-distance or equation

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container to draw on |
| `vertex` | `point \| two numbers (h, k)` | Yes | Vertex of the parabola - either a point expression or two coordinate values |
| `p` | `number` | Yes | Focal parameter - distance from vertex to focus. Must be non-zero. Sign determines opening direction |
| `rotation` | `number (radians)` | No | Rotation angle in radians. Defaults to 0 |
| `equation` | `string` | No | Alternative to parametric args - equation string e.g. "y = x^2" or "x^2 = 4y" |

## Variants

### Vertex point + focal parameter

```
parabola(G, vertex_point, p)
```

Parabola at vertex with focal distance p

### Vertex coordinates + focal parameter

```
parabola(G, h, k, p)
```

Parabola at (h, k) with focal distance p

### With rotation

```
parabola(G, vertex_point, p, rotation)
```

Rotated parabola, angle in radians

### From equation string

```
parabola(G, "y = x^2 - 4x + 3")
```

Parabola defined by equation

### Standard form equation

```
parabola(G, "x^2 = 4y")
```

Parabola in standard x^2 = 4py form

## Examples

### Parabola from equation x^2 = 4y

```
parabola_1 = parabola(graph_2, "x^2=4y")
```

### Parabola from quadratic equation

```
parabola_1 = parabola(G, "y = x^2 - 4x + 3")
```

### Parabola at vertex with focal distance

```
parabola_1 = parabola(G, point(G, 0, 0), 1)
```

### Extract and draw focus

```
F = point(G, property(parabola_1, type(foci, 1)), c(red))
```

### Extract and draw directrix line

```
D = line(G, property(parabola_1, type(directrix, 1)))
```

### Sample point on parabola at ratio

```
P = point(graph_2, parabola_1, 0.5, type(ratio))
```

### Animate focus-directrix equidistance trace

```
trace_1 = trace(G, parabola_1, type(focus), buff(-1, -1))
```

### Animate parallel ray reflection through focus

```
trace_1 = trace(G, parabola_1, type(rays), buff(-1, -1))
```
