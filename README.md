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
- [سجل نتائج الفصل الثاني عشر المحجوزة](docs/RESULTS_REGISTRY_CHAPTER_12_DRAFT.md)
- [مراجعة الفصل السابع المستقلة](docs/CHAPTER_07_INDEPENDENT_REVIEW_2026-07-19.md)
- [مراجعة الفصل الثامن المستقلة](docs/CHAPTER_08_INDEPENDENT_REVIEW_2026-07-20.md)
- [المراجعة المستقلة للفصل التاسع](docs/CHAPTER_09_INDEPENDENT_REVIEW_2026-07-20.md)
- [المراجعة المستقلة للفصل العاشر](docs/CHAPTER_10_INDEPENDENT_REVIEW_2026-07-20.md)
- [سجل أدلة الفصل الحادي عشر](research/literature-reviews/chapter-11-zero-free-regions-exceptional-zeros-evidence.md)
- [خريطة برهان الفصل الحادي عشر](research/literature-reviews/chapter-11-zero-free-regions-exceptional-zeros-proof-map.md)
- [تدقيق ما قبل تأليف الفصل الحادي عشر](docs/CHAPTER_11_PRE_AUTHORING_AUDIT_2026-07-20.md)
- [التدقيق المنطقي للفصل الحادي عشر](docs/CHAPTER_11_LOGIC_AUDIT_2026-07-20.md)
- [تدقيق ما بعد تأليف الفصل الحادي عشر](docs/CHAPTER_11_AUTHORING_AUDIT_2026-07-20.md)
- [حزمة المراجعة المستقلة للفصل الحادي عشر](docs/CHAPTER_11_INDEPENDENT_REVIEW_PACKET_2026-07-20.md)
- [المراجعة المستقلة للفصل الحادي عشر](docs/CHAPTER_11_INDEPENDENT_REVIEW_2026-07-20.md)
- [إيصال إغلاق الفصل الحادي عشر](docs/CHAPTER_11_REVIEW_CLOSURE_2026-07-20.md)
- [سجل أدلة الفصل الثاني عشر](research/literature-reviews/chapter-12-siegel-walfisz-evidence.md)
- [خريطة برهان الفصل الثاني عشر](research/literature-reviews/chapter-12-siegel-walfisz-proof-map.md)
- [تدقيق ديون بيرون والصيغة الصريحة للفصل الثاني عشر](docs/CHAPTER_12_PERRON_CONTOUR_EXPLICIT_FORMULA_AUDIT_2026-07-20.md)
- [تدقيق الصفر الاستثنائي وعدم الفعالية](docs/CHAPTER_12_EXCEPTIONAL_ZERO_INEFFECTIVITY_AUDIT_2026-07-20.md)
- [التدقيق المنطقي للفصل الثاني عشر](docs/CHAPTER_12_LOGIC_AUDIT_2026-07-20.md)
- [تدقيق ما قبل تأليف الفصل الثاني عشر](docs/CHAPTER_12_PRE_AUTHORING_AUDIT_2026-07-20.md)
- [سجل التجارب الحاسوبية](docs/EXPERIMENTS_REGISTRY.md)

## الحالة الحالية

الإصدار: `v0.16.0-dev`

```text
BASE-MAIN             = 9d02c583d416053550d22dfd7acc44d9c264a02c
BRANCH                = agent/chapter-12-siegel-walfisz-v0.16.0
CHAPTER-12            = PRE-AUTHORING / GATE-CLOSED
AUTHORING             = AUTHORIZED / NOT YET STARTED
PERRON-GENERAL-PROOF  = DEFERRED
EXPLICIT-FORMULA      = CITED-INPUT
SIEGEL-CONSTANT       = INEFFECTIVE
BOMBIERI-VINOGRADOV   = DEFERRED
RELEASE-READY         = NO
```

يتضمن الفرع الحالي:

