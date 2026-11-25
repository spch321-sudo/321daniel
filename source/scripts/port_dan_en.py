# -*- coding: utf-8 -*-
"""移植 Ezekiel 英文外殼 → Daniel（build/shell_dan_en.html）。每項替換斷言找到。"""
import json,re
s=open('/home/claude/spch321-sudo/321ezekiel/en.html',encoding='utf-8').read()
M='<script id="DATA" type="application/json">'
i=s.find(M); j=s.find('</script>',i)
shell=s[:i]+'@@DATA@@'+s[j:]
def sub(old,new,cnt=None,regex=False):
    global shell
    c=len(re.findall(old,shell,re.S)) if regex else shell.count(old)
    assert c>0 and (cnt is None or c==cnt),f'替換失敗 {old[:50]!r} 找到{c}'
    shell=re.sub(old,lambda m:new,shell,flags=re.S) if regex else shell.replace(old,new)
    print('✓',c,old[:40].replace('\n',' '))
# 保護：書卷表等中的 Ezekiel/Jeremiah
PROT=['{"n":26,"t":"Ezekiel","a":["Ezek","Eze","Ezk"]','["Ezekiel",26]','["Ezek",26]',
      "proph: 'Isaiah Jeremiah Lamentations Ezekiel Daniel",'["Jeremiah",24]','"t":"Jeremiah","a":["Jer","Je"]',"jeremiah: 'Jeremiah'"]
for k,p in enumerate(PROT):
    assert p in shell,p; shell=shell.replace(p,f'@@P{k}@@')
