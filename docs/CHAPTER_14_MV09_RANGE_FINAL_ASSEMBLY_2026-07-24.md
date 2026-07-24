# MV-09 — تدقيق المجال والتجميع النهائي

التاريخ: 2026-07-24

```text
VERSION                         = 0.18.0-dev
CHAPTER                         = 14
UNIT                            = MV-09
TOPIC                           = RANGE / THRESHOLD / SMALL-X / FINAL-ASSEMBLY
STATUS                          = PROVED-HERE-DRAFT
RANGE-CHECK                     = PROVED-HERE-DRAFT
THRESHOLD-CHECK                 = PROVED-HERE-DRAFT
SMALL-X-ABSORPTION              = PROVED-HERE-DRAFT
INEFFECTIVITY-TRACKING          = PROVED-HERE-DRAFT
CLASSICAL-BDH-UPPER-BOUND       = PROVED-HERE-DRAFT
FORMAL-LOGIC-AUDIT              = PENDING
REFERENCE-AUDIT                 = PENDING
INDEPENDENT-REVIEW              = PENDING
NEXT-UNIT                       = MV-10 / LOGIC-AND-REFERENCE-CLOSURE
PASS-FOR-AUTHORING              = NO
```

## 1. الهدف

من `MV-08` لدينا المرشح

\[
V_\psi(x,Q)
\ll_A xQ\log x
\]

في المجال

\[
\frac{x}{(\log x)^A}\le Q\le x.
\]

تبقى أربع نقاط يجب تثبيتها قبل إعلان الإغلاق الرياضي للمسودة:

1. أن حد الفصل
   \[
   Y=\max\!\left(2,\frac{x}{Q}\log(2Q)\right)
   \]
   يقع في المجال الصحيح.
2. أن جميع الموصلات الصغيرة تقع فعلًا داخل مجال Siegel--Walfisz.
3. أن القيم الصغيرة لـ\(x\) لا تفتح استثناءً غير مسجل.
4. أن اعتماد الثابت وعدم الفعالية موثق بدقة.

## 2. فرضيات المجال

نثبت ثابتًا

\[
A>0.
\]

ونفترض أولًا أن

\[
x\ge x_0(A),
\qquad
\frac{x}{(\log x)^A}\le Q\le x.
\]

يجوز أخذ \(Q\) حقيقيًا؛ فجميع المجاميع على \(q\le Q\) و\(r\le Q\) تعتمد فقط على \(\lfloor Q\rfloor\). وإذا كان المجال غير فارغ، فـ\(Q\ge1\) تلقائيًا عند تكبير \(x_0(A)\).

## 3. تحقق أن حد الفصل لا يتجاوز \(Q\)

نحتاج إلى

\[
Y\le Q
\]

لكي يكون الفصل إلى موصلات صغيرة وكبيرة غير متداخل ويغطي المجال كله.

يكفي إثبات

\[
\frac{x}{Q}\log(2Q)\le Q,
\]

أي

\[
x\log(2Q)\le Q^2.
\]

من الحد الأدنى لـ\(Q\):

\[
Q^2
\ge
\frac{x^2}{(\log x)^{2A}}.
\]

ولأن \(Q\le x\)، فإن

\[
\log(2Q)\le \log(2x)\ll\log x.
\]

إذن يكفي

\[
\frac{x^2}{(\log x)^{2A}}
\ge Cx\log x,
\]

أو

\[
x\ge C(\log x)^{2A+1},
\]

وهو صحيح لكل \(x\ge x_0(A)\) مناسب.

وعليه

\[
\boxed{2\le Y\le Q}
\]

لكل \(x\ge x_0(A)\) في المجال المعتمد.

## 4. دخول الموصلات الصغيرة في Siegel--Walfisz

من

\[
Q\ge \frac{x}{(\log x)^A}
\]

نحصل على

\[
\frac{x}{Q}\le (\log x)^A.
\]

وكذلك

\[
\log(2Q)\le \log(2x)\ll\log x.
\]

إذن

\[
Y
\le
2+(\log x)^A\log(2x)
\ll_A (\log x)^{A+1}.
\]

لذلك يمكن تطبيق Siegel--Walfisz من الفصل الثاني عشر بقوة لوغاريتمية ثابتة، مثل

\[
B=A+2,
\]

على جميع الشخصيات البدائية ذات

\[
r\le Y.
\]

ومن ثم لا توجد فجوة بين تعريف \(Y\) ومجال نتيجة الفصل الثاني عشر.

## 5. الموصلات الكبيرة

للكتل الديادية

\[
R<r\le2R,
\qquad
R\ge Y/2,
\]

ثبت في `MV-04C` أن مساهمتها لا تتجاوز

\[
\ll
x\log x
\left(\frac{x}{R}+R\right)
\log\frac{2Q}{R}.
\]

والجمع على الكتل يعطي

\[
\sum_R R\log\frac{2Q}{R}\ll Q,
\]

و

\[
\sum_R\frac{x}{R}\log\frac{2Q}{R}
\ll
\frac{x}{Y}\log\frac{2Q}{Y}
\le Q.
\]

لذلك

\[
\boxed{\mathcal P_{>Y}(x,Q)\ll xQ\log x}.
\]

الثابت في هذا الجزء مطلق وفعّال.

## 6. الموصلات الصغيرة

من Siegel--Walfisz، بعد اختيار القوة \(B=A+2\)، توجد ثوابت \(c_A>0\) و\(C_A>0\) بحيث

