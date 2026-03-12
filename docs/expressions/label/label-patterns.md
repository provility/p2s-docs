---
title: label
sidebar_label: label
---

# label

Patterns for annotating geometric constructions with multiple labels, covering vertex names, side lengths, and angle measurements. Commonly used for complete triangle annotation including all vertices, edges, and interior angles with appropriate positioning and rotation.

**Utility:** Multi-label annotation patterns for triangles, polygons, and geometric constructions

## Variants

### Full triangle vertex labeling (3 labels)

```
label(G, at(angle_A), "A", buff(-1, 1))
label(G, at(angle_B), "B", buff(-1, -1.8))
label(G, at(angle_C), "C", buff(1, -1))
```

Label all three vertices of a triangle with angle-based positioning

### Full triangle side labeling (3 labels)

```
label(G, at(item(tri, type(edge), 1)), "c", buff(0, -0.5))
label(G, at(item(tri, type(edge), 2)), "a", buff(-1.5, 1), rotation(26))
label(G, at(item(tri, type(edge), 3)), "b", buff(-1.5, -1.5))
```

Label all three sides of a triangle with edge-based positioning

### Trig substitution triangle (sides + angle)

```
label(G, at(item(tri, type(edge), 2)), "a", buff(-2, -0.7), rotation(26))
label(G, at(angle_2), "theta", buff(-0.9, -2))
label(G, at(item(tri, type(edge), 1)), "?", buff(0, 0.5))
label(G, at(item(tri, type(edge), 3)), "x", buff(-0.2, -1.1))
```

Label triangle for trig substitution: hypotenuse a, angle theta, unknown ?, side x

### Two-point secant/tangent labeling

```
label(G, p, "P", buff(-1, 1))
label(G, q, "Q", buff(-1, -1))
```

Label two points on a curve for limit/tangent visualization

### Label with height annotation

```
label(G, at(item(tri, type(edge), 1)), "c", buff(0, -0.5))
label(G, at(line_height), "h", buff(0, 0.5))
```

Label base and height of a triangle

## Examples

### Complete trig substitution triangle annotation

```
graph_1 = g2d(at(5, 26), 13.3, 20.6, range(-1, 5, 1), range(-1, 5, 1), grid(noaxes))
point_1 = point(graph_1, 0, 0, nodraw())
triangle_1 = sss(graph_1, 4, 3, point_1)
angle_1 = angle(graph_1, item(triangle_1, type(angle), 1), 0.8, type(interior))
angle_2 = angle(graph_1, item(triangle_1, type(angle), 2), 0.8, type(interior))
label_1 = label(graph_1, at(item(triangle_1, type(edge), 2)), "a", buff(-2, -0.7), rotation(26), type(write))
label_2 = label(graph_1, at(angle_2), "theta", buff(-0.9, -2))
label_3 = label(graph_1, at(item(triangle_1, type(edge), 1)), "?", buff(0, 0.5), rotation(0))
label_5 = label(graph_1, at(item(triangle_1, type(edge), 3)), "x", buff(-0.2, -1.1), rotation(0))
```

### Label two points P and Q for tangent/secant limit

```
eq = def(x, "x^2")
G = g2d(at(2, 3), 30, 30, range(-2, 3), range(-1, 5))
pl1 = plot(G, eq)
p = point(G, 0.8, fun(eq, 0.8))
label(G, p, "P", buff(-1, 1))
q = point(G, 2, fun(eq, 2))
label(G, q, "Q", buff(-1, -1))
```

### Label all three angle vertices of a triangle

```
angle_A = angle(graph_1, item(triangle_1, type(angle), 1), 0.8, type(interior))
angle_B = angle(graph_1, item(triangle_1, type(angle), 2), 0.8, type(interior))
angle_C = angle(graph_1, item(triangle_1, type(angle), 3), 0.8, type(interior))
label_A = label(graph_1, at(angle_A), "A", buff(-1.0, 1.0))
label_B = label(graph_1, at(angle_B), "B", buff(-1.0, -1.8))
label_C = label(graph_1, at(angle_C), "C", buff(1.0, -1))
```

### Label all three sides of a triangle

```
label_a = label(graph_1, at(item(triangle_1, type(edge), 2)), "a", buff(-1.5, 1), rotation(26))
label_c = label(graph_1, at(item(triangle_1, type(edge), 1)), "c", buff(0, -0.5))
label_b = label(graph_1, at(item(triangle_1, type(edge), 3)), "b", buff(-1.5, -1.5))
```

### Label with textreplace to connect diagram to equation

```
label_3 = label(graph_1, at(item(triangle_1, type(edge), 1)), "?", buff(0, 0.5), rotation(0))
write_2 = write(at(3.1, 2.2), "int sqrt(a^2-x^2) dx", type(write))
select_1 = select(write_2, "a^2-x^2", 1)
text_replace_6 = textreplace(label_3, select_1, buff(0, -2), type(replace))
```

### Label with correlate to visually link diagram label to equation term

```
label_5 = label(graph_1, at(item(triangle_1, type(edge), 3)), "x", buff(-0.2, -1.1), rotation(0))
write_7 = write(at(8, 3), "x = a sin(theta)", type(write))
select_9 = select(write_7, "x", 1)
correlate_1 = correlate(select_9, label_5, type(circle))
```

### Point label and graph label combined

```
graph_1 = g2d(at(5.1, 27.5), 7.4, 12.2, range(-5, 5), range(-5, 5))
point_1 = point(graph_1, 2, 1)
label_1 = label(graph_1, at(point_1), "A", buff(0.5, 0.5))
```
