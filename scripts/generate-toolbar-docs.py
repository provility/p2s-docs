#!/usr/bin/env python3
"""
Generate Markdown toolbar docs from features/ JS files for Docusaurus.
Creates step-by-step guides with ASCII diagrams for end users.
"""

import json
import os
import re

FEATURES_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'p2s-coding-agent', 'features')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs', 'toolbar')


def extract_categories_from_js(filepath):
    """Extract static categories array from a click-items JS file using regex."""
    with open(filepath) as f:
        content = f.read()

    categories = []
    # Find each category block
    cat_pattern = re.compile(
        r"\{\s*id:\s*'([^']+)',\s*label:\s*'([^']+)',\s*(?:subcategories|items):\s*\[",
        re.DOTALL
    )

    # Find all items
    item_pattern = re.compile(
        r"\{\s*id:\s*'([^']+)',\s*label:\s*'([^']*)'.*?signature:\s*'([^']*)'",
        re.DOTALL
    )

    # Extract subcategories too
    subcat_pattern = re.compile(
        r"subcategories:\s*\[(.*?)\]\s*\}",
        re.DOTALL
    )

    # Simple approach: find categories, then items within each
    current_pos = 0
    for cat_match in cat_pattern.finditer(content):
        cat_id = cat_match.group(1)
        cat_label = cat_match.group(2)

        # Find the closing of this category block
        start = cat_match.end()
        # Find items within
        items = []

        # Search for items in the rest until next category or end
        next_cat = cat_pattern.search(content, start)
        end = next_cat.start() if next_cat else len(content)
        section = content[start:end]

        for item_match in item_pattern.finditer(section):
            items.append({
                'id': item_match.group(1),
                'label': item_match.group(2),
                'signature': item_match.group(3),
            })

        if items:
            categories.append({
                'id': cat_id,
                'label': cat_label,
                'items': items,
            })

    return categories


def extract_multiselect_from_js(filepath):
    """Extract operations and method JSDoc from a multi-select items JS file."""
    with open(filepath) as f:
        content = f.read()

    # Get signature
    sig_match = re.search(r"static signature\s*=\s*'([^']+)'", content)
    signature = sig_match.group(1) if sig_match else os.path.basename(filepath)

    # Get operations
    operations = []
    op_pattern = re.compile(r"\{\s*id:\s*'([^']+)',\s*label:\s*'([^']*)'", re.DOTALL)
    for match in op_pattern.finditer(content):
        operations.append({
            'id': match.group(1),
            'label': match.group(2),
        })

    # Get JSDoc comments with expression syntax
    jsdoc_pattern = re.compile(
        r'/\*\*\s*\*\s*(.*?)\s*\*\s*(.*?)\s*\*/',
        re.DOTALL
    )
    methods = []
    for match in jsdoc_pattern.finditer(content):
        desc_block = match.group(0)
        lines = [l.strip().lstrip('* ').strip() for l in desc_block.split('\n')]
        desc = ''
        syntax = ''
        for line in lines:
            if line.startswith('/**') or line.startswith('*/') or not line:
                continue
            if '(' in line and ')' in line and not desc:
                # Might be syntax if it looks like a function call
                pass
            if not desc and line and not line.startswith('@'):
                desc = line
            elif desc and line and not line.startswith('@') and '(' in line:
                syntax = line
                break

        if desc:
            methods.append({'description': desc, 'syntax': syntax})

    return signature, operations, methods


def write_click_creation_doc(output_path, title, description, ascii_diagram, categories):
    """Write a click-creation doc page."""
    lines = []
    lines.append('---')
    lines.append(f'title: "{title}"')
    lines.append(f'sidebar_label: "{title}"')
    lines.append('---')
    lines.append('')
    lines.append(f'# {title}')
    lines.append('')
    lines.append(description)
    lines.append('')
    lines.append('## How It Works')
    lines.append('')
    lines.append('```')
    lines.append(ascii_diagram)
    lines.append('```')
    lines.append('')

    for cat in categories:
        lines.append(f"## {cat['label']}")
        lines.append('')
        lines.append('| Operation | What It Creates |')
        lines.append('|-----------|----------------|')
        for item in cat['items']:
            sig = item.get('signature', '')
            # Extract the description part after →
            desc = sig.split('→')[-1].strip() if '→' in sig else sig
            lines.append(f"| **{item['label']}** | {desc} |")
        lines.append('')

    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))


