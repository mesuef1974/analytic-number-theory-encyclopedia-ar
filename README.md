# الموسوعة الشاملة في نظرية الأعداد التحليلية

**العنوان الكامل:** الموسوعة الشاملة في نظرية الأعداد التحليلية: من الأسس إلى الجبهات البحثية الحديثة

**الإصدار التطويري الحالي:** `v0.22.0-dev`

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
- [سجل نتائج الفصل الثامن عشر](docs/RESULTS_REGISTRY_CHAPTER_18.md)

## الحالة الحالية

```text
BASE-MAIN                  = 1bdaefebe1d2946c6fa728096d4f1d2f74234ad7
VERSION                    = 0.22.0-dev
CHAPTERS-IN-MANUSCRIPT     = 1--18 ON MAIN
CHAPTER-17                 = REVIEWED / OWNER-ADOPTED / MERGED
PR-33                      = MERGED
CHAPTER-18                 = REVIEWED / OWNER-ADOPTED / CITABLE
BRANCH-18                  = MERGED INTO MAIN
ISSUE-34                   = CLOSED
PR-35                      = MERGED
PRE-AUTHORING-GATE-18      = CLOSED
PASS-FOR-AUTHORING-18      = YES
POST-AUTHORING-CORRECTIONS = 3 / 3 CLOSED
PDF-REBUILD-18             = RUN-531 / PASS / 249 PAGES
INDEPENDENT-REVIEW-18      = PASS AFTER CORRECTIONS / OWNER-ADOPTED
MERGE-COMMIT-18            = 1bdaefebe1d2946c6fa728096d4f1d2f74234ad7
RELEASE-READY              = NO
```

## آخر نتائج معتمدة

في الفصل السادس عشر أُثبت داخليًا، لكل عدد زوجي ثابت غير صفري \(h\):

\[
\pi_2(x;h)\ll_h \frac{x}{(\log x)^2},
\]

واستُنتج تقارب مجموع مقلوبات الأزواج الأولية ذات الفرق الثابت بالجمع الجزئي. كما عُرضت مبرهنات تشن وGPY وZhang وMaynard وPolymath8b بوصفها نتائج `CITED` موثقة، من دون ادعاء حدسية الأوليات التوأم أو \(H_1=2\).

## المرحلة الجارية

الفصل الثامن عشر: **المجاميع الأسية وطريقة فان دير كوربوت**.

أُنجزت دفعات التأليف الثلاث، وتشمل:

- الحد التافه والجمع الجزئي وفرق فان دير كوربوت.
- اختبار المشتقة الأولى ببرهان داخلي.
- اختبار المشتقة الثانية بوصفه `CITED / EXPLAINED`.
- نسخة محدودة مثبتة من عملية `A`.
- تعريف الأزواج الأسية وعملية `B` مع مراجع فعلية.
- إغلاق تصحيحات التدقيق الثلاثة بعد دفعة التأليف الثالثة.

نجحت إعادة بناء PDF والمراجعة المستقلة الضيقة بعد التصحيحات، واعتمد المالك الفصل بحالة `REVIEWED` وأذن بدمج PR #35.

## بناء PDF

آخر بناء كامل على فرع الفصل الثامن عشر بعد تصحيحات ما بعد التأليف:

```text
XeLaTeX -> Biber -> XeLaTeX -> XeLaTeX
PDF = 249 pages
UNDEFINED CITATIONS = 0
UNDEFINED REFERENCES = 0
```

نجح البناء في GitHub Actions بلا مراجع أو إحالات غير معرّفة في المرور النهائي. لا تعني المراجعة أو الدمج أن الموسوعة `RELEASE-READY`.
