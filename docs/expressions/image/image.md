---
title: image
sidebar_label: image
---

# image

Embeds an uploaded image asset on the canvas at logical coordinates or within a 2D graph at graph coordinates, with an optional scale factor controlling display size.

**Utility:** Embed an uploaded image asset on the canvas or within a 2D graph

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col) \| graph` | Yes | Either at(row, col) for canvas-level placement, or a g2d graph reference for graph-level placement |
| `imageName` | `string` | Yes | Name of the uploaded image asset (without file extension) - e.g., "photo", "balloon", "diagram" |
| `x` | `number` | No | X coordinate for graph mode positioning (used with graph reference) |
| `y` | `number` | No | Y coordinate for graph mode positioning (used with graph reference) |
| `point` | `point expression` | No | A point expression for graph mode positioning (alternative to x, y) |
| `scale` | `number` | No | Scale factor for the image (default 1.0, must be positive). Multiplies the natural width and height. |

## Variants

### Canvas mode (logical coordinates)

```
image(at(row, col), "name")
```

Place image at logical canvas position without scale

### Canvas mode with scale

```
image(at(row, col), "name", scale)
```

Place image at logical canvas position with custom scale

### Graph mode with x, y

```
image(G, "name", x, y)
```

Place image at graph coordinates (x, y)

### Graph mode with x, y and scale

```
image(G, "name", x, y, scale)
```

Place image at graph coordinates with custom scale

### Graph mode with point

```
image(G, "name", point)
```

Place image at a point expression's position

### Graph mode with point and scale

```
image(G, "name", point, scale)
```

Place image at a point expression's position with custom scale

## Examples

### Place image on canvas at logical position

```
m1 = image(at(5, 5), "myshot", 0.5)
```

### Place image at graph origin

```
G = g2d(at(2, 2), 20, 20)
I = image(G, "photo", 0, 0)
```

### Place image at a point with small scale

```
G = g2d(at(2, 20), 20, 20)
I = image(G, "balloon", point(G, -5, 0), 0.1)
```

### Image with transformation (translate)

```
G = g2d(at(2, 20), 20, 20)
I = image(G, "balloon", point(G, -5, 0), 0.1)
R = translate(G, I, 4, 4)
```

### Fill a shape with an image using fi()

```
G = g2d(at(2, 3), 30, 30)
r1 = rect(G, 12, 4, 4, 3, fi("tree", 0.7), fo(1), s(0.1))
```
