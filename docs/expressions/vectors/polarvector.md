---
title: polarvector
sidebar_label: polarvector
---

# polarvector

Creates a directed arrow from polar coordinates, specified by magnitude and angle in degrees counterclockwise from the positive x-axis.

**Utility:** Create a vector from polar coordinates (length and angle in degrees)

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `length` | `number` | Yes | Magnitude (length) of the vector |
| `angle` | `number` | Yes | Angle in degrees measured counterclockwise from positive x-axis |
| `fromPoint` | `point \| number (x)` | No | Optional start point or x-coordinate for vector origin |
| `fromY` | `number` | No | Optional y-coordinate when fromPoint is an x-coordinate |

## Variants

### From origin

```js
polarvector(G, length, angle)
```

Vector from origin with given length and angle

### From a point

```js
polarvector(G, length, angle, point)
```

Vector starting at given point

### From coordinates

```js
polarvector(G, length, angle, x, y)
```

Vector starting at (x, y)

## Examples

### Create graph

```js
G = g2d(at(8, 0), 20, 20)
```

### Vector of length 5 at 30 degrees from origin

```js
pv1 = polarvector(G, 5, 30)
```

### Vector of length 3 at 90 degrees (straight up)

```js
pv2 = polarvector(G, 3, 90)
```

### Polar vector starting from a point

```js
pv3 = polarvector(G, 4, 60, point(G, 2, 1))
```

### Polar vector starting from coordinates

```js
pv4 = polarvector(G, 4, 45, -1, -1)
```

### Styled polar vector in blue

```js
pv5 = polarvector(G, 5, 120, c(blue))
```
