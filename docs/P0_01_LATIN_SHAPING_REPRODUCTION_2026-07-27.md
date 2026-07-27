# P0-01 — إعادة إنتاج عطل تشكيل النص اللاتيني وإغلاقه

## النطاق

```text
ISSUE                       = #59
PR                          = #60 (DRAFT)
BRANCH                      = agent/release-p0-external-review-remediation-v0.30.1
P0 ITEM                     = P0-01
MAIN MODIFICATION           = NOT PERFORMED
PR MERGE                    = NOT PERFORMED
```

## إعادة الإنتاج

أعيد استخراج نص PDF السابق بالأمر:

```powershell
pdftotext -layout .\build\main.pdf .\build\main-extracted.txt
```

وظهرت صيغ مقلوبة داخل المتن والمراجع، منها:

```text
Siegel--Waflisz
Ahflors
Lfie
Dffierence
verfiication
Zeitschrfit
Heflgott
Asfi
Scientfiique
```

وبذلك ثبت الحكم:

```text
EXTERNAL-CLAIM = REPRODUCED
P0-01           = OPEN BEFORE REMEDIATION
```

## تحليل السبب

كان `Amiri` هو خط السياق العربي، بينما عُرّف `Latin Modern Roman` لـ `\textenglish` فقط من دون سياسة صريحة لتعطيل الروابط الشائعة والاختيارية. كما أن وضع الببليوغرافيا داخل `LTR` لا يفرض وحده استعمال الخط اللاتيني. لذلك بقيت الكلمات اللاتينية غير المغلفة داخل الفقرات العربية عرضة لتشكيل `fi/fl/iff` غير السليم.

لم يُعرّف أمر جديد باسم `\LR`، ولم يظهر تعريف مشروع سابق له في الفحص.

## الإصلاح

عُدّل `manuscript/preamble.tex` كما يأتي:

1. إبقاء `Amiri` خطًا عربيًا مع تعطيل الروابط غير الإلزامية فقط:
   - `Ligatures=NoCommon`
   - `RawFeature={-liga;-clig;-dlig}`
2. تعريف `\englishfont` مستقلًا باستعمال `Latin Modern Roman` مع السياسة نفسها.
3. تطبيق السياسة نفسها على `\arabicfonttt`.
4. فرض الخط اللاتيني على الببليوغرافيا بواسطة:

```tex
\renewcommand*{\bibfont}{\footnotesize\englishfont}
```

تبقى خصائص التشكيل العربي الإلزامية المرتبطة بـ `Script=Arabic` فعالة؛ لم تُعطل خصائص `rlig` أو `curs`.

## اختبار الرجوع

أضيف:

```text
scripts/check_latin_pdf_text.py
```

ويفشل الاختبار عند ظهور أي صيغة تالفة من القائمة المعتمدة، أو عند غياب أي صيغة صحيحة متوقعة. كما أضيفت خطوة إلزامية إلى `.github/workflows/build-book.yml`:

```text
Verify Latin PDF text integrity
```

وتنفذ:

```text
pdftotext -layout build/main.pdf build/main-extracted.txt
python scripts/check_latin_pdf_text.py build/main-extracted.txt
```

## التحقق النهائي

الرأس المختبر:

```text
68da6e6b4437f54c34210c3b8a2e03cc73eefe49
```

نتائج GitHub Actions:

```text
QUALITY CHECKS              = PASS
RUN                         = 959
BUILD ENCYCLOPEDIA PDF      = PASS
RUN                         = 766
LATIN REGRESSION STEP       = PASS
PDF PAGES                   = 319
```

أظهر المسح النصي النهائي:

```text
BAD LATIN FORMS             = 0
Walfisz                     = 7
Zeitschrift                 = 2
Scientifique                = 1
Ahlfors                     = 1
Helfgott                    = 1
Difference                  = 3
Life                        = 1
Asif                        = 1
verification                = 1
EXPECTED CORRECT FORMS      = PRESENT
```

أجري فحص بصري لعينات ممثلة من PDF الناتج:

- صفحة PDF 152: `Siegel--Walfisz` داخل فقرة عربية مختلطة.
- صفحة PDF 314: `Ahlfors`, `Life`, `Difference`, `verification` في المراجع.
- صفحة PDF 316: `Zeitschrift`, `Helfgott`, `Difference` في المراجع.
- صفحة PDF 318: `Asif`, `Zeitschrift`, `Scientifique` في المراجع.

لم تظهر حروف مقلوبة أو مربعات سوداء أو تراكب أو قص في العينات المفحوصة.

## الحكم

```text
INDEX BUILD                = PASS
QUALITY CHECK              = PASS
BAD LATIN FORMS            = 0
EXPECTED CORRECT FORMS     = PRESENT
VISUAL PDF REVIEW          = PASS
PDF LATIN TEXT INTEGRITY   = PASS
P0-01                      = VERIFIED / CLOSED
P0-02                      = NOT STARTED
PUBLICATION-READY          = NO
STABLE RELEASE             = BLOCKED
```

إغلاق P0-01 لا يجيز دمج PR #60 ولا تعديل `main`. تبقى بقية حزم P0 والمراجعة المستقلة النهائية مفتوحة.
