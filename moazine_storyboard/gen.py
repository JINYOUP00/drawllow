import random, os, html

OUT = "/home/user/drawllow/moazine_storyboard"
os.makedirs(OUT + "/frames", exist_ok=True)

INK = "#2b2622"; SKIN = "#f4cba9"; HAIR = "#3b2b27"; SWEATER = "#6f8fd8"; SWEATER_D = "#5a78c0"
WALL = "#f1e6d4"; DESK = "#c9996b"; DESK_D = "#a87a50"; CORAL = "#ff6a4d"; LEAF = "#76ad78"
COLORS = ["#ff6a4d", "#ffc94a", "#6f8fd8", "#76ad78", "#e88fb0", "#8a6fd0", "#4fb8c4", "#f29b4b", "#2b2622", "#d9d2c5"]

def person(x, y, s=1.0, eyes="down", back=False):
    """Upper body, head centre at (x,y)."""
    g = [f'<g transform="translate({x},{y}) scale({s})" stroke="{INK}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">']
    # body
    g.append(f'<path d="M-78,230 L-78,130 Q-76,72 0,70 Q76,72 78,130 L78,230 Z" fill="{SWEATER}"/>')
    g.append(f'<path d="M-22,72 Q0,92 22,72" fill="none" stroke="{SWEATER_D}" stroke-width="6"/>')
    if back:
        g.append(f'<path d="M-56,10 Q-60,-60 0,-62 Q60,-60 56,10 Q58,52 40,62 L-40,62 Q-58,52 -56,10 Z" fill="{HAIR}"/>')
        g.append('</g>'); return "".join(g)
    g.append(f'<rect x="-13" y="38" width="26" height="36" fill="{SKIN}"/>')
    g.append(f'<path d="M-56,10 Q-60,-60 0,-62 Q60,-60 56,10 Q58,52 42,60 L-42,60 Q-58,52 -56,10 Z" fill="{HAIR}"/>')
    g.append(f'<ellipse cx="0" cy="4" rx="40" ry="46" fill="{SKIN}"/>')
    g.append(f'<path d="M-44,-4 Q-46,-52 0,-50 Q46,-52 44,-4 Q30,-30 6,-28 Q-20,-34 -44,-4 Z" fill="{HAIR}"/>')
    if eyes == "down":
        g.append('<path d="M-24,10 Q-16,16 -8,10 M8,10 Q16,16 24,10" fill="none"/>')
    elif eyes == "happy":
        g.append('<path d="M-24,12 Q-16,2 -8,12 M8,12 Q16,2 24,12" fill="none"/>')
    elif eyes == "worried":
        g.append(f'<circle cx="-16" cy="10" r="4" fill="{INK}" stroke="none"/><circle cx="16" cy="10" r="4" fill="{INK}" stroke="none"/>')
        g.append('<path d="M-26,-6 L-8,-2 M26,-6 L8,-2" fill="none"/>')
    else:
        g.append(f'<circle cx="-16" cy="10" r="4" fill="{INK}" stroke="none"/><circle cx="16" cy="10" r="4" fill="{INK}" stroke="none"/>')
    g.append('<circle cx="-26" cy="24" r="7" fill="#f29a8a" stroke="none" opacity=".6"/><circle cx="26" cy="24" r="7" fill="#f29a8a" stroke="none" opacity=".6"/>')
    if eyes == "worried":
        g.append('<path d="M-8,34 Q0,29 8,34" fill="none"/>')
    elif eyes == "happy":
        g.append('<path d="M-10,30 Q0,40 10,30" fill="none"/>')
    else:
        g.append('<path d="M-6,32 Q0,35 6,32" fill="none"/>')
    g.append('</g>')
    return "".join(g)

def subtitle(lines):
    n = len(lines); h = 26 * n + 18; y0 = 600 - h
    s = [f'<rect x="20" y="{y0}" width="320" height="{h}" rx="10" fill="#000" opacity=".62"/>']
    for i, l in enumerate(lines):
        s.append(f'<text x="180" y="{y0 + 32 + i*26}" text-anchor="middle" font-size="19" font-weight="700" fill="#fff">{html.escape(l)}</text>')
    return "".join(s)

