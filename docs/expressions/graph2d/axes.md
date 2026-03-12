---
title: axes
sidebar_label: axes
---

# axes

Bundles x-axis and y-axis ranges with grid visibility options into a single axis configuration for a 2D graph.

**Utility:** Bundle x-range, y-range, and grid options into a single axis configuration for g2d

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `xRange` | `range(min, max)` | Yes | X-axis range expression |
| `yRange` | `range(min, max)` | Yes | Y-axis range expression |
| `gridStyle` | `grid(c(color), s(width))` | No | Optional grid styling with color and stroke width |
| `option` | `"gridlines" \| "nogrid"` | No | 'gridlines' shows grid lines (default hidden). 'nogrid' hides everything including axes. |

## Variants

### Axes only (default, no grid lines)

```js
axes(range(-10, 10), range(-5, 5))
```

Shows axes but no grid lines

### Axes with grid lines

```js
axes(range(-10, 10), range(-5, 5), "gridlines")
```

Shows both axes and grid lines

### No axes or grid (blank background)

```js
axes(range(-10, 10), range(-5, 5), "nogrid")
```

Hides everything - no axes, no grid

### Styled grid lines

```js
axes(range(-10, 10), range(-5, 5), grid(c(gray)), "gridlines")
```

Grid lines with custom color

### Used inside g2d

```js
g2d(at(row, col), height, width, axes(range(-5, 5), range(-5, 5)))
```

Axes as a single argument to g2d

## Examples

### Graph with axes bundled together

```js
G = g2d(at(2, 2), 20, 20, axes(range(-10, 10), range(-5, 5)))
```

### Graph with axes and visible grid lines

```js
G = g2d(at(2, 2), 20, 20, axes(range(-10, 10), range(-5, 5), "gridlines"))
```

### Graph with no axes or grid (bare canvas)

```js
G = g2d(at(2, 2), 20, 20, axes(range(-5, 5), range(-5, 5), "nogrid"))
```

### Graph with styled gray grid lines

```js
G = g2d(at(2, 2), 20, 20, axes(range(-5, 5), range(-5, 5), grid(c(gray)), "gridlines"))
```
