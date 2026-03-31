/**
 * PartLink – Global JavaScript
 * Handles: sidebar toggle, search, table sorting, charts init helpers
 */

document.addEventListener('DOMContentLoaded', function () {

  /* =====================================================
     1. SIDEBAR TOGGLE (Desktop Collapse + Mobile Drawer)
  ===================================================== */
  const sidebar       = document.getElementById('sidebar');
  const mainWrapper   = document.getElementById('mainWrapper');
  const sidebarToggle = document.getElementById('sidebarToggle');
  const sidebarClose  = document.getElementById('sidebarClose');
  const overlay       = document.getElementById('sidebarOverlay');

  function isMobile() { return window.innerWidth < 992; }

  if (sidebarToggle) {
    sidebarToggle.addEventListener('click', function () {
      if (isMobile()) {
        sidebar.classList.toggle('mobile-open');
        overlay.classList.toggle('visible');
      } else {
        sidebar.classList.toggle('collapsed');
        mainWrapper.classList.toggle('sidebar-collapsed');
        // Save preference
        localStorage.setItem('pl-sidebar', sidebar.classList.contains('collapsed') ? 'collapsed' : 'open');
      }
    });
  }

  if (sidebarClose) {
    sidebarClose.addEventListener('click', function () {
      sidebar.classList.remove('mobile-open');
      overlay.classList.remove('visible');
    });
  }
  if (overlay) {
    overlay.addEventListener('click', function () {
      sidebar.classList.remove('mobile-open');
      overlay.classList.remove('visible');
    });
  }

  // Restore sidebar state on desktop
  if (!isMobile() && localStorage.getItem('pl-sidebar') === 'collapsed') {
    sidebar.classList.add('collapsed');
    mainWrapper.classList.add('sidebar-collapsed');
  }

  /* =====================================================
     2. ACTIVE NAV LINK (highlight current page)
  ===================================================== */
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-link').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });

  /* =====================================================
     3. GLOBAL SEARCH – Show/hide suggestions
  ===================================================== */
  const searchInput       = document.getElementById('globalSearch');
  const searchSuggestions = document.getElementById('searchSuggestions');

  if (searchInput && searchSuggestions) {
    searchInput.addEventListener('focus', function () {
      if (this.value.length >= 0) searchSuggestions.style.display = 'block';
    });
    searchInput.addEventListener('input', function () {
      searchSuggestions.style.display = this.value.length >= 0 ? 'block' : 'none';
    });
    document.addEventListener('click', function (e) {
      if (!searchInput.contains(e.target) && !searchSuggestions.contains(e.target)) {
        searchSuggestions.style.display = 'none';
      }
    });
  }

  /* =====================================================
     4. TABLE SORTING (click column headers)
  ===================================================== */
  document.querySelectorAll('.pl-table').forEach(table => {
    const headers = table.querySelectorAll('thead th[data-sort]');
    headers.forEach(th => {
      th.addEventListener('click', function () {
        const col    = this.dataset.sort;
        const tbody  = table.querySelector('tbody');
        const rows   = Array.from(tbody.querySelectorAll('tr'));
        const colIdx = Array.from(this.parentElement.children).indexOf(this);
        const asc    = this.dataset.dir !== 'asc';

        rows.sort((a, b) => {
          const A = a.children[colIdx]?.textContent.trim() || '';
          const B = b.children[colIdx]?.textContent.trim() || '';
          return asc ? A.localeCompare(B, undefined, { numeric: true })
                     : B.localeCompare(A, undefined, { numeric: true });
        });
        rows.forEach(r => tbody.appendChild(r));
        headers.forEach(h => { h.removeAttribute('data-dir'); h.classList.remove('sorted'); });
        this.dataset.dir = asc ? 'asc' : 'desc';
        this.classList.add('sorted');
      });
    });
  });

  /* =====================================================
     5. TABLE SEARCH / FILTER
  ===================================================== */
  document.querySelectorAll('[data-table-search]').forEach(input => {
    const targetTable = document.getElementById(input.dataset.tableSearch);
    if (!targetTable) return;
    input.addEventListener('input', function () {
      const q = this.value.toLowerCase();
      targetTable.querySelectorAll('tbody tr').forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(q) ? '' : 'none';
      });
    });
  });

  /* =====================================================
     6. DRAG & DROP FILE UPLOAD
  ===================================================== */
  document.querySelectorAll('.upload-zone').forEach(zone => {
    const input = zone.querySelector('input[type="file"]');
    zone.addEventListener('dragover', e => {
      e.preventDefault(); zone.classList.add('dragover');
    });
    zone.addEventListener('dragleave', () => zone.classList.remove('dragover'));
    zone.addEventListener('drop', e => {
      e.preventDefault();
      zone.classList.remove('dragover');
      const files = e.dataTransfer.files;
      handleFileUpload(files, zone);
    });
    zone.addEventListener('click', () => input && input.click());
    if (input) {
      input.addEventListener('change', function () {
        handleFileUpload(this.files, zone);
      });
    }
  });

  function handleFileUpload(files, zone) {
    const list = zone.querySelector('.file-list');
    if (!list) return;
    Array.from(files).forEach(file => {
      const item = document.createElement('div');
      item.className = 'file-item d-flex align-items-center gap-2 mt-2 p-2 bg-white rounded border';
      item.innerHTML = `
        <i class="bi bi-file-earmark text-primary"></i>
        <span class="flex-1 small">${file.name}</span>
        <small class="text-muted">${(file.size / 1024).toFixed(1)} KB</small>
        <button class="btn btn-sm btn-link text-danger p-0" onclick="this.parentElement.remove()">
          <i class="bi bi-x-circle"></i>
        </button>
      `;
      list.appendChild(item);
    });
    const hint = zone.querySelector('.upload-hint');
    if (hint) hint.style.display = 'none';
  }

  /* =====================================================
     7. ALERTS – Auto dismiss after 5s
  ===================================================== */
  document.querySelectorAll('.alert.auto-dismiss').forEach(alert => {
    setTimeout(() => {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      bsAlert.close();
    }, 5000);
  });

  /* =====================================================
     8. TOOLTIP INIT
  ===================================================== */
  document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => {
    new bootstrap.Tooltip(el, { trigger: 'hover' });
  });

  /* =====================================================
     9. DEMO ROLE SWITCHER (for prototype testing)
     In production, role is determined by Django context
  ===================================================== */
  const roleSwitcher = document.getElementById('roleSwitcher');
  if (roleSwitcher) {
    const roleProfiles = {
      admin:        { name: 'Admin User',      role: 'Super Admin',        initials: 'AD', email: 'admin@partlink.io' },
      manufacturer: { name: 'Vikram Patel',    role: 'Manufacturer',       initials: 'VP', email: 'vikram@tatasteel.com' },
      supplier:     { name: 'Anita Sharma',    role: 'Supplier (MSME)',    initials: 'AS', email: 'anita@apexforge.in' },
      logistics:    { name: 'Ramesh Singh',    role: 'Logistics Provider', initials: 'RS', email: 'ramesh@nexlog.in' },
      designer:     { name: 'Priya Mehta',     role: 'Part Designer',      initials: 'PM', email: 'priya@metalcraft.com' },
      distributor:  { name: 'Suresh Verma',    role: 'Dealer/Distributor', initials: 'SV', email: 'suresh@partsdepot.in' }
    };

    roleSwitcher.addEventListener('change', function () {
      const role = this.value;
      const profile = roleProfiles[role] || roleProfiles.admin;
      
      // Update Sidebar Nav
      document.querySelectorAll('.nav-section').forEach(s => s.classList.add('d-none'));
      const target = document.querySelector(`.nav-section[data-role="${role}"]`);
      if (target) target.classList.remove('d-none');
      
      // Update Role Badge in sidebar
      const badge = document.getElementById('currentRole');
      if (badge) badge.textContent = profile.role;
      
      // Update Navbar User Profile
      const userName = document.getElementById('userName');
      const userRole = document.getElementById('userRole');
      const userInitials = document.getElementById('userInitials');
      const profileName = document.getElementById('profileName');
      if (userName) userName.textContent = profile.name;
      if (userRole) userRole.textContent = profile.role;
      if (userInitials) userInitials.textContent = profile.initials;
      if (profileName) profileName.textContent = profile.name;
      const profileEmail = profileName?.nextElementSibling;
      if (profileEmail) profileEmail.textContent = profile.email;
      
      // Update Main Content Dashboard View
      document.querySelectorAll('.dashboard-section').forEach(sec => sec.style.display = 'none');
      const targetSection = document.querySelector(`.dashboard-section[data-role="${role}"]`);
      if (targetSection) targetSection.style.display = 'block';
      
      // Scroll to top on switch
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  console.log('%c✅ PartLink UI Loaded', 'color:#1565C0;font-weight:bold;font-size:14px;');
});


/* =====================================================
   CHART.JS HELPER UTILITIES
   Call these from individual dashboard pages
===================================================== */

/**
 * Creates a line chart on Chart.js canvas
 * @param {string} canvasId - canvas element id
 * @param {object} opts - { labels, datasets, title }
 */
function createLineChart(canvasId, opts) {
  const ctx = document.getElementById(canvasId)?.getContext('2d');
  if (!ctx) return;
  return new Chart(ctx, {
    type: 'line',
    data: {
      labels: opts.labels,
      datasets: opts.datasets.map(ds => ({
        label: ds.label,
        data: ds.data,
        borderColor: ds.color || '#1565C0',
        backgroundColor: ds.fill || 'rgba(21,101,192,0.08)',
        fill: true,
        tension: 0.45,
        pointRadius: 4,
        pointBackgroundColor: ds.color || '#1565C0',
        borderWidth: 2.5,
      }))
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: 'top', labels: { font: { family: 'Inter', size: 12 }, boxWidth: 12 } },
        title: { display: !!opts.title, text: opts.title, font: { size: 14, weight: '600' } },
      },
      scales: {
        x: {
          grid: { color: 'rgba(0,0,0,0.04)' },
          ticks: { font: { family: 'Inter', size: 12 }, color: '#718096' }
        },
        y: {
          grid: { color: 'rgba(0,0,0,0.04)' },
          ticks: { font: { family: 'Inter', size: 12 }, color: '#718096' }
        }
      }
    }
  });
}

