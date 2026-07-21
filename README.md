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
- [سجل نتائج الفصل الثالث عشر](docs/RESULTS_REGISTRY_CHAPTER_13.md)
- [سجل أدلة الفصل الثالث عشر](research/literature-reviews/chapter-13-bombieri-vinogradov-evidence.md)
- [خريطة برهان الفصل الثالث عشر](research/literature-reviews/chapter-13-bombieri-vinogradov-proof-map.md)
- [تدقيق ما قبل تأليف الفصل الثالث عشر](docs/CHAPTER_13_PRE_AUTHORING_AUDIT_2026-07-21.md)
- [تدقيق الغربال الكبير والقيمة المتوسطة](docs/CHAPTER_13_LARGE_SIEVE_MEAN_VALUE_AUDIT_2026-07-21.md)
- [تدقيق هوية Vaughan](docs/CHAPTER_13_VAUGHAN_IDENTITY_AUDIT_2026-07-21.md)
- [تدقيق Type I وType II](docs/CHAPTER_13_TYPE_I_TYPE_II_MEAN_VALUE_AUDIT_2026-07-21.md)
- [تدقيق الموصل والشخصية الرئيسية](docs/CHAPTER_13_CONDUCTOR_PRINCIPAL_BV_AUDIT_2026-07-21.md)
- [التدقيق المنطقي للفصل الثالث عشر](docs/CHAPTER_13_LOGIC_AUDIT_2026-07-21.md)
- [التحقق المرجعي للفصل الثالث عشر](docs/CHAPTER_13_REFERENCE_VERIFICATION_2026-07-21.md)
- [تدقيق ما بعد تأليف الفصل الثالث عشر](docs/CHAPTER_13_AUTHORING_AUDIT_2026-07-21.md)
- [التحقق المرجعي بعد التأليف](docs/CHAPTER_13_POST_AUTHORING_REFERENCE_AUDIT_2026-07-21.md)
- [المراجعة المستقلة للفصل الثاني عشر](docs/CHAPTER_12_INDEPENDENT_REVIEW_2026-07-20.md)
- [إيصال إغلاق مراجعة الفصل الثاني عشر](docs/CHAPTER_12_REVIEW_CLOSURE_2026-07-21.md)
- [سجل التجارب الحاسوبية](docs/EXPERIMENTS_REGISTRY.md)

## الحالة الحالية

الإصدار: `v0.17.0-dev`

```text
BASE-MAIN                 = 607c6f8ad76f8085828f49ce6b566c846950ab2a
BRANCH                    = agent/chapter-13-bombieri-vinogradov-v0.17.0
CHAPTER-12                = REVIEWED / MERGED
CHAPTER-13                = VERIFIED
PRE-AUTHORING-GATE        = CLOSED / PASS
POST-AUTHORING-AUDIT      = PASS
LOGIC-AUDIT               = PASS
REFERENCE-VERIFICATION    = PASS
RESULTS                   = 11
LARGE-SIEVE               = CITED / COMPOSITE-INPUT
VAUGHAN-IDENTITY          = PROVED-HERE
TYPE-I                    = PROVED-HERE
TYPE-II                   = PROVED-HERE
BOMBIERI-VINOGRADOV       = PROVED-HERE / INEFFECTIVE-CONSTANT
QUALITY-CHECKS            = RUN-340 / SUCCESS
PDF-BUILD                 = RUN-334 / SUCCESS
INDEPENDENT-REVIEW        = NOT YET STARTED
PR-22                     = DRAFT / UNMERGED
MERGE                     = NOT AUTHORIZED
RELEASE-READY             = NO
```

## الفصل الثالث عشر

يثبت الفصل مبرهنة بومبييري--فينوغرادوف في الصيغة:

\[
\sum_{q\le Q}
\max_{(a,q)=1}
\sup_{2\le y\le x}
\left|
\psi(y;q,a)-\frac{y}{\varphi(q)}
\right|
\ll_A \frac{x}{(\log x)^A},
\qquad
Q\le \frac{x^{1/2}}{(\log x)^{A+3}}.
\]

كما يثبت النسخ الموافقة لـ\(\vartheta\) و\(\pi\)، ونتيجة «تقريبًا كل الترديدات». يعتمد على حزمة الغربال الكبير بوصفها مدخلًا مقتبسًا، ويثبت داخليًا هوية Vaughan وPólya--Vinogradov وتقديري Type I وType II ومبرهنة القيمة المتوسطة ورد الموصلات.

الثابت النهائي غير فعال لأن المسار يستعمل Siegel--Walfisz للموصلات الصغيرة. لا يثبت الفصل Elliott--Halberstam أو مستوى توزيع عامًا أكبر من \(1/2\)، ولا يعالج الفترات القصيرة أو Barban--Davenport--Halberstam.

## الفصل بين النتائج

1. **الفصل العاشر:** نتيجة نوعية لترديد ثابت.
2. **الفصل الثاني عشر:** انتظام فردي عندما \(q\le(\log x)^A\).
3. **الفصل الثالث عشر:** انتظام متوسطي حتى مستوى \(1/2\) مع خسارة لوغاريتمية.
4. **Elliott--Halberstam:** تخمين أقوى خارج النطاق.
5. **نتائج ما بعد \(1/2\):** تحتاج أوزانًا أو بنى خاصة، ولا تثبت التخمين العام.

## حالة الفصول

- الفصول الثلاثة عشر الأولى مرتبطة بالملف الجامع وتظهر في بناء PDF الحالي.
- الفصول من السابع إلى الثاني عشر بحالة `REVIEWED`.
- الفصل الثالث عشر بحالة `VERIFIED`، وتبقى المراجعة المستقلة مطلوبة قبل `REVIEWED`.
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
