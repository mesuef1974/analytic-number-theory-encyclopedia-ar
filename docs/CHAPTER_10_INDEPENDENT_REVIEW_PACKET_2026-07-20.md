# حزمة المراجعة المستقلة للفصل العاشر — 2026-07-20

## هوية النسخة

```text
CHAPTER = 10 — مبرهنة الأعداد الأولية في المتتاليات الحسابية
VERSION = 0.14.0-dev
WORK-BRANCH = agent/chapter-10-prime-number-theorem-arithmetic-progressions-v0.14.0
VERIFIED-MATHEMATICAL-COMMIT = 6e4c4b11a2eba3f36dbbbf4b87484326b45912e8
CHAPTER-STATE = VERIFIED
PR = #15 / DRAFT / UNMERGED
```

هذه الحزمة تطلب مراجعة ثانية مستقلة للنواة الرياضية المثبتة عند الالتزام
أعلاه. لا تعد تقارير التدقيق الداخلي بديلًا عن المراجعة المستقلة.

## التحقق التقني للنسخة الرياضية

```text
QUALITY-CHECKS = run #199 / SUCCESS
PDF-BUILD      = run #198 / SUCCESS
ARTIFACT-ID    = 8456581071
ARTIFACT-SHA256 = 857affde343c6dec1b11bcd6b4e062ffa0cc32ae4419bca94580f47fb72dcfc6
```

## النتيجة المركزية

لكل ترديد ثابت \(q\ge2\) ولكل \((a,q)=1\):

\[
\psi(x;q,a)\sim\frac{x}{\varphi(q)},
\qquad
\vartheta(x;q,a)\sim\frac{x}{\varphi(q)},
\qquad
\pi(x;q,a)\sim\frac{x}{\varphi(q)\log x}.
\]

النطاق نوعي ولترديد ثابت. لا يدعي الفصل حد خطأ فعالًا، ولا انتظامًا في
\(q\)، ولا Siegel--Walfisz، ولا Bombieri--Vinogradov، ولا نتيجة تحت GRH.

## الملفات المطلوب فحصها

### المتن

- `volumes/volume-01-foundations/chapters/chapter-10-prime-number-theorem-arithmetic-progressions.tex`

### الأدلة والحوكمة

- `research/literature-reviews/chapter-10-prime-number-theorem-arithmetic-progressions-evidence.md`
- `research/literature-reviews/chapter-10-prime-number-theorem-arithmetic-progressions-proof-map.md`
- `docs/CHAPTER_10_PRE_AUTHORING_AUDIT_2026-07-20.md`
- `docs/CHAPTER_10_LOGIC_AUDIT_2026-07-20.md`
- `docs/CHAPTER_10_BIBLIOGRAPHIC_VERIFICATION_2026-07-20.md`
- `docs/CHAPTER_10_AUTHORING_AUDIT_2026-07-20.md`
- `docs/RESULTS_REGISTRY.md`

## النتائج السبع

| المعرّف | النتيجة | الحالة الداخلية |
|---|---|---|
| `ANT-PROP-10-01` | تفكيك سلسلة الفئة بواسطة الشخصيات | `PROVED-HERE` |
| `ANT-LEM-10-01` | المتراجحة الموزونة لدوال \(L\) | `PROVED-HERE` |
| `ANT-THM-10-01` | عدم الانعدام على \(\Re(s)=1\) | `PROVED-HERE` |
| `ANT-PROP-10-02` | إزالة قطب سلسلة الفئة | `PROVED-HERE` |
| `ANT-THM-10-02` | \(\psi(x;q,a)\sim x/\varphi(q)\) | `PROVED-HERE` |
| `ANT-COR-10-01` | \(\vartheta(x;q,a)\sim x/\varphi(q)\) | `PROVED-HERE` |
| `ANT-COR-10-02` | \(\pi(x;q,a)\sim x/(\varphi(q)\log x)\) | `PROVED-HERE` |

صيغة Wiener--Ikehara نفسها ليست مثبتة داخل الفصل، بل يعاد استعمال
`ANT-THM-09-02` بحالة `CITED` ومصدر Korevaar المتحقق.

## قائمة الفحص الإلزامية

