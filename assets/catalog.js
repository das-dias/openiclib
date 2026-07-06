document.addEventListener('DOMContentLoaded', function () {
  var grid = document.getElementById('catalog-grid');
  if (!grid) return;

  var cards = grid.querySelectorAll('.design-card');
  var countEl = document.getElementById('catalog-count');
  var searchEl = document.getElementById('filter-search');
  var pdkEl = document.getElementById('filter-pdk');
  var classEl = document.getElementById('filter-class');
  var typeEl = document.getElementById('filter-type');
  var provenEl = document.getElementById('filter-proven');

  function applyFilters() {
    var pdk = pdkEl ? pdkEl.value : 'all';
    var cls = classEl ? classEl.value : 'all';
    var typ = typeEl ? typeEl.value : 'all';
    var proven = provenEl ? provenEl.checked : false;
    var search = searchEl ? searchEl.value.toLowerCase() : '';

    var visible = 0;
    cards.forEach(function (card) {
      var show = true;
      if (pdk !== 'all' && card.dataset.pdk !== pdk) show = false;
      if (cls !== 'all' && card.dataset.class !== cls) show = false;
      if (typ !== 'all') {
        var types = (card.dataset.types || '').split(' ');
        if (types.indexOf(typ) === -1) show = false;
      }
      if (proven && card.dataset.proven !== 'true') show = false;
      if (search && card.dataset.name.indexOf(search) === -1) show = false;

      card.style.display = show ? '' : 'none';
      if (show) visible++;
    });

    if (countEl) {
      countEl.textContent = visible + ' of ' + cards.length + ' designs';
    }
  }

  [searchEl, pdkEl, classEl, typeEl, provenEl].forEach(function (el) {
    if (el) {
      el.addEventListener('input', applyFilters);
      el.addEventListener('change', applyFilters);
    }
  });

  applyFilters();
});
