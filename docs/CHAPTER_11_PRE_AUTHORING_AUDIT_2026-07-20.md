# تدقيق ما قبل تأليف الفصل الحادي عشر

## بيانات القرار

```text
CHAPTER       = 11 — المناطق الخالية من الأصفار والأصفار الاستثنائية
VERSION       = 0.15.0-dev
BRANCH        = agent/chapter-11-zero-free-regions-exceptional-zeros-v0.15.0
BASE-COMMIT   = 6815324de91b20da4b4224522d07424279fd0b41
AUDIT-DATE    = 2026-07-20
AUDIT-STATE   = CLOSED / PASS
AUTHORING     = AUTHORIZED
```

## المواد الداخلة في التدقيق

- `research/literature-reviews/chapter-11-zero-free-regions-exceptional-zeros-evidence.md`
- `research/literature-reviews/chapter-11-zero-free-regions-exceptional-zeros-proof-map.md`
- `docs/CHAPTER_11_REFERENCE_VERIFICATION_2026-07-20.md`
- `docs/CHAPTER_11_LOG_DERIVATIVE_SIGN_AUDIT_2026-07-20.md`
- `docs/CHAPTER_11_QUANTITATIVE_INEQUALITY_AUDIT_2026-07-20.md`
- `docs/CHAPTER_11_UNIFORM_REMAINDER_AUDIT_2026-07-20.md`
- `docs/CHAPTER_11_STANDARD_ZERO_FREE_REGION_LOGIC_AUDIT_2026-07-20.md`
- `docs/CHAPTER_11_LANDAU_PAGE_LOGIC_AUDIT_2026-07-20.md`
- `docs/CHAPTER_11_SIEGEL_INEFFECTIVITY_AUDIT_2026-07-20.md`
- `docs/CHAPTER_11_DEURING_HEILBRONN_VERIFICATION_2026-07-20.md`
- `docs/CHAPTER_11_LOGIC_AUDIT_2026-07-20.md`
- الفصل السابع ونتائجه المسجلة عن الشخصيات البدائية والدالة المكتملة والمعادلة الوظيفية.
- الفصل العاشر ونتيجته المسجلة عن عدم الانعدام على الخط \(\Re(s)=1\).

## الحكم النهائي

```text
EVIDENCE-FIRST        = PASS
SCOPE-SEPARATION      = PASS
REFERENCE-COVERAGE    = PASS-FOR-ADOPTED-SCOPE
PROOF-MAP             = PASS
LOGIC-AUDIT           = PASS
SIGN-AUDIT            = PASS
CIRCULARITY           = PASS
PRE-AUTHORING-GATE    = CLOSED
AUTHORING              = AUTHORIZED
BLOCKING-CORRECTIONS  = NONE
```

## قائمة الفحص المغلقة

### A. النطاق والادعاءات

- [x] فصل الفصل عن مبرهنة الأعداد الأولية النوعية في المتتاليات الحسابية.
- [x] فصل المنطقة القياسية عن منطقة Vinogradov--Korobov.
- [x] فصل مبرهنة Landau--Page عن مبرهنة Siegel.
- [x] فصل النتائج الفعالة عن ثابت Siegel غير الفعال.
- [x] تأجيل Siegel--Walfisz وBombieri--Vinogradov وLinnik.
- [x] عدم ادعاء أفضل ثابت عددي.
- [x] تثبيت المقياس \(\mathcal L(q,t)=\log(q(|t|+2))\).
- [x] تثبيت نطاق النتيجة المركزية وثابت مطلق غير محسن.

### B. التبعيات الداخلية

- [x] تثبيت الاعتماد على بنية الفصل السابع.
- [x] تثبيت الاعتماد على عدم الانعدام على الخط من الفصل العاشر.
- [x] اشتقاق صيغة الكسور الجزئية من هادامار العام والدالة المكتملة.
- [x] وسم هادامار العام والنمو من الرتبة الأولى كمكوّنين قياسيين مقتبسين.
- [x] ضبط العوامل المحلية عند الرد إلى الجد البدائي.

### C. المنطقة القياسية

