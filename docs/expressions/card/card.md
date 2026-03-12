---
title: card
sidebar_label: card
---

# card

Creates a draggable titled card on the canvas for displaying structured content such as definitions, theorems, or instructional text.

**Utility:** Display a titled content card on the canvas at a logical position

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col)` | Yes | Position using logical row, col coordinates on the canvas |
| `title` | `string` | Yes | The card title displayed as a header - e.g., "Definition", "Theorem 1" |
| `content` | `string` | Yes | The card body text content - e.g., "A quadrilateral with four right angles" |

## Variants

### Basic card

```
card(at(row, col), "title", "content")
```

Creates a card with a title and body content at the specified position

## Examples

### Display a definition card

```
card_1 = card(at(2, 3), "Definition", "A rectangle is a quadrilateral with four right angles")
```

### Display a theorem card

```
card_2 = card(at(5, 3), "Theorem", "The sum of interior angles of a triangle is 180 degrees")
```

### Display an instruction card

```
card_3 = card(at(1, 1), "Instructions", "Drag the point to explore the relationship between slope and tangent line")
```
