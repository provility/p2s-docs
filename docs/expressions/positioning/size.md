---
title: size / w / h
sidebar_label: size / w / h
---

# size / w / h

Scale container dimensions by width and height ratios, or query the logical width and height of a container.

**Utility:** Scale container size or query logical width/height of items

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `containers (for size)` | `variable references (g2d \| g3d \| mathtext)` | Yes | One or more container variables to scale |
| `widthRatio (for size)` | `number (positive)` | Yes | Width scale factor (0.5 = half, 1 = no change, 2 = double) |
| `heightRatio (for size)` | `number (positive)` | Yes | Height scale factor (0.5 = half, 1 = no change, 2 = double) |
| `ref (for w/h)` | `variable reference` | Yes | Reference to item for width/height query |

## Variants

### Scale one container

```js
size(G, widthRatio, heightRatio)
```

Scale a single container

### Scale multiple containers

```js
size(G, T, widthRatio, heightRatio)
```

Scale two containers together

### Get width

```js
w(G)
```

Get logical width of container G

### Get height

```js
h(G)
```

Get logical height of container G

### Scale to half size

```js
size(G, 0.5, 0.5)
```

Shrink container to 50%

### Scale to double size

```js
size(G, 2, 2)
```

Enlarge container to 200%

## Examples

### Shrink a graph to half size

```js
G = g2d(at(2, 3), 30, 30)
size(G, 0.5, 0.5)
```

### Double the size of a graph

```js
size(G, 2, 2)
```

### Scale two containers together

```js
G = g2d(at(2, 2), 14, 14)
T = write(at(18, 2), "f(x)", type(write))
size(G, T, 1.5, 1.5)
```

### Scale width only (stretch horizontally)

```js
size(G, 2, 1)
```

### Get width and height of a container

```js
G = g2d(at(2, 2), 14, 14)
width = w(G)
height = h(G)
```