def write_multiselect_doc(output_path, title, sig, operations, methods):
    """Write a multi-select operations doc page."""
    lines = []
    # Make readable title from signature like "point+point" -> "Point + Point"
    readable = ' + '.join(part.replace('3d', ' 3D').title() for part in sig.split('+'))

    lines.append('---')
    lines.append(f'title: "{readable}"')
    lines.append(f'sidebar_label: "{readable}"')
    lines.append('---')
    lines.append('')
    lines.append(f'# {readable}')
    lines.append('')
    parts = sig.split('+')
    if len(parts) >= 2:
        lines.append(f'Operations available when you select a **{parts[0]}** and a **{parts[1]}** together.')
    else:
        lines.append(f'Operations available when you select **{sig}** objects.')
    lines.append('')

    lines.append('## How to Use')
    lines.append('')
    lines.append('```')
    if len(parts) >= 2:
        lines.append(f'  1. Click on a {parts[0]} object to select it')
        lines.append(f'  2. Hold Shift and click on a {parts[1]} object')
        lines.append(f'  3. Right-click to open the context menu')
        lines.append(f'  4. Choose an operation from the menu')
    else:
        lines.append(f'  1. Select multiple {sig} objects (Shift + click)')
        lines.append(f'  2. Right-click to open the context menu')
        lines.append(f'  3. Choose an operation from the menu')
    lines.append('```')
    lines.append('')

    lines.append('## Available Operations')
    lines.append('')
    lines.append('| Operation | Description |')
    lines.append('|-----------|-------------|')

    # Merge operation labels with method descriptions
    for i, op in enumerate(operations):
        desc = ''
        if i < len(methods):
            desc = methods[i].get('description', '')
            syntax = methods[i].get('syntax', '')
            if syntax:
                desc = f'{desc}'
        lines.append(f"| **{op['label']}** | {desc} |")
    lines.append('')

    # Show syntax details if available
    has_syntax = any(m.get('syntax') for m in methods)
    if has_syntax:
        lines.append('## Expression Details')
        lines.append('')
        for m in methods:
            if m.get('syntax'):
                lines.append(f"**{m['description']}**")
                lines.append('')
                lines.append('```')
                lines.append(m['syntax'])
                lines.append('```')
                lines.append('')

    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))