/**
 * Creates a bar chart
 */
function createBarChart(canvasId, opts) {
  const ctx = document.getElementById(canvasId)?.getContext('2d');
  if (!ctx) return;
  return new Chart(ctx, {
    type: 'bar',
    data: {
      labels: opts.labels,
      datasets: opts.datasets.map((ds, i) => ({
        label: ds.label,
        data: ds.data,
        backgroundColor: ds.colors || ['#1565C0','#1976D2','#2196F3','#42A5F5','#64B5F6','#90CAF9'],
        borderRadius: 6,
        borderSkipped: false,
      }))
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: opts.showLegend || false, labels: { font: { family: 'Inter' } } },
      },
      scales: {
        x: { grid: { display: false }, ticks: { font: { family: 'Inter', size: 12 }, color: '#718096' } },
        y: { grid: { color: 'rgba(0,0,0,0.04)' }, ticks: { font: { family: 'Inter', size: 12 }, color: '#718096' } }
      }
    }
  });
}

/**
 * Creates a doughnut chart
 */
function createDoughnutChart(canvasId, opts) {
  const ctx = document.getElementById(canvasId)?.getContext('2d');
  if (!ctx) return;
  return new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: opts.labels,
      datasets: [{
        data: opts.data,
        backgroundColor: opts.colors || ['#1565C0','#16A34A','#D97706','#DC2626','#0891B2'],
        borderWidth: 0,
        hoverOffset: 8,
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      cutout: '72%',
      plugins: {
        legend: {
          position: 'bottom',
          labels: { font: { family: 'Inter', size: 12 }, padding: 16, boxWidth: 12 }
        }
      }
    }
  });
}
