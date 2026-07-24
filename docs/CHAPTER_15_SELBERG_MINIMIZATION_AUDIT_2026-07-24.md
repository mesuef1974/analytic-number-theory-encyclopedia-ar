# الفصل الخامس عشر — تدقيق حل مسألة التصغير في غربال سيلبرغ

التاريخ: 2026-07-24

```text
CHAPTER                = 15
VERSION                = 0.19.0-dev
AUDIT                   = SELBERG-QUADRATIC-MINIMIZATION
STATUS                  = PASS-WITH-STATED-NORMALIZATION
AUTHORING               = BLOCKED
PASS-FOR-AUTHORING      = NO
```

## 1. بيانات الغربال

لتكن \(\mathcal A\) متتالية منتهية من أوزان غير سالبة، ولتكن \(\mathcal P\) مجموعة أوليات. نضع

\[
P(z)=\prod_{\substack{p<z\\p\in\mathcal P}}p,
\qquad
S(\mathcal A,\mathcal P,z)
=\sum_{\substack{n\in\mathcal A\\(n,P(z))=1}}a_n.
\]

ولكل عدد مربع حر \(d\mid P(z)\) نفترض

\[
|\mathcal A_d|=Xg(d)+r_d,
\qquad
0\le g(p)<1,
\]

حيث \(g\) ضربية على الأعداد المربعة الحرة.

## 2. الوزن التربيعي

نختار معاملات حقيقية \(\lambda_d\) مدعومة على

\[
d<R,
\qquad d\mid P(z),
\qquad \lambda_1=1.
\]

إذا كان \((n,P(z))=1\) فإن مجموع القواسم يساوي \(\lambda_1=1\)، ولذلك

\[
S(\mathcal A,\mathcal P,z)
\le
\sum_{n\in\mathcal A}
\left(\sum_{\substack{d\mid n\\d\mid P(z)}}\lambda_d\right)^2.
\]

بعد التوسيع نحصل على

\[
S(\mathcal A,\mathcal P,z)
\le
XQ(\lambda)+E(\lambda),
\]

حيث

\[
Q(\lambda)
=
\sum_{d_1,d_2<R}
\lambda_{d_1}\lambda_{d_2}g([d_1,d_2])
\]

و

\[
E(\lambda)
=
\sum_{d_1,d_2<R}
\lambda_{d_1}\lambda_{d_2}r_{[d_1,d_2]}.
\]

## 3. تحويل الصورة التربيعية

نعرف الدالة الضربية الموجبة

\[
h(p)=\frac{g(p)}{1-g(p)}
\]

على الأعداد المربعة الحرة. نضع

\[
G(R,z)
=
\sum_{\substack{d<R\\d\mid P(z)}}\mu^2(d)h(d).
\]

التحويل الخطي القياسي لصورة سيلبرغ يقطّر \(Q(\lambda)\) إلى مجموع مربعات موزون بـ\(h(d)\). تحت القيد \(\lambda_1=1\)، تعطي متراجحة كوشي--شفارتس

\[
Q(\lambda)\ge \frac{1}{G(R,z)}.
\]

وتتحقق المساواة لاختيار سيلبرغ الأمثل، الذي يمكن كتابته بصيغة مكافئة تعتمد على المجاميع

\[
G_d(y,z)
=
\sum_{\substack{m<y\\m\mid P(z)\\(m,d)=1}}
\mu^2(m)h(m).
\]

لا يحتاج متن الفصل إلى تثبيت صيغة \(\lambda_d\) المغلقة قبل إثبات التحويل الخطي، لكن يجب تسجيلها في البرهان التفصيلي عند التأليف.

## 4. الحد العلوي المنتهي

ينتج الحد

\[
S(\mathcal A,\mathcal P,z)
\le
\frac{X}{G(R,z)}
+
\sum_{\substack{m<R^2\\m\mid P(z)}}
3^{\omega(m)}|r_m|.
\]

سبب ظهور \(R^2\) هو أن \([d_1,d_2]<R^2\). أما العامل \(3^{\omega(m)}\) فيحد عدد الأزواج \((d_1,d_2)\) ذات المضاعف المشترك الأصغر \(m\): لكل أولي يقسم \(m\) ثلاثة اختيارات غير فارغة لموضع ظهوره في \(d_1,d_2\).

الحالة المنشئية المقترحة:

- المتراجحة التربيعية: `PROVED-HERE`.
- التحويل الخطي والتصغير: `PROVED-HERE` بعد كتابة الحساب كاملًا.
- صيغة الحد العلوي المنتهي: `PROVED-HERE`.
- التقدير التقاربي لـ\(G(R,z)\): `CITED` أو `PROVED-HERE` بحسب فرض البعد المختار.

## 5. العلاقة مع حاصل الضرب المحلي

يبقى

\[
V(z)=\prod_{p<z}(1-g(p))
\]

هو الكثافة المحلية المتوقعة. لا يساوي \(G(R,z)\)، لكن تحت فرض بعد غربالي مناسب يكون

\[
G(R,z)\asymp \frac{1}{V(z)}
\]

في المجال الملائم للعلاقة بين \(R\) و\(z\). لذا يعطي الحد المنتهي رتبة من الشكل

\[
S(\mathcal A,\mathcal P,z)
\ll X V(z)+\text{remainder}.
\]

## 6. حدود التدقيق

- لم تُعتمد بعد صيغة تقاربية بثابت رئيسي صريح لـ\(G(R,z)\).
- لم تُعتمد بعد دوال الغربال العامة \(F_\kappa(s),f_\kappa(s)\).
- اللمّة الأساسية تبقى `CITED / COMPOSITE-INPUT`.
- لا يستخدم هذا التدقيق Bombieri--Vinogradov أو Barban--Davenport--Halberstam.

```text
MINIMIZATION-IDENTITY    = PASS
FINITE-UPPER-BOUND       = PASS
ASYMPTOTIC-G-ESTIMATE    = OPEN
RESULT-RESERVATION       = PENDING
PASS-FOR-AUTHORING       = NO
```