def plant(x, y):
    return (f'<g stroke="{INK}" stroke-width="3" stroke-linejoin="round">'
            f'<path d="M{x-12},{y-40} Q{x-40},{y-70} {x-30},{y-100} Q{x-6},{y-80} {x-4},{y-40}Z" fill="{LEAF}"/>'
            f'<path d="M{x+6},{y-40} Q{x+30},{y-80} {x+20},{y-110} Q{x-2},{y-90} {x-2},{y-40}Z" fill="{LEAF}"/>'
            f'<path d="M{x-22},{y-42} L{x+22},{y-42} L{x+16},{y} L{x-16},{y}Z" fill="{CORAL}"/></g>')

def desk_scene(eyes, tablet_extra, extra=""):
    s = [f'<rect width="360" height="640" fill="{WALL}"/>']
    # window
    s.append(f'<g stroke="{INK}" stroke-width="3"><rect x="30" y="50" width="120" height="150" fill="#bfe0f2"/><path d="M90,50 V200 M30,125 H150"/></g>')
    s.append('<circle cx="122" cy="80" r="14" fill="#fff6c8"/>')
    # wall shelf with magazines
    s.append(f'<rect x="210" y="150" width="120" height="8" fill="{DESK_D}" stroke="{INK}" stroke-width="3"/>')
    for i, c in enumerate(["#ff6a4d", "#6f8fd8", "#ffc94a", "#76ad78"]):
        s.append(f'<rect x="{220 + i*20}" y="{100 + (i%2)*6}" width="16" height="{50 - (i%2)*6}" fill="{c}" stroke="{INK}" stroke-width="2.5"/>')
    s.append(extra)
    s.append(person(180, 290, 1.0, eyes))
    # desk
    s.append(f'<rect x="-5" y="455" width="370" height="200" fill="{DESK}" stroke="{INK}" stroke-width="3"/>')
    s.append(f'<rect x="-5" y="455" width="370" height="14" fill="{DESK_D}"/>')
    # tablet
    s.append(f'<g stroke="{INK}" stroke-width="3" stroke-linejoin="round"><path d="M88,440 L272,440 L292,500 L68,500 Z" fill="#3d3a44"/><path d="M98,446 L262,446 L278,494 L82,494 Z" fill="#fdfbf7"/></g>')
    s.append(tablet_extra)
    # arms + hands + pen
    s.append(f'<g stroke="{INK}" stroke-width="3" stroke-linejoin="round"><path d="M-30,520 Q40,470 120,470 L130,490 Q50,500 -20,560Z" fill="{SWEATER}"/>'
             f'<path d="M390,520 Q320,470 240,470 L230,490 Q310,500 380,560Z" fill="{SWEATER}"/>'
             f'<ellipse cx="128" cy="478" rx="16" ry="12" fill="{SKIN}"/><ellipse cx="230" cy="478" rx="16" ry="12" fill="{SKIN}"/>'
             f'<path d="M236,470 L206,440" stroke-width="6"/></g>')
    s.append(plant(320, 455))
    return "".join(s)

def scene1():
    t = f'<path d="M120,486 Q150,452 175,476 T230,462" fill="none" stroke="{CORAL}" stroke-width="3"/><circle cx="150" cy="468" r="8" fill="#ffc94a"/>'
    return desk_scene("down", t) + subtitle(["디자인을 전공한 일러스트레이터"])

def card(x, y, w, h, inner, rot=0):
    return (f'<g transform="rotate({rot} {x+w/2} {y+h/2})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fff" stroke="{INK}" stroke-width="3"/>{inner}</g>')

