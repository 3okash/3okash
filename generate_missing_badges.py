#!/usr/bin/env python3
badges_to_create = {
    'TypeScript': '3178C6',
    'React_Native': '61DAFB',
    'GraphQL': 'E10098',
    'Stripe': '008CDD',
    'Vercel': '000000',
}

for name, color in badges_to_create.items():
    label = name.replace('_', ' ')
    text_width = len(label.upper()) * 7
    badge_width = text_width + 20
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{badge_width}" height="28" role="img">
    <title>{label}</title>
    <rect width="{badge_width}" height="28" fill="#{color}"/>
    <text x="{badge_width/2}" y="15.0" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" 
          font-size="11" fill="#fff" text-anchor="middle" dominant-baseline="middle">
        {label.upper()}
    </text>
</svg>'''
    
    with open(f'badges/{name}.svg', 'w') as f:
        f.write(svg)
    print(f"✓ Created {name}.svg")
