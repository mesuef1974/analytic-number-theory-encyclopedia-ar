# الموسوعة الشاملة في نظرية الأعداد التحليلية

**العنوان الكامل:** الموسوعة الشاملة في نظرية الأعداد التحليلية: من الأسس إلى الجبهات البحثية الحديثة

**الإصدار التطويري الحالي:** `v0.21.0-dev`

مشروع موسوعة عربية بحثية متقدمة في نظرية الأعداد التحليلية، من الأسس إلى طرق الغربال والطريقة الدائرية والمجاميع الأسية والجبهات الحديثة.

## وثائق المشروع

- [أهداف المشروع](docs/PROJECT_GOALS.md)
- [تقدم المشروع](docs/PROGRESS.md)
- [خارطة الطريق](docs/ROADMAP.md)
- [قائمة المهام](docs/TODO.md)
- [الإصدار الحالي](docs/VERSION.md)
- [سياسة اعتماد النتائج](docs/RESULT_STATUS_POLICY.md)
- [سجل النتائج](docs/RESULTS_REGISTRY.md)
- [سجل نتائج الفصل السادس عشر](docs/RESULTS_REGISTRY_CHAPTER_16.md)
- [سجل نتائج الفصل السابع عشر](docs/RESULTS_REGISTRY_CHAPTER_17.md)

## الحالة الحالية

```text
BASE-MAIN                  = 0bd442bc48490115bed48b18ed32783ad5bd1c9c
VERSION                    = 0.21.0-dev
<<<<<<< HEAD
CHAPTERS-IN-MANUSCRIPT     = 1--17 ON WORK BRANCH
CHAPTER-16                 = REVIEWED / OWNER-ADOPTED / MERGED
PR-31                      = MERGED
CHAPTER-17                 = AUTHORED-DRAFT / BATCH-02
BRANCH-17                  = agent/chapter-17-circle-method-goldbach-waring-v0.21.0
ISSUE-32                   = OPEN
PR-33                      = DRAFT / OPEN / UNMERGED
PRE-AUTHORING-GATE-17      = CLOSED
PASS-FOR-AUTHORING-17      = YES
REFERENCE-AUDIT-17         = INITIAL PASS
MATHEMATICAL-AUDIT-17      = INITIAL PASS WITH OPEN ITEMS
PDF-BUILD-17               = NOT YET RUN
=======
CHAPTERS-IN-MANUSCRIPT     = 1--16
CHAPTER-16                 = REVIEWED / OWNER-ADOPTED / MERGED
PR-31                      = MERGED
CHAPTER-17                 = EVIDENCE-FIRST / PRE-AUTHORING
BRANCH-17                  = agent/chapter-17-circle-method-goldbach-waring-v0.21.0
ISSUE-32                   = OPEN
PR-33                      = DRAFT / OPEN / UNMERGED
PRE-AUTHORING-GATE-17      = OPEN
PASS-FOR-AUTHORING-17      = NO
>>>>>>> origin/main
RELEASE-READY              = NO
```

## آخر نتائج معتمدة

في الفصل السادس عشر أُثبت داخليًا، لكل عدد زوجي ثابت غير صفري \(h\):

\[
\pi_2(x;h)\ll_h \frac{x}{(\log x)^2},
\]

واستُنتج تقارب مجموع مقلوبات الأزواج الأولية ذات الفرق الثابت بالجمع الجزئي. كما عُرضت مبرهنات تشن وGPY وZhang وMaynard وPolymath8b بوصفها نتائج `CITED` موثقة، من دون ادعاء حدسية الأوليات التوأم أو \(H_1=2\).

## المرحلة الجارية

<<<<<<< HEAD
الفصل السابع عشر: **الطريقة الدائرية ومدخل إلى غولدباخ ووارينغ**.

أُنجزت دفعتا التأليف الأولى والثانية، وتشملان:

- تعامد الدوال الأسية وهوية عد التمثيلات.
- الأقواس الكبرى والصغرى.
- المجموع المحلي والتقريب الأرخميدي.
- السلسلة المفردة والتكامل المفرد.
- الصيغة الكلاسيكية في وارينغ بوصفها `CITED / EXPLAINED`.
- مبرهنتي فينوغرادوف وهلفغوت بوصفهما `CITED`.
- غولدباخ الثنائية بوصفها `HYPOTHESIS / OPEN`.

لا يزال بناء PDF والتدقيق الرياضي والمرجعي النهائي والمراجعة المستقلة مطلوبًا قبل أي ترقية.

## بناء PDF

آخر بناء كامل معتمد يخص الفصل السادس عشر:
=======
الفصل السابع عشر: **الطريقة الدائرية ومدخل إلى غولدباخ ووارينغ**. التأليف محجوب حتى إغلاق سجل الأدلة، خريطة البرهان، تدقيق المصادر الأولية، تدقيق عدم الدور، وتثبيت نطاق الأقواس الكبرى والصغرى.

## بناء PDF

آخر بناء كامل معتمد:
>>>>>>> origin/main

```text
XeLaTeX -> Biber -> XeLaTeX -> XeLaTeX
PDF = 227 pages
UNDEFINED CITATIONS = 0
UNDEFINED REFERENCES = 0
```

<<<<<<< HEAD
لا تعني المراجعة أو الدمج أن الموسوعة `RELEASE-READY`.
=======
لا تعني المراجعة أو الدمج أن الموسوعة `RELEASE-READY`.
>>>>>>> origin/main
