---
title: vector
sidebar_label: vector
---

# vector

Creates a 2D directed arrow between two points or from coordinates, with support for position vectors and polar form.

**Utility:** Create a 2D vector (arrow) from points or coordinates

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `x1 or point1` | `number \| point` | Yes | Start x-coordinate or start point expression |
| `y1 or point2` | `number \| point` | Yes | Start y-coordinate or end point expression |
| `x2` | `number` | No | End x-coordinate (when using 4-coordinate form) |
| `y2` | `number` | No | End y-coordinate (when using 4-coordinate form) |

## Variants

### From four coordinates

```js
vector(G, x1, y1, x2, y2)
```

Vector from (x1,y1) to (x2,y2)

### From two points

```js
vector(G, P1, P2)
```

Vector from point P1 to point P2

### Position vector

```js
vector(G, P1, type(position))
```

Position vector from origin to point P1

### Polar vector

```js
vector(G, length, angle, type(polar))
```

Vector from origin with given length and angle in degrees

## Examples

### Create graph and vector from coordinates

```js
G = g2d(at(8, 0), 20, 20)
```

### Vector from (0,-2) to (3,4)

```js
V1 = vector(G, 0, -2, 3, 4)
```

### Vector from (-2,-2) to (5,-4)

```js
V2 = vector(G, -2, -2, 5, -4)
```

### Vector between two point variables

```js
V3 = vector(G, point_A, point_B)
```

### Position vector from origin to a point

```js
V4 = vector(G, point_A, type(position))
```

### Polar vector: length 5 at 45 degrees

```js
V5 = vector(G, 5, 45, type(polar))
```

### Red-colored vector

```js
V6 = vector(G, 0, 0, 3, 4, c(red))
```
