import fontforge

font_name = 'draw_in.ttf'
font = fontforge.font()

def draw_box(glyph, i=None):
    pen = glyph.glyphPen()
    pen.moveTo((100,100))
    if i == 1:
        pen.lineTo((300,300))
    pen.lineTo((100,500))
    if i == 2:
        pen.lineTo((300,300))
    pen.lineTo((500,500))
    if i == 3:
        pen.lineTo((300,300))
    pen.lineTo((500,100))
    if i == 4:
        pen.lineTo((300,300))
    pen.closePath()
    glyph.width = 1000

# ligature metadata bookkeeping
# https://fontforge.org/docs/tutorial/editexample4.html#lookups-and-features
lookup_name = "Draw-in Ligatures"
subtable_name = "Subtable"
lang_tuple = ((b"liga",((b"latn",(b"dflt")),)),)  # ha ha wtf
font.addLookup(lookup_name, "gsub_ligature", (), lang_tuple)
font.addLookupSubtable(lookup_name, subtable_name)

glyph = font.createChar(ord('!'), "!")
draw_box(glyph, 1)

glyph = font.createChar(0x200d, "zwj")
draw_box(glyph, 2)

glyph = font.createChar(ord('1'), "one")
draw_box(glyph, 3)

glyph = font.createChar(-1, "excl_1")
draw_box(glyph, 4)

glyph.addPosSub(subtable_name, ('!', 'zwj', 'one'))

font.generate("../fonts/" + font_name)