ARCS=[["Resolve",1,1,"Resolve: resolved in the palace — the names were changed, the heart was not; he would not defile himself with the king’s food; God gave him favor with the chief of the eunuchs"],
["Dream",2,2,"Dream: the dream of the four kingdoms — the stone cut without hands breaks the kingdoms and becomes a great mountain; wisdom and might belong to God"],
["Refining",3,5,"Refining: the furnace and the humbled king — but if not; the presence in the fire; the Most High rules in the kingdom of men; the writing on the wall, you are weighed in the balances"],
["Pit",6,6,"Pit: the lions’ den — praying as before; the kingdom of the living God will not be destroyed"],
["Visions",7,8,"Visions: the visions — the four beasts and the Ancient of Days, the Son of Man receives the kingdom; the ram, the goat and the little horn"],
["Prayer",9,9,"Prayer: prayer and the seventy sevens — understood from the books; a prayer of confession, not for our righteousness but for his great mercies"],
["End",10,12,"End: the last vision — setting the heart to understand, greatly beloved; the king of the north and the king of the south; the people who know their God will be strong; go your way until the end"]]
sub(r'const ARCS = \[.*?\];   /\* eight movements','const ARCS = '+json.dumps(ARCS,ensure_ascii=False)+';   /* seven movements',1,True)
sub("const LASTCH = 48;","const LASTCH = 12;",1)
sub('ezk','dan')
sub('以西結書','但以理書'); sub('以西结书','但以理书')
sub('n === 26 && ch >= 1 && ch <= 48','n === 27 && ch >= 1 && ch <= 12',1)
sub('r.n === 26 && r.ch >= 1 && r.ch <= 48','r.n === 27 && r.ch >= 1 && r.ch <= 12',1)
sub("setTitle('Ezek ' + n","setTitle('Dan ' + n",2)
sub("setTitle(\\'Ezek \\' + n","setTitle(\\'Dan \\' + n") if "setTitle(\\'Ezek" in shell else None
sub('Forty-Eight Lessons','Twelve Lessons',1)
sub('Read from chapter one through chapter forty-eight.','Read from chapter one through chapter twelve.',1)
sub('Follow one Hebrew word through all forty-eight chapters','Follow one Hebrew or Aramaic word through all twelve chapters',1)
sub('forty-eight','twelve'); sub('1,273','357')
sub('Show the Hebrew original text','Show the Hebrew and Aramaic original text',1)
sub('the Hebrew text stays off to begin with','the original-language text stays off to begin with',1)
sub('(e.g. 3:9, listen, שָׁמַע)','(e.g. 3:18, serve, פְּלַח)',1)
# map
MAPH='''    <div class="card"><p style="margin:0 0 10px"><b>Resolve</b> (1)　<b>1:8</b> resolved not to defile himself　→　<b>1:17</b> God gave them knowledge and skill</p>
    <p style="margin:0 0 10px"><b>Dream</b> (2)　<b>2:20</b> wisdom and might belong to God　→　<b>2:34–35</b> a stone cut out without hands　→　<b>2:44</b> the God of heaven will set up a kingdom</p>
    <p style="margin:0 0 10px"><b>Refining</b> (3–5)　<b>3:18</b> but if not　→　<b>3:25</b> a fourth in the fire　→　<b>4:17</b> the Most High rules in the kingdom of men　→　<b>5:27</b> weighed in the balances</p>
    <p style="margin:0 0 10px"><b>Pit</b> (6)　<b>6:10</b> as he did before　→　<b>6:26</b> the kingdom of the living God will not be destroyed</p>
    <p style="margin:0 0 10px"><b>Visions</b> (7–8)　<b>7:9</b> the Ancient of Days sat down　→　<b>7:13–14</b> one like a son of man receives the kingdom　→　<b>7:27</b> the kingdom given to the holy people　→　<b>8:25</b> broken without human hands</p>
    <p style="margin:0 0 10px"><b>Prayer</b> (9)　<b>9:2</b> I understood from the books　→　<b>9:18</b> not for our righteousness　→　<b>9:23</b> you are greatly beloved</p>
    <p style="margin:0"><b>End</b> (10–12)　<b>10:12</b> you set your heart to understand　→　<b>11:32</b> the people who know their God will be strong　→　<b>12:3</b> those who are wise will shine　→　<b>12:13</b> go your way until the end</p></div>
    <div class="card"><p class="eyebrow">The book’s axis · six turning points</p>
    <table><tr><th>Turning point</th><th>Text</th></tr>
    <tr><td><b>① Resolved in the palace: not defiled, not bowing, praying as before</b></td><td>1:8; 3:18; 6:10</td></tr><tr><td><b>② A kingdom no hand can stop: the stone breaks the kingdoms</b></td><td>2:34–35; 2:44</td></tr><tr><td><b>③ The king humbled: the Most High rules in the kingdom of men</b></td><td>4:17; 4:34–35; 5:27</td></tr><tr><td><b>④ The Son of Man receives the kingdom: the Ancient of Days and the Son of Man</b></td><td>7:13–14; 7:27</td></tr><tr><td><b>⑤ Prayer and understanding: from the books, greatly beloved</b></td><td>9:2; 9:23; 10:12</td></tr><tr><td><b>⑥ Go your way until the end: you will rest, and you will stand</b></td><td>11:32; 12:3; 12:13</td></tr></table></div>`;'''
sub(r'    <div class="card"><p style="margin:0 0 10px"><b>Call</b> \(1–3\).*?<td>43:5; 47:9; 48:35</td></tr></table></div>`;',MAPH,1,True)
sub('From the glory departing, to Yahweh Is There.','From resolve in the palace, to “you will stand.”',1)
sub('In eight movements the whole book follows one line: the glory of God departs, and returns; for the sake of his own name he makes people know that he is Yahweh; he himself becomes their shepherd, gives a new heart and a new spirit, makes dry bones live, and at last gives the city a name: “Yahweh Is There.”','In seven movements the whole book follows one line: the God of heaven rules; his people, living in another’s kingdom, can still refuse to be defiled, refuse to bow, and pray as before; and history ends with the Son of Man receiving the kingdom, which is given to the holy people of the Most High.',1)
# 工具頁說明
sub('<span class="s">Follow one Hebrew or Aramaic word','<span class="s">Follow one Hebrew or Aramaic word',1)
# Xiaozhi rules
lines=shell.split('\n')
def fl(t):
    k=[x for x,l in enumerate(lines) if t in l]; assert len(k)==1,(t,k); return k[0]
