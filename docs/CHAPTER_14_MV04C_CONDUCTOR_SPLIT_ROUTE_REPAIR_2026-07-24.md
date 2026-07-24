# MV-04C — إصلاح المسار بفصل الموصلات

التاريخ: 2026-07-24

```text
VERSION                         = 0.18.0-dev
CHAPTER                         = 14
UNIT                            = MV-04C
TOPIC                           = CONDUCTOR-SPLIT / LARGE-SIEVE / SIEGEL-WALFISZ
STATUS                          = PROVED-HERE-DRAFT
OLD-VAUGHAN-RECTANGLE-ROUTE     = NOT-REQUIRED-FOR-CLASSICAL-UPPER-BOUND
SMALL-CONDUCTORS                = CONTROLLED-BY-CHAPTER-12
LARGE-CONDUCTORS                = CONTROLLED-BY-MV-02
PRIMITIVE-WEIGHTED-MEAN-SQUARE  = PROVED-HERE-DRAFT
FORMAL-LOGIC-AUDIT              = PENDING
REFERENCE-AUDIT                 = PENDING
INDEPENDENT-REVIEW              = PENDING
NEXT-UNIT                       = MV-08 / LOCAL-AND-PRINCIPAL-ASSEMBLY
PASS-FOR-AUTHORING              = NO
```

## 1. سبب إصلاح المسار

أثبت `MV-04B` أن تجميع مستطيلات Vaughan في معاملات

\[
c_n=\sum_{mk=n}\alpha_m\beta_k
\]

قبل استعمال المتوسط يولد طاقة تصادمات ضربية لا يتوافر لها شكليًا إلا حد من نوع \(x^{o(1)}\). هذا لا يلزم أن يكون جزءًا من برهان الحد الكلاسيكي لـBDH في المجال

\[
\frac{x}{(\log x)^A}\le Q\le x.
\]

الملاحظة الحاسمة هي أن الغربال الكبير الخام يصبح كافيًا بعد استبعاد الموصلات الصغيرة، بينما الموصلات الصغيرة تقع في مجال Siegel--Walfisz المثبت في الفصل الثاني عشر.

## 2. نقطة الانطلاق

من `MV-01` لدينا

\[
\mathcal S(x,Q)
\le 2\mathcal P(x,Q)+O\!\left(Q(\log x)^2\right),
\]

حيث

\[
\mathcal P(x,Q)=
\sum_{r\le Q}W_Q(r)
\sum_{\chi^*\bmod r}^{*}
|\Psi^\circ(x,\chi^*)|^2
\]

و

\[
W_Q(r)\ll \frac{\log(2Q/r)}{\varphi(r)}.
\]

نثبت أن

\[
\boxed{\mathcal P(x,Q)\ll_A xQ\log x}
\]

بفصل الموصلات فقط.

## 3. حد الفصل

ضع

\[
Y=\max\!\left(2,\frac{x}{Q}\log(2Q)\right).
\]

إذا

\[
Q\ge \frac{x}{(\log x)^A},
\]

فإن

\[
Y\ll_A (\log x)^{A+1}.
\]

نكتب

\[
\mathcal P=\mathcal P_{\le Y}+\mathcal P_{>Y}.
\]

## 4. الموصلات الصغيرة

نتيجة Siegel--Walfisz في الفصل الثاني عشر تعطي، لكل ثابت \(B\)، وبانتظام للشخصيات البدائية ذات

\[
r\le (\log x)^B,
\]

حدًا من الشكل

\[
|\Psi^\circ(x,\chi^*)|
\ll_B x e^{-c_B\sqrt{\log x}}.
\]

يشمل الموصل \(r=1\) بعد استعمال حد دو لا فاليه بوسان للشخصية الرئيسية المتمركزة، كما هو مفصول في الفصل الثاني عشر.

وبما أن عدد الشخصيات البدائية لا يتجاوز \(\varphi(r)\)، فإن

\[
\begin{aligned}
\mathcal P_{\le Y}
&\ll_A
x^2 e^{-2c_A\sqrt{\log x}}
\sum_{r\le Y}W_Q(r)\varphi(r)\\
&\ll_A
x^2 e^{-2c_A\sqrt{\log x}}
\sum_{r\le Y}\log(2Q/r)\\
&\ll_A
Y\log(2Q)\,x^2e^{-2c_A\sqrt{\log x}}.
\end{aligned}
\]

ولأن \(Y\) قوة ثابتة من \(\log x\)، يمتص الادخار الأسي جميع القوى اللوغاريتمية، ومن ثم

\[
\boxed{\mathcal P_{\le Y}=o_A(xQ\log x)}.
\]

## 5. الموصلات الكبيرة: الكتلة الديادية

قسّم \(Y<r\le Q\) إلى كتل

\[
R<r\le2R.
\]

من `MV-02`، مع \(c_n=\Lambda(n)\) المدعومة على \(n\le x\):

\[
\sum_{R<r\le2R}W_Q(r)
\sum_{\chi^*\bmod r}^{*}
\left|\sum_{n\le x}\Lambda(n)\chi^*(n)\right|^2
\]

\[
\ll
\left(\frac{x}{R}+R\right)
\log\frac{2Q}{R}
\sum_{n\le x}\Lambda(n)^2.
\]

