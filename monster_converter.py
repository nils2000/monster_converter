import re
Akolyth = """Akolyth (Priesteranwärter)
Mittelgroßer Humanoider (jedes Volk), jede Gesinnung
Rüstungsklasse 10
Trefferpunkte 9 (2W8)
Bewegungsrate 9 m
STR GES KON INT WEI CHA
10 (+0) 10 (+0) 10 (+0) 10 (+0) 14 (+2) 11 (+0)
Fertigkeiten Heilkunde +4, Religion +2
Sinne Passive Wahrnehmung 12
Sprachen eine Sprache nach Wahl (normalerweise Gemeinsprache)
Herausforderungsgrad 1/4 (50 EP)
Zauberwirken. Der Akolyth ist ein Zauberwirker der 1. Stufe.
Sein Attribut zum Zauberwirken ist Weisheit (Zauberrettungs­wurf-SG 12, +4 zum Treffen mit Zauberangriffen). Der Akolyth hat
die folgenden Klerikerzauber vorbereitet:
Zaubertricks (beliebig oft): Heilige Flamme, Licht, Thaumaturgie
1. Grad (3 Plätze): Heiligtum, Segnen, Wunden heilen
Aktionen
Keule. Nahkampf-Waffenangriff: +2 zum Treffen, Reichweite 1,5 m, ein Ziel. Treffer: 2 (1W4) Wuchtschaden.

Akolythen sind junge Mitglieder des Klerus, die normaler­weise einem Priester unterstellt sind. Sie verrichten eine
Vielzahl von Aufgaben im Tempel und erhalten von ihrer Gott­
heit die Macht, kleinere Zauber zu wirken."""


muster = "(.*)"
name = re.search(muster, Akolyth)[1]
