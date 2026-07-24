# خريطة برهان الفصل الرابع عشر — Barban--Davenport--Halberstam

التاريخ: 2026-07-24

```text
STATUS                     = INTERNAL-PROOF-IN-PROGRESS / ROUTE-REPAIRED
PROOF-POLICY               = FULL-INTERNALIZATION-FIRST
PRE-AUTHORING-GATE         = OPEN
AUTHORING                   = BLOCKED
NORMALIZATION-GATE          = CLOSED / PASS
CHARACTER-TRANSFORM-GATE    = CLOSED / PASS
IMPRIMITIVE-REDUCTION-GATE  = CLOSED / PASS
MV-01                       = COMPLETE / PROVED-HERE-DRAFT
MV-02                       = COMPLETE / PROVED-HERE-DRAFT
MV-03                       = COMPLETE / DEFERRED-FROM-ADOPTED-ROUTE
MV-04                       = PARTIAL / STRICT-DIAGONAL-ONLY
MV-04B                      = OBSTRUCTION-PROVED
MV-04C                      = COMPLETE / PROVED-HERE-DRAFT
PRIMITIVE-WEIGHTED-BOUND    = COMPLETE / PROVED-HERE-DRAFT
PRINCIPAL-LOCAL-ASSEMBLY    = OPEN
CLASSICAL-UPPER-BOUND       = OPEN / FINAL-ASSEMBLY-PENDING
GENERAL-BARBAN-LAYER        = DEFERRED
ASYMPTOTIC-LAYER            = DEFERRED
PASS-FOR-AUTHORING          = NO
```

## الهدف

إثبات

\[
V_\psi(x,Q)=
\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2
\ll_A xQ\log x
\]

في المجال

\[
\frac{x}{(\log x)^A}\le Q\le x,
\]

ثم إجراء التدقيق المنطقي والمرجعي والمستقل قبل التأليف.

## المسار المعتمد بعد الإصلاح

```text
CHARACTER ORTHOGONALITY
 -> RESIDUE VARIANCE / CHARACTER SECOND MOMENT
 -> IMPRIMITIVE TO PRIMITIVE CONDUCTOR REDUCTION
 -> MV-01 WEIGHTED CONDUCTOR DECOMPOSITION
 -> MV-02 WEIGHTED LARGE SIEVE
 -> MV-04C CONDUCTOR SPLIT
      Y = max(2,(x/Q)log(2Q))
      SMALL r <= Y: CHAPTER-12 SIEGEL--WALFISZ
      LARGE r > Y: DIRECT WEIGHTED LARGE SIEVE
 -> PRINCIPAL / LOCAL CORRECTIONS
 -> CLASSICAL BDH UPPER BOUND
 -> LOGIC AUDIT
 -> REFERENCE AUDIT
 -> INDEPENDENT REVIEW
```

## النتائج السابقة على السلسلة

ثبت داخليًا:

\[
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}|\Psi^\circ(x,\chi)|^2.
\]

وإذا كانت \(\chi\bmod q\) مستحثة من \(\chi^*\bmod r\)، فإن

\[
\Psi^\circ(x,\chi)=
\Psi^\circ(x,\chi^*)-C(x;q,r,\chi^*),
\qquad
|C(x;q,r,\chi^*)|\le \omega(q/r)\log x.
\]

## MV-01 — الوزن ورد الموصلات

عُرّف

\[
W_Q(r)=\sum_{m\le Q/r}\frac1{\varphi(rm)}.
\]

وثبت

\[
\frac1{\varphi(r)}
\le W_Q(r)
\ll \frac{\log(2Q/r)}{\varphi(r)}.
\]

ولـ

\[
\mathcal P(x,Q)=
\sum_{r\le Q}W_Q(r)
\sum_{\chi^*\bmod r}^{*}|\Psi^\circ(x,\chi^*)|^2
\]

ثبت

\[
\mathcal S(x,Q)
\le2\mathcal P(x,Q)+O\!\left(Q(\log x)^2\right).
\]

ملف البرهان:

- `docs/CHAPTER_14_MV01_WEIGHTED_CONDUCTOR_DECOMPOSITION_2026-07-24.md`

## MV-02 — الغربال الكبير الموزون

على \(R<r\le2R\):

\[
W_Q(r)
\ll
\frac{\log(2Q/R)}{R}\frac r{\varphi(r)}.
\]

