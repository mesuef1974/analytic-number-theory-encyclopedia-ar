# حزمة المراجعة المستقلة للفصل الثالث عشر

التاريخ: 2026-07-21

```text
CHAPTER                   = 13
TOPIC                     = BOMBIERI--VINOGRADOV
REVIEW-CANDIDATE-HEAD     = d2495dba9cb5cc17a74c6bbb0ac55a914313d3f9
CHAPTER-STATE             = VERIFIED
RESULTS                   = 11
QUALITY-CHECKS            = RUN-357 / SUCCESS
PDF-BUILD                 = RUN-351 / SUCCESS
REFERENCE-CORRECTIONS     = 3 / CLOSED
INDEPENDENT-REVIEW        = COMPLETED / APPROVED-WITH-NONBLOCKING-CORRECTIONS
REVIEW-REPORT             = docs/CHAPTER_13_INDEPENDENT_REVIEW_2026-07-21.md
PROMOTE-TO-REVIEWED       = RECOMMENDED / OWNER ACTION REQUIRED
MERGE                     = NOT AUTHORIZED
RELEASE-READY             = NO
```

## 1. نطاق المراجعة المكتملة

رُوجع الفصل مراجعة مستقلة ثانية في ثلاثة محاور:

1. **الرياضيات:** صحة النتائج والبراهين وعدم الدور.
2. **المراجع:** صحة حالات المنشأ ومواضع المبرهنات والصفحات والمفاتيح.
3. **المحارف والتنضيد العلمي:** الرموز، والمؤشرات، والمتراجحات، وحدود المجاميع، والإشارات.

التقرير النهائي:

`docs/CHAPTER_13_INDEPENDENT_REVIEW_2026-07-21.md`

الحكم:

```text
APPROVED-WITH-NONBLOCKING-CORRECTIONS
```

المراجعة لا تمنح إذن الدمج أو جاهزية الإصدار.

## 2. ملف المتن

`volumes/volume-01-foundations/chapters/chapter-13-bombieri-vinogradov.tex`

الفصل مرتبط بـ`manuscript/main.tex`، وحالته الحالية `VERIFIED`، لا `REVIEWED`.

## 3. النتيجة المركزية

لكل \(A>0\)، وبانتظام عندما

\[
Q\le \frac{x^{1/2}}{(\log x)^{A+3}},
\]

يثبت الفصل

\[
\sum_{q\le Q}
\max_{(a,q)=1}
\sup_{2\le y\le x}
\left|
\psi(y;q,a)-\frac{y}{\varphi(q)}
\right|
\ll_A \frac{x}{(\log x)^A}.
\]

الثابت الضمني غير فعال؛ فالبرهان يستعمل Siegel--Walfisz للموصلات الصغيرة.

## 4. النتائج الأحد عشر

| المعرّف | النتيجة | المنشأ المعلن |
|---|---|---|
| `ANT-THM-13-01` | حزمة الغربال الكبير: التربيعية والثنائية العظمى | `CITED / COMPOSITE-INPUT` |
| `ANT-LEM-13-01` | هوية Vaughan | `PROVED-HERE` |
| `ANT-PROP-13-01` | الرد إلى Type I وType II | `PROVED-HERE` |
| `ANT-LEM-13-02` | تقدير Type I | `PROVED-HERE` |
| `ANT-LEM-13-03` | تقدير Type II | `PROVED-HERE` |
| `ANT-LEM-13-04` | Pólya--Vinogradov للشخصيات البدائية | `PROVED-HERE` |
| `ANT-THM-13-02` | مبرهنة القيمة المتوسطة مع `sup_{y<=x}` | `PROVED-HERE` من المدخل المقتبس |
| `ANT-THM-13-03` | Bombieri--Vinogradov في صيغة `psi` | `PROVED-HERE / INEFFECTIVE-CONSTANT` |
| `ANT-COR-13-01` | النسخة الموافقة لـ`theta` | `PROVED-HERE / INEFFECTIVE-CONSTANT` |
| `ANT-COR-13-02` | النسخة الموافقة لـ`pi` | `PROVED-HERE / INEFFECTIVE-CONSTANT` |
| `ANT-COR-13-03` | تقريبًا كل الترديدات | `PROVED-HERE / INEFFECTIVE-CONSTANT` |

السجل الحاكم:

`docs/RESULTS_REGISTRY_CHAPTER_13.md`

## 5. نقاط المراجعة الرياضية

### 5.1 حزمة الغربال الكبير

- تحقق الوزن \(q/\varphi(q)\).
- تحققت النجمة على الشخصيات البدائية.
- تحقق \(N+Q^2\) في النسخة التربيعية.
- تحقق وجود `sup_Y` في المدخل الثنائي العظمى.
- تحقق أن الفصل لا يدعي برهانًا داخليًا للحزمة.

### 5.2 هوية Vaughan

- روجعت الإشارات في الحدود الأربعة.
- روجع إثبات الالتفاف واستعمال
  \(\log=\mathbf1*\Lambda\) و\(\mathbf1*\mu=\varepsilon\).
- روجع دعم الحد الرابع عند \(m>U\) و\(k>V\).

### 5.3 Pólya--Vinogradov