lines[fl("'3. Disputes are not adjudicated")]="    '3. Disputes are not adjudicated: on the date of composition and the two languages of the book, which four kingdoms, who “one like a son of man” is, how to read the seventy sevens, the fourth figure in the fire, Nebuchadnezzar’s madness and confession, the spiritual conflict of chapter 10 and “the prince of the kingdom of Persia,” the counted days at the end and the naming of “the antichrist,” and how chapter 11 reads against history — always state first what all sides agree on, then present the main positions, and only then the position of these notes; never adjudicate, and never make political judgments.',"
lines[fl("'2. Honesty about the Hebrew")]="    '2. Honesty about the original: when you mention Hebrew or Aramaic, say whether it is a verifiable fact (same word / same root / verb form) or \"one possible reading\". If you are not sure, do not bring up the original language.',"
b=fl("Do not judge people, do not get entangled in politics"); c=fl("If they come about their own sin")
new=["    'Do not judge people, do not get entangled in politics, do not pass verdicts on particular churches or people. Daniel is not a timetable and not a footnote to modern politics — its focus is: the God of heaven rules; his people, living in another’s kingdom, can still refuse to be defiled, refuse to bow, and pray as before; and history ends with the Son of Man receiving the kingdom, which is given to the holy people of the Most High.',",
"    'The end times and prophecy: the seventy sevens, “a time, times, and a half,” the 2,300 evenings and mornings, the 1,290 days and the 1,335 days — do not count days, do not draw timetables, and do not identify any modern person, regime or organization as “the little horn” or “the antichrist”; what calls people to endure, hold fast and wait today is the original meaning; the fruit is patience, not panic.',",
"    'Chapter 3, “But if not”: never preach it as the prosperity gospel or as “if only you have faith God will rescue you”; its point is that God is able to deliver, and even if not, we will not serve other gods; to those who have lost, suffered or were not rescued, never say “your faith was not enough” — stay with them first.',",
"    'Readers may be living where faith is restricted (persecution, surveillance, no public profession): do not ask for public testimony, do not ask where they are or for details, and do not record anything traceable; encourage safe ways — God with them in the heart, and trusted companions.',",
"    'Nebuchadnezzar\\'s madness and confession in chapter 4: stop where the text stops and do not decide his eternal destiny; the spiritual conflict of chapter 10: do not teach identifying, naming or binding territorial spirits — the point is 10:12: setting the heart to understand, humbling oneself before God, and being heard.',",
"    'Despair and self-harm: if someone says life feels meaningless or they want to disappear, stay with them gently and take it seriously; never say \"just have faith\" and never answer with passages of judgment; encourage them to contact someone they trust and their pastor right away. In Taiwan they can call the 1925 mental-health hotline, or 119 in an emergency; elsewhere, their local crisis line and emergency number.',"]
lines[b:c]=new
shell='\n'.join(lines)
sub('Ezekiel','Daniel')
for k,p in enumerate(PROT): shell=shell.replace(f'@@P{k}@@',p)
shell=shell.replace('Daniel Daniel','Daniel')
# 書卷表：Daniel 的別名保持；清掉Ezekiel專屬殘留
left=[(m.group(0),shell[max(0,m.start()-60):m.end()+60]) for m in re.finditer(r'Ezekiel|Ezek\b|Chebar|Gog|Tyre|Yahweh Is There|Sheol|glory departs',shell)]
print('剩',len(left))
for l in left: print('  ',repr(l[1]))
open('build/shell_dan_en.html','w',encoding='utf-8').write(shell)
