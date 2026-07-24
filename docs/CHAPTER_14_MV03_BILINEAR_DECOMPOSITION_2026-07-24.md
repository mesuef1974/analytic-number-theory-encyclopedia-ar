# MV-03 — التفكيك الخطي والثنائي لمعاملات فون مانغولت

التاريخ: 2026-07-24

```text
VERSION                    = 0.18.0-dev
CHAPTER                    = 14
UNIT                       = MV-03
TOPIC                      = VAUGHAN / TYPE-I / TYPE-II / DYADIC-RECTANGLES
STATUS                     = PROVED-HERE-DRAFT
VAUGHAN-INPUT              = PROVED-HERE / CHAPTER-13
TYPE-I-REDUCTION           = PROVED-HERE-DRAFT
TYPE-II-REDUCTION          = PROVED-HERE-DRAFT
DYADIC-RECTANGULATION      = PROVED-HERE-DRAFT
COEFFICIENT-L2-BOUNDS      = PROVED-HERE-DRAFT
FORMAL-LOGIC-AUDIT         = PENDING
REFERENCE-AUDIT            = PENDING
INDEPENDENT-REVIEW         = PENDING
NEXT-UNIT                  = MV-04
PASS-FOR-AUTHORING         = NO
```

## 1. الهدف

نريد تفكيك المجموع الملتوي

\[
\Psi(x,\chi)=\sum_{n\le x}\Lambda(n)\chi(n)
\]

إلى عدد لوغاريتمي من المجاميع القصيرة، ومجاميع Type I، ومجاميع Type II على مستطيلات ديادية، مع ضبط صريح لمعاملاتها في معيار \(\ell^2\).

هذه الوحدة جبرية/تنظيمية. لا تقدر بعد المتوسط التربيعي على الشخصيات.

## 2. مدخل Vaughan الداخلي

من الفصل الثالث عشر، لكل \(U,V\ge1\):

\[
\Lambda=c_1+c_2+c_3+c_4,
\]

حيث

\[
\begin{aligned}
c_1(n)&=\Lambda(n)\mathbf 1_{n\le U},\\
c_2(n)&=-\sum_{rdk=n\atop d\le U,\,k\le V}\Lambda(d)\mu(k),\\
c_3(n)&=\sum_{mk=n\atop k\le V}\mu(k)\log m,\\
c_4(n)&=\sum_{mk=n\atop m>U,\,k>V}b_U(m)\mu(k),
\end{aligned}
\]

مع

\[
b_U(m)=\sum_{d\mid m\atop d>U}\Lambda(d),
\qquad |b_U(m)|\le\log m.
\]

إذن

\[
\Psi(x,\chi)=\Psi_1+\Psi_2+\Psi_3+\Psi_4.
\]

## 3. الحد القصير

لدينا

\[
\Psi_1(x,\chi)=\sum_{n\le\min(x,U)}\Lambda(n)\chi(n).
\]

وبالتالي

\[
|\Psi_1(x,\chi)|\le\sum_{n\le U}\Lambda(n)\le U\log(2U).
\]

كما أن

\[
\sum_{n\le U}|\Lambda(n)|^2\le U(\log(2U))^2.
\]

يسجل هذا الحد بوصفه قطعة قصيرة مستقلة.

## 4. الحد الأول من Type I

عرّف

\[
a(t)=-\sum_{dk=t\atop d\le U,\,k\le V}\Lambda(d)\mu(k).
\]

عندئذ

\[
|a(t)|\le\sum_{d\mid t}\Lambda(d)=\log t,
\qquad a(t)=0\quad(t>UV).
\]

ولدينا

\[
\Psi_2(x,\chi)=\sum_{t\le UV}a(t)\chi(t)
\sum_{r\le x/t}\chi(r).
\]

نقسم \(t\) دياديًا إلى كتل \(T<t\le2T\). لكل كتلة نحصل على شكل Type I:

\[
\mathcal I_2(T;\chi)
=
\sum_{T<t\le2T}a(t)\chi(t)
\sum_{r\le x/t}\chi(r).
\]

وتحقق معاملات الكتلة:

\[
\sum_{T<t\le2T}|a(t)|^2
\le T(\log(2T))^2.
\]

عدد كتل \(T\) هو \(O(\log(2UV))\).

## 5. الحد اللوغاريتمي من Type I

لدينا

\[
\Psi_3(x,\chi)
=
\sum_{k\le V}\mu(k)\chi(k)
\sum_{m\le x/k}(\log m)\chi(m).
\]

نستعمل الجمع الجزئي. إذا

\[
A_\chi(y)=\sum_{m\le y}\chi(m),
\]

فإن

\[
\sum_{m\le Y}(\log m)\chi(m)
=
(\log Y)A_\chi(Y)-\int_1^Y\frac{A_\chi(t)}{t}\,dt.
\]

ومن ثم ترد \(\Psi_3\) إلى مجموع نهائي/تكاملي من أشكال Type I تعتمد على المجاميع الجزئية \(A_\chi(t)\)، مع خسارة قصوى من رتبة \(\log(2x)\).

وبتقسيم \(k\) إلى كتل \(K<k\le2K\):

\[
\mathcal I_3(K,Y;\chi)
=
\sum_{K<k\le2K}\mu(k)\chi(k)A_\chi(Y_k),
\qquad Y_k\le x/k.
\]

ولدينا ببساطة

\[
\sum_{K<k\le2K}|\mu(k)|^2\le K.
\]

عدد كتل \(K\) هو \(O(\log(2V))\).

