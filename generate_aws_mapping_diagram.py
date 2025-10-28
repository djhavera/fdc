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
fig, ax = plt.subplots(figsize=(16, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'Open-Source, Palantir Foundry, and AWS MLOps Mapping', 
        ha='center', va='center', fontsize=18, fontweight='bold')
ax.text(5, 9.1, 'Functional Equivalence Across the USGS SDLM Lifecycle', 
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
ax.text(-0.5, 7.8, 'Open-Source\nImplementation', 
        ha='right', va='center', fontsize=11, fontweight='bold', color='#2c3e50')
ax.text(-0.5, 6.0, 'Palantir Foundry\nReference Architecture', 
        ha='right', va='center', fontsize=11, fontweight='bold', color='#2c3e50')
ax.text(-0.5, 4.2, 'AWS Cloud-Native\nEquivalent', 
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
    {'x': 2.8, 'label': 'DVC\n+\nJupyter', 'sublabel': 'Dataset versioning\n& provenance', 'color': colors['process']},
    {'x': 4.6, 'label': 'Weights &\nBiases', 'sublabel': 'Experiment\ntracking', 'color': colors['analyze']},
    {'x': 6.4, 'label': 'GitHub\n+\nLocal Storage', 'sublabel': 'Version control\n& artifacts', 'color': colors['preserve']},
    {'x': 8.2, 'label': 'RDF Ontology\n+\nERD', 'sublabel': 'Conceptual\nmodeling', 'color': colors['publish']}
]

# Palantir Foundry Layer (Middle Row)
foundry_tools = [
    {'x': 1, 'label': 'Foundry\nData Import', 'sublabel': 'Data acquisition\nworkbooks', 'color': colors['plan']},
    {'x': 2.8, 'label': 'Foundry\nETL Pipeline', 'sublabel': 'Code graph\n& lineage orchestration', 'color': colors['process']},
    {'x': 4.6, 'label': 'Foundry\nContour', 'sublabel': 'Analytics\n& model experimentation', 'color': colors['analyze']},
    {'x': 6.4, 'label': 'Foundry\nDataset Versioning', 'sublabel': 'Versioned data\n& storage', 'color': colors['preserve']},
    {'x': 8.2, 'label': 'Foundry\nOntology Layer', 'sublabel': 'Unified schema\n& knowledge graph', 'color': colors['publish']}
]

# AWS Stack (Bottom Row)
aws_services = [
    {'x': 1, 'label': 'AWS Glue\n+\nS3', 'sublabel': 'Metadata\n& storage', 'color': colors['plan']},
    {'x': 2.8, 'label': 'Step Functions\n+\nGlue Jobs', 'sublabel': 'ETL orchestration\n& lineage', 'color': colors['process']},
    {'x': 4.6, 'label': 'SageMaker\nExperiments\n+\nCloudWatch', 'sublabel': 'Metrics\n& visualization', 'color': colors['analyze']},
    {'x': 6.4, 'label': 'S3 Versioning\n+\nDataZone Catalog', 'sublabel': 'Persistent\nartifacts', 'color': colors['preserve']},
    {'x': 8.2, 'label': 'Neptune\n+\nLake Formation', 'sublabel': 'Semantic graph\n& governance', 'color': colors['publish']}
]

# Draw Open-Source boxes
for tool in opensource_tools:
    # Main box
    box = FancyBboxPatch((tool['x'] - box_width/2, 7.8 - box_height/2), 
                         box_width, box_height,
                         boxstyle=box_style, 
                         edgecolor=tool['color'], 
                         facecolor=tool['color'], 
                         alpha=0.3,
                         linewidth=2.5)
    ax.add_patch(box)
    
    # Tool name
    ax.text(tool['x'], 8.0, tool['label'], 
            ha='center', va='center', fontsize=9, fontweight='bold', color='#2c3e50')
    
    # Function description
    ax.text(tool['x'], 7.5, tool['sublabel'], 
            ha='center', va='center', fontsize=7, color='#34495e', style='italic')

# Draw Palantir Foundry boxes
for tool in foundry_tools:
    # Main box
    box = FancyBboxPatch((tool['x'] - box_width/2, 6.0 - box_height/2), 
                         box_width, box_height,
                         boxstyle=box_style, 
                         edgecolor=tool['color'], 
                         facecolor=tool['color'], 
                         alpha=0.25,
                         linewidth=2)
    ax.add_patch(box)
    
    # Tool name
    ax.text(tool['x'], 6.2, tool['label'], 
            ha='center', va='center', fontsize=9, fontweight='bold', color='#2c3e50')
    
    # Function description
    ax.text(tool['x'], 5.8, tool['sublabel'], 
            ha='center', va='center', fontsize=7, color='#34495e', style='italic')

# Draw AWS boxes
for service in aws_services:
    # Main box
    box = FancyBboxPatch((service['x'] - box_width/2, 4.2 - box_height/2), 
                         box_width, box_height,
                         boxstyle=box_style, 
                         edgecolor=service['color'], 
                         facecolor=service['color'], 
                         alpha=0.3,
                         linewidth=2.5)
    ax.add_patch(box)
    
    # Service name
    ax.text(service['x'], 4.4, service['label'], 
            ha='center', va='center', fontsize=9, fontweight='bold', color='#2c3e50')
    
    # Function description
    ax.text(service['x'], 3.9, service['sublabel'], 
            ha='center', va='center', fontsize=7, color='#34495e', style='italic')

# Draw horizontal arrows for Open-Source flow
for i in range(len(opensource_tools) - 1):
    ax.annotate('', 
                xy=(opensource_tools[i+1]['x'] - box_width/2 - 0.1, 7.8),
                xytext=(opensource_tools[i]['x'] + box_width/2 + 0.1, 7.8),
                arrowprops=dict(arrowstyle='->', lw=2, color='#95a5a6'))

# Draw horizontal arrows for Foundry flow
for i in range(len(foundry_tools) - 1):
    ax.annotate('', 
                xy=(foundry_tools[i+1]['x'] - box_width/2 - 0.1, 6.0),
                xytext=(foundry_tools[i]['x'] + box_width/2 + 0.1, 6.0),
                arrowprops=dict(arrowstyle='->', lw=2, color='#95a5a6'))

# Draw horizontal arrows for AWS flow
for i in range(len(aws_services) - 1):
    ax.annotate('', 
                xy=(aws_services[i+1]['x'] - box_width/2 - 0.1, 4.2),
                xytext=(aws_services[i]['x'] + box_width/2 + 0.1, 4.2),
                arrowprops=dict(arrowstyle='->', lw=2, color='#95a5a6'))

# Draw vertical dotted lines (functional equivalence across all three tiers)
for i in range(len(opensource_tools)):
    line = mlines.Line2D([opensource_tools[i]['x'], opensource_tools[i]['x']], 
                         [7.4, 4.6],  # Spans from Open-Source to AWS through Foundry
                         linestyle='--', linewidth=1.5, color='#95a5a6', alpha=0.7)
    ax.add_line(line)
    


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
