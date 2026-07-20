# الموسوعة الشاملة في نظرية الأعداد التحليلية

**العنوان الكامل:** الموسوعة الشاملة في نظرية الأعداد التحليلية: من الأسس إلى الجبهات البحثية الحديثة

مشروع موسوعة عربية بحثية متقدمة في نظرية الأعداد التحليلية، تبدأ من الأسس التحليلية والحسابية، ثم تنتقل إلى دالة زيتا ودوال \(L\)، وتوزيع الأعداد الأولية، وطرق الغربال، والطريقة الدائرية، والمجاميع الأسية، والأشكال الآلية، والتحليل الطيفي، وصولًا إلى الجبهات البحثية الحديثة والمسائل المفتوحة.

## وثائق المشروع

- [أهداف المشروع بالتفصيل](docs/PROJECT_GOALS.md)
- [تقدم المشروع](docs/PROGRESS.md)
- [خارطة الطريق](docs/ROADMAP.md)
- [سجل العمل](docs/WORKLOG.md)
- [قائمة المهام](docs/TODO.md)
- [الإصدار الحالي](docs/VERSION.md)
- [دليل بناء PDF](docs/BUILD.md)
- [سياسة اعتماد النتائج](docs/RESULT_STATUS_POLICY.md)
- [سجل النتائج المعتمدة](docs/RESULTS_REGISTRY.md)
- [سجل أدلة الفصل الثالث عشر](research/literature-reviews/chapter-13-bombieri-vinogradov-evidence.md)
- [خريطة برهان الفصل الثالث عشر](research/literature-reviews/chapter-13-bombieri-vinogradov-proof-map.md)
- [تدقيق ما قبل تأليف الفصل الثالث عشر](docs/CHAPTER_13_PRE_AUTHORING_AUDIT_2026-07-21.md)
- [سجل أدلة الفصل الثاني عشر](research/literature-reviews/chapter-12-siegel-walfisz-evidence.md)
- [خريطة برهان الفصل الثاني عشر](research/literature-reviews/chapter-12-siegel-walfisz-proof-map.md)
- [المراجعة المستقلة للفصل الثاني عشر](docs/CHAPTER_12_INDEPENDENT_REVIEW_2026-07-20.md)
- [إيصال إغلاق مراجعة الفصل الثاني عشر](docs/CHAPTER_12_REVIEW_CLOSURE_2026-07-21.md)
- [إيصال البناء المحلي المتزامن](docs/LOCAL_BUILD_RECEIPT.md)
- [سجل التجارب الحاسوبية](docs/EXPERIMENTS_REGISTRY.md)

## الحالة الحالية

الإصدار: `v0.17.0-dev`

```text
BASE-MAIN                 = 607c6f8ad76f8085828f49ce6b566c846950ab2a
BRANCH                    = agent/chapter-13-bombieri-vinogradov-v0.17.0
CHAPTER-12                = REVIEWED / MERGED
PR-20                     = MERGED
GOVERNANCE-PR-21          = MERGED
CHAPTER-13                = PRE-AUTHORING
MODE                      = EVIDENCE-FIRST
PRE-AUTHORING-GATE        = OPEN
AUTHORING                 = BLOCKED
CENTRAL-TARGET            = BOMBIERI--VINOGRADOV / NOT YET ADOPTED
PROOF-ROUTE               = VAUGHAN-IDENTITY + LARGE-SIEVE / CANDIDATE
LEVEL-OF-DISTRIBUTION     = 1/2 WITH LOGARITHMIC LOSS / TARGET
DEPENDENCY-AUDIT          = OPEN
LOG-LOSS-AUDIT            = OPEN
EFFECTIVITY-AUDIT         = OPEN
RELEASE-READY             = NO
```

## الفصل الثالث عشر — النطاق المخطط

الهدف المرشح هو إثبات أنه لكل \(A>0\) يوجد \(B=B(A)>0\) بحيث، إذا

\[
Q\le \frac{x^{1/2}}{(\log x)^B},
\]

فإن

