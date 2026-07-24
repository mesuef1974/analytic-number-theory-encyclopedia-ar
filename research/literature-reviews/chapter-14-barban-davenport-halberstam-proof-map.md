# خريطة برهان الفصل الرابع عشر — Barban--Davenport--Halberstam

التاريخ: 2026-07-24

```text
STATUS                     = INTERNAL-PROOF-IN-PROGRESS
PROOF-POLICY               = FULL-INTERNALIZATION-FIRST
PRE-AUTHORING-GATE         = OPEN
AUTHORING                   = BLOCKED
NORMALIZATION-GATE          = CLOSED / PASS
CHARACTER-TRANSFORM-GATE    = CLOSED / PASS
IMPRIMITIVE-REDUCTION-GATE  = CLOSED / PASS
MEAN-VALUE-ROUTE-GATE       = CLOSED / ROUTE-SELECTED
MV-01                       = COMPLETE / PROVED-HERE-DRAFT
MV-02                       = COMPLETE / PROVED-HERE-DRAFT
MV-03                       = OPEN
MEAN-VALUE-THEOREM-GATE     = OPEN / INTERNAL-PROOF-PENDING
CLASSICAL-UPPER-BOUND       = OPEN
ASYMPTOTIC-LAYER            = DEFERRED
PASS-FOR-AUTHORING          = NO
```

## الهدف

إثبات الحد العلوي الكلاسيكي لكمية التباين

\[
V_\psi(x,Q)=
\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2
\]

ببرهان داخلي كامل، ثم إجراء التدقيق المنطقي والمرجعي والمستقل بعد اكتمال سلسلة البرهان.

## سلسلة الاعتماد

```text
ORTHOGONALITY OF CHARACTERS
        |
        v
RESIDUE-CLASS VARIANCE <-> CHARACTER SECOND MOMENT
        |
        v
IMPRIMITIVE CHARACTER -> PRIMITIVE CONDUCTOR REDUCTION
        |
        v
MV-01 WEIGHTED CONDUCTOR DECOMPOSITION
        |
        v
MV-02 DUALITY / WEIGHTED LARGE-SIEVE PREPARATION
        |
        v
MV-03 BILINEAR DECOMPOSITION
        |
        +--> MV-04 DIAGONAL
        +--> MV-05 OFF-DIAGONAL
        |
        v
MV-06 BARBAN GENERAL MEAN-SQUARE ESTIMATE
        |
        v
MV-07 SPECIALIZATION TO LAMBDA
        |
        v
MV-08 PRINCIPAL / LOCAL CORRECTIONS
        |
        v
MV-09 DYADIC SUMMATION / Q-RANGE
        |
        v
MV-10 CLASSICAL BDH UPPER BOUND
        |
        v
LOGIC AUDIT -> REFERENCE AUDIT -> INDEPENDENT REVIEW
```

## ما ثبت نهائيًا قبل سلسلة MV

### التطبيع والتحويل بالشخصيات

\[
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}|\Psi^\circ(x,\chi)|^2.
\]

```text
NORMALIZATION       = PROVED-HERE
CHARACTER-TRANSFORM = PROVED-HERE
```

### رد الشخصيات غير البدائية

إذا كانت \(\chi\bmod q\) مستحثة من \(\chi^*\bmod r\)، حيث \(r\mid q\)، فإن

\[
\Psi^\circ(x,\chi)
=
\Psi^\circ(x,\chi^*)-C(x;q,r,\chi^*),
\qquad
|C(x;q,r,\chi^*)|\le \omega(q/r)\log x.
\]

```text
IMPRIMITIVE-REDUCTION = PROVED-HERE
```

## MV-01 — تفكيك الموصلات الموزون

عُرّف

\[
W_Q(r)=\sum_{m\le Q/r}\frac1{\varphi(rm)}.
\]

وثبت داخليًا كمسودة:

\[
\frac1{\varphi(r)}
\le W_Q(r)
\ll
\frac{\log(2Q/r)}{\varphi(r)}.
\]

وللمتوسطين

\[
\mathcal S(x,Q)=
\sum_{q\le Q}\frac1{\varphi(q)}
\sum_{\chi\bmod q}|\Psi^\circ(x,\chi)|^2
\]

و

\[
\mathcal P(x,Q)=
\sum_{r\le Q}W_Q(r)
\sum_{\chi^*\bmod r}^{*}
|\Psi^\circ(x,\chi^*)|^2,
\]

ثبت

\[
\mathcal S(x,Q)
\le
2\mathcal P(x,Q)+O\!\left(Q(\log x)^2\right).
\]

كما ثبت تقارب المتسلسلة

\[
\sum_{m\ge1}\frac{\omega(m)^2}{m\varphi(m)}<\infty,
\]

