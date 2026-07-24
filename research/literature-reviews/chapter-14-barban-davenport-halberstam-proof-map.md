# خريطة برهان الفصل الرابع عشر — Barban--Davenport--Halberstam

التاريخ: 2026-07-24

```text
STATUS                     = INTERNAL-PROOF-COMPLETE-AS-DRAFT
PROOF-POLICY               = FULL-INTERNALIZATION-FIRST
PRE-AUTHORING-GATE         = OPEN
AUTHORING                   = BLOCKED
NORMALIZATION-GATE          = CLOSED / PASS
CHARACTER-TRANSFORM-GATE    = CLOSED / PASS
IMPRIMITIVE-REDUCTION-GATE  = CLOSED / PASS
MEAN-VALUE-ROUTE-GATE       = CLOSED / ROUTE-REPAIRED
MV-01                       = COMPLETE / PROVED-HERE-DRAFT
MV-02                       = COMPLETE / PROVED-HERE-DRAFT
MV-03                       = COMPLETE / DEFERRED-FROM-ADOPTED-ROUTE
MV-04                       = PARTIAL / STRICT-DIAGONAL-ONLY
MV-04B                      = OBSTRUCTION-PROVED
MV-04C                      = COMPLETE / PROVED-HERE-DRAFT
MV-08                       = COMPLETE / PROVED-HERE-DRAFT
MV-09                       = COMPLETE / PROVED-HERE-DRAFT
MV-10 LOGIC-AUDIT           = PASS
CLASSICAL-UPPER-BOUND       = LOGICALLY-CLOSED-AS-DRAFT
REFERENCE-AUDIT             = PENDING
INDEPENDENT-REVIEW          = PENDING
ASYMPTOTIC-LAYER            = DEFERRED
PASS-FOR-AUTHORING          = NO
```

## الهدف النهائي المدقق

لكل ثابت \(A>0\):

\[
V_\psi(x,Q)=
\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2
\ll_A xQ\log x
\]

بانتظام في

\[
x\ge3,
\qquad
\frac{x}{(\log x)^A}\le Q\le x.
\]

```text
FINAL-CONSTANT = DEPENDS-ON-A / INEFFECTIVE-IN-CURRENT-ROUTE
```

## سلسلة الاعتماد المعتمدة

```text
ORTHOGONALITY OF CHARACTERS
        |
        v
RESIDUE-CLASS VARIANCE <-> CHARACTER SECOND MOMENT
        |
        v
MV-01 WEIGHTED CONDUCTOR REDUCTION
        |
        v
MV-02 WEIGHTED LARGE SIEVE
        |
        v
MV-04C SPLIT AT Y=max(2,(x/Q)log(2Q))
        |
        +--> SMALL CONDUCTORS: CHAPTER-12 SIEGEL--WALFISZ
        +--> LARGE CONDUCTORS: DIRECT LARGE SIEVE ON LAMBDA
        |
        v
MV-08 PRINCIPAL / LOCAL ASSEMBLY
        |
        v
MV-09 RANGE / SMALL-x / FINAL ASSEMBLY
        |
        v
MV-10 END-TO-END LOGIC AUDIT = PASS
        |
        v
REFERENCE AUDIT -> INDEPENDENT REVIEW -> AUTHORING DECISION
```

## العقد المثبتة

