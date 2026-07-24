# حزمة المراجعة المستقلة للفصل الرابع عشر — Barban--Davenport--Halberstam

التاريخ: 2026-07-24

```text
VERSION                    = 0.18.0-dev
CHAPTER                    = 14
PACKET                     = INDEPENDENT-REVIEW
FROZEN-MATHEMATICAL-HEAD   = 49a76dcdb18318aaa548a34d2918b9c7d846a141
PR                         = #26 / DRAFT / OPEN / UNMERGED
ISSUE                      = #25 / OPEN
INTERNAL-PROOF             = COMPLETE-AS-DRAFT
LOGIC-AUDIT                = PASS
REFERENCE-AUDIT            = PASS
INDEPENDENT-REVIEW         = REQUESTED / PENDING
PASS-FOR-AUTHORING         = NO
RESULTS-RESERVED           = 0
RELEASE-READY              = NO
```

## 1. المطلوب من المراجع

إجراء مراجعة مستقلة للمسار الرياضي المعتمد فقط، وإصدار أحد الأحكام:

```text
APPROVED
APPROVED-WITH-NONBLOCKING-CORRECTIONS
CHANGES-REQUIRED
REJECTED
```

لا يعد سكوت المراجع أو غياب الرد موافقة. ولا يجوز فتح التأليف قبل حكم مستقل صريح ومعالجة كل عائق.

## 2. الادعاء المركزي قيد المراجعة

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

الثابت يعتمد على \(A\)، وهو غير فعال في المسار الحالي بسبب Siegel--Walfisz.

## 3. سلسلة البرهان المعتمدة

```text
CHARACTER ORTHOGONALITY
 -> RESIDUE VARIANCE / CHARACTER SECOND MOMENT
 -> MV-01 WEIGHTED CONDUCTOR REDUCTION
 -> MV-02 WEIGHTED LARGE SIEVE
 -> MV-04C SPLIT AT Y=max(2,(x/Q)log(2Q))
      SMALL CONDUCTORS: CHAPTER-12 SIEGEL--WALFISZ
      LARGE CONDUCTORS: DIRECT LARGE SIEVE ON LAMBDA
 -> MV-08 PRINCIPAL / LOCAL ASSEMBLY
 -> MV-09 RANGE / FINAL ASSEMBLY
 -> MV-10 LOGIC AUDIT = PASS
 -> REFERENCE AUDIT = PASS
```

الوحدات `MV-03`, `MV-04`, `MV-04B` ليست ضمن سلسلة الاعتماد النهائية؛ تحفظ لتوثيق مسار Vaughan المؤجل وعائق التصادمات الضربية.

## 4. الملفات الملزمة للمراجعة

1. `docs/CHAPTER_14_MV01_WEIGHTED_CONDUCTOR_DECOMPOSITION_2026-07-24.md`
2. `docs/CHAPTER_14_MV02_DUALITY_WEIGHTED_LARGE_SIEVE_2026-07-24.md`
3. `docs/CHAPTER_14_MV04C_CONDUCTOR_SPLIT_ROUTE_REPAIR_2026-07-24.md`
4. `docs/CHAPTER_14_MV08_PRINCIPAL_LOCAL_ASSEMBLY_2026-07-24.md`
5. `docs/CHAPTER_14_MV09_RANGE_FINAL_ASSEMBLY_2026-07-24.md`
6. `docs/CHAPTER_14_MV10_LOGIC_AUDIT_2026-07-24.md`
7. `docs/CHAPTER_14_REFERENCE_AUDIT_2026-07-24.md`
8. `research/literature-reviews/chapter-14-barban-davenport-halberstam-proof-map.md`

ملفات سياقية غير معتمدة في النتيجة النهائية:

- `docs/CHAPTER_14_MV03_BILINEAR_DECOMPOSITION_2026-07-24.md`
- `docs/CHAPTER_14_MV04_DIAGONAL_SPLIT_2026-07-24.md`
- `docs/CHAPTER_14_MV04B_MULTIPLICATIVE_COLLISION_AUDIT_2026-07-24.md`

## 5. قائمة الفحص الرياضية

على المراجع التحقق صراحة من الآتي:

### A. التطبيع والتعامد

- صحة تعريف \(\Psi^\circ(x,\chi)\).
- صحة عامل \(1/\varphi(q)\) في هوية التباين.
- عدم حذف الشخصية الرئيسية أو مضاعفتها.

### B. رد الموصلات

- فرادة الجد البدائي لكل شخصية.
- دقة إعادة الفهرسة بوزن
  \[
  W_Q(r)=\sum_{m\le Q/r}\frac1{\varphi(rm)}.
  \]
- صحة اتجاه الحد
  \[
  W_Q(r)\ll\frac{\log(2Q/r)}{\varphi(r)}.
  \]
- صحة تقدير التصحيحات المحلية \(O(Q(\log x)^2)\).

### C. الغربال الكبير الموزون