وهو ما يحسن كلفة تصحيحات الاستحثاث إلى

\[
O\!\left(Q(\log x)^2\right).
\]

```text
MV-01 EXACT-REINDEXING      = PROVED-HERE-DRAFT
MV-01 WEIGHT-BOUND          = PROVED-HERE-DRAFT
MV-01 CORRECTION-AGGREGATE  = PROVED-HERE-DRAFT
MV-01 FINAL-REDUCTION       = PROVED-HERE-DRAFT
MV-01                       = COMPLETE-AS-DRAFT
```

ملف البرهان:

- `docs/CHAPTER_14_MV01_WEIGHTED_CONDUCTOR_DECOMPOSITION_2026-07-24.md`

## MV-02 — الازدواجية والغربال الكبير الموزون

على كتلة موصلات ديادية

\[
R<r\le2R,
\]

ثبتت المقارنة

\[
W_Q(r)
\ll
\frac{\log(2Q/R)}{R}
\frac r{\varphi(r)}.
\]

ومن الغربال الكبير للشخصيات البدائية ينتج، لكل متتالية \((c_n)\) مدعومة على فترة طولها \(N\):

\[
\sum_{R<r\le2R}W_Q(r)
\sum_{\chi\bmod r}^{*}
\left|\sum_n c_n\chi(n)\right|^2
\ll
\left(\frac NR+R\right)
\log\frac{2Q}{R}
\sum_n|c_n|^2.
\]

وعرّف المؤثر

\[
(Tc)_{r,\chi}
=
\sqrt{W_Q(r)}\sum_n c_n\chi(n).
\]

بالازدواجية الهيلبرتية ثبتت الصورة المزدوجة

\[
\sum_n
\left|
\sum_{R<r\le2R}
\sqrt{W_Q(r)}
\sum_{\chi\bmod r}^{*}
 b_{r,\chi}\overline{\chi(n)}
\right|^2
\ll
\left(\frac NR+R\right)
\log\frac{2Q}{R}
\sum_{R<r\le2R}\sum_{\chi\bmod r}^{*}|b_{r,\chi}|^2.
\]

الصيغتان صالحتان للفترات المنقولة، ولذلك يمكن استعمالهما على المستطيلات الديادية الناتجة من التفكيك الثنائي في `MV-03`.

```text
MV-02 DYADIC-WEIGHT-COMPARISON = PROVED-HERE-DRAFT
MV-02 WEIGHTED-PRIMAL           = PROVED-HERE-DRAFT
MV-02 WEIGHTED-DUAL             = PROVED-HERE-DRAFT
MV-02 TRANSLATED-INTERVALS      = PROVED-HERE-DRAFT
MV-02                           = COMPLETE-AS-DRAFT
```

ملف البرهان:

- `docs/CHAPTER_14_MV02_DUALITY_WEIGHTED_LARGE_SIEVE_2026-07-24.md`

## سبب عدم كفاية الفصل الثالث عشر وحده

1. مبرهنة القيمة المتوسطة في الفصل الثالث عشر من الرتبة الأولى، وليست متوسطًا تربيعيًا.
2. التطبيق المباشر للغربال الكبير على \(c_n=\Lambda(n)\) يعطي حدًا من الشكل

\[
(x+R^2)x\log x,
\]

وهو أكبر من رتبة \(xR\log x\) المطلوبة.
3. يمنع الاستدلال العكسي من Bombieri--Vinogradov.

## سياسة المنشأ

| المكوّن | الحالة |
|---|---|
| تعامد الشخصيات | `PROVED-HERE` |
| تحويل التباين | `PROVED-HERE` |
| رد الموصلات | `PROVED-HERE` |
| MV-01 | `PROVED-HERE-DRAFT` |
| MV-02 | `PROVED-HERE-DRAFT` |
| الغربال الكبير | `CITED-TOOL / FROM CHAPTER 13` |
| MV-03 إلى MV-10 | `OPEN` |
| صيغة Montgomery--Hooley | `DEFERRED` |

كل حالة `PROVED-HERE-DRAFT` تبقى غير قابلة للاستشهاد حتى اكتمال البرهان ثم اجتياز التدقيق المنطقي والمرجعي والمستقل.

## الخطوة التالية

`MV-03`:

1. اختيار هوية تفكيك صريحة للمعاملات الحسابية المستهدفة.
2. تحويل المجاميع إلى حدود خطية وثنائية على مستطيلات ديادية.
3. تسجيل قيود معاملات الطرفين ومعايير \(\ell^2\) اللازمة.
4. منع أي استعمال ضمني لمبرهنة باربان أو BDH داخل التفكيك.

```text
NEXT = MV-03
PASS-FOR-AUTHORING = NO
```