def scene2():
    s = [f'<rect width="360" height="640" fill="#e7eef8"/>']
    # floating content cards
    tv = (f'<rect x="34" y="92" width="92" height="62" rx="4" fill="#4fb8c4" stroke="{INK}" stroke-width="3"/>'
          f'<path d="M72,110 L92,123 L72,136Z" fill="#fff"/><path d="M60,154 L100,154" stroke="{INK}" stroke-width="3"/>'
          f'<text x="80" y="185" text-anchor="middle" font-size="15" font-weight="700" fill="{INK}">TV</text>')
    s.append(card(24, 80, 112, 116, tv, -6))
    web = (f'<rect x="144" y="56" width="96" height="16" fill="#d9d2c5"/><circle cx="154" cy="64" r="3" fill="{CORAL}"/><circle cx="164" cy="64" r="3" fill="#ffc94a"/>'
           f'<rect x="154" y="82" width="76" height="34" fill="#e88fb0"/><rect x="154" y="122" width="60" height="6" fill="#d9d2c5"/><rect x="154" y="132" width="70" height="6" fill="#d9d2c5"/>'
           f'<text x="192" y="160" text-anchor="middle" font-size="15" font-weight="700" fill="{INK}">인터넷</text>')
    s.append(card(138, 48, 108, 124, web, 3))
    mag = (f'<rect x="262" y="96" width="70" height="66" fill="#ffc94a" stroke="{INK}" stroke-width="2.5"/>'
           f'<text x="297" y="118" text-anchor="middle" font-size="12" font-weight="900" fill="{INK}">MAG</text><circle cx="297" cy="140" r="12" fill="{CORAL}"/>'
           f'<text x="297" y="182" text-anchor="middle" font-size="15" font-weight="700" fill="{INK}">잡지</text>')
    s.append(card(252, 86, 90, 108, mag, 7))
    # lightbulb
    s.append(f'<g stroke="{INK}" stroke-width="3"><circle cx="180" cy="215" r="18" fill="#fff2a8"/><rect x="172" y="232" width="16" height="10" fill="#d9d2c5"/></g>'
             f'<path d="M150,205 L140,200 M210,205 L220,200 M180,188 L180,178" stroke="{INK}" stroke-width="3"/>')
    # sofa
    s.append(f'<rect x="10" y="330" width="340" height="320" rx="30" fill="#e88fb0" stroke="{INK}" stroke-width="3"/>')
    s.append(person(180, 330, 0.95, "down"))
    # open magazine held
    s.append(f'<g stroke="{INK}" stroke-width="3" stroke-linejoin="round">'
             f'<path d="M180,420 L80,400 L72,520 L180,540 Z" fill="#fff"/><path d="M180,420 L280,400 L288,520 L180,540 Z" fill="#fff"/>'
             f'<rect x="96" y="420" width="64" height="44" fill="#6f8fd8" transform="skewY(10) translate(0,-30)" stroke="none"/>'
             f'<path d="M198,440 L262,428 M198,456 L262,444 M198,472 L250,462 M198,488 L262,476" stroke="#b8b0a2" stroke-width="4"/>'
             f'<ellipse cx="80" cy="470" rx="14" ry="16" fill="{SKIN}"/><ellipse cx="282" cy="470" rx="14" ry="16" fill="{SKIN}"/></g>')
    s.append(f'<path d="M286,392 Q300,380 312,392" fill="none" stroke="{INK}" stroke-width="3"/><path d="M296,370 Q310,358 322,370" fill="none" stroke="{INK}" stroke-width="3"/>')
    s.append(subtitle(["영감을 얻기 위해", "다양한 콘텐츠를 찾아보는 일상"]))
    return "".join(s)

def scene3():
    rnd = random.Random(7)
    s = [f'<rect width="360" height="640" fill="{WALL}"/>', f'<rect y="560" width="360" height="80" fill="#d8c3a5"/>']
    s.append(f'<rect x="30" y="30" width="300" height="470" fill="{DESK_D}" stroke="{INK}" stroke-width="4"/>')
    for r in range(4):
        y0 = 42 + r * 114; y1 = y0 + 100
        s.append(f'<rect x="42" y="{y0}" width="276" height="100" fill="#7a5638"/>')
        x = 44
        while x < 314:
            w = rnd.randint(9, 18); w = min(w, 316 - x)
            h = rnd.randint(70, 98)
            s.append(f'<rect x="{x}" y="{y1 - h}" width="{w}" height="{h}" fill="{rnd.choice(COLORS)}" stroke="{INK}" stroke-width="1.8"/>')
            x += w
        s.append(f'<rect x="38" y="{y1}" width="284" height="10" fill="{DESK}" stroke="{INK}" stroke-width="2.5"/>')
    # floor piles
    for px, n in [(20, 7), (250, 9)]:
        for i in range(n):
            w = rnd.randint(70, 90)
            s.append(f'<rect x="{px + rnd.randint(-4, 4)}" y="{590 - i*12}" width="{w}" height="12" fill="{rnd.choice(COLORS)}" stroke="{INK}" stroke-width="2"/>')
    # person from behind
    s.append(person(180, 440, 0.85, back=True))
    s.append(f'<path d="M232,388 Q240,402 232,410 Q224,402 232,388Z" fill="#9fd3f0" stroke="{INK}" stroke-width="2.5"/>')
    # cost / space icons
    s.append(f'<g stroke="{INK}" stroke-width="3"><circle cx="58" cy="350" r="22" fill="#ffc94a"/><circle cx="302" cy="330" r="22" fill="#ffc94a"/></g>'
             f'<text x="58" y="358" text-anchor="middle" font-size="22" font-weight="900" fill="{INK}">₩</text>'
             f'<text x="302" y="338" text-anchor="middle" font-size="22" font-weight="900" fill="{INK}">₩</text>'
             f'<text x="180" y="355" text-anchor="middle" font-size="40" font-weight="900" fill="{CORAL}" stroke="{INK}" stroke-width="2">!?</text>')
    s.append(subtitle(["쌓여가는 잡지,", "공간과 비용의 부담"]))
    return "".join(s)

