# خريطة برهان الفصل الثاني عشر — مبرهنة Siegel--Walfisz

## الهدف المركزي

لكل \(A>0\)، إثبات وجود ثابت \(c_A>0\) بحيث، بانتظام في

\[
q\le(\log x)^A,
\qquad (a,q)=1,
\]

لدينا

\[
\psi(x;q,a)
=
\frac{x}{\varphi(q)}
+
O_A\!\left(xe^{-c_A\sqrt{\log x}}\right),
\]

مع التصريح بأن الثابت غير فعال في الصيغة غير المشروطة العامة.

## الكائنات

نعرف

\[
\psi(x,\chi)=\sum_{n\le x}\chi(n)\Lambda(n),
\]

و

\[
\psi(x;q,a)
=
\sum_{\substack{n\le x\\n\equiv a\pmod q}}\Lambda(n).
\]

عندما \((a,q)=1\)، يعطي التعامد الهوية الدقيقة

\[
\psi(x;q,a)
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}
\overline{\chi(a)}\,\psi(x,\chi).
\]

## العقد البرهانية

### P12-01 — تثبيت الفصل عن نتيجة الترديد الثابت

`ANT-THM-10-02` يثبت النتيجة النوعية لكل \(q\) ثابت. لا يوجد في الفصل العاشر حد خطأ موحد في \(q\)، ولذلك لا يجوز أخذ \(q=q(x)\) داخل نتيجته.

**الحكم:** الفصل العاشر مصدر للهوية والتحفيز فقط؛ البرهان الكمي يبدأ من جديد عند مستوى الصيغة الصريحة والمنطقة الخالية.

### P12-02 — مرشح الفئة بالشخصيات

نعيد استعمال `ANT-PROP-10-01`:

\[
\psi(x;q,a)
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}
\overline{\chi(a)}\psi(x,\chi).
\]

لا تنشأ خسارة بعامل \(q\) عند تجميع الحدود إذا كان التقدير نفسه موحدًا لكل شخصية، لأن عدد الشخصيات هو \(\varphi(q)\) ويقسم عليه في المرشح.

### P12-03 — الرد إلى الشخصية البدائية

إذا استحثت \(\chi\pmod q\) من \(\chi^*\pmod r\)، فإن الفرق بين \(\psi(x,\chi)\) و\(\psi(x,\chi^*)\) مدعوم على القوى الأولية للأعداد الأولية القاسمة لـ\(q\) التي حذفتها العوامل المحلية. لذلك

\[
\psi(x,\chi)
=
\psi(x,\chi^*)
+
O(\log q\log x).
\]

السبب:

\[
\sum_{\substack{p^k\le x\\p\mid q}}\log p
\le
\omega(q)\log x
\ll
\log q\log x.
\]

في المجال \(q\le(\log x)^A\)، هذا الخطأ أصغر من حد Siegel--Walfisz المستهدف.

**الناتج:** `ANT-LEM-12-01`.

### P12-04 — الصيغة الصريحة المقطوعة بوصفها مدخلًا مقتبسًا

للشخصية البدائية غير الرئيسية ذات الموصل \(r\)، نعتمد صيغة صريحة مقطوعة من مرجع قياسي، في نطاق مناسب من \(x,T\)، على صورة كافية:

\[
\psi(x,\chi)
=
-\sum_{\substack{\rho\\|\Im\rho|\le T}}
\frac{x^\rho}{\rho}
+
E(x,\chi,T),
\]

مع حد موحد من الرتبة التي تسمح باختيار

