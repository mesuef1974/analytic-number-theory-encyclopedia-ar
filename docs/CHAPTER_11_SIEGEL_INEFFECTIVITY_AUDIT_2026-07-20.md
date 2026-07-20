# تدقيق مبرهنة Siegel وعدم الفعالية — الفصل الحادي عشر

## بيانات التدقيق

```text
DATE                 = 2026-07-20
SCOPE                = ANT-THM-11-03 / ANT-COR-11-01
AUDIT-STATE          = PASS-FOR-CITED-THEOREM-AND-DERIVED-COROLLARY
RESULT-REGISTRY      = REMAINS-DRAFT-UNTIL-AUTHORING
CHAPTER-AUTHORING     = BLOCKED
```

## 1. صيغة مبرهنة Siegel المعتمدة

لكل \(\varepsilon>0\)، يوجد ثابت
\(c(\varepsilon)>0\) بحيث لكل شخصية ديريشليه حقيقية بدائية غير رئيسية
\(\chi\) بموصل \(q\):

\[
|L(1,\chi)|
\ge
c(\varepsilon)q^{-\varepsilon}.
\tag{1.1}
\]

ولأن الشخصية الحقيقية البدائية غير الرئيسية تربيعية، فهذه هي الصيغة المعروفة عادة بمبرهنة Siegel للشخصيات التربيعية.

الثابت \(c(\varepsilon)\) **غير فعال**: البرهان يثبت وجوده، لكن لا يقدم خوارزمية معروفة لحسابه من \(\varepsilon\).

```text
ANT-THM-11-03 = CITED
CONSTANT       = INEFFECTIVE
```

لا تدعي الموسوعة برهانًا داخليًا كاملًا لمبرهنة Siegel في هذه المرحلة.

## 2. البيانات المرجعية

### المصدر الأصلي

- Carl Siegel.
- “Über die Classenzahl quadratischer Zahlkörper”.
- *Acta Arithmetica* 1 (1935), 83--86.
- DOI: `10.4064/aa-1-1-83-86`.

### تحقق حديث للصيغة

- Zihao Liu, “A Simple Proof of Siegel's Theorem Using Mellin Transform”, arXiv:`2202.00635` (2022).
  يصرح الملخص بأن الموضوع هو الحد السفلي لـ\(L(1,\chi)\) للشخصية التربيعية البدائية.
- Mossinghoff--Starichkova--Trudgian, *Journal of Number Theory* 240 (2022), 641--655، DOI: `10.1016/j.jnt.2021.12.013`.
  تميز المقدمة بين الحد الفعال للشخصيات غير التربيعية والحد الوحيد المعروف في الحالة التربيعية
  \(|L(1,\chi)|\gg_\varepsilon q^{-\varepsilon}\).
- Basak--Pratt (2026) يسجلان الصيغة المكافئة على الصفر الحقيقي مع التأكيد على عدم فعالية الثابت.

```text
SIEGEL-BIBLIOGRAPHY = VERIFIED
SIEGEL-STATEMENT    = VERIFIED
```

## 3. معنى عدم الفعالية

عدم الفعالية لا يعني فقط أن الثابت صغير أو أن حسابه صعب عمليًا. معناه:

> لا توجد من البرهان المعروف طريقة محددة تنتهي في زمن منتهٍ وتعطي قيمة صحيحة مضمونة لـ\(c(\varepsilon)\) لكل \(\varepsilon\).

ولذلك يحظر استعمال (1.1) لإنتاج:

- ثابت عددي صريح.
- حد خطأ فعال معلن.
- مجال حسابي يمكن التحقق منه حتى عتبة محددة اعتمادًا على هذا الثابت وحده.

كل نتيجة مشتقة من (1.1) ترث عدم الفعالية، ما لم يوجد برهان فعال مستقل.

## 4. حد مشتقة \(L\) قرب الواحد

لاشتقاق حد على الصفر الحقيقي، نحتاج حدًا فعالًا للمشتقة لا يعتمد على مبرهنة Siegel.

### اللمّة

يوجد ثابت مطلق \(C>0\) بحيث إذا كانت \(\chi\) غير رئيسية بترديد \(q\)، وكان

\[
1-\frac{c_0}{\log(2q)}\le\sigma\le1,
\]

لثابت مطلق ثابت \(c_0\)، فإن

\[
|L'(\sigma,\chi)|\le C\log^2(2q).
\tag{4.1}
\]

### البرهان

ضع

\[
S(x)=\sum_{n\le x}\chi(n).
\]

من دورية الشخصية وانعدام مجموع دورة كاملة:

\[
|S(x)|\le q.
\tag{4.2}
\]

بتطبيق الجمع الجزئي عند \(q\):

\[
L(s,\chi)
=
\sum_{n\le q}\frac{\chi(n)}{n^s}
+
s\int_q^\infty \frac{S(x)}{x^{s+1}}\,dx,
\qquad \Re(s)>0.
\tag{4.3}
\]

وبالتفاضل عند \(s=\sigma\) الحقيقي:

\[
L'(\sigma,\chi)
=
-
\sum_{n\le q}
\frac{\chi(n)\log n}{n^\sigma}
+
\int_q^\infty\frac{S(x)}{x^{\sigma+1}}\,dx
-
\sigma\int_q^\infty
\frac{S(x)\log x}{x^{\sigma+1}}\,dx.
\tag{4.4}
\]

في المجال المحدد:

\[
q^{1-\sigma}\le e^{c_0}.
\]