\[
\sum_{q\le Q}
\max_{(a,q)=1}
\max_{2\le y\le x}
\left|
\psi(y;q,a)-\frac{y}{\varphi(q)}
\right|
\ll_A \frac{x}{(\log x)^A}.
\]

هذه الصيغة `TARGET / NOT YET ADOPTED`، وليست نتيجة معتمدة بعد.

### المسار المرشح

1. مرشح الشخصيات وفصل الشخصية الرئيسية.
2. الرد من الشخصيات المستحثة إلى البدائية.
3. الغربال الكبير للشخصيات البدائية.
4. هوية Vaughan وتفكيك \(\Lambda\).
5. تقديرات Type I وType II.
6. مبرهنة قيمة متوسطة لـ\(\psi(y,\chi)\) مع `max_{y\le x}`.
7. جمع الموصلات والترديدات واستعادة الفئات الحسابية.
8. اشتقاق النسخ الموافقة لـ\(\vartheta\) و\(\pi\) و«تقريبًا كل الترديدات».

### ما يمنع التأليف الآن

- تثبيت صيغة الغربال الكبير بالصفحات والتطبيع الصحيح.
- برهان هوية Vaughan وتدقيق حدود القطع.
- إغلاق حسابي Type I وType II.
- تدقيق الانتقال بين الموصل والترديد.
- تدقيق الشخصية الرئيسية والعوامل المحلية.
- تثبيت آلية `max_{y\le x}`.
- حساب الخسائر اللوغاريتمية وتحديد شرط \(B(A)\).
- الحكم على فعالية الثوابت وفحص عدم الدور.

## الفصل بين النتائج

1. **الفصل العاشر:** نتيجة نوعية لترديد ثابت.
2. **الفصل الثاني عشر:** انتظام فردي عندما \(q\le(\log x)^A\).
3. **الفصل الثالث عشر:** انتظام متوسطي مخطط حتى مستوى \(1/2\) مع خسارة لوغاريتمية.
4. **Elliott--Halberstam:** تخمين أقوى خارج النطاق.
5. **نتائج ما بعد \(1/2\):** تحتاج أوزانًا أو بنى خاصة، وتبقى في سياق الجبهة الحديثة.

## حالة الفصول

- الفصول الاثنا عشر الأولى مرتبطة بالملف الجامع وتظهر في بناء PDF الحالي.
- الفصول من السابع إلى الثاني عشر بحالة `REVIEWED` ومندمجة في `main`.
- الفصل الثالث عشر في مرحلة `PRE-AUTHORING`; لا يوجد ملف متن له حتى الآن.
- لا يصبح أي فصل `RELEASE-READY` بمجرد التدقيق أو المراجعة أو الدمج.

## مبادئ التحرير

1. الدقة قبل الاختصار.
2. الفصل بين النتائج المثبتة، والنتائج المشروطة، والتخمينات.
3. إسناد كل ادعاء تاريخي أو بحثي إلى مصدر أصلي أو مرجع موثوق.
4. تقديم الحدس، ثم الصياغة الدقيقة، ثم البرهان، ثم التطبيقات.
5. تحديث فصل الجبهات الحديثة بحسب تاريخ إصدار كل نسخة.
6. عدم الادعاء بالشمول المطلق؛ فالموسوعة مشروع قابل للتحديث المستمر.

## بناء PDF

لمزامنة `main` والبناء المحلي:

```powershell
cd "D:\analytic-number-theory-encyclopedia-ar"
.\scripts\sync-build.ps1 -Branch main -Open
```

وللبناء فقط من الشجرة الحالية:

```powershell
.\scripts\build.ps1 -Clean -Open
```

على GitHub يُبنى PDF تلقائيًا بعد كل Push يؤثر في ملفات الكتاب، ثم يُرفع كـArtifact.

## هيكل المشروع

- `manuscript/`: الملف الجامع وإعدادات التنضيد.
- `volumes/`: المجلدات والفصول.
- `research/`: مراجعات الأدبيات وملفات الجبهات الحديثة.
- `computational/`: تجارب Python وSageMath وPARI/GP.
- `references/`: بيانات وملاحظات المراجع.
- `releases/`: النسخ النهائية المنشورة.