\[
T=\exp(\bigl(\kappa\sqrt{\log x}\bigr)
\]

والحصول على

\[
E(x,\chi,T)
\ll
xe^{-c\sqrt{\log x}}
\]

بعد خسائر لوغاريتمية قابلة للامتصاص.

الصياغة النهائية داخل المتن يجب أن تثبت بدقة:

- هل تستعمل \(\psi\) أو النسخة المنصفة \(\psi_0\) عند نقاط القفز.
- شروط \(T\) وتجنب وقوعه على ترتيب صفر.
- الاعتماد على الموصل البدائي \(r\)، لا الترديد المستحث \(q\).
- الحدود الإضافية من الأصفار البديهية وعامل غاما.

**الحالة:** `ANT-THM-12-02 = CITED`.

### P12-05 — مساهمة الشخصية الرئيسية

الشخصية الرئيسية تستحث من الشخصية التافهة. بعد حذف القوى الأولية القاسمة لـ\(q\):

\[
\psi(x,\chi_0)
=
\psi(x)+O(\log q\log x).
\]

نعتمد حد de la Vallée Poussin الفعال

\[
\psi(x)
=
x+O\!\left(xe^{-c\sqrt{\log x}}\right)
\]

بوصفه نتيجة مقتبسة؛ لا يشتق من `ANT-THM-09-03` النوعية وحدها.

**الحالة:** `ANT-THM-12-01 = CITED`.

### P12-06 — فصل الصفر الاستثنائي قبل التقدير

إذا وجدت شخصية حقيقية بدائية \(\chi_1\) ذات صفر استثنائي \(\beta_1\)، نفصل حدها من مجموع الأصفار:

\[
\psi(x,\chi_1)
=
-\frac{x^{\beta_1}}{\beta_1}
-
\sum_{\rho\ne\beta_1}
\frac{x^\rho}{\rho}
+
E(x,\chi_1,T).
\]

بعد مرشح الفئة يصبح حد الاستثناء

\[
-\frac{\overline{\chi_1(a)}}{\varphi(q)}
\frac{x^{\beta_1}}{\beta_1}.
\]

لا يحذف هذا الحد، ولا يدمج في \(O\)-term، قبل تطبيق مبرهنة Siegel.

### P12-07 — ضبط الأصفار غير الاستثنائية

من `ANT-THM-11-01`، لكل صفر غير استثنائي في النطاق المقطوع:

\[
\beta
\le
1-
\frac{c_0}{\log(r(|\gamma|+2))}.
\]

نختار

\[
T=e^{\kappa\sqrt{L}},
\qquad L=\log x.
\]

ولأن \(r\le q\le L^A\)، فإن

\[
\log(r(T+2))
\le
A\log L+\kappa\sqrt L+O(1)
\ll_{A,\kappa}\sqrt L.
\]

إذن

\[
x^\beta
\le
x\exp\!\left(
-\frac{c_0L}{A\log L+\kappa\sqrt L+O(1)}
\right)
\le
xe^{-c_{A,\kappa}\sqrt L}.
\]

باستعمال تقدير عد الأصفار أو مجموع \(1/|\rho|\) في الارتفاع \(T\)، تكون الخسارة متعددة الحدود في \(\log(rT)\)، وتمتص في الأس الأسي بعد تصغير الثابت.

**الناتج:** `ANT-LEM-12-02`.

### P12-08 — امتصاص الصفر الاستثنائي ومصدر عدم الفعالية

من `ANT-COR-11-01`، لكل \(\varepsilon>0\):

\[
1-\beta_1
\gg_\varepsilon
r^{-\varepsilon},
\]

والثابت غير فعال. نأخذ، عند \(A>0\)، قيمة مثل

\[
\varepsilon=\frac1{2A}
\]

مع معالجة \(A\) الصغير بالطريقة نفسها بعد اختيار أي \(\varepsilon\) يحقق \(A\varepsilon<1\). عندئذ

\[
r^{-\varepsilon}
\ge
q^{-\varepsilon}
\ge
(\log x)^{-A\varepsilon}
=(\log x)^{-1/2}.
\]

ومن ثم

\[
x^{\beta_1}
=x\exp(-(1-\beta_1)L)
\le
xe^{-c_A\sqrt L}.
\]

الثابت \(c_A\) غير فعال، وهذا هو الموضع الوحيد الذي تدخل فيه عدم فعالية Siegel في المسار الأدنى.

**الناتج:** `ANT-LEM-12-03`.

### P12-09 — تجميع حدود الشخصيات

لكل شخصية غير رئيسية، بعد الرد إلى الجد البدائي:

\[
\psi(x,\chi)
\ll_A
xe^{-c_A\sqrt L}
+
O(\log q\log x).
\]

وللشخصية الرئيسية:

\[
\psi(x,\chi_0)
=
x+O_A(xe^{-c_A\sqrt L}).
\]

ندخل هذه التقديرات في مرشح الفئة. الخطأ المحلي \(\log q\log x\) يمتص لأن

\[
\log q\log x
\ll_A
(\log x)(\log\log x)
=o\!\left(xe^{-c_A\sqrt{\log x}}\right).
\]

فنحصل على `ANT-THM-12-03`.

### P12-10 — الصيغة اللوغاريتمية

لكل \(B>0\):

\[
e^{-c_A\sqrt{\log x}}
\ll_{A,B}
(\log x)^{-B}.
\]

إذن تنتج `ANT-COR-12-01` مباشرة. الثابت يبقى غير فعال لأنه يعتمد على \(c_A\).

### P12-11 — الانتقال إلى \(\vartheta\)

نستعمل

\[
\psi(x;q,a)-\vartheta(x;q,a)
\le
\sum_{k\ge2}\vartheta(x^{1/k})
\ll
\sqrt x\log^2 x.
\]

هذا أصغر من \(x(\log x)^{-B}\) لأي \(B\) ثابت عند كبر \(x\). تنتج الصيغة الموحدة لـ\(\vartheta\).

**الناتج:** `ANT-COR-12-02`.

### P12-12 — الانتقال إلى \(\pi\)

من الجمع الجزئي:

\[
\pi(x;q,a)
=
\frac{\vartheta(x;q,a)}{\log x}
+
\int_2^x
\frac{\vartheta(t;q,a)}{t\log^2t}\,dt.
\]

يجب تدقيق المجال عند تغير القيد \(q\le(\log x)^A\) داخل التكامل. المسار الآمن:

- إما تطبيق الصيغة اللوغاريتمية بقوة أكبر \(B'\) وتقسيم التكامل عند حد يعتمد على \(q\).
- أو صياغة النتيجة مباشرة بانتظام للـ\(q\) الحالي مع معالجة الجزء الصغير معالجة تافهة.

الناتج المتوقع:

\[
\pi(x;q,a)
=
\frac{\operatorname{Li}(x)}{\varphi(q)}
+
O_{A,B}\!\left(\frac{x}{(\log x)^B}\right)
\]

بعد إعادة تسمية قوة اللوغاريتم.

**الناتج:** `ANT-COR-12-03`.

## خريطة الاعتماد

```text
ANT-COR-07-01 + ANT-PROP-10-01
                  |
                  v
          character decomposition
                  |
                  v
ANT-THM-07-04 + ANT-PROP-07-03 ---> ANT-LEM-12-01
                  |
                  v
       ANT-THM-12-02 [CITED explicit formula]
                  |
          +-------+--------+
          |                |
          v                v
 ANT-THM-11-01      exceptional beta_1 isolated
          |                |
          v                v
 ANT-LEM-12-02      ANT-COR-11-01 + Siegel
                           |
                           v
                    ANT-LEM-12-03
          +----------------+
          |
          v
 ANT-THM-12-01 [CITED principal PNT error]
          |
          v
     ANT-THM-12-03
          |
          +--> ANT-COR-12-01
          +--> ANT-COR-12-02
          +--> ANT-COR-12-03
```

## حظر الدور

يحظر داخل البرهان:

- استعمال `ANT-THM-10-02` مع \(q=q(x)\).
- استعمال Siegel--Walfisz لإثبات الصيغة الصريحة أو المنطقة الخالية.
- استعمال Bombieri--Vinogradov.
- استعمال Linnik.
- استعمال GRH.
- إخفاء حد \(x^{\beta_1}/\beta_1\) قبل Siegel.
- وصف الثابت النهائي بأنه فعال.
- ادعاء إثبات بيرون وتحويل المسار كاملين داخل الموسوعة من دون نص مستقل.

## قرار المسار

```text
CORE-ROUTE             = CHARACTER FILTER + CITED EXPLICIT FORMULA + ZERO-FREE REGION + SIEGEL
FIXED-Q-RESULT         = SEPARATED
BOMBIERI-VINOGRADOV    = DEFERRED
EXCEPTIONAL-ZERO       = EXPLICITLY ISOLATED
SIEGEL-USE             = P12-08 ONLY
FINAL-CONSTANT         = INEFFECTIVE
AUTHORING              = BLOCKED-PENDING-AUDITS
```