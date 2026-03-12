---
title: fi
sidebar_label: fi
---

# fi

Inline modifier that fills a shape's interior with an image asset instead of a solid color, clipping the image to the shape boundary with an optional scale factor.

**Utility:** Fill a shape with an image asset clipped to shape bounds

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `imageName` | `string` | Yes | Name of the uploaded image asset in quotes - e.g., "tree", "star" |
| `scale` | `number` | No | Scale factor for the image, default 1. Positive number, e.g., 0.5, 0.8, 1.5 |

## Variants

### Basic fill image

```js
fi("imageName")
```

Fill shape with image at default scale

### Scaled fill image

```js
fi("imageName", 0.7)
```

Fill shape with image scaled to 70%

### On a rectangle

```js
rect(G, 12, 4, 4, 3, fi("tree", 0.7))
```

Rectangle filled with a scaled image

### On a square

```js
square(G, -2, -2, 3, fi("star", 0.8))
```

Square filled with a scaled image

### On a point

```js
point(G, L, r, type(ratio), fi("tree", 1))
```

Point marker filled with an image

## Examples

### Rectangle with tree image and thin stroke

```js
r1 = rect(G, 12, 4, 4, 3, fi("tree", 0.7), fo(1), s(0.1))
```

### Square with star image

```js
s1 = square(G, -2, -2, 3, fi("star", 0.8))
```

### Point along a line with image fill and notes

```js
P = point(G, L, r, type(ratio), fi("tree", 1), notes("You can write a long sentence here"))
```
