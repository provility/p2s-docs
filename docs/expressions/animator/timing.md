---
title: change
sidebar_label: change
---

# change

Smoothly animates a numeric variable from its current value to a target value over a specified duration, with all dependent expressions updating in real time.

**Utility:** Animate a numeric variable smoothly from current value to target value

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `variable` | `variable` | Yes | Reference to a previously defined numeric variable |
| `target` | `number` | Yes | Target value the variable animates toward |
| `duration` | `t(seconds)` | No | Animation duration in seconds - e.g., t(5) for 5 seconds |

## Variants

### Instant change

```
change(variable, targetValue)
```

Animate variable to target with default duration

### Timed change

```
change(variable, targetValue, t(seconds))
```

Animate variable to target over specified duration

### Change ratio to animate point on curve

```
change(r, 0.8)
```

Animate a ratio variable to slide a point along a line or curve

## Examples

### Animate secant line approaching tangent (limit demonstration)

```
eq = def(x, "x^2")
G = g2d(at(2, 3), 30, 30, range(-2, 3), range(-1, 5))
pl1 = plot(G, eq)
b = 0.8
q_1 = 2
tangent(G, pl1, b, c(blue))
p = point(G, b, fun(eq, b))
q = point(G, q_1, fun(eq, q_1))
line(G, p, q, c(red))
change(q_1, 0.8, t(5))
```

### Animate point sliding along a line segment

```
G = g2d(at(2, 3), 30, 30)
L = line(G, -5, 0, 5, 7)
r = 0
P = point(G, L, r, type(ratio))
change(r, 0, 0.8)
```

### Animate polar angle sweep

```
G = p2d(at(2, 4), 20, 20, range(0, 10, 1), grid())
ang = 30
change(ang, 210)
```

### Animate 3D point coordinate

```
G = g3d(at(0, 0), 30, 30)
x0 = 2
point(G, x0, 1, 3)
change(x0, 1, -2)
```

### Animate limit approach from one side

```
G = g2d(at(1, 25), 14, 15, range(-2, 3, 1), range(-1, 5, 1))
q1x = 2
change(q1x, 0.8)
```
