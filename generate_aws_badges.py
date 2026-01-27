#!/usr/bin/env python3
badges_to_create = {
    'AWS_S3': '569A31',
    'AWS_Lambda': 'FF9900',
    'AWS_EC2': 'FF9900',
    'AWS_CloudFront': 'FF9900',
    'AWS_Route53': 'FF9900',
    'AWS_RDS': '527FFF',
    'AWS_IAM': 'DD1717',
    'AWS_API_Gateway': '8C2F2F',
    'AWS_Amplify': 'FF9900',
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