### 1. تحويل التباين

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
MV-10-AUDIT         = PASS
```

### 2. رد الموصلات والتصحيحات المحلية

\[
W_Q(r)=\sum_{m\le Q/r}\frac1{\varphi(rm)},
\qquad
W_Q(r)\ll\frac{\log(2Q/r)}{\varphi(r)}.
\]

و

\[
\mathcal S(x,Q)
\le2\mathcal P(x,Q)+O\!\left(Q(\log x)^2\right).
\]

```text
MV-01 EXACT-REINDEXING     = PROVED-HERE-DRAFT
MV-01 WEIGHT-BOUND         = PROVED-HERE-DRAFT
MV-01 CORRECTION-AGGREGATE = PROVED-HERE-DRAFT
MV-10-AUDIT                = PASS
```

### 3. الغربال الكبير الموزون

على \(R<r\le2R\):

\[
\sum W_Q(r)\sum_{\chi\bmod r}^{*}
\left|\sum_n c_n\chi(n)\right|^2
\ll
\left(\frac NR+R\right)
\log\frac{2Q}{R}
\sum_n|c_n|^2.
\]

```text
MV-02 = COMPLETE / PROVED-HERE-DRAFT
MV-10-AUDIT = PASS
```

### 4. فصل الموصلات

\[
Y=\max\!\left(2,\frac{x}{Q}\log(2Q)\right).
\]

في المجال المعتمد:

\[
2\le Y\le Q,
\qquad
Y\ll_A(\log x)^{A+1}.
\]

- \(r\le Y\): Siegel--Walfisz.
- \(r>Y\): الغربال الكبير مباشرة على \(\Lambda\).

وينتج

\[
\mathcal P(x,Q)\ll_A xQ\log x.
\]

```text
MV-04C = COMPLETE / PROVED-HERE-DRAFT
MV-10-AUDIT = PASS
```

### 5. التجميع النهائي

\[
V_\psi(x,Q)=\mathcal S(x,Q)
\ll_A xQ\log x.
\]

```text
MV-08 = COMPLETE / PROVED-HERE-DRAFT
MV-09 = COMPLETE / PROVED-HERE-DRAFT
MV-10 LOGIC-AUDIT = PASS
```

## المسار المؤجل

`MV-03`, `MV-04`, `MV-04B` تحفظ بوصفها مواد بحثية:

```text
VAUGHAN-DECOMPOSITION       = PROVED-HERE-DRAFT
STRICT-DIAGONAL             = PROVED-HERE-DRAFT
COLLISION-OBSTRUCTION       = PROVED-HERE-DRAFT
USED-IN-FINAL-DEPENDENCY    = NO
GENERAL-BARBAN-LAYER        = DEFERRED
```

عائق التصادمات الضربية لم يُخفَ؛ بل تم تجاوزه في المجال الكلاسيكي بفصل الموصلات.

## عدم الدور

المسار النهائي لا يعتمد على:

- BDH نفسها؛
- Bombieri--Vinogradov؛
- Vaughan في المسار المعتمد؛
- GRH.

```text
NON-CIRCULARITY = PASS
```

## ملفات الإثبات والتدقيق

- `docs/CHAPTER_14_MV01_WEIGHTED_CONDUCTOR_DECOMPOSITION_2026-07-24.md`
- `docs/CHAPTER_14_MV02_DUALITY_WEIGHTED_LARGE_SIEVE_2026-07-24.md`
- `docs/CHAPTER_14_MV03_BILINEAR_DECOMPOSITION_2026-07-24.md`
- `docs/CHAPTER_14_MV04_DIAGONAL_SPLIT_2026-07-24.md`
- `docs/CHAPTER_14_MV04B_MULTIPLICATIVE_COLLISION_AUDIT_2026-07-24.md`
- `docs/CHAPTER_14_MV04C_CONDUCTOR_SPLIT_ROUTE_REPAIR_2026-07-24.md`
- `docs/CHAPTER_14_MV08_PRINCIPAL_LOCAL_ASSEMBLY_2026-07-24.md`
- `docs/CHAPTER_14_MV09_RANGE_FINAL_ASSEMBLY_2026-07-24.md`
- `docs/CHAPTER_14_MV10_LOGIC_AUDIT_2026-07-24.md`

## سياسة المنشأ

| المكوّن | الحالة |
|---|---|
| تعامد الشخصيات وتحويل التباين | `PROVED-HERE` |
| رد الموصلات والتصحيحات | `PROVED-HERE-DRAFT` |
| الغربال الكبير | `CITED-TOOL / FROM CHAPTER 13` |
| Siegel--Walfisz | `CHAPTER-12 REVIEWED INPUT` |
| حد مربع فون مانغولت | `STANDARD / REFERENCE-AUDIT-PENDING` |
| الفصل والجمع الديادي | `PROVED-HERE-DRAFT` |
| الحد الكلاسيكي | `LOGICALLY-CLOSED-AS-DRAFT` |

## الخطوة التالية

```text
NEXT                 = REFERENCE-AUDIT
LOGIC-AUDIT          = PASS
REFERENCE-AUDIT      = PENDING
INDEPENDENT-REVIEW   = PENDING
PASS-FOR-AUTHORING   = NO
```
