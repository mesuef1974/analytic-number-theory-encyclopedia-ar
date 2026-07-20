# تدقيق ما قبل تأليف الفصل الثاني عشر

## بيانات القرار

```text
CHAPTER       = 12 — مبرهنة Siegel--Walfisz والتوزيع المنتظم للأعداد الأولية في المتتاليات الحسابية
VERSION       = 0.16.0-dev
BRANCH        = agent/chapter-12-siegel-walfisz-v0.16.0
BASE-COMMIT   = 9d02c583d416053550d22dfd7acc44d9c264a02c
AUDIT-DATE    = 2026-07-20
AUDIT-STATE   = CLOSED / PASS
AUTHORING     = AUTHORIZED / NOT YET STARTED
```

## المواد الداخلة في التدقيق

- `docs/PROJECT_GOALS.md`
- `docs/ROADMAP.md`
- `research/literature-reviews/chapter-12-siegel-walfisz-evidence.md`
- `research/literature-reviews/chapter-12-siegel-walfisz-proof-map.md`
- `docs/CHAPTER_12_PERRON_CONTOUR_EXPLICIT_FORMULA_AUDIT_2026-07-20.md`
- `docs/CHAPTER_12_EXCEPTIONAL_ZERO_INEFFECTIVITY_AUDIT_2026-07-20.md`
- `docs/CHAPTER_12_LOGIC_AUDIT_2026-07-20.md`
- نتائج الفصول السابع والعاشر والحادي عشر المسجلة في سجل النتائج.
- مسح Consensus الأولي، ثم التحقق من arXiv وصفحات الناشرين.

## الحكم النهائي

```text
PROJECT-GOALS-REVIEW        = PASS
ROADMAP-REVIEW              = PASS
BRANCH-FROM-APPROVED-MAIN   = PASS
VERSION-TARGET              = 0.16.0-dev
CONSENSUS-FIRST             = PASS
EVIDENCE-LEDGER             = PASS
PROOF-MAP                   = PASS
DEPENDENCY-MAP              = PASS
PERRON-DEBT-AUDIT           = PASS-FOR-CITED-INPUT-ROUTE
SCOPE-SEPARATION            = PASS
EXCEPTIONAL-ZERO-HANDLING   = PASS
SIEGEL-USE-LOCATION         = FIXED
INEFFECTIVITY-LABEL         = PASS
CIRCULARITY                 = PASS
PRE-AUTHORING-GATE          = CLOSED
AUTHORING                    = AUTHORIZED / NOT YET STARTED
BLOCKING-CORRECTIONS        = NONE
```

## قائمة الفحص المغلقة

### A. الحوكمة

- [x] دمج PR #19 وإغلاق حوكمة `0.15.0-dev` بأمر مالك المشروع.
- [x] تثبيت رأس `main` الجديد:
  `9d02c583d416053550d22dfd7acc44d9c264a02c`.
- [x] إنشاء فرع الفصل الثاني عشر من هذا الرأس مباشرة.
- [x] عدم تكديس الفرع على فرع الفصل الحادي عشر أو فرع إغلاقه.
- [x] تخصيص الإصدار `0.16.0-dev` للفصل الثاني عشر.

### B. النطاق

- [x] فصل نتيجة الترديد الثابت في الفصل العاشر عن النتيجة الموحدة.
- [x] تثبيت مجال Siegel--Walfisz:
  \(q\le(\log x)^A\).
- [x] تأجيل Bombieri--Vinogradov صراحة.
- [x] عدم ادعاء مجال من رتبة \(x^\theta\).
- [x] عدم استعمال GRH.
- [x] عدم ادعاء أفضل ثابت عددي.

### C. الأدلة والمراجع

- [x] بدء المسح عبر Consensus قبل بقية المصادر.
- [x] التحقق من Thorner--Zaman عبر arXiv `2108.10878` وصفحة النشر وDOI.
- [x] التحقق من Koukoulopoulos عبر صفحة Cambridge وDOI.
- [x] تسجيل أدوار Davenport وApostol وMontgomery--Vaughan وIwaniec--Kowalski.
- [x] فصل مصدر الاكتشاف عن المصدر الكامل القابل للاعتماد.

### D. بيرون والصيغة الصريحة

