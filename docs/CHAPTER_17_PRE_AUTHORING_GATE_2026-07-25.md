# بوابة ما قبل التأليف — الفصل السابع عشر

التاريخ: 2026-07-25

```text
CHAPTER                    = 17
VERSION                    = 0.21.0-dev
TOPIC                      = CIRCLE METHOD / GOLDBACH / WARING
ISSUE                      = #32 / OPEN
PR                         = #33 / DRAFT / OPEN / UNMERGED
BRANCH                     = agent/chapter-17-circle-method-goldbach-waring-v0.21.0
EVIDENCE-LEDGER            = PASS
PROOF-MAP                  = FROZEN / PASS
PRIMARY-SOURCE-AUDIT       = PASS
NONCIRCULARITY-AUDIT       = PASS
RESULT-IDS                 = 8 / AUTHORED-DRAFT
REFERENCE-BLOCKERS         = 0
SCOPE-BLOCKERS             = 0
TECHNICAL-BLOCKERS         = 0
PARAMETER-BLOCKERS         = 0
PRE-AUTHORING-GATE         = CLOSED
PASS-FOR-AUTHORING         = YES
AUTHORING                  = STARTED ON WORK BRANCH
MANUSCRIPT-LINK            = ACTIVE ON WORK BRANCH
POST-AUTHORING-AUDIT       = REQUIRED
MERGE                      = NOT AUTHORIZED
RELEASE-READY              = NO
```

## النطاق المعتمد

1. التعامد الفورييري وصيغة تكامل عدد التمثيلات.
2. الأقواس الكبرى والأقواس الصغرى.
3. التقريب المحلي، والسلسلة المفردة، والتكامل المفرد.
4. الصيغة التقاربية الكلاسيكية في وارينغ بحالة `CITED / EXPLAINED`.
5. مبرهنة فينوغرادوف بحالة `CITED`.
6. مبرهنة هلفغوت بحالة `CITED / MODERN COMPLETION`، مع فصل المكوّن الحاسوبي بوصفه `FINITE-VERIFIED`.
7. غولدباخ الثنائية بحالة `HYPOTHESIS / OPEN`.
8. إبقاء النظرية العامة للمجاميع الأسية وفان دير كوربوت للفصل الثامن عشر.

## التطبيع المجمد

\[
e(t)=e^{2\pi i t},
\qquad
P=N^{1/k},
\qquad
Q=P^\eta,
\qquad
0<\eta<\frac{1}{4k}.
\]

\[
f_k(\alpha;P)=\sum_{1\le x\le P}e(\alpha x^k),
\qquad
r_{s,k}(N)=\int_0^1f_k(\alpha;P)^s e(-N\alpha)\,d\alpha.
\]

وللكسور المختزلة `a/q`:

\[
\mathfrak M(q,a)
=
\left\{\alpha\in[0,1):
\left|\alpha-\frac aq\right|
\le\frac{Q}{qN}
\right\},
\]

\[
\mathfrak M
=
\bigcup_{q\le Q}\bigcup_{(a,q)=1}\mathfrak M(q,a),
\qquad
\mathfrak m=[0,1)\setminus\mathfrak M.
\]

## نتائج التدقيق

- [x] هدف وارينغ مجمد.
- [x] مدخل الأقواس الصغرى موثق ومصنف `CITED / COMPOSITE INPUT`.
- [x] مرجع فينوغرادوف مثبت.
- [x] نطاق هلفغوت محسوم.
- [x] التطبيع والمعلمات مجمدة.
- [x] عدم الدور مع الفصل الثامن عشر مثبت.
- [x] التدقيق الداخلي المستقل المسار صدر بحكم `PASS`.
- [x] صدرت وثيقة مستقلة لإغلاق البوابة.
- [x] بدأ متن الفصل وربط بالمخطوط على فرع العمل.

## الحكم الحالي

```text
AUTHORING-BATCH-01       = COMPLETE-AS-DRAFT
CHAPTER-TEX              = CREATED
MANUSCRIPT-MAIN          = LINKED ON WORK BRANCH
REFERENCE-INSERTION      = PENDING
LOCAL-PDF-BUILD          = NOT YET RUN
POST-AUTHORING-AUDIT     = PENDING
REVIEWED                 = NO
MERGE                    = NOT AUTHORIZED
RELEASE-READY            = NO
```

إغلاق هذه البوابة يمنح إذن الكتابة فقط. لا يمنح اعتمادًا علميًا نهائيًا ولا إذن دمج.
