---
title: vecproject
sidebar_label: vecproject
---

# vecproject

Projects one vector onto another, returning the orthogonal projection component along the target direction.

**Utility:** Project one vector onto another to get the projection component

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container created with g2d() |
| `vectorToProject` | `vector \| line` | Yes | The vector being projected (A) |
| `vectorTarget` | `vector \| line` | Yes | The vector to project onto (B) |

## Variants

### Project A onto B

```js
vecproject(G, vecA, vecB)
```

Projection of vecA onto vecB

## Examples

### Create graph and two vectors

```js
G = g2d(at(8, 0), 20, 20)
```

### Vector to project

```js
V1 = vector(G, 0, 0, 3, 4)
```

### Target vector to project onto

```js
V2 = vector(G, 0, 0, 5, 0)
```

### Project V1 onto V2 (horizontal component of V1)

```js
proj_1 = vecproject(G, V1, V2)
```

### Styled projection in purple

```js
proj_2 = vecproject(G, V1, V2, c(purple))
```
