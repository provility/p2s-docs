---
title: g2d
sidebar_label: g2d
---

# g2d

Creates a 2D Cartesian graph container with configurable position, size, axis ranges, and coordinate modes including uniform-scale, trigonometric, and complex plane.

**Utility:** Create a 2D graph container with position, size, range, axes, grid, and type configuration

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col)` | Yes | Logical position using at(row, col) coordinates on the canvas grid |
| `height` | `number (1-50)` | Yes | Height in logical row units (e.g., 20, 30) |
| `width` | `number (1-50)` | Yes | Width in logical column units (e.g., 20, 30) |
| `xRange` | `range(min, max) \| range(min, max, step) \| range(min, max, step, "trig")` | No | X-axis range. Defaults to -10 to 10 if omitted. step controls tick spacing (auto if omitted). Add "trig" for pi-based labels. |
| `yRange` | `range(min, max) \| range(min, max, step) \| range(min, max, step, "trig")` | No | Y-axis range. Defaults to -10 to 10 if omitted. step controls tick spacing. Add "trig" for pi-based labels on y-axis (inverse trig). |
| `graphType` | `type(uniform)` | No | Set equal scale on both axes. When uniform, only one range needed. |
| `grid` | `grid() \| grid(noaxes) \| grid("Re", "Im")` | No | grid() shows grid lines with axes. grid(noaxes) shows grid without axis lines. grid("Re", "Im") labels axes for complex plane. |
| `border` | `br(radius)` | No | Add border shadow with given radius, e.g., br(0.5) |

## Variants

### Minimal graph (position + size only)

```
g2d(at(row, col), height, width)
```

Creates graph with default -10 to 10 range on both axes

### Graph with both ranges

```
g2d(at(row, col), height, width, range(xMin, xMax), range(yMin, yMax))
```

Explicit x and y axis ranges

### Graph with ranges and step sizes

```
g2d(at(row, col), height, width, range(xMin, xMax, xStep), range(yMin, yMax, yStep))
```

Ranges with custom tick/gridline step sizes for precise control

### Uniform scale graph

```
g2d(at(row, col), height, width, range(min, max, step), type(uniform))
```

Equal scale on both axes - one range controls both. Step optional.

### Graph with grid lines

```
g2d(at(row, col), height, width, range(xMin, xMax), range(yMin, yMax), grid())
```

Shows grid lines with axes visible

### Graph with grid but no axes

```
g2d(at(row, col), height, width, range(xMin, xMax, step), range(yMin, yMax, step), grid(noaxes))
```

Shows grid lines without axis lines

### Trig graph (pi-based x axis)

```
g2d(at(row, col), height, width, range(-2*pi, 2*pi, pi/4, "trig"), range(-2, 2))
```

X-axis uses pi-based labels. Pi step options: pi/6, pi/4, pi/3, pi/2, pi

### Inverse trig graph (pi-based y axis)

```
g2d(at(row, col), height, width, range(-1, 1), range(-pi, pi, pi/4, "trig"))
```

Y-axis uses pi-based labels for arcsin, arccos, arctan

### Complex plane

```
g2d(at(row, col), height, width, range(-5, 5), range(-5, 5), type(uniform), grid("Re", "Im"))
```

Complex plane with Re/Im axis labels, uniform scale, always has grid

### Graph with border shadow

```
g2d(at(row, col), height, width, range(xMin, xMax), range(yMin, yMax), br(0.5))
```

Adds a border shadow effect

### Graph with grid + shadow

```
g2d(at(row, col), height, width, range(xMin, xMax), range(yMin, yMax), grid(), br(0.5))
```

Full-featured graph with grid lines and border shadow

## Examples

### Simple graph for plotting

```
G = g2d(at(2, 3), 30, 30)
```

### Graph with explicit ranges

```
G = g2d(at(2, 2), 20, 20, range(-5, 5), range(-5, 5))
```

### Graph with step sizes on both axes

```
G = g2d(at(2, 3), 30, 30, range(-2, 2, 0.5), range(-2, 2, 1))
```

### Graph with grid lines and no axes

```
graph_1 = g2d(at(5, 26), 13.3, 20.6, range(-1, 5, 1), range(-1, 5, 1), grid(noaxes))
```

### Graph with grid lines visible

```
graph_1 = g2d(at(4.2, 37), 16.6, 16.1, range(-1, 2, 0.5), range(-1, 2, 0.5), grid())
```

### Uniform scale graph with step

```
graph_1 = g2d(at(5.2, 21.2), 25, 25, range(-1, 4, 1), type(uniform))
```

### Trig graph for sine/cosine

```
G = g2d(at(2, 2), 20, 30, range(-2*pi, 2*pi, pi/4, "trig"), range(-2, 2))
```

### Inverse trig graph for arcsin

```
G = g2d(at(2, 2), 20, 30, range(-1, 1), range(-pi, pi, pi/4, "trig"))
```

### Complex plane with grid

```
G = g2d(at(2, 2), 20, 20, range(-5, 5), range(-5, 5), type(uniform), grid("Re", "Im"))
```

### Multiple small graphs in a grid layout

```
G1 = g2d(at(2, 2), 14, 14)
G2 = g2d(at(2, 18), 14, 14)
```

### Two graphs with different y ranges for function and derivative

```
G1 = g2d(at(1, 14), 12, 18, range(-1, 5, 1), range(-1, 15, 2))
G2 = g2d(at(15, 14), 12, 18, range(-1, 5, 1), range(-2, 12, 2))
```

### Graph with border shadow

```
G = g2d(at(2, 2), 20, 20, range(-5, 5), range(-5, 5), br(0.5))
```