## 6. الحد من Type II

لدينا

\[
\Psi_4(x,\chi)
=
\sum_{mk\le x\atop m>U,\,k>V}
 b_U(m)\mu(k)\chi(mk).
\]

وبتضاعف الشخصية:

\[
\Psi_4(x,\chi)
=
\sum_{mk\le x\atop m>U,\,k>V}
 b_U(m)\mu(k)\chi(m)\chi(k).
\]

نقسم المتغيرين دياديًا:

\[
M<m\le2M,
\qquad
K<k\le2K,
\qquad MK\ll x.
\]

فتنتج مستطيلات Type II:

\[
\mathcal B(M,K;\chi)
=
\sum_{M<m\le2M} \alpha_m\chi(m)
\sum_{K<k\le \min(2K,x/m)}\beta_k\chi(k),
\]

حيث

\[
\alpha_m=b_U(m),
\qquad
\beta_k=\mu(k).
\]

حدود المعاملات:

\[
|\alpha_m|\le\log(2M),
\qquad |\beta_k|\le1,
\]

ومن ثم

\[
\sum_{M<m\le2M}|\alpha_m|^2
\le M(\log(2M))^2,
\]

و

\[
\sum_{K<k\le2K}|\beta_k|^2\le K.
\]

كما أن عدد المستطيلات المقبولة هو \(O((\log(2x))^2)\).

## 7. إزالة الحد المائل \(mk\le x\)

داخل المستطيل الديادي قد يظهر القيد المائل \(mk\le x\). نعالجه بإحدى طريقتين متكافئتين:

1. إبقاء النهاية الداخلية \(k\le x/m\) واستعمال صيغة الغربال الكبير للفترات المنقولة والمجاميع الجزئية؛ أو
2. تقسيم المستطيل المائل إلى \(O(\log(2x))\) مستطيلات/شرائط إضافية باستعمال تقسيم ديادي أو مبدأ الفصل الثنائي.

في كلا المسارين لا تزيد الخسارة التنظيمية على قوة لوغاريتمية ثابتة. في الوحدات التالية سنستعمل الصيغة ذات النهاية المتغيرة لأنها تحافظ على عدد أقل من القطع.

## 8. صيغة التجميع النهائية

توجد عائلة \(\mathfrak I\) من قطع Type I وعائلة \(\mathfrak B\) من قطع Type II بحيث

\[
\Psi(x,\chi)
=
\Psi_1(x,\chi)
+
\sum_{I\in\mathfrak I} I(\chi)
+
\sum_{B\in\mathfrak B} B(\chi),
\]

مع

\[
|\mathfrak I|\ll (\log(2x))^2,
\qquad
|\mathfrak B|\ll (\log(2x))^2,
\]

بعد إدخال خسارة الجمع الجزئي والتنظيم الديادي في الثوابت اللوغاريتمية.

كل قطعة Type I لها معامل خارجي مدعوم على كتلة طولها \(T\) أو \(K\) ومعيار تربيعي من الرتبة

\[
\ll T(\log(2x))^2
\quad\text{أو}\quad
\ll K,
\]

وكل قطعة Type II على مستطيل \(M\times K\) تحقق

\[
\|\alpha\|_2^2\ll M(\log(2x))^2,
\qquad
\|\beta\|_2^2\ll K.
\]

## 9. اختيار المعلمات

لم نختر بعد \(U,V\). يجب أن يحدد الاختيار في `MV-04` و`MV-05` بعد موازنة:

- القطعة القصيرة؛
- طول المتغير الخارجي في Type I؛
- الشرطين \(m>U\), \(k>V\) في Type II؛
- حد الغربال الكبير الموزون

\[
\left(\frac NR+R\right)\log\frac{2Q}{R}.
\]

لذلك يبقى \(U,V\) حرين في هذه الوحدة.

## 10. عدم الدور

هذه الوحدة تعتمد فقط على:

1. هوية Vaughan المثبتة داخليًا في الفصل الثالث عشر؛
2. التضاعف التام لشخصيات ديريشليه؛
3. الجمع الجزئي؛
4. التقسيم الديادي؛
5. حدود أولية للمعاملات.

لا تستعمل مبرهنة Barban أو BDH أو نتيجة متوسطة تربيعية مكافئة.

## 11. حدود الادعاء

- لم تقدر بعد قطع Type I في المتوسط على الشخصيات.
- لم تقدر بعد قطع Type II.
- لم يفصل بعد الحد القطري عن خارج القطري.
- لم تثبت بعد مبرهنة باربان العامة.
- الحالات الحالية تبقى `PROVED-HERE-DRAFT` حتى التدقيق اللاحق.

## 12. الحكم

```text
MV-03 VAUGHAN-DECOMPOSITION  = PROVED-HERE-DRAFT
MV-03 TYPE-I-REDUCTION       = PROVED-HERE-DRAFT
MV-03 TYPE-II-REDUCTION      = PROVED-HERE-DRAFT
MV-03 DYADIC-RECTANGULATION  = PROVED-HERE-DRAFT
MV-03 COEFFICIENT-L2-BOUNDS  = PROVED-HERE-DRAFT
MV-03 NON-CIRCULARITY        = PASS-AT-DRAFT-LEVEL
MV-03 LOGIC-AUDIT            = PENDING
MV-03 REFERENCE-AUDIT        = PENDING
MV-03 INDEPENDENT-REVIEW     = PENDING
MV-03                        = COMPLETE-AS-DRAFT
NEXT                         = MV-04
PASS-FOR-AUTHORING           = NO
```