ونستعمل الحد الأولي

\[
\sum_{n\le x}\Lambda(n)^2\ll x\log x.
\]

إذن مساهمة الكتلة لا تتجاوز

\[
\ll
x\log x
\left(\frac{x}{R}+R\right)
\log\frac{2Q}{R}.
\]

## 6. جمع الكتل الكبيرة

للكتل الديادية بين \(Y\) و\(Q\):

\[
\sum_R R\log\frac{2Q}{R}\ll Q.
\]

كذلك، بسبب التناقص الهندسي لـ\(1/R\):

\[
\sum_R \frac{x}{R}\log\frac{2Q}{R}
\ll
\frac{x}{Y}\log(2Q/Y).
\]

ومن تعريف \(Y\):

\[
\frac{x}{Y}\log(2Q/Y)
\le
\frac{x}{Y}\log(2Q)
\le Q.
\]

وعليه

\[
\boxed{
\mathcal P_{>Y}\ll xQ\log x
}.
\]

## 7. النتيجة البدائية الموزونة

بجمع الجزأين:

\[
\boxed{
\mathcal P(x,Q)\ll_A xQ\log x,
\qquad
\frac{x}{(\log x)^A}\le Q\le x
}.
\]

ثم من `MV-01`:

\[
\mathcal S(x,Q)
\ll_A xQ\log x+Q(\log x)^2.
\]

ولـ\(x\) الكبير يكون الحد الثاني أصغر من الهدف، فنحصل على

\[
\boxed{
\mathcal S(x,Q)\ll_A xQ\log x
}.
\]

هذه النتيجة ما تزال `PROVED-HERE-DRAFT` إلى حين تدقيق التجميع المحلي والشخصية الرئيسية ونقلها النهائي إلى تباين الفئات.

## 8. لماذا اختفى عائق التصادمات

لم نستعمل تفكيك Vaughan في هذا المسار. الغربال الكبير يطبق مباشرة على المتتالية الأصلية \(\Lambda(n)\)، ولكن فقط على الموصلات

\[
r>Y\asymp \frac{x}{Q}\log Q.
\]

عند هذا الحد تصبح مساهمة \(x/R\) بعد الجمع الديادي من رتبة \(Q\)، بينما تسيطر Siegel--Walfisz على الباقي. لذلك لا تتكون معاملات الالتفاف \(c_n\)، ولا تظهر طاقة التصادمات الضربية.

## 9. تصحيح الحوكمة

المسار السابق

```text
MV-03 -> MV-04 -> MV-05 -> MV-06
```

ليس لازمًا للحد الكلاسيكي في المجال القريب من \(x\). يبقى صالحًا كمسار بحثي لمبرهنة باربان العامة أو لمجالات أوسع، لكنه ينقل إلى طبقة مؤجلة ولا يحجب الفصل الكلاسيكي.

المسار المعتمد الآن هو

```text
MV-01 WEIGHTED CONDUCTOR REDUCTION
 -> MV-02 WEIGHTED LARGE SIEVE
 -> MV-04C SPLIT AT Y=(x/Q)log(2Q)
      -> SMALL CONDUCTORS: SIEGEL--WALFISZ
      -> LARGE CONDUCTORS: DIRECT LARGE SIEVE
 -> PRINCIPAL / LOCAL ASSEMBLY
 -> CLASSICAL BDH UPPER BOUND
```

## 10. الاعتمادات وعدم الدور

يعتمد البرهان على:

1. تحويل الشخصيات ورد الموصلات ووزن `MV-01`؛
2. الغربال الكبير الموزون من `MV-02`؛
3. نتيجة Siegel--Walfisz المدققة في الفصل الثاني عشر؛
4. حد \(\sum_{n\le x}\Lambda(n)^2\ll x\log x\)؛
5. جمع ديادي هندسي.

لا يستعمل Barban أو BDH أو Bombieri--Vinogradov أو تفكيك Vaughan في إثبات النتيجة.

## 11. حدود الادعاء

- لم يجر بعد التدقيق المنطقي الرسمي لهذه الوحدة.
- يجب تدقيق الموصل \(1\) والتوسيط والتصحيحات المحلية مرة أخيرة في `MV-08`.
- لم ينقل بعد الحد من متوسط الشخصيات إلى الصيغة النهائية للفئات في وحدة الإغلاق.
- لا إذن بالتأليف بعد.

## 12. الحكم

```text
MV-04C CONDUCTOR-THRESHOLD       = PROVED-HERE-DRAFT
MV-04C SMALL-CONDUCTORS           = PROVED-HERE-DRAFT / CHAPTER-12-INPUT
MV-04C LARGE-CONDUCTORS           = PROVED-HERE-DRAFT
MV-04C DYADIC-SUMMATION           = PROVED-HERE-DRAFT
MV-04C PRIMITIVE-WEIGHTED-BOUND   = PROVED-HERE-DRAFT
VAUGHAN-COLLISION-OBSTRUCTION     = BYPASSED-FOR-CLASSICAL-RANGE
GENERAL-BARBAN-ROUTE              = DEFERRED
NEXT                              = MV-08 / PRINCIPAL-LOCAL-ASSEMBLY
PASS-FOR-AUTHORING                = NO
```