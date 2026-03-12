---
title: "Point + Point"
sidebar_label: "Point + Point"
---

# Point + Point

Operations available when you select a **point** and a **point** together.

## How to Use

```
  1. Click on a point object to select it
  2. Hold Shift and click on a point object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Line** | Handler for two-point selection |
| **Vector** | Create a line between two points |
| **Distance** | Create a vector from first point to second point |
| **Midpoint** | Show distance between two points with visualization |
| **Circle** | Create midpoint between two points |
| **Ellipse** | Create a circle from two points |
| **Arc** | Create an ellipse with two points as foci |
| **Measure** | Create an arc between two points |

## Expression Details

**Create a line between two points**

```
line(G, P1, P2, type(line|segment|ray))
```

**Create a vector from first point to second point**

```
vector(G, P1, P2)
```

**Show distance between two points with visualization**

```
trace(G, P1, type(distance), P2, buff(-1, -1))
```

**Create midpoint between two points**

```
midpoint(G, P1, P2)
```

**Create a circle from two points**

```
circle(G, P1, P2) — center + through point
```

**Create an ellipse with two points as foci**

```
ellipse(G, F1, F2, type(foci))
```

**Create an arc between two points**

```
arc(G, P1, P2, rx, ry)
```

**Create a measurement indicator between two points**

```
measure(G, P1, P2, "label", buff(x))
```