- [x] جرد `ANT-THM-03-09` بوصفها `DEFERRED`.
- [x] عدم إعادة تصنيف دين الفصل السادس على أنه مغلق.
- [x] اعتماد صيغة صريحة مقطوعة محددة بحالة `CITED`.
- [x] منع ادعاء برهان داخلي كامل لتحويل المسار.
- [x] تحديد ما يثبت داخل الفصل بعد المدخل المقتبس.

### E. الصفر الاستثنائي

- [x] عزل حد \(x^{\beta_1}/\beta_1\) قبل التقدير.
- [x] إظهاره حدًا ثانويًا في الفئة الحسابية.
- [x] استعمال موصل الجد البدائي.
- [x] تثبيت موضع استعمال مبرهنة Siegel.
- [x] تحويل الإبعاد غير الفعال إلى ادخار أسي في المجال اللوغاريتمي.
- [x] وسم الثابت النهائي بأنه غير فعال.
- [x] عدم استعمال Landau--Page بدل Siegel.
- [x] تسجيل Deuring--Heilbronn بوصفه غير لازم للمسار الأدنى.

### F. البنية البرهانية

- [x] مرشح الفئة بالشخصيات.
- [x] الرد إلى الجد البدائي.
- [x] معالجة الشخصية الرئيسية بحد PNT فعال مقتبس.
- [x] ضبط الأصفار غير الاستثنائية بالمنطقة القياسية.
- [x] اختيار ارتفاع قطع أسي في \(\sqrt{\log x}\).
- [x] تجميع الشخصيات من دون خسارة بعامل \(q\).
- [x] الانتقال إلى الادخار اللوغاريتمي الاعتباطي.
- [x] ضبط القوى الأولية العليا للانتقال إلى \(\vartheta\).
- [x] تثبيت مسار آمن للجمع الجزئي إلى \(\pi\).

### G. عدم الدور

- [x] حظر استعمال نتيجة الفصل العاشر مع ترديد متغير.
- [x] حظر Siegel--Walfisz داخل إثبات مدخلاتها.
- [x] حظر Bombieri--Vinogradov.
- [x] حظر Linnik.
- [x] حظر GRH.
- [x] حظر إخفاء الصفر الاستثنائي.
- [x] حظر وصف الثابت العام بأنه فعال.

## النتائج المحجوزة بعد إغلاق البوابة

```text
ANT-LEM-12-01 = DRAFT / EXPECTED-PROVED-HERE
ANT-THM-12-01 = DRAFT / EXPECTED-CITED
ANT-THM-12-02 = DRAFT / EXPECTED-CITED
ANT-LEM-12-02 = DRAFT / EXPECTED-PROVED-HERE
ANT-LEM-12-03 = DRAFT / EXPECTED-PROVED-HERE / INEFFECTIVE
ANT-THM-12-03 = DRAFT / EXPECTED-PROVED-HERE / INEFFECTIVE-CONSTANT
ANT-COR-12-01 = DRAFT / EXPECTED-PROVED-HERE / INEFFECTIVE-CONSTANT
ANT-COR-12-02 = DRAFT / EXPECTED-PROVED-HERE
ANT-COR-12-03 = DRAFT / EXPECTED-PROVED-HERE
```

تبقى جميع هذه النتائج `DRAFT` وغير قابلة للاستشهاد حتى كتابة المتن، ونجاح البناء، واجتياز تدقيق ما بعد التأليف.

## الديون غير الحاجزة

- أرقام الصفحات الدقيقة في النسخ المحلية للكتب القياسية.
- اختيار الصيغة المنصفة أو الملساء النهائية للصيغة الصريحة.
- تثبيت صيغة تقدير عد الأصفار المستعملة في العرض.
- اختيار ثابت القطع الرمزي من دون تحسين عددي.
- تنفيذ تفاصيل الجمع الجزئي الموحد إلى \(\pi\).
- أفضل الصيغ الحديثة لحد الخطأ.

هذه الديون لا تسمح بتجاوز التوثيق داخل المتن، لكنها لا تمنع بدء التأليف بعد أن أصبح مسار كل منها محددًا وحالته معلنة.

## قرار الإغلاق

```text
PRE-AUTHORING-GATE = CLOSED
AUTHORING           = AUTHORIZED / NOT YET STARTED
CURRENT-ACTION      = SYNCHRONIZE-GOVERNANCE-AND-OPEN-DRAFT-PR
NEXT-GATE           = CHAPTER-12-POST-AUTHORING-AUDIT
BOMBIERI-VINOGRADOV = DEFERRED
RELEASE-READY       = NO
```
