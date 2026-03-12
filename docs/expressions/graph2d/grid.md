---
title: grid
sidebar_label: grid
---

# grid

Configures grid line visibility, color, and stroke width on a 2D graph, with options to hide axes or set custom axis labels.

**Utility:** Show grid lines on a g2d graph with optional color, stroke, and axis visibility control

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `color` | `c(colorName)` | No | Grid line color, e.g., c(gray), c(lightblue) |
| `strokeWidth` | `s(width)` | No | Grid line stroke width, e.g., s(0.5) |
| `noaxes` | `noaxes` | No | Hide axis lines while keeping grid lines visible |
| `axisLabels` | `"label1", "label2"` | No | Custom axis labels as strings, e.g., "Re", "Im" for complex plane |

## Variants

### Default grid (with axes)

```js
grid()
```

Show grid lines with default styling, axes visible

### Grid without axes

```js
grid(noaxes)
```

Show grid lines but hide axis lines

### Grid with custom axis labels

```js
grid("Re", "Im")
```

Label axes for complex plane (Real, Imaginary)

### Styled grid

```js
grid(c(gray), s(0.5))
```

Grid lines with custom color and stroke width

### Used inside g2d

```js
g2d(at(row, col), height, width, range(-5, 5), range(-5, 5), grid())
```

Enable grid lines on a graph

## Examples

### Graph with default grid lines

```js
G = g2d(at(4.2, 37), 16.6, 16.1, range(-1, 2, 0.5), range(-1, 2, 0.5), grid())
```

### Graph with grid lines but no axes

```js
graph_1 = g2d(at(5, 26), 13.3, 20.6, range(-1, 5, 1), range(-1, 5, 1), grid(noaxes))
```

### Complex plane with Re/Im axis labels

```js
G = g2d(at(2, 2), 20, 20, range(-5, 5), range(-5, 5), type(uniform), grid("Re", "Im"))
```

### Graph with grid on a single range

```js
G2 = g2d(at(0, 30), 20, 20, range(-10, 10), grid())
```
