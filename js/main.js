// Menu openen en sluiten op de telefoon
(function () {
  var knop = document.querySelector('.menu-knop');
  var nav = document.getElementById('menu');
  if (!knop || !nav) return;
  knop.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    knop.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
})();

// Bij afdrukken alle vragen openklappen
window.addEventListener('beforeprint', function () {
  document.querySelectorAll('details').forEach(function (d) { d.open = true; });
});
