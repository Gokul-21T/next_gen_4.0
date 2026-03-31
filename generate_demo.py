import re

dashboards = ['admin', 'manufacturer', 'supplier', 'logistics', 'designer', 'distributor']
template_dir = 'templates/dashboards/'

# Read base demo template (we'll read the current demo.html up to the <main class="content-area"> tag)
with open('demo.html', 'r') as f:
    demo_content = f.read()

prefix = demo_content[:demo_content.find('<main class="content-area">') + len('<main class="content-area">')]
suffix = demo_content[demo_content.find('</main>'):]
# wait we need to change script tags at the end too
suffix_no_scripts = suffix[:suffix.find('<script>\n/* Charts */')]
script_suffix = suffix[suffix.find('</script>\n</body>'):]

main_content = ""
all_scripts = ""

for role in dashboards:
    with open(f'{template_dir}{role}_dashboard.html', 'r') as f:
        content = f.read()
    
    # Extract blocks
    title_match = re.search(r'{% block page_title %}(.*?){% endblock %}', content, re.DOTALL)
    title = title_match.group(1).strip() if title_match else role.capitalize() + " Dashboard"
    
    actions_match = re.search(r'{% block page_actions %}(.*?){% endblock %}', content, re.DOTALL)
    actions = actions_match.group(1).strip() if actions_match else ''
    
    content_match = re.search(r'{% block content %}(.*?){% endblock %}', content, re.DOTALL)
    body = content_match.group(1).strip() if content_match else ''
    
    js_match = re.search(r'{% block extra_js %}\s*<script>(.*?)</script>\s*{% endblock %}', content, re.DOTALL)
    js = js_match.group(1).strip() if js_match else ''
    
    css_match = re.search(r'{% block extra_css %}(.*?){% endblock %}', content, re.DOTALL)
    css = css_match.group(1).strip() if css_match else ''
    
    # Clean up django tags from body
    body = re.sub(r'{% for .*? %}', '', body)
    body = re.sub(r'{% empty %}', '', body)
    body = re.sub(r'{% endfor %}', '', body)
    
    # Add to main content
    style_str = '' if role == 'admin' else 'style="display:none;"'
    main_content += f'\n<div class="dashboard-section" data-role="{role}" {style_str}>\n'
    if css:
        main_content += css + '\n'
    main_content += f'''
    <div class="page-header mb-4">
      <div class="d-flex align-items-center justify-content-between">
        <div>
          <h4 class="page-title mb-1">{title}</h4>
          <nav aria-label="breadcrumb">
            <ol class="breadcrumb mb-0">
              <li class="breadcrumb-item"><a href="#">Home</a></li>
              <li class="breadcrumb-item active">{title}</li>
            </ol>
          </nav>
        </div>
        <div>
          {actions if actions else '<button class="btn-pl-primary"><i class="bi bi-download me-1"></i>Export Report</button>'}
        </div>
      </div>
    </div>
    '''
    main_content += body
    main_content += '\n</div>\n'
    
    if js:
        all_scripts += f'\n// --- {role} scripts ---\n'
        all_scripts += js + '\n'

# Get admin scripts from the current demo_content if they are missing
admin_scripts = demo_content[demo_content.find('<script>\n/* Charts */'):demo_content.find('</script>\n</body>')]
admin_scripts = admin_scripts.replace('<script>\n', '')

combined = prefix + main_content + suffix_no_scripts + "<script>\n" + admin_scripts + "\n" + all_scripts + "\n" + script_suffix
with open('demo.html', 'w') as f:
    f.write(combined)

print("Demo generated!")