def device_frame(bg):
    return (f'<rect width="360" height="640" fill="{bg}"/>'
            f'<rect x="24" y="24" width="312" height="560" rx="28" fill="#3d3a44" stroke="{INK}" stroke-width="4"/>'
            f'<rect x="38" y="44" width="284" height="520" rx="12" fill="#fdfbf7"/>')

def scene4():
    G = "#2db563"
    s = [device_frame("#cfe6d6")]
    s.append(f'<rect x="38" y="44" width="284" height="92" rx="12" fill="{G}"/><rect x="38" y="110" width="284" height="26" fill="{G}"/>')
    s.append('<text x="56" y="76" font-size="16" font-weight="900" fill="#fff">지식백과</text>')
    s.append(f'<rect x="52" y="90" width="256" height="34" rx="17" fill="#fff" stroke="{INK}" stroke-width="2"/>'
             f'<text x="68" y="113" font-size="14" fill="{INK}">일러스트 레퍼런스 자료</text>'
             f'<circle cx="286" cy="105" r="7" fill="none" stroke="{G}" stroke-width="3"/><path d="M291,110 L297,116" stroke="{G}" stroke-width="3"/>')
    y = 156
    for i in range(4):
        hl = (i == 2)
        if hl:
            s.append(f'<rect x="48" y="{y-8}" width="264" height="86" rx="10" fill="#fff1ec" stroke="{CORAL}" stroke-width="4"/>'
                     f'<rect x="60" y="{y+2}" width="56" height="66" rx="4" fill="{CORAL}" stroke="{INK}" stroke-width="2"/>'
                     f'<text x="88" y="{y+42}" text-anchor="middle" font-size="13" font-weight="900" fill="#fff">MZ</text>'
                     f'<text x="128" y="{y+24}" font-size="17" font-weight="900" fill="{INK}">모아진</text>'
                     f'<text x="128" y="{y+46}" font-size="12" fill="#6b625a">매거진 콘텐츠 모음</text>'
                     f'<rect x="128" y="{y+56}" width="120" height="6" rx="3" fill="#e6ddd0"/>')
        else:
            s.append(f'<rect x="60" y="{y+2}" width="56" height="56" rx="4" fill="#e6ddd0"/>'
                     f'<rect x="128" y="{y+10}" width="150" height="9" rx="4" fill="#cfc6b8"/>'
                     f'<rect x="128" y="{y+28}" width="170" height="6" rx="3" fill="#e6ddd0"/><rect x="128" y="{y+40}" width="120" height="6" rx="3" fill="#e6ddd0"/>')
        y += 96 if hl else 74
    # finger tap
    s.append(f'<circle cx="282" cy="342" r="30" fill="none" stroke="{CORAL}" stroke-width="3" opacity=".5"/><circle cx="282" cy="342" r="18" fill="none" stroke="{CORAL}" stroke-width="3"/>')
    s.append(f'<path d="M262,368 L262,330 Q262,318 274,318 Q286,318 286,330 L286,372 Q300,362 312,372 Q320,380 314,392 L300,460 L250,470 L230,410 Q226,396 240,394 Q252,394 262,404 Z" fill="{SKIN}" stroke="{INK}" stroke-width="3" stroke-linejoin="round" transform="translate(20,12)"/>')
    s.append(subtitle(["자료를 찾다가", "우연히 발견한 모아진"]))
    return "".join(s)

