---
title: mlist
sidebar_label: mlist
---

# mlist

Create bulleted or styled lists for mathematical content with customizable bullet styles (bullet, arrow, check, dash, star, circle, diamond, none). Supports optional vertical spacing control between items.

**Utility:** Display bulleted lists with customizable bullet styles

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `items` | `"item", "item type(style)", ...` | Yes | Quoted items, each optionally with type(bulletStyle) suffix |
| `lineGap` | `number` | No | Vertical spacing between items in points (e.g., 12) |

## Variants

### Default bullets

```
write(at(row, col), mlist("item1", "item2", "item3"))
```

List with default bullet points

### Custom bullet types

```
write(at(row, col), mlist("given type(bullet)", "find type(arrow)", "solution type(check)"))
```

Different bullet for each item

### With line gap

```
write(at(row, col), mlist("item1", "item2", 12))
```

Custom spacing between items

## Examples

### List given information for problem

```
write_1 = write(at(3, 2), mlist("Given: sin(theta) = 1/2 type(bullet)", "Find: theta in [0, 2pi] type(arrow)", "Solution: theta = pi/6, 5pi/6 type(check)"))
```

### Present theorem requirements

```
write_2 = write(at(4, 3), mlist("f is continuous on [a,b]", "f is differentiable on (a,b)", "f(a) = f(b)", 12))
```

### List differentiation rules

```
write_3 = write(at(5, 2), mlist("Power rule: d/dx[x^n] = nx^(n-1) type(arrow)", "Product rule: d/dx[uv] = u'v + uv' type(arrow)", "Chain rule: d/dx[f(g)] = f'(g)g' type(arrow)"))
```

### Show solution steps with checkmarks

```
write_4 = write(at(G, buff(3, 0)), mlist("Factor: x^2-4 = (x+2)(x-2) type(check)", "Set each factor = 0 type(check)", "Solutions: x = -2, 2 type(star)"))
```