ومن ثم

\[
\sum_{n\le q}\frac{\log n}{n^\sigma}
\le
q^{1-\sigma}
\sum_{n\le q}\frac{\log n}{n}
\ll
\log^2(2q).
\tag{4.5}
\]

وباستخدام (4.2):

\[
\int_q^\infty\frac{|S(x)|}{x^{\sigma+1}}\,dx
\le
\frac{q^{1-\sigma}}{\sigma}
\ll1,
\tag{4.6}
\]

و

\[
\int_q^\infty
\frac{|S(x)|\log x}{x^{\sigma+1}}\,dx
\le
q^{1-\sigma}
\left(
\frac{\log q}{\sigma}+rac1{\sigma^2}
\right)
\ll
\log(2q).
\tag{4.7}
\]

فتنتج (4.1).

```text
DERIVATIVE-BOUND = PROVED-HERE / EFFECTIVE
POLYA-VINOGRADOV = NOT NEEDED
```

## 5. الانتقال من \(L(1,\chi)\) إلى الصفر \(\beta\)

لنفترض أن \(L(s,\chi)\) تملك الصفر الاستثنائي الحقيقي

\[
\beta>1-\frac{c_0}{\log(2q)}.
\]

بما أن \(L(\beta,\chi)=0\)، فإن

\[
L(1,\chi)
=
\int_\beta^1 L'(u,\chi)\,du.
\]

ومن (4.1):

\[
|L(1,\chi)|
\le
C(1-\beta)\log^2(2q).
\tag{5.1}
\]

نطبق مبرهنة Siegel بالأس \(\varepsilon/2\):

\[
|L(1,\chi)|
\ge
c(\varepsilon/2)q^{-\varepsilon/2}.
\tag{5.2}
\]

إذن

\[
1-\beta
\ge
\frac{c(\varepsilon/2)}{C}
\frac{q^{-\varepsilon/2}}{\log^2(2q)}.
\tag{5.3}
\]

ولأن

\[
\log^2(2q)\ll_\varepsilon q^{\varepsilon/2},
\]

نحصل، بعد امتصاص الموصلات الصغيرة في الثابت، على

\[
1-\beta
\gg_\varepsilon
q^{-\varepsilon}.
\tag{5.4}
\]

الثابت في (5.4) غير فعال لأنه يعتمد على ثابت Siegel.

```text
ANT-COR-11-01 LOGIC = PASS
ZERO-SEPARATION      = INEFFECTIVE
```

## 6. الاتجاه العكسي وحدوده

الصيغة (5.1) تعطي:

\[
L(1,\chi)\ll(1-\beta)\log^2 q
\]

عند وجود صفر استثنائي. لكنها لا تعطي حدًا سفليًا فعالًا لـ\(L(1,\chi)\) من المنطقة القياسية وحدها، لأن المنطقة تسمح بالصفر الحقيقي الاستثنائي.

كما لا يجوز استبدال مبرهنة Siegel بالحد الفعال

\[
L(1,\chi)\gg\frac1{\log q}
\]

في الحالة التربيعية العامة؛ هذا الحد معروف للشخصيات غير التربيعية، أما الحالة التربيعية فهي موضع عقبة Siegel.

## 7. Tatuzawa

تعطي مبرهنة Tatuzawa نسخة فعالة من حد Siegel لجميع الشخصيات التربيعية البدائية باستثناء شخصية واحدة محتملة. هذه النتيجة مهمة تاريخيًا وتطبيقيًا، لكنها لا تزيل الاستثناء غير الفعال تمامًا.

تُسجل في الفصل كملاحظة مقارنة، لا كبديل منطقي عن (1.1)، إلا إذا خصص لها نص مستقل ومصدر دقيق.

```text
TATUZAWA = CONTEXT / DEFERRED-FORMAL-STATEMENT
```

## 8. عدم الدور

إثبات (4.1) واشتقاق (5.4) لا يستخدمان:

- Siegel--Walfisz.
- Bombieri--Vinogradov.
- Linnik.
- Deuring--Heilbronn.
- GRH.

ويستخدمان فقط:

- دورية الشخصية وانعدام مجموع دورة كاملة.
- الجمع الجزئي.
- مبرهنة Siegel المقتبسة في خطوة واحدة محددة.

```text
CIRCULARITY = PASS
```

## 9. الحكم النهائي

```text
ANT-THM-11-03 SOURCE          = CITED / VERIFIED
ANT-THM-11-03 EFFECTIVITY     = INEFFECTIVE
DERIVATIVE-BOUND              = PROVED-HERE / EFFECTIVE
ANT-COR-11-01 LOGIC           = PASS
ANT-COR-11-01 EFFECTIVITY     = INEFFECTIVE
MISUSE-AS-EFFECTIVE-BOUND     = PROHIBITED
RESULT-STATUS                 = DRAFT-UNTIL-AUTHORING
PRE-AUTHORING-GATE            = OPEN
CHAPTER-AUTHORING              = BLOCKED
```

## 10. الإجراء التالي

الانتقال إلى ظاهرة Deuring--Heilbronn وتثبيت صيغة نوعية واحدة قابلة للاقتباس، مع التحقق من:

1. نطاق الموصلات والارتفاعات.
2. اعتماد الحد على \(1-\beta_1\).
3. الفرق بين الصيغة الفعالة والصيغة غير الفعالة.
4. عدم الخلط بين تنافر الأصفار وفرادة Landau--Page.
