import sys, re
sys.path.insert(0,'.')
from _kit import topbar

OLD_START = '  <div style="display: flex; justify-content: space-between; align-items: center; gap: 40px; padding: 26px 64px 22px;">'
END = '\n    </div>\n  </div>'

for fname, active in [('Main.dc.html', None), ('Column.dc.html', 'Analysis'), ('Glossary.dc.html', 'Glossary')]:
    s = open(fname).read()
    i = s.index(OLD_START)
    j = s.index(END, i) + len(END)
    s = s[:i] + topbar(active) + s[j:]
    assert 'Interactives' not in s.split('</helmet>')[1][:2000], fname
    open(fname, 'w').write(s)
    print(f'{fname}: nav -> {active or "(home)"}')
