import os
credits = {}
with open("credits.txt") as f:
    for l in f.readlines():
        l = l.rstrip()
        if l:
            spl = l.split("`")
            credits[spl[0]] = spl[1]



imgs = []
for x in os.listdir("img"):
    if x in credits.keys():
        imgs.append('''<div class="imgcontainer" style="background: url('img/%s') no-repeat center"><div class="imginfo">
                        <a class="imgtitle" href="img/%s">%s</a><br>
                        <span class="credit">Credit: %s</span>
                    </div></div>''' % (x, x, x.replace(".jpg", ""), credits[x]))
    else:
        imgs.append('''<div class="imgcontainer" style="background: url('img/%s') no-repeat center"><div class="imginfo">
                <a class="imgtitle" href="img/%s">%s</a>
            </div></div>''' % (x, x, x.replace(".jpg", "")))
with open("template.html") as temp:
    with open("index.html", "w") as f:
        f.write(temp.read().replace("%pics%", "\n    ".join(imgs)))