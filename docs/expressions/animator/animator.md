---
title: animator
sidebar_label: animator
---

# animator

Creates a clickable button on the canvas that animates a numeric variable to a target value when pressed.

**Utility:** Create an interactive button that animates a variable to a target value on click

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col)` | Yes | Position of the animator button on the canvas |
| `variable` | `variable` | Yes | Reference to a previously defined numeric or point variable |
| `target` | `number` | Yes | Target value the variable animates toward when button is clicked |
| `label` | `string` | No | Custom button label text in quotes - defaults to 'Apply' |

## Variants

### Basic animator

```
animator(at(row, col), variable, target)
```

Button that animates variable to target with default label

### Animator with custom label

```
animator(at(row, col), variable, target, "Go")
```

Button with custom label text

## Examples

### Animate a translation parameter interactively

```
G = g2d(at(2, 20), 20, 20)
a = 4
I = image(G, "balloon", point(G, -5, 0), 0.1)
R = translate(G, I, 4, a)
animator(at(10, 10), a, 2)
```

### Interactive coefficient explorer

```
G = g2d(at(2, 3), 30, 30)
a = 1
plot(G, "a*x^2")
animator(at(2, 30), a, 5)
```