- مطابقة الصيغة للمبرهنة 19.16 من Montgomery--Vaughan II.
- صحة الانتقال على الكتلة \(R<r\le2R\):
  \[
  W_Q(r)\ll \frac{\log(2Q/R)}{R}\frac r{\varphi(r)}.
  \]
- عدم وجود عامل مفقود في عدد الشخصيات أو طول الفترة.

### D. فصل الموصلات

- صحة اختيار
  \[
  Y=\max\!\left(2,\frac{x}{Q}\log(2Q)\right).
  \]
- صحة \(2\le Y\le Q\) بعد حد يعتمد على \(A\).
- دخول \(r\le Y\) في مجال Siegel--Walfisz.
- صحة جمع كتل \(r>Y\)، ولا سيما
  \[
  \sum_R R\log\frac{2Q}{R}\ll Q,
  \qquad
  \sum_R\frac{x}{R}\log\frac{2Q}{R}\ll Q.
  \]

### E. الشخصية الرئيسية والتجميع

- صحة حالة الموصل `1`.
- صحة صيغة حذف القوى الأولية القاسمة للترديد.
- صحة العودة من المتوسط على الشخصيات إلى تباين الفئات.
- صحة امتصاص \(Q(\log x)^2\) في \(xQ\log x\).

### F. المجال والفعالية

- صحة معالجة المجال المحدود \(3\le x<x_0(A)\).
- تسجيل اعتماد الثابت على \(A\).
- تسجيل عدم الفعالية وعدم وجود ادعاء فعالية زائف.

### G. عدم الدور

- عدم استعمال BDH أو Bombieri--Vinogradov لإثبات النتيجة.
- عدم اعتماد المسار النهائي على Vaughan أو طبقة التصادمات.
- عدم استعمال GRH.

## 6. أسئلة حرجة للمراجع

1. هل يوجد خطأ في التطبيع أو عامل \(\varphi(q)\)؟
2. هل تقدير تصحيحات الاستحثاث \(O(Q(\log x)^2)\) مكتمل؟
3. هل تطبيق الغربال الكبير على \(\Lambda\) في الموصلات الكبيرة مشروع بالتطبيع المستعمل؟
4. هل حد الفصل \(Y\) يوازن حد \(x/R\) دون فجوة عند أول كتلة ديادية؟
5. هل استعمال Siegel--Walfisz يغطي الشخصية البدائية modulo `1` كما صيغ؟
6. هل توجد دائرة خفية عبر الفصلين 12 أو 13؟
7. هل الادعاء الموسوم «الحد الكلاسيكي لـBDH» مضبوط من حيث المجال والنطاق، ولا يتجاوز ما ثبت؟

## 7. نموذج الحكم

```text
REVIEWER                    =
REVIEW-DATE                 =
REVIEWED-HEAD               = 49a76dcdb18318aaa548a34d2918b9c7d846a141
VERDICT                     = APPROVED | APPROVED-WITH-NONBLOCKING-CORRECTIONS | CHANGES-REQUIRED | REJECTED
BLOCKING-CORRECTIONS        =
NONBLOCKING-CORRECTIONS     =
NORMALIZATION               = PASS | FAIL
CONDUCTOR-REDUCTION         = PASS | FAIL
LOCAL-CORRECTIONS           = PASS | FAIL
WEIGHTED-LARGE-SIEVE        = PASS | FAIL
CONDUCTOR-SPLIT             = PASS | FAIL
SMALL-CONDUCTORS            = PASS | FAIL
LARGE-CONDUCTORS            = PASS | FAIL
FINAL-ASSEMBLY              = PASS | FAIL
NON-CIRCULARITY             = PASS | FAIL
REFERENCE-SUPPORT           = PASS | FAIL
INEFFECTIVITY-LABEL         = PASS | FAIL
AUTHORING-RECOMMENDATION    = YES | NO
COMMENTS                    =
```

## 8. قواعد الإغلاق

- `APPROVED`: يجوز للمالك اتخاذ قرار `PASS-FOR-AUTHORING`.
- `APPROVED-WITH-NONBLOCKING-CORRECTIONS`: تطبق التصحيحات وتسجل قبل قرار التأليف.
- `CHANGES-REQUIRED`: يبقى التأليف محجوبًا حتى الإصلاح وإعادة المراجعة.
- `REJECTED`: يعاد فتح المسار الرياضي.

لا تدمج PR #26، ولا تحجز معرفات نتائج، ولا ينشأ متن LaTeX قبل القرار الصريح للمالك بعد استلام الحكم.

## 9. الحالة الحالية

```text
INDEPENDENT-REVIEW-PACKET = COMPLETE
INDEPENDENT-REVIEW        = PENDING
PASS-FOR-AUTHORING        = NO
PR-26                     = DRAFT / OPEN / UNMERGED
NEXT                      = OBTAIN-INDEPENDENT-VERDICT
```
