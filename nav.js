// Shared site header. Imported via <x-import from="./nav.js" component="Nav">
// on every page so nav markup/links can't drift out of sync between pages.
function Nav(props) {
  var t = props.t;
  var toggleTheme = props.toggleTheme;
  var e = React.createElement;

  // Same links, in the same order, on every page.
  var links = [
    e('a', { key: 'home', href: './index.html', style: { color: t.textSecondary } }, 'Home'),
    e('a', { key: 'services', href: './index.html#services', style: { color: t.textSecondary } }, 'Services'),
    e('a', { key: 'portfolio', href: './index.html#portfolio', style: { color: t.textSecondary } }, 'Portfolio'),
    e('a', { key: 'about', href: './index.html#about', style: { color: t.textSecondary } }, 'About'),
    e('a', { key: 'ethics', href: './ethical-ai.html', style: { color: t.textSecondary } }, 'Ethics'),
    e('a', { key: 'contact', href: './index.html#contact', style: { color: t.textSecondary } }, 'Contact')
  ];

  return e(
    'div',
    {
      'data-nav': true,
      style: {
        position: 'sticky', top: 0, zIndex: 50, display: 'flex', alignItems: 'center',
        justifyContent: 'space-between', padding: '20px 48px', background: t.navBg,
        backdropFilter: 'blur(6px)', borderBottom: '1px solid ' + t.border
      }
    },
    e(
      'a',
      { href: './index.html', style: { display: 'flex', alignItems: 'center', gap: 12, textDecoration: 'none' } },
      e('img', { src: 'assets/skull-dark-mode.gif', alt: 'Demilich Digital skull mark', style: { width: 36, height: 36, imageRendering: 'pixelated', display: t.darkLogoDisplay } }),
      e('img', { src: 'assets/skull-light-mode.gif', alt: 'Demilich Digital skull mark', style: { width: 36, height: 36, imageRendering: 'pixelated', display: t.lightLogoDisplay } }),
      e('span', { 'data-nav-title': true, style: { fontFamily: "'IBM Plex Mono', monospace", fontWeight: 600, fontSize: 16, letterSpacing: '0.04em', color: t.textPrimary } }, 'DEMILICH DIGITAL')
    ),
    e(
      'div',
      { 'data-nav-links': true, style: { display: 'flex', alignItems: 'center', flexWrap: 'wrap', gap: 12 + 'px ' + 32 + 'px', fontFamily: "'IBM Plex Mono', monospace", fontSize: 13, letterSpacing: '0.03em' } },
      links.concat([
        e('button', {
          key: 'toggle',
          onClick: toggleTheme,
          style: {
            fontFamily: "'IBM Plex Mono', monospace", fontSize: 12, letterSpacing: '0.1em',
            background: 'transparent', border: '1px solid ' + t.border, color: t.textSecondary,
            padding: '6px 12px', borderRadius: 20, cursor: 'pointer'
          }
        }, t.toggleLabel)
      ])
    )
  );
}

module.exports = { Nav: Nav };