### 1. مرشح الفئة

- [ ] صحة علاقة التعامد لكل \(n\)، بما في ذلك \((n,q)>1\).
- [ ] جواز تبديل مجموع الشخصيات مع سلسلة فون مانغولت.
- [ ] صحة معامل \(1/\varphi(q)\) والمرافق \(\overline{\chi(a)}\).

### 2. المتراجحة الموزونة

- [ ] صحة الإشارات في حدود \(-\zeta'/\zeta\) و\(-L'/L\).
- [ ] صحة المتراجحة
  \[
  3+4\Re z+\Re(z^2)\ge0\qquad(|z|\le1).
  \]
- [ ] تغطية قيم الشخصية الصفرية وعدم الاقتصار على دائرة الوحدة.

### 3. عدم الانعدام على الخط

- [ ] فصل حالة \(t=0\) عن \(t\ne0\).
- [ ] استعمال `ANT-THM-07-09` عند \(s=1\) من دون دور.
- [ ] صحة معاملات الأقطاب والأصفار المحلية في حجة \(3-4-1\).
- [ ] التحقق من أن \(L(s,\chi^2)\) لا يملك قطبًا عند \(1+2it\) عندما \(t\ne0\).
- [ ] سلامة حالة الشخصيات غير البدائية والعوامل المحلية المحذوفة.

### 4. تحليل القطب

- [ ] صحة
  \[
  L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s}).
  \]
- [ ] صحة باقي \(-L'/L(s,\chi_0)\) عند \(1\)، وهو \(1\).
- [ ] صحة باقي سلسلة الفئة، وهو \(1/\varphi(q)\).
- [ ] امتداد الباقي عبر جميع نقاط الخط \(\Re(s)=1\).

### 5. Wiener--Ikehara

- [ ] تطبيق الأداة على سلسلة الفئة ذات المعاملات غير السالبة، لا على الالتواءات المركبة.
- [ ] تحقق حد المجاميع الجزئية \(\psi(n;q,a)=O(n)\).
- [ ] مطابقة ثابت القطب \(A=1/\varphi(q)\).
- [ ] صحة الانتقال من الأعداد الصحيحة إلى \(x\) الحقيقي.

### 6. الانتقالات النهائية

- [ ] صحة ضبط القوى الأولية العليا داخل الفئة بالفرق العالمي.
- [ ] صحة الجمع الجزئي والحد المتبقي \(O(x/(\log x)^2)\).
- [ ] عدم وجود اعتماد دائري على PNT-AP أو نتائج كمية لاحقة.

### 7. حدود الادعاء

- [ ] تثبيت أن \(q\) ثابت في جميع الصيغ.
- [ ] عدم وجود ادعاء فعالية أو انتظام مستتر.
- [ ] بقاء Siegel--Walfisz وBombieri--Vinogradov والأصفار الاستثنائية خارج النطاق.

## الأحكام المقبولة

يجب أن يصدر المراجع حكمًا صريحًا من أحد الخيارات:

```text
APPROVED
APPROVED WITH MINOR CORRECTIONS
MAJOR REVISION REQUIRED
REJECTED
```

وعند وجود ملاحظات، يلزم تحديد:

```text
LOCATION
SEVERITY = MUST / SHOULD / OPTIONAL
MATHEMATICAL-IMPACT
REQUIRED-ACTION
```

## نموذج الحكم

```text
REVIEWED-COMMIT = 6e4c4b11a2eba3f36dbbbf4b87484326b45912e8
REVIEWER-ROLE = Independent second review
VERDICT = <one accepted verdict>
MATHEMATICAL-CORRECTIONS = <none or list>
EDITORIAL-CORRECTIONS = <none or list>
SCOPE-COMPLIANCE = PASS/FAIL
CIRCULARITY-CHECK = PASS/FAIL
BIBLIOGRAPHIC-CHECK = PASS/FAIL
```

لا يرفع الفصل إلى `REVIEWED`، ولا يحول PR #15 من Draft، ولا يدمج، قبل
استلام حكم مستقل مقبول ومعالجة الملاحظات الإلزامية. ولا تمنح المراجعة حالة
`RELEASE-READY` تلقائيًا.
