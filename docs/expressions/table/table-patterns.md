---
title: table-patterns
sidebar_label: table-patterns
---

# table-patterns

Common patterns for connecting data tables to graphs, including plotting columns as curves or scatter points, extracting cell values, and annotating specific cells.

**Utility:** Common usage patterns for table creation and interaction

## Variants

### Plot table data as curve

```js
T = table(at(r, c), "x", "x^2", range(0, 5))
G = g2d(at(r2, c2), w, h, range(xmin, xmax), range(ymin, ymax))
plottable(G, T, 2)
```

Create table, then plot column 2 (y) against column 1 (x) on a graph

### Plot table data as discrete points

```js
plottable(G, T, 2, type(points))
```

Plot table data as scatter points instead of a connected curve

### Extract cell value as a point

```js
T = table(at(r, c), "x", "x^2", range(0, 5))
P = point(G, item(T, 2, 1), item(T, 2, 2))
```

Use item() to get cell values and create a point from table data

### Arrow from table cell to shape

```js
T = table(at(2, 30), "x", "y = x", range(1, 3))
arrow(at(T, 1, 2), P, "f(x)")
```

Draw an arrow from a specific table cell to a point or shape

### Select table cell for annotation

```js
sel = selectcell(T, 1, 2)
arrow(at(sel), target)
```

Select a specific cell then use it as arrow source

### Select entire table row

```js
sel = selectcell(T, 3)
```

Select an entire row for highlighting or annotation

### Limit exploration with two-sided approach

```js
eq = def(x, "x^2")
slopeeq = def(x, "(x^2-1)/(x-1)")
t1 = table(at(1, 7), "x", eq, slopeeq, range(2, 1.5, 1.1, 1.01, 1.001), c(blue))
t2 = table(at(15, 7), "x", eq, slopeeq, range(0, 0.5, 0.9, 0.99, 0.999), c(green))
```

Two tables showing values approaching x=1 from right (blue) and left (green)

### Table with function definitions as columns

```js
eq = def(x, "x^2")
T = table(at(r, c), "x", eq, range(0, 5))
```

Use def() variables as table columns instead of raw formula strings

### Multi-column table plotted on separate graphs

```js
T = table(at(6, 2), "x", "x^2", "2*x", range(0, 5, 1))
G1 = g2d(at(1, 14), 12, 18, range(-1, 5, 1), range(-1, 15, 2))
plottable(G1, T, 2, c(blue))
G2 = g2d(at(15, 14), 12, 18, range(-1, 5, 1), range(-2, 12, 2))
plottable(G2, T, 3, c(red))
```

One table with f(x) and f'(x), each plotted on its own graph

## Examples

### Limit exploration: table + graph with trace

```js
table_1 = table(at(4, 26), "x", "(x-1)/(x^2-1)", range(0, 0.2, 0.5, 0.7, 0.8, 0.9, 0.99, 0.999, 1, 1.1, 1.2, 2), f(16))
graph_1 = g2d(at(4.2, 37), 16.6, 16.1, range(-1, 2, 0.5), range(-1, 2, 0.5), grid())
plot_1 = plottable(graph_1, table_1, 2)
limit_1 = trace(graph_1, plot_1, type(limit), 1, buff(-1.6, -30))
```

### Derivative table with dual graph comparison

```js
T = table(at(6, 2), "x", "x^2", "2*x", range(0, 5, 1))
G1 = g2d(at(1, 14), 12, 18, range(-1, 5, 1), range(-1, 15, 2))
plottable(G1, T, 2, c(blue))
G2 = g2d(at(15, 14), 12, 18, range(-1, 5, 1), range(-2, 12, 2))
plottable(G2, T, 3, c(red))
```

### Secant line convergence with table and animation

```js
eq = def(x, "x^2")
slopeeq = def(x, "(x^2-1)/(x-1)")
G = g2d(at(2, 3), 30, 30, range(-2, 3), range(-1, 5))
pl1 = plot(G, eq)
t = table(at(5, 27), "x", eq, slopeeq, range(2, 1.5, 1.1, 1.01, 1.001), type(1))
b = 0.8
q_1 = 2
tangent(G, pl1, b, c(blue))
p = point(G, b, fun(eq, b))
q = point(G, q_1, fun(eq, q_1))
line(G, p, q, c(red))
change(q_1, 0.8, t(5))
```

### Table with arrow annotations pointing to graph elements

```js
G = g2d(at(5, 10), 16, 8, -5, 5, -5, 5)
P = point(G, 2, 3)
T = table(at(2, 30), "x", "y = x", range(1, 3))
arrow(at(T, 1, 2), P, "f(x)")
```
