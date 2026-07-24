# حكم المراجعة المستقلة للفصل الرابع عشر — Barban--Davenport--Halberstam

التاريخ: 2026-07-24

```text
VERSION                    = 0.18.0-dev
CHAPTER                    = 14
REVIEW                     = INDEPENDENT-REVIEW-VERDICT
REVIEWER                   = Claude (مراجعة مستقلة بطلب المالك)
REVIEW-DATE                = 2026-07-24
REVIEWED-HEAD              = 49a76dcdb18318aaa548a34d2918b9c7d846a141
VERDICT                    = APPROVED-WITH-NONBLOCKING-CORRECTIONS
BLOCKING-CORRECTIONS       = NONE
NONBLOCKING-CORRECTIONS    = 5
AUTHORING-RECOMMENDATION   = YES
OWNER-AUTHORING-DECISION   = PENDING
PASS-FOR-AUTHORING         = NO
PR-26                      = DRAFT / OPEN / UNMERGED
```

## 1. نطاق المراجعة

راجع المراجع المستقل السلسلة الرياضية المعتمدة كاملة، لا ملخصات التدقيق الداخلي فقط:

```text
CHARACTER ORTHOGONALITY
 -> MV-01 WEIGHTED CONDUCTOR REDUCTION
 -> MV-02 WEIGHTED LARGE SIEVE
 -> MV-04C CONDUCTOR SPLIT
      SMALL CONDUCTORS: CHAPTER-12 SIEGEL--WALFISZ
      LARGE CONDUCTORS: DIRECT LARGE SIEVE ON LAMBDA
 -> MV-08 PRINCIPAL / LOCAL ASSEMBLY
 -> MV-09 RANGE / FINAL ASSEMBLY
 -> MV-10 LOGIC AUDIT
 -> REFERENCE AUDIT
```

الوحدات `MV-03` و`MV-04` و`MV-04B` ليست ضمن سلسلة الاعتماد النهائية.

## 2. الادعاء الذي جرى اعتماده

لكل ثابت \(A>0\):

\[
V_\psi(x,Q)
=
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

الثابت يعتمد على \(A\)، وغير فعّال في المسار الحالي بسبب Siegel--Walfisz.

## 3. نتائج الفحص المستقل

```text
NORMALIZATION               = PASS
CONDUCTOR-REDUCTION         = PASS
LOCAL-CORRECTIONS           = PASS
WEIGHTED-LARGE-SIEVE        = PASS
CONDUCTOR-SPLIT             = PASS
SMALL-CONDUCTORS            = PASS
LARGE-CONDUCTORS            = PASS
FINAL-ASSEMBLY              = PASS
NON-CIRCULARITY             = PASS
REFERENCE-SUPPORT           = PASS
INEFFECTIVITY-LABEL         = PASS
```

أكدت المراجعة خصوصًا أن الشخصية الرئيسية البدائية لا تظهر في طبقة الموصلات الكبيرة: الشخصية الرئيسية البدائية تقع عند الموصل \(1\) فقط، بينما الطبقة الكبيرة تحقق \(r>Y\ge2\)، ومن ثم \(\Psi^\circ(x,\chi^*)=\Psi(x,\chi^*)\) تلقائيًا هناك.

## 4. التصحيحات غير الحاجزة

1. توضيح الرمز الوسيط في `MV-01 §5` عند استبدال الشخصية المستحثة بجدها البدائي قبل إدخال التصحيح المحلي.
2. تثبيت تقسيم ديادي غير متراكب للمجال \((Y,Q]\) بدل الصياغة المختصرة `R>=Y/2`.
3. تحديث الحالة الوصفية للوحدات الفردية لتسجيل أن `MV-10` غطى التدقيق المنطقي النهائي.
4. تقديم برهان أكثر صراحة لتقارب
   \[
   \sum_{m\ge1}\frac{\omega(m)^2}{m\varphi(m)}.
   \]
5. تسجيل صريح لغياب الشخصية الرئيسية البدائية عن الموصلات الكبيرة.

سجل إغلاق هذه البنود:

`docs/CHAPTER_14_NONBLOCKING_REVIEW_CORRECTIONS_2026-07-24.md`

## 5. الحكم

```text
VERDICT                     = APPROVED-WITH-NONBLOCKING-CORRECTIONS
BLOCKING-CORRECTIONS        = NONE
MATHEMATICAL-ROUTE          = APPROVED
REFERENCE-ROUTE             = APPROVED
AUTHORING-RECOMMENDATION    = YES
```

## 6. قيد سلطة المالك

هذا الحكم يغلق بوابة المراجعة المستقلة، لكنه لا يفتح التأليف تلقائيًا. وفق حوكمة المشروع، قرار:

```text
PASS-FOR-AUTHORING = YES
```

يبقى قرارًا صريحًا لمالك المشروع. وحتى صدوره:

- لا يُنشأ متن LaTeX للفصل الرابع عشر؛
- لا تُحجز معرفات نتائج نهائية؛
- لا يُدمج PR #26؛
- يبقى PR #26 في حالة Draft.
