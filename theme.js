// Persists the light/dark theme choice across page loads via localStorage.
// Loaded as a plain script (not an x-import) so it's available before the
// per-page Component classes read it during their initial render.
(function () {
  var KEY = 'demilich-theme';

  function get() {
    try {
      var v = localStorage.getItem(KEY);
      return v === 'light' || v === 'dark' ? v : 'dark';
    } catch (e) {
      return 'dark';
    }
  }

  function set(theme) {
    try {
      localStorage.setItem(KEY, theme);
    } catch (e) {}
  }

  window.DemilichTheme = { get: get, set: set };
})();
