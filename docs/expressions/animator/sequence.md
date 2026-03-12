---
title: seq
sidebar_label: seq
---

# seq

Chains multiple drawing commands to execute in strict sequential order, where each completes before the next begins.

**Utility:** Chain commands to execute one after another in sequential order

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `commands` | `expression...` | Yes | One or more expressions or variable references to execute in order |

## Variants

### Two-step sequence

```js
seq(command1, command2)
```

Execute command1 then command2

### Multi-step sequence

```js
seq(command1, command2, command3)
```

Execute three commands in order

### Sequence with inline expressions

```js
seq(line(G, x1, y1, x2, y2), line(G, P, Q))
```

Chain inline line drawings sequentially

## Examples

### Parabola ray reflection - incoming ray hits curve then reflects to focus

```js
G = g2d(at(3, 3), 30, 30)
f = def(x, "x^2/6 - 0.5")
P = plot(G, f, -7, 7)
F = point(G, 0, 1)
H1 = intersect(G, P, vline(G, -2))
y_start = 6
seq(line(G, -2, y_start, x(H1), y(H1)), line(G, H1, F))
```

### Multiple parallel ray sequences for parabola focus demonstration

```js
para(seq(line(G, -2, y_start, x(H1), y(H1)), line(G, H1, F)), seq(line(G, -1, y_start, x(H2), y(H2)), line(G, H2, F)), seq(line(G, 0, y_start, x(H3), y(H3)), line(G, H3, F)))
```

### Sequential fade animations

```js
seq(fadeout(shapeA), fadein(shapeB))
```
