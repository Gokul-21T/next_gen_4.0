"""
Generate individual sub-pages for PartLink demo.
Each page shares the same sidebar+navbar layout but has unique content.
"""
import os

# Shared head, sidebar, navbar template
HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title} – PartLink</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"/>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
  <link rel="stylesheet" href="{css_path}"/>
  {extra_css}
</head>
<body>
'''

SIDEBAR_TEMPLATE = '''
<aside class="sidebar" id="sidebar">
  <div class="sidebar-brand">
    <div class="brand-logo"><i class="bi bi-link-45deg"></i></div>
    <div class="brand-text">
      <span class="brand-name">PartLink</span>
      <span class="brand-tagline">B2B Platform</span>
    </div>
    <button class="sidebar-close-btn d-lg-none" id="sidebarClose"><i class="bi bi-x-lg"></i></button>
  </div>
  <div class="role-badge-wrapper px-3 pb-3">
    <div class="role-badge"><i class="bi bi-shield-fill-check me-1"></i>{role_label}</div>
  </div>
  <nav class="sidebar-nav" id="sidebarNav">
    {sidebar_nav}
  </nav>
  <div class="sidebar-bottom">
    <a href="#" class="sidebar-bottom-link"><i class="bi bi-question-circle me-2"></i><span>Help & Support</span></a>
    <a href="#" class="sidebar-bottom-link"><i class="bi bi-book me-2"></i><span>Documentation</span></a>
  </div>
</aside>
<div class="sidebar-overlay" id="sidebarOverlay"></div>
'''

NAVBAR_TEMPLATE = '''
<div class="main-wrapper" id="mainWrapper">
  <nav class="top-navbar" id="topNavbar">
    <button class="sidebar-toggle btn btn-link" id="sidebarToggle"><i class="bi bi-list fs-4"></i></button>
    <div class="navbar-search ms-3">
      <div class="input-group">
        <span class="input-group-text bg-light border-end-0"><i class="bi bi-search text-muted"></i></span>
        <input type="text" class="form-control bg-light border-start-0 ps-0" placeholder="Search parts, suppliers, orders..." autocomplete="off"/>
      </div>
    </div>
    <div class="navbar-right ms-auto d-flex align-items-center gap-3">
      <div class="dropdown">
        <button class="nav-icon-btn position-relative" data-bs-toggle="dropdown">
          <i class="bi bi-bell fs-5"></i><span class="notification-badge pulse">4</span>
        </button>
        <div class="dropdown-menu dropdown-menu-end" style="width:280px;">
          <div class="px-3 py-2 border-bottom"><h6 class="mb-0 fw-semibold">Notifications</h6></div>
          <div class="notif-item unread"><div class="notif-icon bg-primary-soft"><i class="bi bi-file-text text-primary"></i></div><div class="notif-content"><p class="mb-0 fw-medium" style="font-size:13px;">New activity</p><small class="text-muted">2 minutes ago</small></div></div>
        </div>
      </div>
      <div class="vr opacity-25 d-none d-md-block" style="height:28px;"></div>
      <div class="dropdown">
        <button class="user-profile-btn d-flex align-items-center gap-2" data-bs-toggle="dropdown">
          <div class="user-avatar"><span>{initials}</span></div>
          <div class="d-none d-md-block text-start">
            <div class="user-name fw-semibold">{user_name}</div>
            <div class="user-role">{role_label}</div>
          </div>
          <i class="bi bi-chevron-down small ms-1 d-none d-md-block"></i>
        </button>
        <ul class="dropdown-menu dropdown-menu-end">
          <li class="px-3 py-2"><div class="fw-semibold">{user_name}</div><small class="text-muted">{email}</small></li>
          <li><hr class="dropdown-divider"></li>
          <li><a class="dropdown-item" href="#"><i class="bi bi-person me-2"></i>My Profile</a></li>
          <li><a class="dropdown-item" href="#"><i class="bi bi-gear me-2"></i>Settings</a></li>
          <li><hr class="dropdown-divider"></li>
          <li><a class="dropdown-item text-danger" href="#"><i class="bi bi-box-arrow-right me-2"></i>Sign Out</a></li>
        </ul>
      </div>
    </div>
  </nav>
  <main class="content-area">
    <div class="page-header mb-4">
      <div class="d-flex align-items-center justify-content-between">
        <div>
          <h4 class="page-title mb-1">{title}</h4>
          <nav aria-label="breadcrumb"><ol class="breadcrumb mb-0">
            <li class="breadcrumb-item"><a href="{dashboard_link}">Dashboard</a></li>
            <li class="breadcrumb-item active">{title}</li>
          </ol></nav>
        </div>
        <div>{page_actions}</div>
      </div>
    </div>