ومن ثم، لمتتالية مدعومة على فترة طولها \(N\):

\[
\sum_{R<r\le2R}W_Q(r)
\sum_{\chi\bmod r}^{*}
\left|\sum_n c_n\chi(n)\right|^2
\ll
\left(\frac NR+R\right)
\log\frac{2Q}{R}
\sum_n|c_n|^2.
\]

ملف البرهان:

- `docs/CHAPTER_14_MV02_DUALITY_WEIGHTED_LARGE_SIEVE_2026-07-24.md`

## المسار المستكشف ثم المؤجل

أثبت `MV-03` تفكيك Vaughan إلى Type I وType II. وأثبت `MV-04` القطر الصارم فقط. ثم أثبت `MV-04B` أن تجميع المستطيل الثنائي في

\[
c_n=\sum_{mk=n}\alpha_m\beta_k
\]

لا يعطي شكليًا إلا خسارة \(x^{o(1)}\) بسبب تصادمات حاصل الضرب. لذلك لا يعتمد هذا المسار للحد الكلاسيكي، لكنه يبقى مادة صحيحة لمسار مبرهنة باربان العامة المؤجل.

الملفات:

- `docs/CHAPTER_14_MV03_BILINEAR_DECOMPOSITION_2026-07-24.md`
- `docs/CHAPTER_14_MV04_DIAGONAL_SPLIT_2026-07-24.md`
- `docs/CHAPTER_14_MV04B_MULTIPLICATIVE_COLLISION_AUDIT_2026-07-24.md`

## MV-04C — فصل الموصلات

ضع

\[
Y=\max\!\left(2,\frac{x}{Q}\log(2Q)\right).
\]

إذا \(Q\ge x/(\log x)^A\)، فإن \(Y\ll_A(\log x)^{A+1}\).

### الموصلات الصغيرة

باستعمال Siegel--Walfisz من الفصل الثاني عشر:

\[
\mathcal P_{\le Y}=o_A(xQ\log x).
\]

### الموصلات الكبيرة

بتطبيق `MV-02` مباشرة على \(c_n=\Lambda(n)\)، واستعمال

\[
\sum_{n\le x}\Lambda(n)^2\ll x\log x,
\]

ثم الجمع الديادي:

\[
\sum_R R\log\frac{2Q}{R}\ll Q,
\]

و

\[
\sum_R\frac{x}{R}\log\frac{2Q}{R}
\ll\frac{x}{Y}\log(2Q/Y)\le Q.
\]

إذن

\[
\boxed{\mathcal P(x,Q)\ll_A xQ\log x}.
\]

ملف البرهان:

- `docs/CHAPTER_14_MV04C_CONDUCTOR_SPLIT_ROUTE_REPAIR_2026-07-24.md`

## سياسة المنشأ

| المكوّن | الحالة |
|---|---|
| تعامد الشخصيات وتحويل التباين | `PROVED-HERE` |
| رد الشخصيات غير البدائية | `PROVED-HERE` |
| MV-01 | `PROVED-HERE-DRAFT` |
| MV-02 | `PROVED-HERE-DRAFT` |
| MV-03 | `PROVED-HERE-DRAFT / DEFERRED-FROM-ADOPTED-ROUTE` |
| MV-04 strict diagonal | `PROVED-HERE-DRAFT` |
| MV-04B obstruction | `PROVED-HERE-DRAFT` |
| MV-04C conductor split | `PROVED-HERE-DRAFT` |
| Siegel--Walfisz | `CHAPTER-12 INPUT / REVIEWED` |
| الغربال الكبير | `CHAPTER-13 INPUT / REVIEWED` |
| التجميع النهائي | `OPEN` |
| مبرهنة باربان العامة | `DEFERRED` |
| Montgomery--Hooley asymptotic | `DEFERRED` |

## الخطوة التالية

`MV-08`:

1. تدقيق الموصل \(1\) والشخصية الرئيسية المتمركزة.
2. إعادة إدخال تصحيحات الأوليات القاسمة للترديد.
3. مقارنة حد التصحيحات \(Q(\log x)^2\) بالمقياس النهائي.
4. نقل المتوسط على الشخصيات إلى تباين الفئات.
5. تثبيت الاعتماد على \(A\) وعدم الفعالية الموروثة من Siegel--Walfisz.

```text
NEXT = MV-08 / PRINCIPAL-LOCAL-ASSEMBLY
PASS-FOR-AUTHORING = NO
```