def scene5():
    s = [device_frame("#fde3da")]
    s.append(f'<rect x="38" y="44" width="284" height="56" rx="12" fill="#fff"/><path d="M38,100 H322" stroke="#e6ddd0" stroke-width="2"/>'
             f'<text x="56" y="80" font-size="20" font-weight="900" fill="{CORAL}">모아진</text><text x="132" y="80" font-size="11" font-weight="700" fill="#6b625a">MAGAZINE</text>')
    x = 50
    for i, c in enumerate(["디자인", "패션", "여행", "아트"]):
        w = 14 * len(c) + 22
        fill = INK if i == 0 else "#fff"; tc = "#fff" if i == 0 else INK
        s.append(f'<rect x="{x}" y="112" width="{w}" height="26" rx="13" fill="{fill}" stroke="{INK}" stroke-width="1.8"/>'
                 f'<text x="{x + w/2}" y="130" text-anchor="middle" font-size="12" font-weight="700" fill="{tc}">{c}</text>')
        x += w + 8
    rnd = random.Random(3)
    covers = ["#ffc94a", "#6f8fd8", "#e88fb0", "#76ad78", "#8a6fd0", "#4fb8c4"]
    for i in range(6):
        cx = 52 + (i % 3) * 88; cy = 152 + (i // 3) * 118
        c = covers[i]
        s.append(f'<rect x="{cx}" y="{cy}" width="80" height="106" rx="4" fill="{c}" stroke="{INK}" stroke-width="2.5"/>'
                 f'<rect x="{cx+8}" y="{cy+8}" width="44" height="8" fill="#fff"/>'
                 f'<circle cx="{cx+40}" cy="{cy+60}" r="{rnd.randint(16,24)}" fill="#fff" opacity=".75"/>'
                 f'<rect x="{cx+8}" y="{cy+90}" width="34" height="5" fill="#fff" opacity=".8"/>')
    # 지식백과 confirmation card
    s.append(f'<g transform="rotate(-3 180 430)"><rect x="56" y="392" width="250" height="74" rx="12" fill="#fff" stroke="{INK}" stroke-width="3"/>'
             f'<rect x="56" y="392" width="250" height="24" rx="12" fill="#2db563"/><rect x="56" y="404" width="250" height="12" fill="#2db563"/>'
             f'<text x="70" y="410" font-size="12" font-weight="900" fill="#fff">지식백과</text>'
             f'<text x="70" y="440" font-size="14" font-weight="900" fill="{INK}">모아진 매거진 콘텐츠</text>'
             f'<text x="70" y="456" font-size="11" fill="#6b625a">지식백과에서도 확인 가능</text>'
             f'<circle cx="276" cy="442" r="16" fill="{CORAL}" stroke="{INK}" stroke-width="2.5"/><path d="M268,442 L274,448 L285,435" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/></g>')
    s.append(subtitle(["다양한 분야의 매거진을 한곳에서", "네이버 지식백과에서도 확인 가능한 콘텐츠"]).replace('font-size="19"', 'font-size="16"'))
    return "".join(s)

def scene6():
    t = (f'<rect x="104" y="452" width="70" height="38" fill="#ffc94a" stroke="{INK}" stroke-width="2" transform="skewX(-8)"/>'
         f'<circle cx="138" cy="471" r="9" fill="{CORAL}"/>'
         f'<path d="M190,486 Q206,450 226,470 T262,456" fill="none" stroke="{CORAL}" stroke-width="3"/><circle cx="214" cy="466" r="7" fill="#6f8fd8"/>')
    extra = (f'<g stroke="{INK}" stroke-width="3"><circle cx="270" cy="200" r="24" fill="#fff2a8"/><rect x="260" y="222" width="20" height="12" fill="#d9d2c5"/></g>'
             f'<path d="M236,186 L226,180 M304,186 L314,180 M270,166 L270,154 M242,214 L232,220 M298,214 L308,220" stroke="{INK}" stroke-width="3"/>'
             f'<path d="M60,240 l6,14 14,6 -14,6 -6,14 -6,-14 -14,-6 14,-6z" fill="#ffc94a" stroke="{INK}" stroke-width="2"/>'
             f'<path d="M300,100 l4,9 9,4 -9,4 -4,9 -4,-9 -9,-4 9,-4z" fill="{CORAL}" stroke="{INK}" stroke-width="2"/>')
    s = desk_scene("happy", t, extra)
    s += (f'<rect x="110" y="18" width="140" height="44" rx="22" fill="{CORAL}" stroke="{INK}" stroke-width="3"/>'
          f'<text x="180" y="48" text-anchor="middle" font-size="22" font-weight="900" fill="#fff">모아진</text>')
    return s + subtitle(["새로운 영감들이 모인 곳,", "모아진"])

SCENES = [
    dict(no="01", t="0:00~0:05", dur="5초", title="나의 정체성", shot="MS · 정면 / 작업 몰입", art=scene1,
         screen="작업실에서 태블릿으로 그림을 그리는 일러스트레이터. 작업에 몰입한 모습.",
         nar="“저는 디자인을 전공한 일러스트레이터입니다.”", sub="디자인을 전공한 일러스트레이터"),
    dict(no="02", t="0:05~0:12", dur="7초", title="영감을 얻는 습관", shot="MS · 잡지 넘김 + TV/인터넷 인서트", art=scene2,
         screen="잡지, 인터넷, TV 등 다양한 콘텐츠를 접하는 모습. 잡지를 넘기거나 자료를 살펴보는 장면.",
         nar="“학생 때부터 새로운 영감을 얻기 위해 잡지나 인터넷, TV 등 다양한 콘텐츠를 즐겨 봤어요.”", sub="영감을 얻기 위해 다양한 콘텐츠를 찾아보는 일상"),
    dict(no="03", t="0:12~0:17", dur="5초", title="현실적인 고민", shot="FS · 뒷모습 / 책장 틸트업", art=scene3,
         screen="책장에 빼곡하게 쌓인 잡지와 책. 공간을 차지하는 잡지들을 바라보는 모습.",
         nar="“그런데 잡지를 하나둘 사다 보니 책장은 가득 차고, 공간도 비용도 부담이 되더라고요.”", sub="쌓여가는 잡지, 공간과 비용의 부담"),
    dict(no="04", t="0:17~0:25", dur="8초", title="지식백과에서 발견한 모아진", shot="CU · 화면 녹화 / 검색 → 탭", art=scene4,
         screen="작업 자료를 찾기 위해 네이버 지식백과를 검색하는 모습. 검색 결과를 살펴보다 모아진을 발견하고 접속하는 장면.",
         nar="“최근에도 작업에 필요한 자료를 찾으려고 네이버 지식백과를 살펴보다가, 우연히 모아진을 발견했어요.”", sub="자료를 찾다가 우연히 발견한 모아진"),
    dict(no="05", t="0:25~0:33", dur="8초", title="신뢰할 수 있는 매거진 콘텐츠", shot="CU · 사이트 스크롤 + 지식백과 화면 팝업", art=scene5,
         screen="모아진 웹사이트와 다양한 분야의 잡지를 둘러보는 모습. 네이버 지식백과에서 모아진 관련 콘텐츠를 확인하는 화면도 함께 보여줌.",
         nar="“들어가 보니 다양한 분야의 잡지를 한곳에서 볼 수 있더라고요. 네이버 지식백과에서도 모아진의 매거진 콘텐츠를 확인할 수 있어서 더 신뢰가 갔어요.”",
         sub="다양한 분야의 매거진을 한곳에서 / 네이버 지식백과에서도 확인 가능한 콘텐츠"),
    dict(no="06", t="0:33~0:40", dur="7초", title="영감 회복과 활용", shot="MS · 작업 복귀 → 엔딩 로고", art=scene6,
         screen="다시 작업에 몰입하는 모습. 태블릿으로 모아진을 살펴보다 그림에 아이디어를 반영하는 장면. 마지막에 모아진 로고.",
         nar="“저는 작업하다가 새로운 영감이 필요할 때 모아진을 한 번씩 찾아봐요. 잡지를 좋아하거나 새로운 영감이 필요한 분들에게 추천합니다.”",
         sub="새로운 영감들이 모인 곳, 모아진"),
]

FONT = "'Noto Sans KR','WenQuanYi Zen Hei',sans-serif"

def svg(inner, w=None):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 640" font-family="{FONT}">'
            f'<defs><clipPath id="c"><rect width="360" height="640"/></clipPath></defs><g clip-path="url(#c)">{inner}</g></svg>')