- مراجعة أهداف المشروع وخارطة الطريق قبل التأليف.
- إنشاء الفصل الثاني عشر من رأس `main` الناتج من دمج PR #19.
- مسحًا علميًا بدأ عبر Consensus ثم تحقق من arXiv وصفحات الناشرين.
- سجل أدلة وخريطة برهان واعتمادات.
- تدقيقًا مستقلًا لديون بيرون وتحويل المسار والصيغة الصريحة.
- فصلًا صريحًا بين نتيجة الترديد الثابت في الفصل العاشر وSiegel--Walfisz وBombieri--Vinogradov.
- عزلًا صريحًا لمساهمة الصفر الاستثنائي قبل استعمال مبرهنة Siegel.
- تثبيتًا لموضع عدم فعالية الثابت النهائي.
- تدقيقًا منطقيًا بحكم `PASS` وإغلاقًا رسميًا لبوابة ما قبل التأليف.
- تسعة معرفات نتائج محجوزة بحالة `DRAFT / NON-CITABLE`.
- لا يوجد ملف متن للفصل الثاني عشر، ولم يربط فصل جديد بالكتاب بعد.

## الهدف الرياضي للفصل الثاني عشر

لكل \(A>0\)، تستهدف المرحلة إثبات صيغة موحدة من الشكل

\[
\psi(x;q,a)
=
\frac{x}{\varphi(q)}
+
O_A\!\left(xe^{-c_A\sqrt{\log x}}\right),
\qquad q\le(\log x)^A,
\]

ثم اشتقاق الصيغ الموافقة لـ\(\vartheta(x;q,a)\) و\(\pi(x;q,a)\). الثابت العام غير فعال لأن امتصاص حد الصفر الاستثنائي يعتمد على مبرهنة Siegel.

## الفصل بين النتائج

1. **الفصل العاشر:** مبرهنة الأعداد الأولية في المتتاليات الحسابية لترديد ثابت، من دون انتظام في \(q\).
2. **الفصل الثاني عشر:** Siegel--Walfisz بانتظام للترديدات \(q\le(\log x)^A\).
3. **فصل لاحق:** Bombieri--Vinogradov، وهي نتيجة متوسطية على مجال أكبر من الترديدات ولا تستعمل في هذا البرهان.

## حالة الفصول الموجودة

- الفصول الأحد عشر الأولى موجودة داخل PDF.
- الفصول السابع والثامن والتاسع والعاشر والحادي عشر بحالة `REVIEWED` ومندمجة في `main`.
- الفصل الحادي عشر مدمج عند الالتزام `fb1571eaa6328eac597ddbebda79b09d0ebd1696`.
- أغلقت حوكمة `0.15.0-dev` بدمج PR #19 عند الالتزام `9d02c583d416053550d22dfd7acc44d9c264a02c`.
- لا يصبح أي فصل `RELEASE-READY` بمجرد التدقيق أو المراجعة أو الدمج؛ تبقى ديون الإصدار المعلنة مستقلة.

## مبادئ التحرير

1. الدقة قبل الاختصار.
2. الفصل بين النتائج المثبتة، والنتائج المشروطة، والتخمينات.
3. إسناد كل ادعاء تاريخي أو بحثي إلى مصدر أصلي أو مرجع موثوق.
4. تقديم الحدس، ثم الصياغة الدقيقة، ثم البرهان، ثم التطبيقات.
5. تحديث فصل الجبهات الحديثة بحسب تاريخ إصدار كل نسخة.
6. عدم الادعاء بالشمول المطلق؛ فالموسوعة مشروع قابل للتحديث المستمر.

## بناء PDF

على Windows:

```powershell
.\scripts\build.ps1 -Clean -Open
```

وعلى GitHub يُبنى PDF تلقائيًا بعد كل Push يؤثر في ملفات الكتاب، ثم يُرفع كـArtifact. راجع [دليل بناء PDF](docs/BUILD.md).

## هيكل المشروع

- `manuscript/`: الملف الجامع وإعدادات التنضيد.
- `volumes/`: المجلدات والفصول.
- `research/`: مراجعات الأدبيات وملفات الجبهات الحديثة.
- `computational/`: تجارب Python وSageMath وPARI/GP.
- `references/`: بيانات وملاحظات المراجع.
- `releases/`: النسخ النهائية المنشورة.
