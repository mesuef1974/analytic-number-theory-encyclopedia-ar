# إيصال البناء المحلي — الفصل السادس عشر

التاريخ: 2026-07-24

```text
CHAPTER                 = 16
VERSION                 = 0.20.0-dev
BRANCH                  = agent/chapter-16-sieve-applications-prime-gaps-v0.20.0
BUILD-COMMAND           = .\scripts\build.ps1 -Clean
BUILD-PIPELINE          = XELATEX -> BIBER -> XELATEX -> XELATEX
LOCAL-BUILD             = PASS
FINAL-PDF-PAGES         = 227
UNDEFINED-CITATIONS     = 0
UNDEFINED-REFERENCES    = 0
LATEX-ERRORS            = 0
FATAL-ERRORS            = 0
SHA256                  = FB478B145D0D37581AB018D7D615F36D5A052EEC61D06F42A01E16D71FBF50DD
```

## مخرجات البناء

- `build/main.pdf`
- `releases/preview.pdf`

## التحقق المرجعي

قرأ Biber بنجاح ملفات المراجع الأربعة:

- `manuscript/bibliography.bib`
- `manuscript/chapter-13-bibliography.bib`
- `manuscript/chapter-15-bibliography.bib`
- `manuscript/chapter-16-bibliography.bib`

ظهرت إحالات الفصل السادس عشر في التمرير الأول بوصفها غير معرّفة، وهو السلوك المتوقع قبل تشغيل Biber. بعد تشغيل Biber وتمريرَي XeLaTeX اللاحقين اختفت تحذيرات الإحالات والمراجع غير المعرّفة الخاصة بالفصل.

## التحذيرات غير الحاجبة

بقيت تحذيرات تنضيدية لا تمنع البناء ولا تغير النتائج الرياضية:

1. `Overfull/Underfull \hbox` في مواضع متعددة، وأكثرها موروث من فصول سابقة والفهرس.
2. محارف عربية أو علامات اتجاه داخل سياقات تستخدم Latin Modern.
3. تحذير `biblatex` بأن اللغة العربية تستعمل تعريفات توطين بديلة.
4. تحذيرات `hyperref` عند وجود رموز رياضية في عناوين الفهرس.
5. تحذير `microtype` غير الحاجب المتعلق برقعة الحاشية.

## الحكم

```text
BUILD-GATE              = PASS
REFERENCE-BUILD-GATE    = PASS
TYPOGRAPHY-WARNINGS     = NONBLOCKING
REVIEWED                = NOT DECIDED BY THIS RECEIPT
RELEASE-READY           = NO
```

هذا الإيصال يثبت نجاح البناء المحلي فقط، ولا يحل محل المراجعة العلمية المستقلة أو قرار المالك.