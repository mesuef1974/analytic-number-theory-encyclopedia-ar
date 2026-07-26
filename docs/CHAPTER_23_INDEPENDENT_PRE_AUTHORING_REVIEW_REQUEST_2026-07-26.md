# طلب مراجعة مستقلة قبل تأليف الفصل الثالث والعشرين

## الرأس المطلوب

```text
BRANCH        = agent/chapter-23-zero-statistics-random-matrices-v0.27.0
REVIEW-STAGE  = PRE-AUTHORING
AUTHORING     = BLOCKED
RESULTS       = 10 RESERVED / NON-CITABLE
```

يجب على المراجع تسجيل SHA الكامل الذي راجعه وعدم قبول رأس متحرك بلا تثبيت.

## الملفات الإلزامية

1. `docs/CHAPTER_23_SCOPE_2026-07-26.md`
2. `docs/CHAPTER_23_EVIDENCE_LEDGER_2026-07-26.md`
3. `docs/CHAPTER_23_NORMALIZATION_TABLE_2026-07-26.md`
4. `docs/CHAPTER_23_PROOF_MAP_2026-07-26.md`
5. `docs/RESULTS_REGISTRY_CHAPTER_23.md`
6. `docs/CHAPTER_23_PRE_AUTHORING_AUDIT_2026-07-26.md`

## الفحوص العلمية المطلوبة

### 1. صيغة ريمان--فون مانغولت

تحقق من:

\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T),
\]

ومن أن العد بالتعدد، وأن متوسط التباعد المحلي مستنتج بالتطبيع الصحيح.

### 2. مبرهنة Montgomery

تحقق مستقلًا من:

- شرط RH في الصياغة التاريخية.
- الوزن \(w(u)=4/(4+u^2)\).
- عامل التطبيع \((T/(2\pi)\log T)^{-1}\).
- كون الأزواج مرتبة والقطر داخل \(F(\alpha,T)\).
- الصيغة على \(0\le\alpha<1\).
- ترجمتها إلى دوال اختبار ذات \(\operatorname{supp}\widehat f\subset(-1,1)\).
- عدم مساواة الجزء المثبت بالحدسية الكاملة.

### 3. فورييه ونواة الجيب

تحقق من الاتفاقية
\[
\widehat f(\alpha)=\int f(u)e^{-2\pi i\alpha u}\,du
\]
ومن الهوية
\[
\widehat{\left(\frac{\sin\pi u}{\pi u}\right)^2}(\alpha)=(1-|\alpha|)_+.
\]
وتحقق من أن \(R_2(u)=1-(\sin\pi u/(\pi u))^2\) مصنفة مبرهنة في GUE وحدسية لزيتا.

### 4. Odlyzko

تحقق من بيانات ورقة 1987:

- أول \(10^5\) أصفار.
- عينة \(10^5\) قرب الفهرس \(10^{12}\).
- الدقة المعلنة \(10^{-8}\) تقريبًا.
- التصنيف `NUMERICAL-EVIDENCE / FINITE-VERIFIED` فقط.

### 5. الحدود المنطقية

تحقق من الفصل بين:

- pair correlation؛
- nearest-neighbor spacing؛
- number variance؛
- n-level correlation.

وتحقق من عدم الدور مع الفصول 6 و9 و21 و22، ومن أن نتائج Katz--Sarnak فوق الحقول المنتهية لا تنقل آليًا إلى زيتا الكلاسيكية.

### 6. السجل

- عشرة معرفات بالضبط.
- لا تصادم مع معرفات المشروع.
- `ANT-THM-23-01` وحدها `PROVED-HERE`.
- جميع النتائج `RESERVED / NON-CITABLE`.

## مخرج المراجعة

أنشئ ملفًا جديدًا فقط:

`docs/CHAPTER_23_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-26.md`

ويحتوي على:

```text
REVIEWED-HEAD      = <full SHA>
REVIEWER           = INDEPENDENT LOCAL CLIENT
REVIEW-STAGE       = PRE-AUTHORING
VERDICT            = PASS | CHANGES-REQUIRED | FAIL
BLOCKERS           = <integer>
PASS-FOR-AUTHORING = YES | NO
RESULTS-CITABLE    = NO
MERGE              = NOT AUTHORIZED
```

لا تعدل ملفات الحزمة الأصلية، ولا تنشئ متن الفصل، ولا تربطه بالمخطوط.
