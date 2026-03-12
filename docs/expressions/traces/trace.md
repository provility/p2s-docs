---
title: trace
sidebar_label: trace
---

# trace

Annotates a geometric shape on a graph with its mathematical properties, such as equation forms, conic parameters, vector components, or calculus theorem visualizations.

**Utility:** Display mathematical property annotations and equations for shapes on a graph

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `variable` | Yes | Reference to the graph container (g2d or p2d) |
| `shape` | `variable` | Yes | Reference to the shape to annotate (line, circle, vector, plot, etc.) |
| `traceType` | `type(typeName)` | Yes | The trace type - determines what property or equation is displayed |
| `extraShape` | `variable` | No | Second shape reference for types that compare two objects (e.g., angle between vectors) |
| `targetValue` | `number` | No | Numeric parameter for certain trace types (e.g., limit point for type(limit)) |
| `buff` | `buff(col, row)` | No | Offset the label position in logical units |

## Variants

### Line slope-intercept trace

```js
trace(G, L, type(slopeintercept))
```

Show y = mx + b equation for a line

### Line standard form trace

```js
trace(G, L, type(standard))
```

Show ax + by = c equation for a line

### Line two-point form

```js
trace(G, L, type(twopoint))
```

Show equation through two given points

### Line point-slope form

```js
trace(G, L, type(pointslope))
```

Show y - y1 = m(x - x1) form

### Circle center-radius trace

```js
trace(G, C, type(centerradius))
```

Show (x-h)^2 + (y-k)^2 = r^2 equation

### Circle trig trace with arc sweep

```js
trace(G, C, type(sin), buff(-2, 0))
```

Trace sine values around circle - adjustable from/to angles

### Vector angle between two vectors

```js
trace(G, V1, type(angle), V2, buff(-6, 0))
```

Show angle measurement between two vectors

### Vector components decomposition

```js
trace(G, V, type(components))
```

Show x and y component breakdown of a vector

### Parabola focus trace

```js
trace(G, parabola, type(focus), buff(-1, -1))
```

Show focus point and properties of a parabola

### Plot limit trace

```js
trace(G, plot, type(limit), value, buff(-1.6, -30))
```

Show limit analysis at a specific x-value

### Dynamic trace type via variable

```js
trace(G, L, type(traceTypeVar))
```

Use a string variable to dynamically control trace type

## Examples

### Line with dynamic trace type controlled by input dropdown

```js
G = g2d(at(2, 2), 30, 30)
A = point(G, -2, 1)
B = point(G, 3, 4)
L = line(G, A, B)
plot_trace_type = "slopeintercept"
input_trace = input(at(2, 30), plot_trace_type, pd(10), value("slopeintercept", "standard", "pointslope", "slope", "intercept"))
trace(G, L, type(plot_trace_type))
```

### Angle between two vectors

```js
G = g2d(at(8, 0), 20, 20)
V1 = vector(G, 0, -2, 3, 4)
V2 = vector(G, -2, -2, 5, -4)
trace(G, V1, type(angle), V2, buff(-6, 0))
```

### Parabola focus property trace

```js
graph_2 = g2d(at(4.6, 16.6), 14.5, 24, range(-5, 5), range(-5, 5))
parabola_1 = parabola(graph_2, "x^2=4y")
trace_1 = trace(graph_2, parabola_1, type(focus), buff(-1, -1))
```

### Limit exploration with plottable table data

```js
table_1 = table(at(4, 26), "x", "(x-1)/(x^2-1)", range(0, 0.2, 0.5, 0.7, 0.8, 0.9, 0.99, 0.999, 1, 1.1, 1.2, 2), f(16))
graph_1 = g2d(at(4.2, 37), 16.6, 16.1, range(-1, 2, 0.5), range(-1, 2, 0.5), grid())
plot_1 = plottable(graph_1, table_1, 2)
limit_1 = trace(graph_1, plot_1, type(limit), 1, buff(-1.6, -30))
```

### Vector angle trace between two vectors

```js
G = g2d(at(8, 0), 20, 20)
V2 = vector(G, 0, -2, 3, 4)
V2 = vector(G, -2, -2, 5, -4)
trace(G, V2, type(angle), V2)
```
