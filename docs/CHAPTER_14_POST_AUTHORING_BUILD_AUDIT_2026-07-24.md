# تدقيق ما بعد التأليف والبناء — الفصل الرابع عشر

التاريخ: 2026-07-24

```text
VERSION                    = 0.18.0-dev
CHAPTER                    = 14
AUDIT                      = POST-AUTHORING-BUILD
AUDITED-HEAD               = c6c1459
MANUSCRIPT                 = volumes/volume-01-foundations/chapters/chapter-14-barban-davenport-halberstam.tex
PDF-BUILD                  = PASS
BIBER                      = PASS
PDF-PAGES                  = 208
FATAL-ERRORS               = 0
UNDEFINED-CONTROL-SEQUENCE = 0
CHAPTER-14-ATOP-WARNING    = FIXED
CHAPTER-14-TITLE-OVERFLOW  = FIXED
CHAPTER-14-LOCAL-BLOCKERS  = 0
QUALITY-CHECKS             = PASS-FOR-CHAPTER-14
GLOBAL-LEGACY-WARNINGS     = PRESENT / NONBLOCKING
PR-26                      = DRAFT / OPEN / UNMERGED
MERGE                      = NOT AUTHORIZED
```

## 1. دليل البناء

نفذ البناء محليًا بالتسلسل:

```text
xelatex manuscript/main.tex
biber main
xelatex manuscript/main.tex
xelatex manuscript/main.tex
```

وانتهى كل تشغيل نهائيًا إلى:

```text
Output written on main.pdf (208 pages).
```

لم يظهر `Fatal error` ولا `Undefined control sequence`، ونجح Biber في قراءة ملفي المراجع وكتابة `main.bbl`.

## 2. تصحيحات الفصل الرابع عشر

أغلق الالتزام `c6c1459` الملاحظتين المحليتين المتبقيتين:

1. استبدال استعمال `\atop` بصيغة `\substack` المتوافقة مع `amsmath`.
2. اختصار عنوان المبرهنة المركزية لإزالة تجاوز العرض الخاص بالفصل الرابع عشر.

تحقق `git diff --check` بعد إزالة BOM والسطر الزائد في نهاية الملف، ولم يبق إلا تحذير تحويل نهايات الأسطر `LF/CRLF` المحلي، وهو غير متعلق بمحتوى LaTeX ولا يغير المصدر الملتزم.

## 3. التحذيرات المتبقية

السجل الكامل ما يزال يحتوي على تحذيرات قديمة أو عامة من:

- الفهرس العام؛
- فصول سابقة؛
- `biblatex` مع اللغة العربية؛
- خطوط Latin Modern في مواضع عربية داخل المراجع؛
- صناديق `Overfull/Underfull` خارج الفصل الرابع عشر.

هذه التحذيرات لم تُنشأ بواسطة البرهان أو صياغة الفصل الرابع عشر، ولا تمنع بناء PDF. التحذير المحلي الوحيد المتبقي داخل الفصل 14 كان تجاوزًا صغيرًا في فقرة الحالة الافتتاحية (`2.69038pt`) وهو تنسيقي غير حاجز ولا يمس المبرهنة أو البرهان.

## 4. ملف PDF المحلي

`main.pdf` ناتج بناء محلي وغير متتبع. لا ينبغي إضافته إلى Git ما لم تعتمد سياسة المشروع صراحة حفظ ملفات المعاينة الثنائية. بقاؤه `untracked` لا يعني أن الشجرة المصدرية غير نظيفة من حيث الملفات المتتبعة.

## 5. الحكم

```text
CHAPTER-14-MANUSCRIPT      = BUILD-PASS
CHAPTER-14-INTEGRATION     = PASS
CHAPTER-14-LOCAL-WARNINGS  = NONBLOCKING-ONLY
POST-AUTHORING-BUILD-AUDIT = PASS
QUALITY-CHECKS-CHAPTER-14  = PASS
GLOBAL-PDF-CLEANUP         = DEFERRED / CROSS-CHAPTER
READY-FOR-FINAL-CHAPTER-REVIEW = YES
MERGE                      = NOT AUTHORIZED
```

الخطوة التالية هي المراجعة النهائية للمتن المؤلف مقابل حزمة البرهان المعتمدة، ثم قرار تحويل PR #26 من Draft أو دمجه، ولا يحدث أي منهما دون إذن المالك الصريح.
