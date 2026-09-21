import sys; sys.path.insert(0,'.')
from _kit import topbar

START = '  <div style="display: flex; justify-content: space-between; align-items: center; gap: 36px; padding: 26px 64px 22px;">'
END = '\n    </div>\n  </div>'

for fname, active in [('Main.dc.html', None), ('Team.dc.html', 'Team'),
                      ('Players.dc.html', 'Players'), ('Player.dc.html', 'Players'),
                      ('Column.dc.html', 'Articles'), ('Glossary.dc.html', 'Glossary')]:
    s = open(fname).read()
    i = s.index(START); j = s.index(END, i) + len(END)
    s = s[:i] + topbar(active) + s[j:]
    head = s.split('</helmet>')[1][:2500]
    for gone in ('Analysis</a>', 'News</a>', 'Interactives</a>', 'Numbers</a>'):
        assert gone not in head, f'{fname} still has {gone}'
    open(fname,'w').write(s)
    print(f'{fname}: nav -> {active or "(home)"}')
