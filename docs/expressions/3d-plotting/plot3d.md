---
title: plot3d
sidebar_label: plot3d
---

# plot3d

Renders a 3D surface as a wireframe mesh from an explicit equation z = f(x, y) or an implicit equation f(x, y, z) = 0 over a rectangular domain.

**Utility:** Plot a 3D surface z = f(x, y) on a g3d graph

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d reference` | Yes | The 3D graph container created with g3d() |
| `equation` | `string \| def reference` | Yes | Surface equation as a quoted string "x^2 + y^2" or a function definition reference from def() |
| `xRange` | `range(min, max)` | No | Domain for x variable. Defaults to g3d axis range if omitted |
| `yRange` | `range(min, max)` | No | Domain for y variable. Defaults to g3d axis range if omitted |
| `color` | `c(colorName)` | No | Surface color - e.g., c("blue"), c("magenta") |

## Variants

### Explicit surface with auto domain

```js
plot3d(G, "x^2 + y^2")
```

Surface using g3d default axis ranges

### Explicit surface with custom domain

```js
plot3d(G, "x^2 + y^2", range(-3, 3), range(-3, 3))
```

Surface with explicit x and y domain

### Surface from function definition

```js
plot3d(G, f, range(-3, 3), range(-3, 3))
```

Surface using a def() function reference for reuse

### Implicit surface

```js
plot3d(G, "x^2 + y^2 + z^2 - 1")
```

Implicit surface f(x,y,z) = 0 when expression uses x, y, and z

### Surface with color

```js
plot3d(G, "sin(x)*cos(y)", range(-3, 3), range(-3, 3), c("blue"))
```

Colored surface

## Examples

### Paraboloid surface with custom range

```js
G = g3d(at(0, 0), 30, 30)
S = plot3d(G, "x^2 + y^2", range(-3, 3), range(-3, 3))
```

### Surface from function definition with point and tangent plane

```js
G = g3d(at(0, 0), 30, 30)
f = def(x, y, "x^2 + y^2")
P = plot3d(G, f, range(-3, 3), range(-3, 3))
x0 = 1
y0 = 1
pt = point3d(G, x0, y0, fun(f, x0, y0))
T = tangentplane(G, P, x0, y0)
```

### Implicit sphere surface

```js
G = g3d(at(0, 0), 30, 30)
S = plot3d(G, "x^2 + y^2 + z^2 - 1")
```
