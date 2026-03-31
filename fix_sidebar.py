"""Fix the sidebar nav in demo.html with proper page links."""

with open('demo.html', 'r') as f:
    content = f.read()

sidebar_start = content.find('<nav class="sidebar-nav"')
sidebar_end = content.find('</nav>', sidebar_start) + len('</nav>')

new_sidebar = '''<nav class="sidebar-nav" id="sidebarNav">
    <!-- ===== ADMIN ===== -->
    <div class="nav-section" data-role="admin">
      <div class="nav-section-title">Main</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="#" class="nav-link active"><span class="nav-icon"><i class="bi bi-speedometer2"></i></span><span class="nav-label">Dashboard</span></a></li>
        <li class="nav-item"><a href="pages/admin_users.html" class="nav-link"><span class="nav-icon"><i class="bi bi-people"></i></span><span class="nav-label">User Management</span><span class="nav-badge">12</span></a></li>
        <li class="nav-item"><a href="pages/admin_approvals.html" class="nav-link"><span class="nav-icon"><i class="bi bi-person-check"></i></span><span class="nav-label">Approvals</span><span class="nav-badge urgent">5</span></a></li>
        <li class="nav-item"><a href="pages/admin_roles.html" class="nav-link"><span class="nav-icon"><i class="bi bi-shield-lock"></i></span><span class="nav-label">Roles &amp; Permissions</span></a></li>
      </ul>
      <div class="nav-section-title">Operations</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="pages/admin_orders.html" class="nav-link"><span class="nav-icon"><i class="bi bi-bag-check"></i></span><span class="nav-label">All Orders</span></a></li>
        <li class="nav-item"><a href="pages/admin_rfq.html" class="nav-link"><span class="nav-icon"><i class="bi bi-file-earmark-text"></i></span><span class="nav-label">RFQ Overview</span></a></li>
        <li class="nav-item"><a href="pages/admin_reports.html" class="nav-link"><span class="nav-icon"><i class="bi bi-flag"></i></span><span class="nav-label">Reports &amp; Flags</span><span class="nav-badge urgent">3</span></a></li>
        <li class="nav-item"><a href="pages/admin_analytics.html" class="nav-link"><span class="nav-icon"><i class="bi bi-bar-chart-line"></i></span><span class="nav-label">Analytics</span></a></li>
        <li class="nav-item"><a href="pages/admin_revenue.html" class="nav-link"><span class="nav-icon"><i class="bi bi-cash-coin"></i></span><span class="nav-label">Revenue Dashboard</span></a></li>
        <li class="nav-item"><a href="pages/admin_system.html" class="nav-link"><span class="nav-icon"><i class="bi bi-display"></i></span><span class="nav-label">System Status</span></a></li>
      </ul>
      <div class="nav-section-title">System</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="pages/admin_audit.html" class="nav-link"><span class="nav-icon"><i class="bi bi-journal-text"></i></span><span class="nav-label">Audit Logs</span></a></li>
        <li class="nav-item"><a href="pages/admin_settings.html" class="nav-link"><span class="nav-icon"><i class="bi bi-gear"></i></span><span class="nav-label">Platform Settings</span></a></li>
      </ul>
    </div>
    <!-- ===== MANUFACTURER ===== -->
    <div class="nav-section d-none" data-role="manufacturer">
      <div class="nav-section-title">Procurement</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="#" class="nav-link active"><span class="nav-icon"><i class="bi bi-speedometer2"></i></span><span class="nav-label">Dashboard</span></a></li>
        <li class="nav-item"><a href="pages/mfg_search.html" class="nav-link"><span class="nav-icon"><i class="bi bi-search"></i></span><span class="nav-label">Search Parts</span></a></li>
        <li class="nav-item"><a href="pages/mfg_rfq.html" class="nav-link"><span class="nav-icon"><i class="bi bi-file-earmark-plus"></i></span><span class="nav-label">Submit RFQ</span></a></li>
        <li class="nav-item"><a href="pages/mfg_quotes.html" class="nav-link"><span class="nav-icon"><i class="bi bi-receipt"></i></span><span class="nav-label">Compare Quotes</span><span class="nav-badge">4</span></a></li>
      </ul>
      <div class="nav-section-title">Orders &amp; Delivery</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="pages/mfg_orders.html" class="nav-link"><span class="nav-icon"><i class="bi bi-bag-check"></i></span><span class="nav-label">My Orders</span></a></li>
        <li class="nav-item"><a href="pages/mfg_tracking.html" class="nav-link"><span class="nav-icon"><i class="bi bi-truck"></i></span><span class="nav-label">Track Deliveries</span></a></li>
        <li class="nav-item"><a href="pages/mfg_returns.html" class="nav-link"><span class="nav-icon"><i class="bi bi-arrow-return-left"></i></span><span class="nav-label">Returns &amp; Disputes</span></a></li>
      </ul>
      <div class="nav-section-title">Intelligence</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="pages/mfg_forecast.html" class="nav-link"><span class="nav-icon"><i class="bi bi-graph-up-arrow"></i></span><span class="nav-label">Demand Forecast</span></a></li>
        <li class="nav-item"><a href="pages/mfg_suppliers.html" class="nav-link"><span class="nav-icon"><i class="bi bi-building"></i></span><span class="nav-label">Supplier Directory</span></a></li>
        <li class="nav-item"><a href="pages/mfg_settings.html" class="nav-link"><span class="nav-icon"><i class="bi bi-gear"></i></span><span class="nav-label">Settings</span></a></li>
      </ul>
    </div>
    <!-- ===== SUPPLIER ===== -->
    <div class="nav-section d-none" data-role="supplier">
      <div class="nav-section-title">Inventory</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="#" class="nav-link active"><span class="nav-icon"><i class="bi bi-speedometer2"></i></span><span class="nav-label">Dashboard</span></a></li>
        <li class="nav-item"><a href="pages/supplier_inventory.html" class="nav-link"><span class="nav-icon"><i class="bi bi-boxes"></i></span><span class="nav-label">Manage Inventory</span></a></li>
        <li class="nav-item"><a href="pages/supplier_add_part.html" class="nav-link"><span class="nav-icon"><i class="bi bi-plus-square"></i></span><span class="nav-label">Add New Part</span></a></li>
        <li class="nav-item"><a href="pages/supplier_low_stock.html" class="nav-link"><span class="nav-icon"><i class="bi bi-exclamation-triangle"></i></span><span class="nav-label">Low Stock Alerts</span><span class="nav-badge urgent">3</span></a></li>
      </ul>
      <div class="nav-section-title">Quotes &amp; Orders</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="pages/supplier_rfq_inbox.html" class="nav-link"><span class="nav-icon"><i class="bi bi-inbox"></i></span><span class="nav-label">RFQ Inbox</span><span class="nav-badge urgent">7</span></a></li>
        <li class="nav-item"><a href="pages/supplier_quotes.html" class="nav-link"><span class="nav-icon"><i class="bi bi-send"></i></span><span class="nav-label">My Quotes</span></a></li>
        <li class="nav-item"><a href="pages/supplier_orders.html" class="nav-link"><span class="nav-icon"><i class="bi bi-bag-check"></i></span><span class="nav-label">Active Orders</span></a></li>
        <li class="nav-item"><a href="pages/supplier_history.html" class="nav-link"><span class="nav-icon"><i class="bi bi-clock-history"></i></span><span class="nav-label">Order History</span></a></li>
      </ul>
      <div class="nav-section-title">Finance</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="pages/supplier_revenue.html" class="nav-link"><span class="nav-icon"><i class="bi bi-currency-rupee"></i></span><span class="nav-label">Revenue &amp; Payments</span></a></li>
        <li class="nav-item"><a href="pages/supplier_invoices.html" class="nav-link"><span class="nav-icon"><i class="bi bi-file-earmark-pdf"></i></span><span class="nav-label">Invoices</span></a></li>
        <li class="nav-item"><a href="pages/supplier_ratings.html" class="nav-link"><span class="nav-icon"><i class="bi bi-star"></i></span><span class="nav-label">My Ratings</span></a></li>
        <li class="nav-item"><a href="pages/supplier_settings.html" class="nav-link"><span class="nav-icon"><i class="bi bi-gear"></i></span><span class="nav-label">Settings</span></a></li>
      </ul>
    </div>
    <!-- ===== LOGISTICS ===== -->
    <div class="nav-section d-none" data-role="logistics">
      <div class="nav-section-title">Shipments</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="#" class="nav-link active"><span class="nav-icon"><i class="bi bi-speedometer2"></i></span><span class="nav-label">Dashboard</span></a></li>
        <li class="nav-item"><a href="pages/log_shipments.html" class="nav-link"><span class="nav-icon"><i class="bi bi-truck"></i></span><span class="nav-label">Active Shipments</span><span class="nav-badge">42</span></a></li>
        <li class="nav-item"><a href="pages/log_pickup.html" class="nav-link"><span class="nav-icon"><i class="bi bi-inbox"></i></span><span class="nav-label">Pickup Requests</span><span class="nav-badge urgent">15</span></a></li>
        <li class="nav-item"><a href="pages/log_delivered.html" class="nav-link"><span class="nav-icon"><i class="bi bi-check2-all"></i></span><span class="nav-label">Delivered</span></a></li>
      </ul>
      <div class="nav-section-title">Operations</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="pages/log_tracking.html" class="nav-link"><span class="nav-icon"><i class="bi bi-geo-alt"></i></span><span class="nav-label">Live Tracking</span></a></li>
        <li class="nav-item"><a href="pages/log_routes.html" class="nav-link"><span class="nav-icon"><i class="bi bi-map"></i></span><span class="nav-label">Route Planner</span></a></li>
        <li class="nav-item"><a href="pages/log_fleet.html" class="nav-link"><span class="nav-icon"><i class="bi bi-people"></i></span><span class="nav-label">Drivers &amp; Fleet</span></a></li>
        <li class="nav-item"><a href="pages/log_delays.html" class="nav-link"><span class="nav-icon"><i class="bi bi-exclamation-triangle"></i></span><span class="nav-label">Delays &amp; Issues</span><span class="nav-badge urgent">4</span></a></li>
      </ul>
      <div class="nav-section-title">Reports</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="pages/log_notifications.html" class="nav-link"><span class="nav-icon"><i class="bi bi-bell"></i></span><span class="nav-label">Notifications</span></a></li>
        <li class="nav-item"><a href="pages/log_performance.html" class="nav-link"><span class="nav-icon"><i class="bi bi-bar-chart"></i></span><span class="nav-label">Performance</span></a></li>
        <li class="nav-item"><a href="pages/log_pod.html" class="nav-link"><span class="nav-icon"><i class="bi bi-file-earmark-pdf"></i></span><span class="nav-label">POD Archive</span></a></li>
        <li class="nav-item"><a href="pages/log_settings.html" class="nav-link"><span class="nav-icon"><i class="bi bi-gear"></i></span><span class="nav-label">Settings</span></a></li>
      </ul>
    </div>
    <!-- ===== DESIGNER ===== -->
    <div class="nav-section d-none" data-role="designer">
      <div class="nav-section-title">Design Work</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="#" class="nav-link active"><span class="nav-icon"><i class="bi bi-speedometer2"></i></span><span class="nav-label">Dashboard</span></a></li>
        <li class="nav-item"><a href="pages/des_upload.html" class="nav-link"><span class="nav-icon"><i class="bi bi-cloud-upload"></i></span><span class="nav-label">Upload Files</span></a></li>
        <li class="nav-item"><a href="pages/des_projects.html" class="nav-link"><span class="nav-icon"><i class="bi bi-folder2-open"></i></span><span class="nav-label">My Projects</span><span class="nav-badge">12</span></a></li>
        <li class="nav-item"><a href="pages/des_requests.html" class="nav-link"><span class="nav-icon"><i class="bi bi-clipboard-check"></i></span><span class="nav-label">Project Requests</span><span class="nav-badge urgent">5</span></a></li>
      </ul>
      <div class="nav-section-title">Collaboration</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="pages/des_versions.html" class="nav-link"><span class="nav-icon"><i class="bi bi-clock-history"></i></span><span class="nav-label">Version History</span></a></li>
        <li class="nav-item"><a href="pages/des_chat.html" class="nav-link"><span class="nav-icon"><i class="bi bi-chat-dots"></i></span><span class="nav-label">Client Chat</span><span class="nav-badge bg-success">2</span></a></li>
        <li class="nav-item"><a href="pages/des_shared.html" class="nav-link"><span class="nav-icon"><i class="bi bi-share"></i></span><span class="nav-label">Shared Files</span></a></li>
        <li class="nav-item"><a href="pages/des_revisions.html" class="nav-link"><span class="nav-icon"><i class="bi bi-pencil-square"></i></span><span class="nav-label">Revision Notes</span></a></li>
      </ul>
      <div class="nav-section-title">Account</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="pages/des_portfolio.html" class="nav-link"><span class="nav-icon"><i class="bi bi-person-lines-fill"></i></span><span class="nav-label">My Portfolio</span></a></li>
        <li class="nav-item"><a href="pages/des_earnings.html" class="nav-link"><span class="nav-icon"><i class="bi bi-currency-rupee"></i></span><span class="nav-label">Earnings</span></a></li>
        <li class="nav-item"><a href="pages/des_settings.html" class="nav-link"><span class="nav-icon"><i class="bi bi-gear"></i></span><span class="nav-label">Settings</span></a></li>
      </ul>
    </div>
    <!-- ===== DISTRIBUTOR ===== -->
    <div class="nav-section d-none" data-role="distributor">
      <div class="nav-section-title">Catalog</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="#" class="nav-link active"><span class="nav-icon"><i class="bi bi-speedometer2"></i></span><span class="nav-label">Dashboard</span></a></li>
        <li class="nav-item"><a href="pages/dist_upload.html" class="nav-link"><span class="nav-icon"><i class="bi bi-upload"></i></span><span class="nav-label">Inventory Upload</span></a></li>
        <li class="nav-item"><a href="pages/dist_catalog.html" class="nav-link"><span class="nav-icon"><i class="bi bi-boxes"></i></span><span class="nav-label">My Catalog</span><span class="nav-badge">2,840</span></a></li>
        <li class="nav-item"><a href="pages/dist_bundles.html" class="nav-link"><span class="nav-icon"><i class="bi bi-tags"></i></span><span class="nav-label">Discount Bundles</span><span class="nav-badge">12</span></a></li>
      </ul>
      <div class="nav-section-title">Sales</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="pages/dist_matching.html" class="nav-link"><span class="nav-icon"><i class="bi bi-diagram-3"></i></span><span class="nav-label">Matching Requests</span><span class="nav-badge urgent">94</span></a></li>
        <li class="nav-item"><a href="pages/dist_orders.html" class="nav-link"><span class="nav-icon"><i class="bi bi-bag-check"></i></span><span class="nav-label">Sales Orders</span></a></li>
        <li class="nav-item"><a href="pages/dist_trends.html" class="nav-link"><span class="nav-icon"><i class="bi bi-graph-up"></i></span><span class="nav-label">Market Trends</span></a></li>
        <li class="nav-item"><a href="pages/dist_dispatch.html" class="nav-link"><span class="nav-icon"><i class="bi bi-truck"></i></span><span class="nav-label">Dispatch Queue</span></a></li>
      </ul>
      <div class="nav-section-title">Finance</div>
      <ul class="nav-list">
        <li class="nav-item"><a href="pages/dist_revenue.html" class="nav-link"><span class="nav-icon"><i class="bi bi-currency-rupee"></i></span><span class="nav-label">Revenue</span></a></li>
        <li class="nav-item"><a href="pages/dist_invoices.html" class="nav-link"><span class="nav-icon"><i class="bi bi-file-earmark-pdf"></i></span><span class="nav-label">Invoices</span></a></li>
        <li class="nav-item"><a href="pages/dist_settings.html" class="nav-link"><span class="nav-icon"><i class="bi bi-gear"></i></span><span class="nav-label">Settings</span></a></li>
      </ul>
    </div>
  </nav>'''

content = content[:sidebar_start] + new_sidebar + content[sidebar_end:]

with open('demo.html', 'w') as f:
    f.write(content)

print("Done! Sidebar links fixed.")
