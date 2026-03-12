---
title: "Line + Line"
sidebar_label: "Line + Line"
---

# Line + Line

Operations available when you select a **line** and a **line** together.

## How to Use

```
  1. Click on a line object to select it
  2. Hold Shift and click on a line object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Intersect** | Handler for two-line selection |
| **Angle** | Find intersection point of two lines |

## Expression Details

**Find intersection point of two lines**

```
intersect(G, L1, L2, n)
```

**Create angle between two lines**

```
angle(G, L1, L2, type(interior), radius(0.2))
```