- روجع اصطلاح المرافق في تحويل فورييه المنتهي.
- روجع عامل \(1/\sqrt q\).
- روجع تحويل مجموع الأسس إلى \(O(\sqrt q\log q)\).

### 5.4 Type I وType II

- روجع ظهور \(Q^{5/2}U\) و\(Q^{5/2}V\) في Type I.
- روجعت معياريات المعاملات في الكتل الديادية.
- روجعت الحدود
  \(QxU^{-1/2}\)، و\(QxV^{-1/2}\)، و\(Q^2x^{1/2}\).
- روجع الحد \(Qx^{1/2}(UV)^{1/2}\) في الجزء الكبير من \(S_2\).

### 5.5 اختيار المعلمات

- عندما \(Q\le x^{1/3}\): \(U=V=x^{1/3}\).
- عندما \(x^{1/3}\le Q\le x^{1/2}\): \(U=V=x^{2/3}/Q\).
- عندما \(Q>x^{1/2}\): التطبيق المباشر مع \(M=1\)، و\(a_1=1\)، و\(b_n=\Lambda(n)\).

### 5.6 الشخصية الرئيسية والموصل

- روجع تعريف
  \(\psi'(y,\chi)=\psi(y,\chi)-\mathbf1_{\chi=\chi_0}y\).
- روجع الخطأ المحلي للشخصية المستحثة.
- روجعت المتراجحة

\[
\sum_{\substack{q\le Q\\d\mid q}}\frac1{\varphi(q)}
\ll\frac1{\varphi(d)}\log\frac{2Q}{d}.
\]

### 5.7 المبرهنة المركزية

- روجع الفصل عند \(D=(\log x)^{A+4}\).
- روجع استعمال Siegel--Walfisz للموصلات الصغيرة.
- روجع جمع الكتل الكبيرة.
- روجع اختيار \(Q=x^{1/2}(\log x)^{-(A+3)}\).
- روجع تصريح عدم الفعالية.

### 5.8 النتائج التابعة

- روجع امتصاص القوى الأولية العليا في نسخة `theta`.
- روجع استعمال الأس \(A+1\)، ومن ثم المجال \(A+4\)، في نسخة `pi`.
- روجع استعمال متراجحة ماركوف في نتيجة تقريبًا كل الترديدات.

## 6. فحص عدم الدور

تحقق ترتيب الاعتماد الآتي:

```text
الفصول السابقة + حزمة الغربال الكبير المقتبسة
  -> Vaughan + Pólya--Vinogradov
  -> Type I / Type II
  -> مبرهنة القيمة المتوسطة
  -> رد الموصلات
  -> Bombieri--Vinogradov
  -> theta / pi / almost-all
```

ولا تدخل Bombieri--Vinogradov أو نتيجة تابعة لها في أي مدخل سابق.

## 7. المراجع الحاكمة

التحقق المرجعي التفصيلي:

- `docs/CHAPTER_13_REFERENCE_VERIFICATION_2026-07-21.md`
- `docs/CHAPTER_13_REFERENCE_CORRECTIONS_2026-07-21.md`

المصادر الأساسية:

- Bombieri (1965), *On the Large Sieve*.
- A. I. Vinogradov (1965), مع تصحيح 1966.
- Gallagher (1968), *Bombieri's Mean Value Theorem*.
- Vaughan (1975), *Mean Value Theorems in Prime Number Theory*.
- Montgomery--Vaughan (2026), *Multiplicative Number Theory II*.

المواضع التقنية المصححة والمعتمدة في Montgomery--Vaughan II:

- هوية Vaughan: الصيغة (17.5)، ص. 55--56.
- الغربال الكبير: المبرهنة 19.16، ص. 174.
- الأداة العظمى السابقة: الصيغة (19.34)، ص. 180.
- المدخل الثنائي الأعظمي: المبرهنة 19.19، الصيغة (19.35)، ص. 181.
- القيمة المتوسطة: المبرهنة 20.1، ص. 189.
- Bombieri--Vinogradov: المبرهنة 20.2، ص. 194، والبرهان ورد الموصلات ص. 195--197.

## 8. الملفات الداعمة

- `docs/CHAPTER_13_PRE_AUTHORING_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_LARGE_SIEVE_MEAN_VALUE_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_VAUGHAN_IDENTITY_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_TYPE_I_TYPE_II_MEAN_VALUE_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_CONDUCTOR_PRINCIPAL_BV_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_LOGIC_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_AUTHORING_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_POST_AUTHORING_REFERENCE_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_INDEPENDENT_REVIEW_2026-07-21.md`

## 9. الحكم

```text
REVIEWED-CANDIDATE-HEAD = d2495dba9cb5cc17a74c6bbb0ac55a914313d3f9
VERDICT                 = APPROVED-WITH-NONBLOCKING-CORRECTIONS
MATHEMATICAL-BLOCKERS    = 0
REFERENCE-BLOCKERS       = 0
TYPOGRAPHIC-BLOCKERS     = 0
NONBLOCKING-CORRECTIONS  = 1 EXPLANATORY SENTENCE
PROMOTE-TO-REVIEWED      = YES / RECOMMENDED / OWNER ACTION REQUIRED
MERGE-AUTHORIZATION      = OUT OF REVIEW SCOPE
RELEASE-READY            = NO
```
