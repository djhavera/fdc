"""
Generate Open-Source to AWS MLOps Architecture Mapping Diagram
Creates a publication-ready figure showing functional equivalence between
open-source tools and AWS services across the SDLM lifecycle.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

# Set up the figure
fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Open-Source to AWS MLOps Architecture Mapping', 
        ha='center', va='center', fontsize=18, fontweight='bold')
ax.text(5, 9.1, 'Functional Equivalence Across SDLM Phases', 
        ha='center', va='center', fontsize=12, style='italic', color='gray')

# Color palette (matching your request)
colors = {
    'plan': '#3498db',      # Blue - Data Management
    'process': '#2ecc71',   # Green - Versioning & Provenance
    'analyze': '#f1c40f',   # Yellow - Experiment Tracking
    'preserve': '#e67e22',  # Orange - Storage & Preservation
    'publish': '#9b59b6'    # Purple - Ontology / Knowledge
}

# Box styling
box_style = "round,pad=0.1"
box_height = 0.8
box_width = 1.6

# Row labels
ax.text(-0.5, 7.5, 'Open-Source\nImplementation', 
        ha='right', va='center', fontsize=11, fontweight='bold', color='#2c3e50')
ax.text(-0.5, 4.5, 'AWS Cloud-Native\nEquivalent', 
        ha='right', va='center', fontsize=11, fontweight='bold', color='#2c3e50')

# SDLM Phase positions
phases = [
    {'x': 1, 'name': 'Plan/Acquire', 'color': colors['plan']},
    {'x': 2.8, 'name': 'Process', 'color': colors['process']},
    {'x': 4.6, 'name': 'Analyze', 'color': colors['analyze']},
    {'x': 6.4, 'name': 'Preserve', 'color': colors['preserve']},
    {'x': 8.2, 'name': 'Publish/Share', 'color': colors['publish']}
]

# Open-Source Stack (Top Row)
opensource_tools = [
    {'x': 1, 'label': 'Jupyter\n+\npandas', 'sublabel': 'Data ingestion\n& exploration', 'color': colors['plan']},
    {'x': 2.8, 'label': 'Jupyter\n+\nDVC', 'sublabel': 'Dataset versioning\n& provenance', 'color': colors['process']},
    {'x': 4.6, 'label': 'Jupyter\n+\nWeights &\nBiases', 'sublabel': 'Experiment\ntracking', 'color': colors['analyze']},
    {'x': 6.4, 'label': 'GitHub\n+\nLocal Storage', 'sublabel': 'Version control\n& artifacts', 'color': colors['preserve']},
    {'x': 8.2, 'label': 'RDF Ontology\n+\nERD', 'sublabel': 'Conceptual\nmodeling', 'color': colors['publish']}
]

# AWS Stack (Bottom Row)
aws_services = [
    {'x': 1, 'label': 'AWS Glue\n+\nS3 Versioning', 'sublabel': 'Metadata\n& storage', 'color': colors['plan']},
    {'x': 2.8, 'label': 'SageMaker\nLineage\n+\nStep Functions', 'sublabel': 'Provenance\n& orchestration', 'color': colors['process']},
    {'x': 4.6, 'label': 'SageMaker\nExperiments\n+\nCloudWatch', 'sublabel': 'Metrics\n& visualization', 'color': colors['analyze']},
    {'x': 6.4, 'label': 'Amazon S3\nVersioned\nBuckets', 'sublabel': 'Persistent\nartifacts', 'color': colors['preserve']},
    {'x': 8.2, 'label': 'Amazon\nNeptune\n+\nLake Formation', 'sublabel': 'Semantic graph\n& governance', 'color': colors['publish']}
]

# Draw Open-Source boxes
for tool in opensource_tools:
    # Main box
    box = FancyBboxPatch((tool['x'] - box_width/2, 7.5 - box_height/2), 
                         box_width, box_height,
                         boxstyle=box_style, 
                         edgecolor=tool['color'], 
                         facecolor=tool['color'], 
                         alpha=0.3,
                         linewidth=2.5)
    ax.add_patch(box)
    
    # Tool name
    ax.text(tool['x'], 7.7, tool['label'], 
            ha='center', va='center', fontsize=9, fontweight='bold', color='#2c3e50')
    
    # Function description
    ax.text(tool['x'], 7.2, tool['sublabel'], 
            ha='center', va='center', fontsize=7, color='#34495e', style='italic')

# Draw AWS boxes
for service in aws_services:
    # Main box
    box = FancyBboxPatch((service['x'] - box_width/2, 4.5 - box_height/2), 
                         box_width, box_height,
                         boxstyle=box_style, 
                         edgecolor=service['color'], 
                         facecolor=service['color'], 
                         alpha=0.3,
                         linewidth=2.5)
    ax.add_patch(box)
    
    # Service name
    ax.text(service['x'], 4.7, service['label'], 
            ha='center', va='center', fontsize=9, fontweight='bold', color='#2c3e50')
    
    # Function description
    ax.text(service['x'], 4.2, service['sublabel'], 
            ha='center', va='center', fontsize=7, color='#34495e', style='italic')

# Draw horizontal arrows (pipeline flow) - Open Source
for i in range(len(opensource_tools) - 1):
    arrow = FancyArrowPatch((opensource_tools[i]['x'] + box_width/2 + 0.1, 7.5),
                           (opensource_tools[i+1]['x'] - box_width/2 - 0.1, 7.5),
                           arrowstyle='->', mutation_scale=20, 
                           linewidth=2, color='#7f8c8d', alpha=0.7)
    ax.add_patch(arrow)

# Draw horizontal arrows (pipeline flow) - AWS
for i in range(len(aws_services) - 1):
    arrow = FancyArrowPatch((aws_services[i]['x'] + box_width/2 + 0.1, 4.5),
                           (aws_services[i+1]['x'] - box_width/2 - 0.1, 4.5),
                           arrowstyle='->', mutation_scale=20, 
                           linewidth=2, color='#7f8c8d', alpha=0.7)
    ax.add_patch(arrow)

# Draw vertical dotted lines (functional equivalence)
for i in range(len(opensource_tools)):
    line = mlines.Line2D([opensource_tools[i]['x'], aws_services[i]['x']], 
                         [7.1, 4.9],
                         linestyle='--', linewidth=1.5, color='#95a5a6', alpha=0.7)
    ax.add_line(line)
    
    # Add "Functional Equivalence" label on first line only
    if i == 2:  # Middle position
        ax.text(opensource_tools[i]['x'] + 0.3, 6, 'Functional\nEquivalence', 
                ha='center', va='center', fontsize=7, style='italic', 
                color='#7f8c8d', rotation=90)

# Add SDLM phase labels at the top
for phase in phases:
    ax.text(phase['x'], 8.5, phase['name'], 
            ha='center', va='center', fontsize=8, fontweight='bold', 
            color=phase['color'],
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                     edgecolor=phase['color'], linewidth=1.5, alpha=0.8))

# Legend
legend_y = 2.5
ax.text(5, legend_y + 0.8, 'Legend', ha='center', va='center', 
        fontsize=11, fontweight='bold', color='#2c3e50')

legend_items = [
    {'label': 'Data Management', 'color': colors['plan']},
    {'label': 'Versioning & Provenance', 'color': colors['process']},
    {'label': 'Experiment Tracking', 'color': colors['analyze']},
    {'label': 'Storage & Preservation', 'color': colors['preserve']},
    {'label': 'Ontology / Knowledge Modeling', 'color': colors['publish']}
]

legend_x_start = 2
for i, item in enumerate(legend_items):
    x = legend_x_start + (i * 1.5)
    # Color box
    box = FancyBboxPatch((x - 0.15, legend_y - 0.1), 0.3, 0.2,
                         boxstyle="round,pad=0.02", 
                         facecolor=item['color'], 
                         edgecolor=item['color'],
                         alpha=0.5)
    ax.add_patch(box)
    # Label
    ax.text(x + 0.2, legend_y, item['label'], 
            ha='left', va='center', fontsize=7, color='#2c3e50')



# Save figure
plt.tight_layout()
plt.savefig('aws_mlops_mapping.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('aws_mlops_mapping.pdf', bbox_inches='tight', facecolor='white')
print("✅ Diagram saved as 'aws_mlops_mapping.png' and 'aws_mlops_mapping.pdf'")


# Also display if running interactively
plt.show()
