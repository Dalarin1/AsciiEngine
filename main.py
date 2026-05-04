import time
import os

frame = []

if os.name == 'nt':
    os.system('')

def clear_frame():
    global frame
    frame = []
    for _ in range(23):
        frame.append([" "] * 80)


def add_border():
    global frame
    frame[0] = ["-"] * 80
    frame[-1] = ["-"] * 80

    for i in range(23):
        frame[i][0] = "|"
        frame[i][-1] = "|"

    frame[0][0] = "+"
    frame[0][-1] = "+"
    frame[-1][0] = "+"
    frame[-1][-1] = "+"


def format_option_old(op: str, flag: bool, op2: str = ""):
    res: list[str] = ["", ""]
    if len(op) > 30 - 4:
        if op2:
            res[0] = op[: 27 - 4] + "..."
        else:
            res[0] = op[: 30 - 4]
    else:
        res[0] = op + " " * (30 - 4 - len(op))

    if op2:
        if len(op2) > 30:
            res[1] = op2[: 30 - 4]
        else:
            res[1] = op2 + " " * (30 - 4 - len(op2))
    else:
        if len(op) > 30:
            if len(op) > 60:
                res[1] = op[26:50]
            else:
                res[1] = op + " " * (30 - 4 - len(op))

        else:
            res[1] = op2 + " " * (30 - 4 - len(op2))

    res[0] = f"[{'*' if flag else ' '}] " + res[0]
    res[1] = " " * 4 + res[1]

    return res


def format_option(op: str, flag: bool, op2: str = ""):
    res: list[str] = ["", ""]
    len_op = 28

    if not op:
        return [" " * 32] * 2

    res[0] = (
        f"[{'*' if flag else ' '}] "
        + op[:len_op][::-1]
        .replace("0", "°")
        .zfill(len_op)
        .replace("0", " ")
        .replace("°", "0")[::-1]
    )
    res[1] = " " * 4 + (
        (op2[:len_op] if op2 else op[len_op : 2 * len_op])[::-1]
        .replace("0", "°")
        .zfill(len_op)
        .replace("0", " ")
        .replace("°", "0")[::-1]
    )
    return res


def draw_menu(a, b, c, d, e):
    global frame
    frame[14] = [_ for _ in "+" + "-" * 78 + "+"]

    choose = [False] * 4
    if e >= 0:
        choose[e] = True

    op_a = format_option(a, choose[0], "op2")
    op_b = format_option(b, choose[1])
    op_c = format_option(c, choose[2])
    op_d = format_option(d, choose[3])

    frame[16] = [_ for _ in f"|      {op_a[0]}  {op_b[0]}      |"]
    frame[17] = [_ for _ in f"|      {op_a[1]}  {op_b[1]}      |"]
    frame[19] = [_ for _ in f"|      {op_c[0]}  {op_d[0]}      |"]
    frame[20] = [_ for _ in f"|      {op_c[1]}  {op_d[1]}      |"]


def draw_character(pers: str, pos: int = 4, emotion: str = ""):
    global frame
    characters = {
        "WHITE": [
            "###########################",
            "###########################",
            "###########################",
            "###########################",
            "###########################",
            "###########################",
            "###########################",
            "###########################",
            "###########################",
            "###########################",
            "###########################",
            "###########################",
            "###########################",
        ],
        "TOTORO": [
            r"                     ",
            r"                     ",
            r"      /\    /\       ",
            r"     /  \__/  \      ",
            r"    +          +     ",
            r"   {  (0) _ (0) }    ",
            r"  >>>>   =+=   <<<<  ",
            r"  /      ._.      \  ",
            r" /    .#^###^#.    \ ",
            r" /   .###^###^#.   \ ",
            r"|   .#^#########.   |",
            r"|   .###########.   |",
            r"\    .#########.    /",
        ],
    }

    emotions = {"WHITE": {}, "TOTORO": {"sleep": {5: r"   {  (_) _ (_) }    "}}}

    if pers not in characters:
        pers = "WHITE"

    width = len(characters[pers][0])
    if width + pos >= 80:
        pos = 80 - width - 2

    idx = 1
    for line in characters[pers]:
        frame[idx][0] = "|"
        for c in range(len(line)):
            frame[idx][c + pos + 1] = line[c]
        idx += 1

    if emotion and emotion in emotions[pers]:
        for line_num, newline in emotions[pers][emotion].items():
            for c in range(len(newline)):
                frame[line_num+1][c + pos + 1] = newline[c]
    elif emotion and emotion not in emotions:
        1 / 0        

def draw():
    print("\033[H", end="")
    for i in frame:
        print("".join(i), end="\r\n")
    
    print("\033[24;1H", end="", flush=True)
    print(" ~ % ", end="", flush=True)


# clear_frame()
# add_border(frame)
# draw_menu("00000", "213", "OLEG", "", 0)
# draw_character("TOTORO", 100)

if __name__ == "__main__":
    pos = 4
    x = 1
    while True:
        clear_frame()
        add_border()
        draw_menu(
            "KEKS",
            "TILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILTTILT",
            "OLEG",
            "",
            0,
        )
        if x:
            draw_character("TOTORO", pos, "sleep")
            x = 0
        else:
            draw_character("TOTORO", pos, )
            x = 1
        # pos += 10
        # pos %= 80
        # print(frame)
        draw()
        time.sleep(0.5)

r"""

+------------------------------------------------------------------------------+
|                                                                              |
|                                                                              |
|                                 _+=----------=+_                             |
|          /\    /\              /  text          \                            |
|         /  \__/  \             |                |                            |
|        +          +            |                |                            |
|       {  (0) _ (0) }           /                /                            |
|      >>>>   =+=   <<<<        |/"+------------=^                             |
|      /      ._.      \                                                       |
|     /    .#^###^#.    \                                                      |
|     /   .###^###^#.   \                                                      |
|    |   .#^#########.   |                                                     |
|    |   .###########.   |                                                     |
|    \    .#########.    /                                                     |
+------------------------------------------------------------------------------+
|                                                                              |
|      [*] op1                           [ ] TILTTILTTILTTILTTILTTILTTILT      |
|          op1.2                             TILTTILTTILTTILTTILTTILTTILT      |
|                                                                              |
|      [ ] OLEG                                                                |
|                                                                              |
|                                                                              |
+------------------------------------------------------------------------------+

darw_buble(x, y, w, h, l/r, text)

x, y - позиция левого нижнего угла
w, h - размер внутренего окна для текста
l/r - направление (буль)


    _+=----------=+_
   /                \
   |                |
   \                /
    ^=------------=^


    _+=----------=+_
   /  text          \
   |                |
   |                |
   \                 \
    ^=------------+"\|
                     


"""
