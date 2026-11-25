# 英文版翻譯進度（但以理書，17 包 P001–P017）
流程：Read en/in/Pxxx.txt → 寫 en/out/Pxxx.txt（Write 後以 cat >> 追加）→ `python3 -I scripts/en_units.py fixheb Pxxx` → `check Pxxx` 必須 ✓。
WEB 查經：`python3 -I scripts/web.py "Dan 3:18"`；術語見 en/GLOSSARY.md；不得用 subagent。
全部通過後：`python3 scripts/en_merge_dan.py`（待寫，改自 scripts/ez/en_merge.py）→ port 英文外殼 → make_site_dan（HAVE_EN）→ push → 完成報告。
已完成包：P001, P002, P003, P004, P005, P006, P007, P008, P009, P010, P011, P012, P013, P014, P015, P016, P017