\[
|\Psi^\circ(x,\chi^*)|
\le
C_Ax e^{-c_A\sqrt{\log x}}
\]

بانتظام لكل \(r\le Y\).

ومن ثم

\[
\mathcal P_{\le Y}(x,Q)
\ll_A
Y\log(2Q)x^2e^{-2c_A\sqrt{\log x}}.
\]

وبما أن \(Y\ll_A(\log x)^{A+1}\)، فإن الادخار الأسي يمتص جميع القوى اللوغاريتمية. كذلك من

\[
Q\ge x(\log x)^{-A}
\]

ينتج

\[
xQ\log x
\ge
\frac{x^2}{(\log x)^{A-1}}.
\]

لذلك

\[
\boxed{\mathcal P_{\le Y}(x,Q)=o_A(xQ\log x)}.
\]

مصدر عدم الفعالية في الثابت النهائي هو هذا القسم وحده.

## 7. تصحيحات الاستحثاث

من `MV-01` و`MV-08`:

\[
\mathcal S(x,Q)
\le
2\mathcal P(x,Q)
+O\!\left(Q(\log x)^2\right).
\]

ولأن \(x\ge3\):

\[
Q(\log x)^2
\le
xQ\log x
\]

بعد تعديل ثابت مطلق. إذن تصحيحات الاستحثاث لا تضيق المجال ولا تغير رتبة الحد النهائي.

## 8. القيم الصغيرة لـ\(x\)

البرهان السابق استعمل \(x\ge x_0(A)\). نزيل هذا القيد من صيغة المبرهنة بتكبير الثابت.

لأي مجال محدود

\[
3\le x<x_0(A),
\qquad
1\le Q\le x,
\]

لدينا تقدير تافه

\[
\psi(x;q,a)\le\psi(x)\le x\log x,
\]

ومن ثم

\[
V_\psi(x,Q)
\ll_A 1
\]

على هذا المجال المضغوط بعد القسمة على \(xQ\log x>0\). وبأخذ أكبر نسبة على المجال المحدود وضمها إلى الثابت نحصل على صيغة موحدة لكل \(x\ge3\).

لا يدعي هذا حساب ثابت صريح؛ بل يثبت وجود ثابت يعتمد على \(A\).

## 9. الصيغة النهائية للمسودة

لكل ثابت \(A>0\)، يوجد ثابت \(C_A>0\) بحيث لكل \(x\ge3\) ولكل \(Q\) يحقق

\[
\frac{x}{(\log x)^A}\le Q\le x,
\]

لدينا

\[
\boxed{
V_\psi(x,Q)
\le
C_A xQ\log x
}.
\]

حيث

\[
V_\psi(x,Q)=
\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|
\psi(x;q,a)-\frac{x}{\varphi(q)}
\right|^2.
\]

نسجلها بصيغة الاختصار:

\[
\boxed{
V_\psi(x,Q)\ll_A xQ\log x,
\qquad
x(\log x)^{-A}\le Q\le x
}.
\]

## 10. اعتماد الثابت وفعاليته

```text
DEPENDENCE-ON-A       = YES
EFFECTIVE-LARGE-SIEVE = YES
EFFECTIVE-LOCAL-TERMS = YES
SIEGEL-WALFISZ-INPUT  = INEFFECTIVE
FINAL-CONSTANT        = INEFFECTIVE-IN-CURRENT-ROUTE
```

لا يجوز وصف ثابت المتراجحة بأنه فعّال ما دام المسار الصغير يعتمد على صيغة Siegel--Walfisz غير الفعالة.

## 11. عدم الدور

المسار النهائي يعتمد على:

1. تعامد الشخصيات وتحويل التباين؛
2. رد الشخصيات إلى موصلاتها؛
3. وزن الموصل من `MV-01`؛
4. الغربال الكبير الموزون من `MV-02`؛
5. Siegel--Walfisz من الفصل الثاني عشر؛
6. الحد الأولي \(\sum_{n\le x}\Lambda(n)^2\ll x\log x\)؛
7. جمع ديادي هندسي.

ولا يعتمد على:

- مبرهنة Barban--Davenport--Halberstam نفسها؛
- Bombieri--Vinogradov؛
- مسار Vaughan المؤجل؛
- GRH.

## 12. حدود الادعاء

1. الحد الكلاسيكي مغلق رياضيًا على مستوى المسودة فقط.
2. لم يجر بعد التدقيق المنطقي الشامل عبر جميع الوحدات.
3. لم يجر بعد التدقيق المرجعي للمسار النهائي.
4. لم تجر المراجعة المستقلة.
5. لا يوجد إذن بالتأليف أو حجز نتيجة في السجل المركزي بعد.

## 13. الحكم

```text
MV-09 RANGE                       = PROVED-HERE-DRAFT
MV-09 Y-LE-Q                      = PROVED-HERE-DRAFT
MV-09 SMALL-CONDUCTOR-COVERAGE    = PROVED-HERE-DRAFT
MV-09 SMALL-X-ABSORPTION          = PROVED-HERE-DRAFT
MV-09 INEFFECTIVITY               = PROVED-HERE-DRAFT
MV-09 CLASSICAL-BDH-UPPER-BOUND   = PROVED-HERE-DRAFT
MV-09                             = COMPLETE-AS-DRAFT
NEXT                              = MV-10 / LOGIC-AND-REFERENCE-CLOSURE
PASS-FOR-AUTHORING                = NO
```