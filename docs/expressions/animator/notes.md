---
title: notes
sidebar_label: notes
---

# notes

Attaches a popup text annotation to a shape or expression, displayed on user interaction. Supports custom text and background colors.

**Utility:** Attach popup text notes or media to shapes and expressions

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `string` | Yes | Text content or media asset name in quotes |
| `color` | `c(colorName)` | No | Text color for the note - e.g., c(black), c(red) |
| `fillColor` | `fc(colorName)` | No | Background fill color - e.g., fc(orange), fc(yellow) |

## Variants

### Simple text note on a point

```js
point(G, x, y, notes("text"))
```

Attach a text annotation to a point

### Styled note with colors

```js
point(G, x, y, notes("text", c(black), fc(orange)))
```

Note with text color and background color

### Note on textreveal

```js
textreveal(selectVar, buff(r, c), notes("explanation"))
```

Show note when text is revealed

### Long note on a point

```js
point(G, x, y, notes("You can write a long sentence here"))
```

Detailed annotation text

## Examples

### Point with colored popup note

```js
G = g2d(at(2, 20), 20, 20)
px = point(G, 2, 3, notes("Hello there", c(black), fc(orange)))
```

### Point with descriptive note on a line

```js
G = g2d(at(2, 3), 30, 30)
L = line(G, -5, 0, 5, 7)
r = 0
P = point(G, L, r, type(ratio), fi("tree", 1), notes("You can write a long sentence here"))
```

### Textreveal with note narration

```js
writewithout_1 = writewithout(at(21.4, 14.2), "(a+x^2 + 1) / (x^2 + 1)", select("x^2 + 1", 2), type(write), f(48))
text_reveal_1 = textreveal(writewithout_1_select_1, buff(-0.4, -0.2), notes("hello world"))
```
