# حزمة المراجعة المستقلة للفصل الثالث عشر

التاريخ: 2026-07-21

```text
CHAPTER                   = 13
TOPIC                     = BOMBIERI--VINOGRADOV
REVIEW-CANDIDATE-HEAD     = af0457207e73178831c815be9aa3f5c1cae10d34
CHAPTER-STATE             = VERIFIED
RESULTS                   = 11
QUALITY-CHECKS            = RUN-357 / SUCCESS
PDF-BUILD                 = RUN-351 / IN-PROGRESS
INDEPENDENT-REVIEW        = REQUESTED / NOT YET STARTED
MERGE                     = NOT AUTHORIZED
RELEASE-READY             = NO
```

## 1. المطلوب من المراجع

مراجعة الفصل مراجعة مستقلة ثانية في ثلاثة محاور:

1. **الرياضيات:** صحة النتائج والبراهين وعدم الدور.
2. **المراجع:** صحة حالات المنشأ ومواضع المبرهنات والصفحات والمفاتيح.
3. **المحارف والتنضيد العلمي:** الرموز، والمؤشرات، والمتراجحات، وحدود المجاميع، والإشارات.

المراجعة لا تمنح إذن الدمج أو جاهزية الإصدار. الحكم المطلوب هو أحد:

```text
APPROVED
APPROVED-WITH-NONBLOCKING-CORRECTIONS
CHANGES-REQUIRED
REJECTED
```

مع تعداد العوائق الرياضية والمرجعية والمحرفية كلٌّ على حدة.

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

- تحقق من الوزن \(q/\varphi(q)\).
- تحقق من النجمة على الشخصيات البدائية.
- تحقق من \(N+Q^2\) في النسخة التربيعية.
- تحقق من وجود `sup_Y` في المدخل الثنائي العظمى.
- تحقق من أن الفصل لا يدعي برهانًا داخليًا للحزمة.

### 5.2 هوية Vaughan

- راجع الإشارات في الحدود الأربعة.
- راجع إثبات الالتفاف واستعمال
  \(\log=\mathbf1*\Lambda\) و\(\mathbf1*\mu=\varepsilon\).
- راجع دعم الحد الرابع عند \(m>U\) و\(k>V\).

### 5.3 Pólya--Vinogradov

- راجع اصطلاح المرافق في تحويل فورييه المنتهي.
- راجع عامل \(1/\sqrt q\).
- راجع تحويل مجموع الأسس إلى \(O(\sqrt q\log q)\).

### 5.4 Type I وType II

- راجع ظهور \(Q^{5/2}U\) و\(Q^{5/2}V\) في Type I.
- راجع معياريات المعاملات في الكتل الديادية.
- راجع الحدود
  \(QxU^{-1/2}\)، و\(QxV^{-1/2}\)، و\(Q^2x^{1/2}\).
- راجع الحد \(Qx^{1/2}(UV)^{1/2}\) في الجزء الكبير من \(S_2\).

### 5.5 اختيار المعلمات

- عندما \(Q\le x^{1/3}\): \(U=V=x^{1/3}\).
- عندما \(x^{1/3}\le Q\le x^{1/2}\): \(U=V=x^{2/3}/Q\).
- عندما \(Q>x^{1/2}\): التطبيق المباشر مع \(M=1\)، و\(a_1=1\)، و\(b_n=\Lambda(n)\).

### 5.6 الشخصية الرئيسية والموصل

- راجع تعريف
  \(\psi'(y,\chi)=\psi(y,\chi)-\mathbf1_{\chi=\chi_0}y\).
- راجع الخطأ المحلي للشخصية المستحثة.
- راجع المتراجحة

\[
\sum_{\substack{q\le Q\\d\mid q}}\frac1{\varphi(q)}
\ll\frac1{\varphi(d)}\log\frac{2Q}{d}.
\]

### 5.7 المبرهنة المركزية

- راجع الفصل عند \(D=(\log x)^{A+4}\).
- راجع استعمال Siegel--Walfisz للموصلات الصغيرة.
- راجع جمع الكتل الكبيرة.
- راجع اختيار \(Q=x^{1/2}(\log x)^{-(A+3)}\).
- راجع تصريح عدم الفعالية.

### 5.8 النتائج التابعة

- راجع امتصاص القوى الأولية العليا في نسخة `theta`.
- راجع استعمال الأس \(A+1\)، ومن ثم المجال \(A+4\)، في نسخة `pi`.
- راجع استعمال متراجحة ماركوف في نتيجة تقريبًا كل الترديدات.

## 6. فحص عدم الدور

المطلوب التأكد من أن ترتيب الاعتماد هو:

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

`docs/CHAPTER_13_REFERENCE_VERIFICATION_2026-07-21.md`

المصادر الأساسية:

- Bombieri (1965), *On the Large Sieve*.
- A. I. Vinogradov (1965), مع تصحيح 1966.
- Gallagher (1968), *Bombieri's Mean Value Theorem*.
- Vaughan (1975), *Mean Value Theorems in Prime Number Theory*.
- Montgomery--Vaughan (2026), *Multiplicative Number Theory II*.

المواضع التقنية المعتمدة في Montgomery--Vaughan II:

- هوية Vaughan: الصيغة (17.5)، ص. 55--56.
- الغربال الكبير: المبرهنة 19.16، ص. 175.
- المدخل الثنائي العظمى: المبرهنة 19.19، الصيغة (19.34)، ص. 181.
- القيمة المتوسطة: المبرهنة 20.1، ص. 189.
- Bombieri--Vinogradov: المبرهنة 20.2، ص. 195، والرد ص. 196--197.

## 8. الملفات الداعمة

- `docs/CHAPTER_13_PRE_AUTHORING_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_LARGE_SIEVE_MEAN_VALUE_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_VAUGHAN_IDENTITY_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_TYPE_I_TYPE_II_MEAN_VALUE_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_CONDUCTOR_PRINCIPAL_BV_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_LOGIC_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_AUTHORING_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_POST_AUTHORING_REFERENCE_AUDIT_2026-07-21.md`

## 9. نموذج الحكم

```text
REVIEWED-CANDIDATE-HEAD = af0457207e73178831c815be9aa3f5c1cae10d34
VERDICT                 =
MATHEMATICAL-BLOCKERS    =
REFERENCE-BLOCKERS       =
TYPOGRAPHIC-BLOCKERS     =
NONBLOCKING-CORRECTIONS  =
PROMOTE-TO-REVIEWED      = YES / NO
MERGE-AUTHORIZATION      = OUT OF REVIEW SCOPE
RELEASE-READY            = NO
```