def main():
    output_dir = os.path.abspath(OUTPUT_DIR)
    features_dir = os.path.abspath(FEATURES_DIR)

    # Clean output
    if os.path.exists(output_dir):
        import shutil
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # ========================================
    # 1. 2D Click Creation docs
    # ========================================
    click_dir = os.path.join(output_dir, 'click-creation-2d')
    os.makedirs(click_dir, exist_ok=True)

    with open(os.path.join(click_dir, '_category_.json'), 'w') as f:
        json.dump({'label': 'Click Creation (2D)', 'position': 1, 'collapsed': True}, f, indent=2)

    click_configs = [
        {
            'file': 'graph-click-creation/click-items/OnePointClickItems.js',
            'title': 'One Point',
            'description': 'After clicking **one point** on a 2D graph, a menu appears with these operations.',
            'ascii': (
                '  +---------------------------+\n'
                '  |          2D Graph          |\n'
                '  |                            |\n'
                '  |        x  <-- click        |\n'
                '  |                            |\n'
                '  |   +------------------+     |\n'
                '  |   | Point            |     |\n'
                '  |   | Line             |     |\n'
                '  |   | Vector           |     |\n'
                '  |   | Circle           |     |\n'
                '  |   | Arc              |     |\n'
                '  |   | Polygon          |     |\n'
                '  |   | Triangle         |     |\n'
                '  |   +------------------+     |\n'
                '  +---------------------------+'
            ),
            'position': 1,
        },
        {
            'file': 'graph-click-creation/click-items/TwoPointClickItems.js',
            'title': 'Two Points',
            'description': 'After clicking **two points** on a 2D graph, a menu appears with these operations.',
            'ascii': (
                '  +---------------------------+\n'
                '  |          2D Graph          |\n'
                '  |                            |\n'
                '  |     x  <-- 1st click       |\n'
                '  |              x  <-- 2nd    |\n'
                '  |                            |\n'
                '  |   +------------------+     |\n'
                '  |   | Line             |     |\n'
                '  |   | Vector           |     |\n'
                '  |   | Measure          |     |\n'
                '  |   | Arc              |     |\n'
                '  |   | Conics > Circle  |     |\n'
                '  |   | Conics > Ellipse |     |\n'
                '  |   +------------------+     |\n'
                '  +---------------------------+'
            ),
            'position': 2,
        },
        {
            'file': 'graph-click-creation/click-items/ThreePointClickItems.js',
            'title': 'Three Points',
            'description': 'After clicking **three points** on a 2D graph, a menu appears with these operations.',
            'ascii': (
                '  +---------------------------+\n'
                '  |          2D Graph          |\n'
                '  |     x  <-- 1st             |\n'
                '  |          x  <-- 2nd        |\n'
                '  |     x  <-- 3rd             |\n'
                '  |                            |\n'
                '  |   +------------------+     |\n'
                '  |   | Angle            |     |\n'
                '  |   | Polygon          |     |\n'
                '  |   | Conics > Circle  |     |\n'
                '  |   +------------------+     |\n'
                '  +---------------------------+'
            ),
            'position': 3,
        },
        {
            'file': 'graph-click-creation/click-items/FourPlusPointClickItems.js',
            'title': 'Four or More Points',
            'description': 'After clicking **four or more points** on a 2D graph, a menu appears with these operations.',
            'ascii': (
                '  +---------------------------+\n'
                '  |          2D Graph          |\n'
                '  |   x       x                |\n'
                '  |       x       x            |\n'
                '  |   x               x        |\n'
                '  |                            |\n'
                '  |   +------------------+     |\n'
                '  |   | Point            |     |\n'
                '  |   | Polygon          |     |\n'
                '  |   +------------------+     |\n'
                '  +---------------------------+'
            ),
            'position': 4,
        },
    ]

    for config in click_configs:
        filepath = os.path.join(features_dir, config['file'])
        if not os.path.exists(filepath):
            print(f"Warning: {filepath} not found, skipping")
            continue
        categories = extract_categories_from_js(filepath)
        output_path = os.path.join(click_dir, f"{config['title'].lower().replace(' ', '-').replace('+', 'plus')}.md")
        write_click_creation_doc(output_path, config['title'], config['description'], config['ascii'], categories)

    # ========================================
    # 2. 3D Click Creation docs
    # ========================================
    click3d_dir = os.path.join(output_dir, 'click-creation-3d')
    os.makedirs(click3d_dir, exist_ok=True)

    with open(os.path.join(click3d_dir, '_category_.json'), 'w') as f:
        json.dump({'label': 'Click Creation (3D)', 'position': 2, 'collapsed': True}, f, indent=2)

    click3d_configs = [
        {
            'file': 'graph3d-click-creation/click-items/ZeroPoint3DClickItems.js',
            'title': 'No Points (Expressions)',
            'description': 'Without clicking any points on a 3D graph, you can create expression-based objects like surfaces and curves.',
            'ascii': (
                '  +---------------------------+\n'
                '  |          3D Graph          |\n'
                '  |       /        /           |\n'
                '  |      /  click /            |\n'
                '  |     /--------/             |\n'
                '  |                            |\n'
                '  |   +------------------+     |\n'
                '  |   | Plot (surface)   |     |\n'
                '  |   | Region           |     |\n'
                '  |   | Revolution        |     |\n'
                '  |   | Disk Stack        |     |\n'
                '  |   +------------------+     |\n'
                '  +---------------------------+'
            ),
            'position': 1,
        },
        {
            'file': 'graph3d-click-creation/click-items/OnePoint3DClickItems.js',
            'title': 'One Point (3D)',
            'description': 'After clicking **one point** on a 3D graph, a menu appears with these operations.',
            'ascii': (
                '  +---------------------------+\n'
                '  |          3D Graph          |\n'
                '  |       /        /           |\n'
                '  |      /  x     /            |\n'
                '  |     /--------/             |\n'
                '  |                            |\n'
                '  |   +------------------+     |\n'
                '  |   | Point            |     |\n'
                '  |   | Vector           |     |\n'
                '  |   | Sphere           |     |\n'
                '  |   +------------------+     |\n'
                '  +---------------------------+'
            ),
            'position': 2,
        },
        {
            'file': 'graph3d-click-creation/click-items/TwoPoint3DClickItems.js',
            'title': 'Two Points (3D)',
            'description': 'After clicking **two points** on a 3D graph, a menu appears with these operations.',
            'ascii': (
                '  +---------------------------+\n'
                '  |          3D Graph          |\n'
                '  |       /        /           |\n'
                '  |      / x    x /            |\n'
                '  |     /--------/             |\n'
                '  |                            |\n'
                '  |   +------------------+     |\n'
                '  |   | Point            |     |\n'
                '  |   | Line             |     |\n'
                '  |   | Vector           |     |\n'
                '  |   | Measure          |     |\n'
                '  |   +------------------+     |\n'
                '  +---------------------------+'
            ),
            'position': 3,
        },
        {
            'file': 'graph3d-click-creation/click-items/ThreePoint3DClickItems.js',
            'title': 'Three Points (3D)',
            'description': 'After clicking **three points** on a 3D graph, a menu appears with these operations.',
            'ascii': (
                '  +---------------------------+\n'
                '  |          3D Graph          |\n'
                '  |       /  x     /           |\n'
                '  |      / x    x /            |\n'
                '  |     /--------/             |\n'
                '  |                            |\n'
                '  |   +------------------+     |\n'
                '  |   | Point            |     |\n'
                '  |   | Polygon          |     |\n'
                '  |   | Plane            |     |\n'
                '  |   +------------------+     |\n'
                '  +---------------------------+'
            ),
            'position': 4,
        },
        {
            'file': 'graph3d-click-creation/click-items/FourPlusPoint3DClickItems.js',
            'title': 'Four+ Points (3D)',
            'description': 'After clicking **four or more points** on a 3D graph, a menu appears with these operations.',
            'ascii': (
                '  +---------------------------+\n'
                '  |          3D Graph          |\n'
                '  |     x   /  x     /         |\n'
                '  |      / x    x   /          |\n'
                '  |     /--------/             |\n'
                '  |                            |\n'
                '  |   +------------------+     |\n'
                '  |   | Point            |     |\n'
                '  |   | Polygon          |     |\n'
                '  |   +------------------+     |\n'
                '  +---------------------------+'
            ),
            'position': 5,
        },
    ]

    for config in click3d_configs:
        filepath = os.path.join(features_dir, config['file'])
        if not os.path.exists(filepath):
            print(f"Warning: {filepath} not found, skipping")
            continue
        categories = extract_categories_from_js(filepath)
        slug = config['title'].lower().replace(' ', '-').replace('(', '').replace(')', '').replace('+', 'plus')
        output_path = os.path.join(click3d_dir, f"{slug}.md")
        write_click_creation_doc(output_path, config['title'], config['description'], config['ascii'], categories)

    # ========================================
    # 3. Multi-Select docs
    # ========================================
    multi_dir = os.path.join(output_dir, 'multi-select')
    os.makedirs(multi_dir, exist_ok=True)

    with open(os.path.join(multi_dir, '_category_.json'), 'w') as f:
        json.dump({'label': 'Multi-Select Operations', 'position': 3, 'collapsed': True}, f, indent=2)

    multi_items_dir = os.path.join(features_dir, 'context-menu', 'multi-select', 'items')
    if os.path.exists(multi_items_dir):
        for js_file in sorted(os.listdir(multi_items_dir)):
            if not js_file.endswith('.js'):
                continue
            filepath = os.path.join(multi_items_dir, js_file)
            sig, operations, methods = extract_multiselect_from_js(filepath)

            if not operations:
                continue

            slug = js_file.replace('.js', '').lower()
            # Convert CamelCase to kebab-case
            slug = re.sub(r'(?<!^)(?=[A-Z])', '-', slug).lower()
            output_path = os.path.join(multi_dir, f"{slug}.md")
            write_multiselect_doc(output_path, js_file.replace('.js', ''), sig, operations, methods)

    # ========================================
    # 4. Overview / intro page
    # ========================================
    overview_path = os.path.join(output_dir, 'overview.md')
    with open(overview_path, 'w') as f:
        f.write("""---
title: "Toolbar Overview"
sidebar_label: "Overview"
sidebar_position: 0
---

# Toolbar Overview

Point2Space provides interactive toolbars for creating and editing mathematical objects.
There are several ways to create objects:

## Click Creation (2D)

Click points on a 2D graph to create objects. A menu appears based on how many points you've clicked.

```
  +-------------------------------+
  |           2D Graph            |
  |                               |
  |   Click points on the graph   |
  |   to place them, then choose  |
  |   what to create from the     |
  |   menu that appears.          |
  |                               |
  |   1 point  -> Point, Line,    |
  |               Vector, Circle  |
  |   2 points -> Line, Segment,  |
  |               Vector, Measure |
  |   3 points -> Angle, Triangle,|
  |               Circle          |
  |   4+ points-> Polygon         |
  +-------------------------------+
```

## Click Creation (3D)

Similar to 2D, but works on 3D graphs with 3D objects like points, lines, vectors, planes, and spheres.

## Multi-Select Operations

Select two or more objects (hold Shift + click) to see operations that combine them.

```
  +-------------------------------+
  |   Select two objects:         |
  |                               |
  |   1. Click first object       |
  |   2. Shift + click second     |
  |   3. Right-click for menu     |
  |                               |
  |   Examples:                   |
  |   Point + Point -> Line,      |
  |     Vector, Distance, Circle  |
  |   Line + Point -> Project,    |
  |     Reflect, Perpendicular    |
  |   Vector + Vector -> Sum,     |
  |     Difference, Dot Product   |
  +-------------------------------+
```
""")

    print(f'Generated toolbar docs in {output_dir}')


if __name__ == '__main__':
    main()