'''

FOOTER = '''
  </main>
  <footer class="app-footer">
    <span>© 2025 <strong>PartLink</strong> – B2B Industrial Platform.</span>
    <span class="ms-auto">v1.0.0</span>
  </footer>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script src="{js_path}"></script>
{extra_js}
</body>
</html>
'''

# ============================================================
# ROLE DEFINITIONS
# ============================================================
ROLES = {
    'admin': {
        'label': 'Super Admin', 'name': 'Admin User', 'initials': 'AD', 'email': 'admin@partlink.io',
        'nav_sections': [
            ('Main', [
                ('Dashboard', 'bi-speedometer2', '../demo.html', False),
                ('User Management', 'bi-people', 'admin_users.html', False, '12'),
                ('Approvals', 'bi-person-check', 'admin_approvals.html', False, '5!'),
                ('Roles & Permissions', 'bi-shield-lock', 'admin_roles.html', False),
            ]),
            ('Operations', [
                ('All Orders', 'bi-bag-check', 'admin_orders.html', False),
                ('RFQ Overview', 'bi-file-earmark-text', 'admin_rfq.html', False),
                ('Reports & Flags', 'bi-flag', 'admin_reports.html', False, '3!'),
                ('Analytics', 'bi-bar-chart-line', 'admin_analytics.html', False),
                ('Revenue Dashboard', 'bi-cash-coin', 'admin_revenue.html', False),
                ('System Status', 'bi-display', 'admin_system.html', False),
            ]),
            ('System', [
                ('Audit Logs', 'bi-journal-text', 'admin_audit.html', False),
                ('Platform Settings', 'bi-gear', 'admin_settings.html', False),
            ]),
        ]
    },
    'supplier': {
        'label': 'Supplier (MSME)', 'name': 'Anita Sharma', 'initials': 'AS', 'email': 'anita@apexforge.in',
        'nav_sections': [
            ('Inventory', [
                ('Dashboard', 'bi-speedometer2', '../demo.html', False),
                ('Manage Inventory', 'bi-boxes', 'supplier_inventory.html', False),
                ('Add New Part', 'bi-plus-square', 'supplier_add_part.html', False),
                ('Low Stock Alerts', 'bi-exclamation-triangle', 'supplier_low_stock.html', False, '3!'),
            ]),
            ('Quotes & Orders', [
                ('RFQ Inbox', 'bi-inbox', 'supplier_rfq_inbox.html', False, '7!'),
                ('My Quotes', 'bi-send', 'supplier_quotes.html', False),
                ('Active Orders', 'bi-bag-check', 'supplier_orders.html', False),
                ('Order History', 'bi-clock-history', 'supplier_history.html', False),
            ]),
            ('Finance', [
                ('Revenue & Payments', 'bi-currency-rupee', 'supplier_revenue.html', False),
                ('Invoices', 'bi-file-earmark-pdf', 'supplier_invoices.html', False),
                ('My Ratings', 'bi-star', 'supplier_ratings.html', False),
                ('Settings', 'bi-gear', 'supplier_settings.html', False),
            ]),
        ]
    },
    'manufacturer': {
        'label': 'Manufacturer', 'name': 'Vikram Patel', 'initials': 'VP', 'email': 'vikram@tatasteel.com',
        'nav_sections': [
            ('Procurement', [
                ('Dashboard', 'bi-speedometer2', '../demo.html', False),
                ('Search Parts', 'bi-search', 'mfg_search.html', False),
                ('Submit RFQ', 'bi-file-earmark-plus', 'mfg_rfq.html', False),
                ('Compare Quotes', 'bi-receipt', 'mfg_quotes.html', False, '4'),
            ]),
            ('Orders & Delivery', [
                ('My Orders', 'bi-bag-check', 'mfg_orders.html', False),
                ('Track Deliveries', 'bi-truck', 'mfg_tracking.html', False),
                ('Returns & Disputes', 'bi-arrow-return-left', 'mfg_returns.html', False),
            ]),
            ('Intelligence', [
                ('Demand Forecast', 'bi-graph-up-arrow', 'mfg_forecast.html', False),
                ('Supplier Directory', 'bi-building', 'mfg_suppliers.html', False),
                ('Settings', 'bi-gear', 'mfg_settings.html', False),
            ]),
        ]
    },
    'logistics': {
        'label': 'Logistics Provider', 'name': 'Ramesh Singh', 'initials': 'RS', 'email': 'ramesh@nexlog.in',
        'nav_sections': [
            ('Shipments', [
                ('Dashboard', 'bi-speedometer2', '../demo.html', False),
                ('Active Shipments', 'bi-truck', 'log_shipments.html', False, '42'),
                ('Pickup Requests', 'bi-inbox', 'log_pickup.html', False, '15!'),
                ('Delivered', 'bi-check2-all', 'log_delivered.html', False),
            ]),
            ('Operations', [
                ('Live Tracking', 'bi-geo-alt', 'log_tracking.html', False),
                ('Route Planner', 'bi-map', 'log_routes.html', False),
                ('Drivers & Fleet', 'bi-people', 'log_fleet.html', False),
                ('Delays & Issues', 'bi-exclamation-triangle', 'log_delays.html', False, '4!'),
            ]),
            ('Reports', [
                ('Notifications', 'bi-bell', 'log_notifications.html', False),
                ('Performance', 'bi-bar-chart', 'log_performance.html', False),
                ('POD Archive', 'bi-file-earmark-pdf', 'log_pod.html', False),
                ('Settings', 'bi-gear', 'log_settings.html', False),
            ]),
        ]
    },
    'designer': {
        'label': 'Part Designer', 'name': 'Priya Mehta', 'initials': 'PM', 'email': 'priya@metalcraft.com',
        'nav_sections': [
            ('Design Work', [
                ('Dashboard', 'bi-speedometer2', '../demo.html', False),
                ('Upload Files', 'bi-cloud-upload', 'des_upload.html', False),
                ('My Projects', 'bi-folder2-open', 'des_projects.html', False, '12'),
                ('Project Requests', 'bi-clipboard-check', 'des_requests.html', False, '5!'),
            ]),
            ('Collaboration', [
                ('Version History', 'bi-clock-history', 'des_versions.html', False),
                ('Client Chat', 'bi-chat-dots', 'des_chat.html', False, '2'),
                ('Shared Files', 'bi-share', 'des_shared.html', False),
                ('Revision Notes', 'bi-pencil-square', 'des_revisions.html', False),
            ]),
            ('Account', [
                ('My Portfolio', 'bi-person-lines-fill', 'des_portfolio.html', False),
                ('Earnings', 'bi-currency-rupee', 'des_earnings.html', False),
                ('Settings', 'bi-gear', 'des_settings.html', False),
            ]),
        ]
    },
    'distributor': {
        'label': 'Dealer/Distributor', 'name': 'Suresh Verma', 'initials': 'SV', 'email': 'suresh@partsdepot.in',
        'nav_sections': [
            ('Catalog', [
                ('Dashboard', 'bi-speedometer2', '../demo.html', False),
                ('Inventory Upload', 'bi-upload', 'dist_upload.html', False),
                ('My Catalog', 'bi-boxes', 'dist_catalog.html', False, '2840'),
                ('Discount Bundles', 'bi-tags', 'dist_bundles.html', False, '12'),
            ]),
            ('Sales', [
                ('Matching Requests', 'bi-diagram-3', 'dist_matching.html', False, '94!'),
                ('Sales Orders', 'bi-bag-check', 'dist_orders.html', False),
                ('Market Trends', 'bi-graph-up', 'dist_trends.html', False),
                ('Dispatch Queue', 'bi-truck', 'dist_dispatch.html', False),
            ]),
            ('Finance', [
                ('Revenue', 'bi-currency-rupee', 'dist_revenue.html', False),
                ('Invoices', 'bi-file-earmark-pdf', 'dist_invoices.html', False),
                ('Settings', 'bi-gear', 'dist_settings.html', False),
            ]),
        ]
    },
}

# ============================================================
# PAGE CONTENT TEMPLATES
# ============================================================

def make_coming_soon(title, icon, description):
    return f'''
    <div class="pl-card" style="text-align:center;padding:60px 20px;">
      <div style="font-size:64px;color:var(--pl-primary);margin-bottom:16px;"><i class="bi {icon}"></i></div>
      <h3 class="fw-bold mb-2">{title}</h3>
      <p class="text-muted mb-4" style="max-width:500px;margin:0 auto;">{description}</p>
      <a href="../demo.html" class="btn-pl-primary"><i class="bi bi-arrow-left me-2"></i>Back to Dashboard</a>
    </div>'''

def make_table_page(title, icon, columns, rows, action_btn='View'):
    thead = ''.join(f'<th>{c}</th>' for c in columns)
    tbody_rows = ''
    for row in rows:
        cells = ''.join(f'<td>{c}</td>' for c in row)
        tbody_rows += f'<tr>{cells}</tr>\n'
    return f'''
    <div class="pl-table-wrapper">
      <div class="pl-table-toolbar">
        <h6 class="mb-0 fw-bold"><i class="bi {icon} me-2 text-primary"></i>{title}</h6>
        <div class="ms-auto d-flex gap-2">
          <input type="text" class="form-control form-control-sm" placeholder="Search..." style="width:200px;">
          <button class="btn-pl-primary"><i class="bi bi-plus me-1"></i>Add New</button>
        </div>
      </div>
      <div class="table-responsive">
        <table class="pl-table"><thead><tr>{thead}</tr></thead><tbody>{tbody_rows}</tbody></table>
      </div>
      <div class="d-flex align-items-center justify-content-between px-4 py-3 border-top">
        <span style="font-size:13px;color:var(--pl-text-muted);">Showing {len(rows)} items</span>
        <nav><ul class="pagination pagination-sm mb-0">
          <li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>
          <li class="page-item active"><a class="page-link" href="#">1</a></li>
          <li class="page-item"><a class="page-link" href="#">2</a></li>
          <li class="page-item"><a class="page-link" href="#">Next</a></li>
        </ul></nav>
      </div>
    </div>'''

# PAGE DEFINITIONS: { filename: (role, title, content_html, page_actions, extra_js) }
PAGES = {}

# --- ADMIN PAGES ---
PAGES['admin_users.html'] = ('admin', 'User Management', make_table_page('All Users', 'bi-people',
    ['User', 'Email', 'Role', 'Status', 'Joined', 'Actions'],
    [
        ['<div class="user-chip"><div class="avatar-sm">RK</div><span>Rajesh Kumar</span></div>', 'rajesh@forgeind.com', '<span class="status-badge status-approved">Supplier</span>', '<span class="status-badge status-active">Active</span>', '15 Jan 2025', '<button class="btn btn-sm btn-outline-primary"><i class="bi bi-pencil"></i></button>'],
        ['<div class="user-chip"><div class="avatar-sm">PM</div><span>Priya Mehta</span></div>', 'priya@metalcraft.com', '<span class="status-badge status-pending">Designer</span>', '<span class="status-badge status-active">Active</span>', '20 Feb 2025', '<button class="btn btn-sm btn-outline-primary"><i class="bi bi-pencil"></i></button>'],
        ['<div class="user-chip"><div class="avatar-sm">VP</div><span>Vikram Patel</span></div>', 'vikram@tatasteel.com', '<span class="status-badge status-transit">Manufacturer</span>', '<span class="status-badge status-active">Active</span>', '05 Mar 2025', '<button class="btn btn-sm btn-outline-primary"><i class="bi bi-pencil"></i></button>'],
        ['<div class="user-chip"><div class="avatar-sm">AS</div><span>Arvind Shah</span></div>', 'arvind@nexlog.in', '<span class="status-badge status-approved">Logistics</span>', '<span class="status-badge status-pending">Pending</span>', '28 Mar 2025', '<div class="d-flex gap-1"><button class="btn-approve btn-sm"><i class="bi bi-check-lg"></i></button><button class="btn-reject btn-sm"><i class="bi bi-x-lg"></i></button></div>'],
    ]), '<button class="btn-pl-primary"><i class="bi bi-person-plus me-1"></i>Add User</button>', '')

PAGES['admin_approvals.html'] = ('admin', 'Pending Approvals', make_table_page('Pending Approvals', 'bi-person-check',
    ['User', 'Company', 'Role', 'Requested', 'Documents', 'Actions'],
    [
        ['<div class="user-chip"><div class="avatar-sm">RK</div><span>Rajesh Kumar</span></div>', 'Forge Industries Pvt. Ltd.', '<span class="status-badge status-pending">Supplier</span>', '28 Mar 2025', '<a href="#" class="text-primary small">View Docs</a>', '<div class="d-flex gap-2"><button class="btn-approve"><i class="bi bi-check-lg me-1"></i>Approve</button><button class="btn-reject"><i class="bi bi-x-lg me-1"></i>Reject</button></div>'],
        ['<div class="user-chip"><div class="avatar-sm">PM</div><span>Priya Mehta</span></div>', 'Nex Logistics Solutions', '<span class="status-badge status-pending">Logistics</span>', '27 Mar 2025', '<a href="#" class="text-primary small">View Docs</a>', '<div class="d-flex gap-2"><button class="btn-approve"><i class="bi bi-check-lg me-1"></i>Approve</button><button class="btn-reject"><i class="bi bi-x-lg me-1"></i>Reject</button></div>'],
        ['<div class="user-chip"><div class="avatar-sm">AS</div><span>Arvind Shah</span></div>', 'MetalCraft Design Studio', '<span class="status-badge status-pending">Designer</span>', '26 Mar 2025', '<a href="#" class="text-primary small">View Docs</a>', '<div class="d-flex gap-2"><button class="btn-approve"><i class="bi bi-check-lg me-1"></i>Approve</button><button class="btn-reject"><i class="bi bi-x-lg me-1"></i>Reject</button></div>'],
    ]), '', '')

for fname, title, icon, desc in [
    ('admin_roles.html', 'Roles & Permissions', 'bi-shield-lock', 'Configure role-based access control. Define permissions for Admin, Manufacturer, Supplier, Logistics, Designer, and Distributor roles.'),
    ('admin_orders.html', 'All Orders', 'bi-bag-check', 'View and manage all orders across the platform. Filter by status, date range, or parties involved.'),
    ('admin_rfq.html', 'RFQ Overview', 'bi-file-earmark-text', 'Monitor all Request for Quotations across the platform. Track submission, response rates, and conversion metrics.'),
    ('admin_reports.html', 'Reports & Flags', 'bi-flag', 'Review flagged content, user reports, and compliance issues. Take moderation actions on reported items.'),
    ('admin_analytics.html', 'Analytics', 'bi-bar-chart-line', 'Platform-wide analytics including user growth, order trends, revenue metrics, and engagement data.'),
    ('admin_revenue.html', 'Revenue Dashboard', 'bi-cash-coin', 'Track platform commissions, transaction fees, and subscription revenue. View financial forecasts.'),
    ('admin_system.html', 'System Status', 'bi-display', 'Monitor server health, API performance, database load, and third-party service integrations.'),
    ('admin_audit.html', 'Audit Logs', 'bi-journal-text', 'Complete audit trail of all user actions, login events, data changes, and administrative operations.'),
    ('admin_settings.html', 'Platform Settings', 'bi-gear', 'Configure global platform settings including business rules, notifications, integrations, and appearance.'),
]:
    PAGES[fname] = ('admin', title, make_coming_soon(title, icon, desc), '', '')

# --- SUPPLIER PAGES ---
PAGES['supplier_inventory.html'] = ('supplier', 'Manage Inventory', make_table_page('Inventory', 'bi-boxes',
    ['SKU', 'Part Name', 'Category', 'Stock', 'Unit Price', 'Status', 'Actions'],
    [
        ['<code>PL-1082</code>', 'Steel Bolt M12', 'Fasteners', '12,400 pcs', '₹27.50', '<span class="status-badge status-active">In Stock</span>', '<button class="btn btn-sm btn-outline-primary"><i class="bi bi-pencil"></i> Edit</button>'],
        ['<code>PL-1091</code>', 'Aluminium Sheet 2mm', 'Sheet Metal', '340 sheets', '₹145.00', '<span class="status-badge status-active">In Stock</span>', '<button class="btn btn-sm btn-outline-primary"><i class="bi bi-pencil"></i> Edit</button>'],
        ['<code>PL-1104</code>', 'Hex Nut M10', 'Fasteners', '8,200 pcs', '₹12.00', '<span class="status-badge status-active">In Stock</span>', '<button class="btn btn-sm btn-outline-primary"><i class="bi bi-pencil"></i> Edit</button>'],
        ['<code>PL-1125</code>', 'Rubber O-Ring 50mm', 'Seals', '<span class="text-danger fw-bold">120 pcs</span>', '₹8.75', '<span class="status-badge status-rejected">Low Stock</span>', '<button class="btn btn-sm btn-outline-warning"><i class="bi bi-arrow-repeat"></i> Reorder</button>'],
        ['<code>PL-1133</code>', 'Spring Washer M8', 'Fasteners', '5,600 pcs', '₹6.50', '<span class="status-badge status-active">In Stock</span>', '<button class="btn btn-sm btn-outline-primary"><i class="bi bi-pencil"></i> Edit</button>'],
    ]), '<button class="btn-pl-primary"><i class="bi bi-plus me-1"></i>Add Part</button>', '')

PAGES['supplier_rfq_inbox.html'] = ('supplier', 'RFQ Inbox', make_table_page('Incoming RFQs', 'bi-inbox',
    ['RFQ ID', 'Buyer', 'Part Required', 'Quantity', 'Budget', 'Deadline', 'Status', 'Action'],
    [
        ['<code>#RFQ-892</code>', '<div class="user-chip"><div class="avatar-sm">HM</div><span>Hero MotoCorp</span></div>', 'Steel Bolt M12', '3,000 pcs', '₹30/unit', '05 Apr 2025', '<span class="status-badge status-pending">New</span>', '<button class="btn-approve"><i class="bi bi-send me-1"></i>Quote</button>'],
        ['<code>#RFQ-887</code>', '<div class="user-chip"><div class="avatar-sm">TV</div><span>TVS Motors</span></div>', 'O-Ring 50mm', '8,000 pcs', '₹9/unit', '08 Apr 2025', '<span class="status-badge status-pending">New</span>', '<button class="btn-approve"><i class="bi bi-send me-1"></i>Quote</button>'],
        ['<code>#RFQ-881</code>', '<div class="user-chip"><div class="avatar-sm">MH</div><span>Mahindra</span></div>', 'Spring Washer M8', '12,000 pcs', '₹7/unit', '10 Apr 2025', '<span class="status-badge status-transit">Quoted</span>', '<button class="btn btn-sm btn-outline-secondary">View</button>'],
        ['<code>#RFQ-876</code>', '<div class="user-chip"><div class="avatar-sm">AL</div><span>Ashok Leyland</span></div>', 'Al Sheet 2mm', '500 sheets', '₹160/pc', '03 Apr 2025', '<span class="status-badge status-approved">Won</span>', '<button class="btn btn-sm btn-outline-success">Process</button>'],
    ]), '', '')

for fname, title, icon, desc in [
    ('supplier_add_part.html', 'Add New Part', 'bi-plus-square', 'Add a new part to your inventory catalog. Specify SKU, category, pricing, stock levels, and technical specifications.'),
    ('supplier_low_stock.html', 'Low Stock Alerts', 'bi-exclamation-triangle', 'Parts that have fallen below their reorder threshold. Review and replenish stock to avoid missed opportunities.'),
    ('supplier_quotes.html', 'My Quotes', 'bi-send', 'Track all quotes you have submitted. Monitor acceptance rates, pending responses, and expired quotes.'),
    ('supplier_orders.html', 'Active Orders', 'bi-bag-check', 'Manage orders currently being processed. Update statuses, coordinate shipping, and communicate with buyers.'),
    ('supplier_history.html', 'Order History', 'bi-clock-history', 'Complete history of all past orders. Download invoices, view ratings received, and analyze patterns.'),
    ('supplier_revenue.html', 'Revenue & Payments', 'bi-currency-rupee', 'Track your earnings, pending payments, and payment history. Download statements and manage bank details.'),
    ('supplier_invoices.html', 'Invoices', 'bi-file-earmark-pdf', 'Generate, download, and manage invoices for all completed orders. Auto-generate GST-compliant invoices.'),
    ('supplier_ratings.html', 'My Ratings', 'bi-star', 'View ratings and reviews from buyers. Track your overall quality score and delivery performance metrics.'),
    ('supplier_settings.html', 'Settings', 'bi-gear', 'Manage your company profile, notification preferences, banking details, and account security settings.'),
]:
    PAGES[fname] = ('supplier', title, make_coming_soon(title, icon, desc), '', '')

# --- MANUFACTURER PAGES ---
for fname, title, icon, desc in [
    ('mfg_search.html', 'Search Parts', 'bi-search', 'Search across thousands of industrial parts from verified suppliers. Filter by category, material, size, and price range.'),
    ('mfg_rfq.html', 'Submit RFQ', 'bi-file-earmark-plus', 'Create a new Request for Quotation. Specify part requirements, quantities, deadlines, and preferred suppliers.'),
    ('mfg_quotes.html', 'Compare Quotes', 'bi-receipt', 'Compare responses from multiple suppliers side-by-side. Analyze pricing, lead times, and supplier ratings.'),
    ('mfg_orders.html', 'My Orders', 'bi-bag-check', 'Track all your active and past orders. Monitor delivery status, quality inspections, and payment schedules.'),
    ('mfg_tracking.html', 'Track Deliveries', 'bi-truck', 'Real-time delivery tracking for all active shipments. View route progress, ETAs, and driver information.'),
    ('mfg_returns.html', 'Returns & Disputes', 'bi-arrow-return-left', 'Manage returns, quality complaints, and disputes with suppliers. Track resolution status and outcomes.'),
    ('mfg_forecast.html', 'Demand Forecast', 'bi-graph-up-arrow', 'AI-powered demand predictions based on historical data. Plan procurement and inventory accordingly.'),
    ('mfg_suppliers.html', 'Supplier Directory', 'bi-building', 'Browse verified suppliers by category, location, and capability. View profiles, certifications, and ratings.'),
    ('mfg_settings.html', 'Settings', 'bi-gear', 'Manage your company profile, procurement preferences, and notification settings.'),
]:
    PAGES[fname] = ('manufacturer', title, make_coming_soon(title, icon, desc), '', '')

# --- LOGISTICS PAGES ---
for fname, title, icon, desc in [
    ('log_shipments.html', 'Active Shipments', 'bi-truck', 'All currently active shipments. View pickup locations, drop points, weights, and estimated delivery times.'),
    ('log_pickup.html', 'Pickup Requests', 'bi-inbox', 'New pickup requests awaiting your acceptance. Review shipment details and accept or decline jobs.'),
    ('log_delivered.html', 'Delivered', 'bi-check2-all', 'Successfully delivered shipments. Download Proof of Delivery documents and view delivery confirmations.'),
    ('log_tracking.html', 'Live Tracking', 'bi-geo-alt', 'Real-time GPS tracking for all active fleet vehicles. Monitor routes, checkpoints, and driver status.'),
    ('log_routes.html', 'Route Planner', 'bi-map', 'Plan optimal routes for multi-stop deliveries. Consider traffic, weather, and toll data for efficient logistics.'),
    ('log_fleet.html', 'Drivers & Fleet', 'bi-people', 'Manage your driver team and vehicle fleet. Track availability, maintenance schedules, and certifications.'),
    ('log_delays.html', 'Delays & Issues', 'bi-exclamation-triangle', 'Monitor delayed shipments and reported issues. Take corrective action and communicate with stakeholders.'),
    ('log_notifications.html', 'Notifications', 'bi-bell', 'All notifications including weather alerts, route changes, pickup requests, and delivery confirmations.'),
    ('log_performance.html', 'Performance', 'bi-bar-chart', 'Delivery performance metrics including on-time rate, average delivery time, and customer satisfaction scores.'),
    ('log_pod.html', 'POD Archive', 'bi-file-earmark-pdf', 'Archive of all Proof of Delivery documents. Search, download, and share delivery confirmations.'),
    ('log_settings.html', 'Settings', 'bi-gear', 'Configure fleet management preferences, notification settings, and company profile details.'),
]:
    PAGES[fname] = ('logistics', title, make_coming_soon(title, icon, desc), '', '')

# --- DESIGNER PAGES ---
for fname, title, icon, desc in [
    ('des_upload.html', 'Upload Files', 'bi-cloud-upload', 'Upload CAD files (DWG, DXF, STEP, STL, IGES, PDF) to your projects. Attach version notes and assign to clients.'),
    ('des_projects.html', 'My Projects', 'bi-folder2-open', 'View and manage all your active and completed design projects. Track progress, deadlines, and client feedback.'),
    ('des_requests.html', 'Project Requests', 'bi-clipboard-check', 'Incoming design project requests from manufacturers and clients. Review requirements and accept assignments.'),
    ('des_versions.html', 'Version History', 'bi-clock-history', 'Complete version history of all uploaded design files. Compare versions, restore previous iterations, and track changes.'),
    ('des_chat.html', 'Client Chat', 'bi-chat-dots', 'Communicate with clients about project requirements, revisions, and approvals. Share files and discuss designs.'),
    ('des_shared.html', 'Shared Files', 'bi-share', 'Files shared with you by clients and collaborators. Download specs, reference documents, and design guidelines.'),
    ('des_revisions.html', 'Revision Notes', 'bi-pencil-square', 'Track revision requests, change notes, and client feedback on each design iteration.'),
    ('des_portfolio.html', 'My Portfolio', 'bi-person-lines-fill', 'Showcase your best design work. Manage portfolio items that are visible to potential clients on the platform.'),
    ('des_earnings.html', 'Earnings', 'bi-currency-rupee', 'Track your project earnings, pending payments, and payment history. Request withdrawals and manage payouts.'),
    ('des_settings.html', 'Settings', 'bi-gear', 'Manage your designer profile, specializations, availability, and notification preferences.'),
]:
    PAGES[fname] = ('designer', title, make_coming_soon(title, icon, desc), '', '')

# --- DISTRIBUTOR PAGES ---
for fname, title, icon, desc in [
    ('dist_upload.html', 'Inventory Upload', 'bi-upload', 'Bulk upload your inventory catalog via CSV or Excel. Map columns and process thousands of SKUs at once.'),
    ('dist_catalog.html', 'My Catalog', 'bi-boxes', 'Manage your complete product catalog. Edit prices, update stock levels, and organize by categories.'),
    ('dist_bundles.html', 'Discount Bundles', 'bi-tags', 'Create and manage discount bundle offers. Set expiry dates, minimum quantities, and promotional pricing.'),
    ('dist_matching.html', 'Matching Requests', 'bi-diagram-3', 'AI-matched buyer requests that fit your catalog. View match scores and send competitive offers.'),
    ('dist_orders.html', 'Sales Orders', 'bi-bag-check', 'Manage incoming sales orders. Process, pack, and coordinate dispatch with logistics partners.'),
    ('dist_trends.html', 'Market Trends', 'bi-graph-up', 'Market demand analytics and pricing trends. Identify growing categories and optimize your catalog.'),
    ('dist_dispatch.html', 'Dispatch Queue', 'bi-truck', 'Orders ready for dispatch. Assign logistics partners, generate shipping labels, and track handoffs.'),
    ('dist_revenue.html', 'Revenue', 'bi-currency-rupee', 'Track your sales revenue, margins, and payment collections. View financial summaries and forecasts.'),
    ('dist_invoices.html', 'Invoices', 'bi-file-earmark-pdf', 'Generate and manage sales invoices. Auto-generate GST-compliant documents for all transactions.'),
    ('dist_settings.html', 'Settings', 'bi-gear', 'Configure distribution preferences, warehouse details, pricing rules, and account settings.'),
]:
    PAGES[fname] = ('distributor', title, make_coming_soon(title, icon, desc), '', '')


# ============================================================
# GENERATION
# ============================================================
def build_sidebar_nav(role_key, active_page):
    role = ROLES[role_key]
    html = ''
    for section_title, items in role['nav_sections']:
        html += f'<div class="nav-section-title">{section_title}</div>\n<ul class="nav-list">\n'
        for item in items:
            label, icon, href, *rest = item
            badge = ''
            if len(rest) > 1 and rest[1]:
                b = rest[1]
                if b.endswith('!'):
                    badge = f'<span class="nav-badge urgent">{b[:-1]}</span>'
                else:
                    badge = f'<span class="nav-badge">{b}</span>'
            is_active = 'active' if href == active_page else ''
            html += f'  <li class="nav-item"><a href="{href}" class="nav-link {is_active}"><span class="nav-icon"><i class="bi {icon}"></i></span><span class="nav-label">{label}</span>{badge}</a></li>\n'
        html += '</ul>\n'
    return html

def generate_page(filename, role_key, title, content, page_actions='', extra_js=''):
    role = ROLES[role_key]
    sidebar_nav = build_sidebar_nav(role_key, filename)
    
    page = HEAD.format(title=title, css_path='../static/css/partlink.css', extra_css='')
    page += SIDEBAR_TEMPLATE.format(role_label=role['label'], sidebar_nav=sidebar_nav)
    page += NAVBAR_TEMPLATE.format(
        title=title, initials=role['initials'], user_name=role['name'],
        role_label=role['label'], email=role['email'],
        dashboard_link='../demo.html', page_actions=page_actions
    )
    page += content
    page += FOOTER.format(js_path='../static/js/partlink.js', extra_js=extra_js)
    return page

# Create pages directory
os.makedirs('pages', exist_ok=True)

count = 0
for filename, (role_key, title, content, page_actions, extra_js) in PAGES.items():
    html = generate_page(filename, role_key, title, content, page_actions, extra_js)
    with open(f'pages/{filename}', 'w') as f:
        f.write(html)
    count += 1

print(f"✅ Generated {count} pages in pages/ directory!")