for sc in SCENES:
    sc["svg"] = svg(sc["art"]())
    with open(f'{OUT}/frames/cut{sc["no"]}.svg', "w") as f:
        f.write(sc["svg"])

def col(sc):
    e = html.escape
    return f'''<section class="cut">
  <header><span class="no">{sc["no"]}</span><div><b>{e(sc["title"])}</b><small>{sc["t"]} · {sc["dur"]}</small></div></header>
  <div class="frame">{sc["svg"]}</div>
  <div class="shot">{e(sc["shot"])}</div>
  <dl>
    <dt>화면</dt><dd>{e(sc["screen"])}</dd>
    <dt>내레이션</dt><dd class="nar">{e(sc["nar"])}</dd>
    <dt>자막</dt><dd class="sub">{e(sc["sub"]).replace(" / ", "<br>")}</dd>
  </dl>
</section>'''

pages = []
for p in range(2):
    cols = "".join(col(sc) for sc in SCENES[p*3:p*3+3])
    pages.append(f'''<div class="page">
  <div class="top"><h1>모아진 숏폼 홍보영상 콘티</h1><div class="meta">9:16 세로 · 총 0:40 · 컷 6 · <b>{p+1}/2</b></div></div>
  <div class="cols">{cols}</div>
</div>''')

doc = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap" rel="stylesheet">
<style>
@page {{ size: 420mm 297mm; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: {FONT}; color: {INK}; background: #fff; }}
.page {{ width: 420mm; height: 297mm; padding: 14mm 16mm; background: #faf7f2; page-break-after: always; display: flex; flex-direction: column; }}
.top {{ display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 1.2mm solid {INK}; padding-bottom: 3mm; margin-bottom: 5mm; }}
h1 {{ font-size: 24pt; font-weight: 900; letter-spacing: -0.5pt; }}
h1::before {{ content: ""; display: inline-block; width: 5mm; height: 5mm; border-radius: 50%; background: {CORAL}; margin-right: 3mm; vertical-align: 1mm; }}
.meta {{ font-size: 11pt; color: #6b625a; }}
.cols {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10mm; flex: 1; }}
.cut {{ display: flex; flex-direction: column; }}
.cut header {{ display: flex; align-items: center; gap: 3mm; margin-bottom: 4mm; }}
.no {{ background: {CORAL}; color: #fff; font-weight: 900; font-size: 16pt; width: 13mm; height: 13mm; border-radius: 3mm; display: flex; align-items: center; justify-content: center; }}
.cut header b {{ display: block; font-size: 14pt; font-weight: 900; }}
.cut header small {{ font-size: 10pt; color: #6b625a; }}
.frame {{ align-self: center; width: 88mm; height: 156.4mm; border: 0.8mm solid {INK}; border-radius: 2mm; overflow: hidden; background: #fff; }}
.frame svg {{ width: 100%; height: 100%; display: block; }}
.shot {{ margin: 3mm 0 3mm; font-size: 9pt; font-weight: 700; color: {CORAL}; }}
dl {{ display: grid; grid-template-columns: 17mm 1fr; row-gap: 2.4mm; font-size: 9.5pt; line-height: 1.5; border-top: 0.3mm solid #d9d2c5; padding-top: 3mm; }}
dt {{ font-weight: 900; font-size: 8.5pt; color: #6b625a; padding-top: 0.4mm; }}
dd.nar {{ font-style: normal; }}
dd.sub {{ font-weight: 700; background: {INK}; color: #fff; padding: 1mm 2mm; border-radius: 1mm; }}
</style></head><body>{"".join(pages)}</body></html>'''

with open(f"{OUT}/storyboard.html", "w") as f:
    f.write(doc)
print("ok")
