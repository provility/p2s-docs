#!/usr/bin/env python3
"""
Generate Markdown docs from rag-source JSON files for Docusaurus.
Each JSON file becomes a doc page; each rag-source subdirectory becomes a sidebar category.
"""

import json
import os

RAG_SOURCE = os.path.join(os.path.dirname(__file__), '..', '..', 'p2s-coding-agent', 'rag-source')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'docs', 'expressions')

CATEGORY_LABELS = {
    '3d': '3D Shapes',
    '3d-plotting': '3D Plotting',
    '3d-vectors': '3D Vectors',
    'triangle-polygon': 'Triangles & Polygons',
    'graph2d': '2D Graphs',
    'graph3d': '3D Graphs',
    'mathtext': 'Math Text',
    'geometry': 'Geometry',
    'conics': 'Conics',
    'vectors': 'Vectors',
    'plotting': 'Plotting',
    'analytical': 'Analytical',
    'transforms': 'Transforms',
    'animator': 'Animator',
    'card': 'Card',
    'image': 'Image',
    'positioning': 'Positioning',
    'styling': 'Styling',
    'label': 'Labels',
    'markers': 'Markers',
    'correlate': 'Correlate',
    'table': 'Table',
    'traces': 'Traces',
}

CATEGORY_POSITION = {
    'geometry': 1,
    'conics': 2,
    'triangle-polygon': 3,
    'vectors': 4,
    '3d': 5,
    '3d-vectors': 6,
    'graph2d': 7,
    'graph3d': 8,
    'plotting': 9,
    '3d-plotting': 10,
    'analytical': 11,
    'transforms': 12,
    'label': 13,
    'markers': 14,
    'mathtext': 15,
    'styling': 16,
    'positioning': 17,
    'animator': 18,
    'correlate': 19,
    'table': 20,
    'traces': 21,
    'card': 22,
    'image': 23,
}


def escape_mdx(text):
    """Escape curly braces for MDX compatibility (outside code blocks)."""
    return text.replace('{', '\\{').replace('}', '\\}').replace('<', '&lt;').replace('>', '&gt;')


def render_expression_markdown(data):
    lines = []
    expr = data.get('expression', 'unknown')
    desc = escape_mdx(data.get('description', ''))
    utility = escape_mdx(data.get('utility', ''))

    # Frontmatter
    lines.append('---')
    lines.append(f'title: {expr}')
    lines.append(f'sidebar_label: {expr}')
    lines.append('---')
    lines.append('')
    lines.append(f'# {expr}')
    lines.append('')
    lines.append(desc)
    lines.append('')

    if utility:
        lines.append(f'**Utility:** {utility}')
        lines.append('')

    # Arguments table
    args = data.get('arguments', [])
    if args:
        lines.append('## Arguments')
        lines.append('')
        lines.append('| Name | Type | Required | Description |')
        lines.append('|------|------|----------|-------------|')
        for arg in args:
            req = 'Yes' if arg.get('required') else 'No'
            atype = escape_mdx(arg.get('type', '')).replace('|', '\\|')
            lines.append(f"| `{arg['name']}` | `{atype}` | {req} | {escape_mdx(arg.get('description', ''))} |")
        lines.append('')

    # Alternates / Variants
    alts = data.get('alternates', [])
    if alts:
        lines.append('## Variants')
        lines.append('')
        for alt in alts:
            lines.append(f"### {escape_mdx(alt.get('variant', ''))}")
            lines.append('')
            lines.append('```')
            lines.append(alt.get('syntax', ''))
            lines.append('```')
            lines.append('')
            lines.append(escape_mdx(alt.get('description', '')))
            lines.append('')

    # Examples
    examples = data.get('examples', [])
    if examples:
        lines.append('## Examples')
        lines.append('')
        for ex in examples:
            scenario = ex.get('scenario', '')
            expression = ex.get('expression', '')
            if scenario:
                lines.append(f'### {escape_mdx(scenario)}')
                lines.append('')
            lines.append('```')
            lines.append(expression)
            lines.append('```')
            lines.append('')

    return '\n'.join(lines)


def main():
    rag_source = os.path.abspath(RAG_SOURCE)
    output_dir = os.path.abspath(OUTPUT_DIR)

    # Clean output directory
    if os.path.exists(output_dir):
        import shutil
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    total_files = 0

    for category_dir in sorted(os.listdir(rag_source)):
        category_path = os.path.join(rag_source, category_dir)
        if not os.path.isdir(category_path):
            continue

        out_category = os.path.join(output_dir, category_dir)
        os.makedirs(out_category, exist_ok=True)

        # Write _category_.json for sidebar ordering
        label = CATEGORY_LABELS.get(category_dir, category_dir.replace('-', ' ').title())
        position = CATEGORY_POSITION.get(category_dir, 99)
        with open(os.path.join(out_category, '_category_.json'), 'w') as f:
            json.dump({
                'label': label,
                'position': position,
                'collapsed': True,
            }, f, indent=2)

        for json_file in sorted(os.listdir(category_path)):
            if not json_file.endswith('.json'):
                continue

            with open(os.path.join(category_path, json_file)) as f:
                data = json.load(f)

            md = render_expression_markdown(data)
            slug = json_file.replace('.json', '')
            md_path = os.path.join(out_category, f'{slug}.md')
            with open(md_path, 'w') as f:
                f.write(md)

            total_files += 1

    print(f'Generated {total_files} expression docs in {output_dir}')


if __name__ == '__main__':
    main()