- [x] اشتقاق صيغة حقيقية منتظمة لـ\(-\Re L'/L\) بمجموع على الأصفار.
- [x] تثبيت تقدير عامل غاما عند الارتفاعات الصغيرة والكبيرة.
- [x] تدقيق إشارة مساهمة الصفر المفترض.
- [x] تدقيق قطب زيتا في المتراجحة الموزونة.
- [x] فصل حالة \(\chi^2\) الرئيسية.
- [x] استبعاد الأصفار غير الحقيقية من المنطقة المختارة.
- [x] استبعاد الشخصية غير الحقيقية من الاستثناء.
- [x] إثبات أن الاستثناء المحتمل حقيقي وبسيط ووحيد داخل الدالة.
- [x] تدقيق الانتقال من البدائية إلى الشخصيات العامة.

### D. مبرهنة Landau--Page

- [x] تثبيت الصيغة النوعية مع ثابت مطلق.
- [x] تدقيق حاصل الضرب
  \(\zeta L(s,\chi_1)L(s,\chi_2)L(s,\chi_1\chi_2)\).
- [x] إثبات الموجبية عبر
  \((1+\chi_1(n))(1+\chi_2(n))\ge0\).
- [x] ضبط موصل جد حاصل الضرب بحد \(Q^2\).
- [x] فصل حالة حاصل الضرب الرئيسية واستبعادها عند تميز الشخصيتين.
- [x] إثبات الفرادة في عتبة \(1-c_P/\log Q\).

### E. Siegel وعدم الفعالية

- [x] تثبيت نص مبرهنة Siegel والافتراضات على الشخصية.
- [x] تسجيلها `CITED`.
- [x] شرح معنى عدم الفعالية رياضيًا.
- [x] إثبات حد فعال للمشتقة قرب الواحد.
- [x] تدقيق الاشتقاق إلى \(1-\beta\gg_\varepsilon q^{-\varepsilon}\).
- [x] منع استعمال ثابت Siegel في أي نتيجة يعلن أنها فعالة.

### F. Deuring--Heilbronn

- [x] اختيار صيغة نوعية ثابتة الترديد.
- [x] مطابقة المقياس \((1-\beta_1)\log(q(T+2))\).
- [x] تسجيل النتيجة `CITED` مع فكرة تفسيرية فقط.
- [x] فصل تنافر الأصفار عن فرادة Page.
- [x] فصل النسخة الفعالة عن النسخة غير الفعالة.
- [x] عدم اعتماد أفضل الثوابت الحديثة في النواة الأساسية.

### G. المراجع

- [x] بدء البحث عبر Consensus قبل بقية المصادر.
- [x] التحقق من McCurley وLi وHeath-Brown وKadiri وKhale من بيانات الناشرين.
- [x] التحقق من Basak--Pratt وLiu وBenli--Goel--Twiss--Zaman من arXiv.
- [x] التحقق من المصدر الأصلي لـSiegel وDOI.
- [x] تثبيت الإحالات القياسية إلى Davenport وIwaniec--Kowalski من المصادر المفتوحة المتاحة.
- [x] تسجيل أن أرقام الصفحات المباشرة لبعض النسخ المحلية تبقى دينًا غير حاجز قبل `RELEASE-READY`.

### H. عدم الدور

- [x] حظر Siegel--Walfisz داخل برهان المنطقة الخالية.
- [x] حظر Bombieri--Vinogradov.
- [x] حظر Linnik.
- [x] حظر حد خطأ موحد لـPNT-AP مشتق من النتيجة المطلوبة.
- [x] حظر Deuring--Heilbronn داخل إثبات المنطقة القياسية.
- [x] حظر مبرهنة Siegel داخل إثبات Landau--Page.
- [x] حظر GRH.
- [x] تدقيق كل عقدة في خريطة الاعتماد.

## النتائج المحجوزة بعد إغلاق البوابة

```text
ANT-PROP-11-01 = DRAFT / EXPECTED-PROVED-HERE
ANT-LEM-11-01  = DRAFT / EXPECTED-PROVED-HERE
ANT-THM-11-01  = DRAFT / EXPECTED-PROVED-HERE
ANT-THM-11-02  = DRAFT / EXPECTED-PROVED-HERE
ANT-THM-11-03  = DRAFT / EXPECTED-CITED / INEFFECTIVE
ANT-COR-11-01  = DRAFT / EXPECTED-PROVED-HERE
ANT-THM-11-04  = DRAFT / EXPECTED-CITED
ANT-PROP-11-02 = DRAFT / DIAGNOSTIC / NONBLOCKING-DEFERRED
```

تبقى الحالات `DRAFT` في سجل النتائج حتى كتابة المتن، ونجاح البناء، واجتياز تدقيق ما بعد التأليف.

## الديون غير الحاجزة

- أرقام الصفحات المباشرة لبعض النسخ المحلية من الكتب القياسية.
- أفضل الثوابت الصريحة للمناطق الخالية والتنافر.
- بيان Tatuzawa الكامل.
- الصيغة الصريحة الكاملة لـ\(\psi(x,\chi)\).
- تطبيقات Linnik وSiegel--Walfisz وBombieri--Vinogradov.

هذه الديون تمنع `RELEASE-READY`، لكنها لا تمنع كتابة النواة المعتمدة.

## قرار الإغلاق

```text
CLOSURE-REPORT = docs/CHAPTER_11_LOGIC_AUDIT_2026-07-20.md
PRE-AUTHORING-GATE = CLOSED
AUTHORING = AUTHORIZED
CURRENT-ACTION = AUTHOR-CHAPTER-11-CORE
NEXT-GATE = CHAPTER-11-POST-AUTHORING-AUDIT
```
