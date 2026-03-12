---
title: square
sidebar_label: square
---

# square

Create a square from a top-left corner point and side length. All four sides are equal and all angles are 90 degrees.

**Utility:** Create square from top-left corner and side length

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `topLeft` | `point \| x, y` | Yes | Top-left corner (point variable or x,y coordinates) |
| `size` | `number` | Yes | Side length of the square |

## Variants

### From point variable

```
square(G, P, size)
```

Square with corner at point variable P

### From coordinates

```
square(G, x, y, size)
```

Square with corner at coordinates

### From inline point

```
square(G, point(G, 1, 5), 4)
```

Square with inline point definition

### With styling

```
square(G, P, 4, c(red), f(pink))
```

Colored square with stroke and fill

## Examples

### Unit square at origin

```
square_1 = square(graph_1, point(graph_1, 0, 1), 1)
```

### Square for Pythagorean proof

```
square_a = square(graph_1, point(graph_1, 0, 5), 3)
```

### Extract edge for labeling

```
edge_1 = line(graph_1, item(square_1, type(edge), 1), type(segment))
```

### Get square diagonal

```
diag = property(square_1, type(diagonal))
```

### Colored square with fill

```
square_2 = square(graph_1, point(graph_1, 3, 4), 2, c(blue), f(lightblue))
```
