# P0-02 — فصل بناء المسودة عن بناء النشر

## النتيجة

```text
CLAIM                = REPRODUCED
IMPLEMENTATION       = FIXED
CI VERIFICATION      = PASS
INDEPENDENT REVIEW   = PASS
STATUS               = VERIFIED / CLOSED
```

## النطاق

أُنشئ مساران مستقلان للبناء:

- `draft`: نسخة تدقيقية تحتفظ بوسوم الحوكمة، ومعرفات النتائج الداخلية، وأدلة المراجعة.
- `release`: نسخة نشر مولدة من المصدر نفسه، مع إزالة مواد الحوكمة والبناء من النسخة المولدة فقط.

المصدر القانوني لم يتغير إلى نسخة منقحة يدويًا؛ بل تُولّد شجرة النشر في `build/release-src` بواسطة:

- `scripts/prepare_release_source.py`
- `scripts/check_release_pdf_text.py`

ويُبنى المساران عبر `.github/workflows/build-book.yml`.

## التحقق الآلي النهائي

رأس التنفيذ المختبر:

```text
IMPLEMENTATION HEAD = ac632552e439a4c084bfa424a8746b7dfed36813
QUALITY RUN         = 969 / PASS
BUILD RUN           = 776 / PASS
ARTIFACT ID         = 8665994526
ARTIFACT DIGEST     = sha256:1f3d79022274854241f2f2994167bb5c249a6847c994104dc60770f3aba02d7d
```

جميع خطوات البناء نجحت، ومنها:

- بناء المسودة بـ XeLaTeX وBiber.
- توليد مصدر النشر.
- بناء نسخة النشر.
- وجود ملفي PDF.
- استخراج النص من الملفين.
- إثبات احتفاظ المسودة بأدلة الحوكمة.
- فحص سلامة النص اللاتيني في الملفين.
- فحص غياب بيانات الحوكمة والبناء من نسخة النشر.

## التحقق المستقل من الأثر

تم تنزيل أثر تشغيل 776 وفحصه خارج خطوة CI.

### البصمات

```text
DRAFT SHA256   = fe7fc995dceaad6da83d583ccf795322f1bc870e337a3d6bc36d5e052bfd1b51
RELEASE SHA256 = 48be814a4d513eb825e97a0524da3a20783b278e0a4f707149caff89dac17a4e
```

### خصائص الملفين

```text
DRAFT PAGES       = 319
DRAFT SIZE        = 1231777 bytes
RELEASE PAGES     = 299
RELEASE SIZE      = 1126316 bytes
```

### فصل الحوكمة

في نص نسخة النشر كانت جميع القيم التالية صفرًا:

- `REVIEWED`, `APPROVED`, `RELEASE-READY`, `NOT-RELEASE-READY`.
- `PASS-FOR-AUTHORING`, `REFERENCE-AUDIT`, `EVIDENCE-FIRST`.
- `PRE-AUTHORING`, `POST-AUTHORING`, `OWNER-ADOPTED`, `ACTIVE-CITABLE`.
- `docs/`, `manuscript/`, `build/`, `.md`, `worktree`.
- تعليمات XeLaTeX/Biber.
- مراجع PR/Issue.
- بصمات Git ذات 40 محرفًا ووسم SHA-256.
- معرفات `ANT-THM/LEM/PROP/COR/DEF/EX/REM/OPEN-*` الداخلية.

وفي المقابل احتفظت المسودة بـ:

```text
DRAFT REVIEWED MARKERS = 21
DRAFT INTERNAL ANT IDS = 301
```

كما بقيت النصوص العلمية المطلوبة ظاهرة في نسخة النشر، ومنها:

- `Walfisz`
- `Ahlfors`
- `Helfgott`
- `Zeitschrift`

## الحكم

الفصل بين النسخة التدقيقية ونسخة النشر تحقق دون حذف مواد الحوكمة من المصدر القانوني. نسخة النشر خالية من البيانات الداخلية المحددة في بوابة P0-02، والمسودة تحتفظ بها وقابلة للتدقيق.

```text
P0-02 = REPRODUCED / FIXED / VERIFIED / CLOSED
```
