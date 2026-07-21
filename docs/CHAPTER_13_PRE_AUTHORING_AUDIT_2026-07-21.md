# تدقيق ما قبل تأليف الفصل الثالث عشر

التاريخ: 2026-07-21

```text
CHAPTER              = 13
TOPIC                = BOMBIERI--VINOGRADOV
BASE-MAIN            = 607c6f8ad76f8085828f49ce6b566c846950ab2a
BRANCH               = agent/chapter-13-bombieri-vinogradov-v0.17.0
AUDIT-STATUS         = CLOSED / PASS
PRE-AUTHORING-GATE   = CLOSED / PASS
AUTHORING            = AUTHORIZED / NOT YET STARTED
CENTRAL-TARGET       = ADOPTED-FOR-AUTHORING
LARGE-SIEVE          = CITED / COMPOSITE-INPUT
VAUGHAN-IDENTITY     = PROVED-HERE
TYPE-I               = PROVED-HERE
TYPE-II              = PROVED-HERE
MEAN-VALUE           = PROVED-HERE FROM CITED PACKAGE
LOG-LOSS             = B(A)=A+3
EFFECTIVITY          = INEFFECTIVE-CONSTANT
LOGIC-AUDIT          = PASS
REFERENCE-AUDIT      = PASS
RELEASE-READY        = NO
```

## الحكم النهائي

`PASS-FOR-AUTHORING`

أُغلقت جميع الديون العلمية والمنطقية والمرجعية اللازمة لبدء كتابة متن الفصل.
هذا الإغلاق يسمح بالتأليف فقط؛ ولا يرفع الفصل إلى `DRAFT` قبل إنشاء ملفه،
ولا إلى `VERIFIED` أو `REVIEWED`، ولا يعني `RELEASE-READY`.

## قائمة الإغلاق

### الأدلة والمصادر

- [x] قراءة README وROADMAP وPROGRESS وTODO وRESULTS_REGISTRY وCHANGELOG قبل التعديل.
- [x] بدء المسح عبر Consensus.
- [x] التحقق من Bombieri 1965.
- [x] التحقق من A. I. Vinogradov 1965 وتصحيح 1966.
- [x] التحقق من Gallagher 1968 وVaughan 1975.
- [x] التحقق من Montgomery--Vaughan II وبياناته الرسمية.
- [x] مطابقة هوية Vaughan والغِربال الكبير ومبرهنتي القيمة المتوسطة وBombieri--Vinogradov بأرقام المبرهنات والصفحات.
- [x] إنشاء ملف BibTeX مستقل وربطه ببناء Biber.

### الاعتمادات البرهانية

- [x] تثبيت حزمة الغربال الكبير التربيعية والثنائية العظمى بحالة `CITED / COMPOSITE-INPUT`.
- [x] إثبات هوية Vaughan داخليًا بالتفاف ديريشليه.
- [x] تدقيق الإشارات والدعم وحدود القطع في الهوية.
- [x] إثبات Pólya--Vinogradov داخليًا من نتائج الفصل السابع.
- [x] إثبات تقدير Type I.
- [x] إثبات تقدير Type II.
- [x] تدخيل `sup_{y\le x}` بواسطة المدخل الثنائي العظمى.
- [x] تحسين المعلمات في المجالات الثلاثة لـ\(Q\).
- [x] إثبات مبرهنة القيمة المتوسطة للشخصيات البدائية.
- [x] تدقيق الشخصية الرئيسية.
- [x] تدقيق العوامل المحلية للشخصيات المستحثة.
- [x] إثبات الانتقال من الموصل إلى الترديد.
- [x] فصل الموصلات الصغيرة والكبيرة.
- [x] إثبات مبرهنة Bombieri--Vinogradov في صيغة `psi`.
- [x] إثبات النتائج الموافقة لـ`theta` و`pi` و«تقريبًا كل الترديدات».

### الخسائر والفعالية والنطاق

- [x] تثبيت الخسارة اللوغاريتمية الصريحة \(B(A)=A+3\) في صيغة `psi`.
- [x] تثبيت المجال \(A+4\) في صيغة `pi` الناتجة من استعمال ادخار إضافي.
- [x] تثبيت أن المسار غير فعال بسبب Siegel--Walfisz للموصلات الصغيرة.
- [x] فصل Elliott--Halberstam وBarban--Davenport--Halberstam والفترات القصيرة والنتائج الموزونة بعد حاجز \(1/2\) عن نطاق الفصل.
- [x] اجتياز فحص عدم الدور.

### الحوكمة

- [x] حجز أحد عشر معرفًا للنتائج بحالة `NON-CITABLE`.
- [x] إصدار التدقيق المنطقي النهائي بحكم `PASS-FOR-AUTHORING`.
- [x] إصدار التحقق المرجعي النهائي بحكم `PASS-FOR-AUTHORING`.
- [x] بقاء نقل النتائج إلى السجل المركزي محجوبًا حتى كتابة المتن وتدقيقه.

## الملفات الحاكمة

- `research/literature-reviews/chapter-13-bombieri-vinogradov-evidence.md`
- `research/literature-reviews/chapter-13-bombieri-vinogradov-proof-map.md`
- `docs/CHAPTER_13_LARGE_SIEVE_MEAN_VALUE_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_VAUGHAN_IDENTITY_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_TYPE_I_TYPE_II_MEAN_VALUE_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_CONDUCTOR_PRINCIPAL_BV_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_LOGIC_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_REFERENCE_VERIFICATION_2026-07-21.md`
- `docs/CHAPTER_13_RESULTS_RESERVATION.md`

## القرار

```text
RESEARCH MAY CONTINUE = YES
AUTHORING MAY START   = YES
RESULT-REGISTRY-SYNC  = NO / WAIT FOR AUTHORED MANUSCRIPT
MERGE                 = NOT AUTHORIZED
RELEASE-READY         = NO
```
