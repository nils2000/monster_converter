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
Zauberwirken. Der Akolyth ist ein Zauberwirker der 1. Stufe. Sein Attribut zum Zauberwirken ist Weisheit (Zauberrettungs­wurf-SG 12, +4 zum Treffen mit Zauberangriffen).
Zaubertricks (beliebig oft): Heilige Flamme, Licht, Thaumaturgie
1. Grad (3 Plätze): Heiligtum, Segnen, Wunden heilen
Aktionen
Keule. Nahkampf-Waffenangriff: +2 zum Treffen, Reichweite 1,5 m, ein Ziel. Treffer: 2 (1W4) Wuchtschaden.
/Aktionen

Akolythen sind junge Mitglieder des Klerus, die normaler­weise einem Priester unterstellt sind. Sie verrichten eine Vielzahl von Aufgaben im Tempel und erhalten von ihrer Gott­heit die Macht, kleinere Zauber zu wirken."""


def parse(monster_description):
    ret = dict()
    muster = "(.*)\n(.*)"
    ret["Name"], ret["Klassifikation"] = re.search(
        muster, monster_description).groups()

    muster = "Rüstungsklasse (.+)"
    ret["Rüstungsklasse"] = re.search(muster, monster_description)[1]

    muster = "Trefferpunkte (\d+) \((.+)\)"
    ret["Trefferpunkte"],  ret["Trefferwürfel"] = re.search(
        muster, monster_description).groups()

    muster = "Bewegungsrate (.*)"
    ret["Bewegungsrate"] = re.search(
        muster, monster_description)[1]

    muster = "STR GES KON INT WEI CHA\n(\d+) \S+ (\d+) \S+ (\d+) \S+ (\d+) \S+ (\d+) \S+ (\d+) \S+"
    ret["Stärke"], ret["Geschicklichkeit"], ret["Konstitution"], ret["Intelligenz"], ret["Weisheit"], ret["Charisma"] = re.search(
        muster, monster_description).groups()

    muster = "Fertigkeiten (.*)"
    parse_result = re.search(muster, monster_description)
    if (parse_result):
        fertigkeiten = parse_result[1]
        fertigkeiten_list = fertigkeiten.split(",")
        ret["Fertigkeiten"] = dict([item.split()
                                    for item in fertigkeiten_list])

    muster = "Sinne (.*)"
    ret["Sinne"] = re.search(muster, monster_description)[1]

    muster = "Sprachen (.*)"
    ret["Sprachen"] = re.search(muster, monster_description)[1]

    muster = "(Herausforderungsgrad|Herausforderung) (.*)"
    ret["Herausforderungsgrad"] = re.search(muster, monster_description)[2]

    muster = "\n\n(.*)"
    ret["Beschreibung"] = re.search(
        muster, monster_description, re.DOTALL)[1]

    muster = "Zauberwirken. (.*)"
    parse_result = re.search(muster, monster_description)
    if (parse_result):
        ret["Zauberwirken"] = parse_result[1]
        #"Zaubertricks (beliebig oft): Ausbessern, Feuerpfeil, Taschenspielerei"
        muster = "Zaubertricks(.+?): (.*)"
        parse_result_l = re.search(muster, monster_description)
        if (parse_result_l):
            ret["Zaubertricks"] = dict()
            ret["Zaubertricks"]["Plätze"] = parse_result_l[1]
            ret["Zaubertricks"]["Zauber"] = parse_result_l[2].split(",")
        ret["Zauber"] = dict()
        ret["Zauberplätze"] = dict()
        for grad in range(1, 10):
            #"1. Grad (3 Plätze): Heiligtum, Segnen, Wunden heilen"
            muster = str(grad) + r"\. Grad(.+?): (.*)"
            parse_result_lo = re.search(muster, monster_description)
            if (parse_result_lo):
                ret["Zauber"][grad] = parse_result_lo[2].split(",")
                ret["Zauberplätze"][grad] = parse_result_lo[1]

    muster = "Aktionen\n(.*?)\n/Aktionen"
    ret["Aktionen"] = re.search(
        muster, monster_description, re.DOTALL)[1]

    muster = "Reaktionen\n(.*?)\n/Reaktionen"
    parse_result = re.search(muster, monster_description, re.DOTALL)
    if (parse_result):
        ret["Reaktionen"] = parse_result[1]

    muster = "Legendäre Aktionen\n(.*?)\n/Legendäre Aktionen"
    parse_result = re.search(muster, monster_description, re.DOTALL)
    if (parse_result):
        ret["Legendäre Aktionen"] = parse_result[1]

    muster = "Schadensimmunitäten (.*)"
    parse_result = re.search(muster, monster_description)
    if (parse_result):
        ret["Schadensimmunitäten"] = parse_result[1]

    muster = "Schadensresistenzen (.*)"
    parse_result = re.search(muster, monster_description)
    if (parse_result):
        ret["Schadensresistenzen"] = parse_result[1]

    muster = "Zustandsimmunitäten (.*)"
    parse_result = re.search(muster, monster_description)
    if (parse_result):
        ret["Zustandsimmunitäten"] = parse_result[1]

    muster = "Rettungswürfe (.*)"
    parse_result = re.search(muster, monster_description)
    if (parse_result):
        ret["Rettungswürfe"] = parse_result[1]

    muster = "Magieresistenz(.*)"
    parse_result = re.search(muster, monster_description)
    if (parse_result):
        ret["Magieresistenz"] = parse_result[1]

    return ret


# print(parse(Akolyth))
