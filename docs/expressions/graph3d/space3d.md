---
title: space3d
sidebar_label: space3d
---

# space3d

Creates a bare 3D space container with no axes, grid, or coordinate overlays, using a native Y-up system for raw 3D object manipulation.

**Utility:** Create a bare 3D space with no axes or grid overlays

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `row` | `number` | Yes | Starting row position on the canvas |
| `col` | `number` | Yes | Starting column position on the canvas |
| `rowHeight` | `number` | Yes | Height of the container in logical row units (must be &gt; 0) |
| `colWidth` | `number` | Yes | Width of the container in logical column units (must be &gt; 0) |

## Variants

### Via g3d with type(space)

```js
g3d(at(row, col), height, width, type(space))
```

Preferred way to create a space3d container through the g3d API

### Direct s3d call

```js
s3d(row, col, rowHeight, colWidth)
```

Direct creation of Space3D container (low-level)

## Examples

### Space for box-fold animation with polygon groups

```js
S = g3d(at(0, 0), 30, 30, type(space))
```

### Space with polygon face and group transform

```js
S = g3d(at(0, 0), 30, 30, type(space))
p1 = polygon3d(S, c(red), point3d(S, 0, 0, 0), point3d(S, 1, 0, 0), point3d(S, 1, 1, 0), point3d(S, 0, 1, 0))
g = group(S)
attach(S, g, p1)
translate3d(S, g, 1, 0, 0)
rotate3d(S, g, 90, 0, 1, 0)
```

### Full-screen space for solid geometry

```js
S = g3d(at(5, 5), 20, 20, type(space))
```
