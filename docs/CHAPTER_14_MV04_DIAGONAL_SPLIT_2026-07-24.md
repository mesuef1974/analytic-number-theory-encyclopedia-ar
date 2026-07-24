# MV-04 — فصل المساهمة القطرية

التاريخ: 2026-07-24

```text
VERSION                         = 0.18.0-dev
CHAPTER                         = 14
UNIT                            = MV-04
TOPIC                           = STRICT-DIAGONAL / MULTIPLICATIVE-COLLISIONS
STATUS                          = PARTIAL / PROVED-HERE-DRAFT
STRICT-DIAGONAL                 = PROVED-HERE-DRAFT
MULTIPLICATIVE-COLLISION-LAYER  = OPEN
FULL-DIAGONAL                   = OPEN
FORMAL-LOGIC-AUDIT              = PENDING
REFERENCE-AUDIT                 = PENDING
INDEPENDENT-REVIEW              = PENDING
NEXT-UNIT                       = MV-04B / COLLISION-DIAGONAL
PASS-FOR-AUTHORING              = NO
```

## 1. لماذا نحتاج فصلًا أدق

بعد `MV-03` تظهر قطع ثنائية من الشكل

\[
\mathcal B(\chi)
=
\sum_{M<m\le2M}\alpha_m\chi(m)
\sum_{K<k\le K_m}\beta_k\chi(k),
\]

حيث \(K_m\le2K\) و\(mk\le x\)، ومع

\[
\|\alpha\|_2^2\ll M(\log(2x))^2,
\qquad
\|\beta\|_2^2\ll K.
\]

عند توسيع \(|\mathcal B(\chi)|^2\) تظهر أربع متغيرات:

\[
(m_1,k_1,m_2,k_2).
\]

لكن توجد طبقتان مختلفتان يجب عدم خلطهما:

1. **القطر الصارم**:
   \[
   m_1=m_2,
   \qquad
   k_1=k_2.
   \]
2. **تصادمات حاصل الضرب**:
   \[
   m_1k_1=m_2k_2
   \]
   مع احتمال أن تكون الأزواج مختلفة.

الطبقة الثانية ليست خارج القطر بالمعنى العددي النهائي، وليست القطر الصارم أيضًا. لذلك لا يجوز إعلان `MV-04` مغلقة قبل ضبطها.

## 2. المتوسط الموزون على كتلة موصلات

ثبّت كتلة ديادية

\[
R<r\le2R.
\]

ولكل شخصية بدائية \(\chi\bmod r\) ندرس

\[
\mathfrak M_{R}(\mathcal B)
=
\sum_{R<r\le2R}W_Q(r)
\sum_{\chi\bmod r}^{*}
|\mathcal B(\chi)|^2.
\]

بتوسيع المربع:

\[
\begin{aligned}
|\mathcal B(\chi)|^2
&=
\sum_{m_1,k_1}
\sum_{m_2,k_2}
\alpha_{m_1}\overline{\alpha_{m_2}}
\beta_{k_1}\overline{\beta_{k_2}}\\
&\qquad\qquad\times
\chi(m_1k_1)\overline{\chi(m_2k_2)}.
\end{aligned}
\]

نعرّف المساهمة القطرية الصارمة باختيار

\[
(m_1,k_1)=(m_2,k_2).
\]

## 3. المساهمة القطرية الصارمة

لكل \(r\)، عدد الشخصيات البدائية modulo \(r\) هو \(\varphi^*(r)\le\varphi(r)\). وعلى القطر الصارم يكون عامل الشخصية مساويًا لـ1 عندما يكون حاصل الضرب أوليًا مع \(r\)، ومقداره على الأكثر 1 عمومًا. لذا

\[
\begin{aligned}
\mathfrak D_0
&\le
\sum_{R<r\le2R}
W_Q(r)\varphi^*(r)
\sum_{M<m\le2M}|\alpha_m|^2
\sum_{K<k\le2K}|\beta_k|^2.
\end{aligned}
\]

من `MV-01` و`MV-02`:

\[
W_Q(r)
\ll
\frac{\log(2Q/R)}{\varphi(r)}
\qquad(R<r\le2R).
\]

إذن

\[
W_Q(r)\varphi^*(r)
\le
W_Q(r)\varphi(r)
\ll
\log\frac{2Q}{R}.
\]

وبجمع \(r\) في الكتلة:

\[
\sum_{R<r\le2R}W_Q(r)\varphi^*(r)
\ll
R\log\frac{2Q}{R}.
\]

وعليه

\[
\boxed{
\mathfrak D_0
\ll
R\log\frac{2Q}{R}
\,\|\alpha\|_2^2\,\|\beta\|_2^2
}.
\]

هذا حد داخلي كامل للقطر الصارم.

## 4. التطبيق على معاملات Type II من `MV-03`

من حدود المعاملات:

\[
\|\alpha\|_2^2
\ll M(\log(2x))^2,
\qquad
\|\beta\|_2^2\ll K.
\]

فنحصل على

\[
\boxed{
\mathfrak D_0
\ll
RMK
\log\frac{2Q}{R}
(\log(2x))^2
}.
\]

ومع \(MK\ll x\):

\[
\boxed{
\mathfrak D_0
\ll
Rx
\log\frac{2Q}{R}
(\log(2x))^2
}.
\]

هذا يثبت أن القطر الصارم يقع على مقياس \(Rx\) مضروبًا في خسارة لوغاريتمية ناتجة من معاملات Vaughan الحالية.

## 5. لماذا لا يغلق هذا القطر الكامل

إذا كان

\[
m_1k_1=m_2k_2
\]

مع

\[
(m_1,k_1)\ne(m_2,k_2),
\]

فإن معامل الشخصية يساوي أيضًا 1 متى كان حاصل الضرب أوليًا مع \(r\). هذه المساهمة لا تظهر في \(\mathfrak D_0\)، لكنها تنتمي إلى القطر العددي بعد تجميع الالتفاف في معامل واحد

\[
c_n=
\sum_{mk=n}\alpha_m\beta_k.
\]

إذن القطر الكامل هو

\[
\sum_n|c_n|^2,
\]

وليس فقط

\[
\|\alpha\|_2^2\|\beta\|_2^2.
\]

الفرق بينهما هو **طاقة التصادمات الضربية**:

\[
\mathcal E_\times(\alpha,\beta)
=
\sum_n
\left|
\sum_{mk=n}\alpha_m\beta_k
\right|^2
-
\sum_{m,k}|\alpha_m|^2|\beta_k|^2.
\]

هذه الكمية غير سالبة عمومًا، ولا يجوز حذفها أو امتصاصها بلا برهان.

## 6. بوابة التصادمات

لإغلاق `MV-04` كاملًا يجب إثبات أحد المسارين:

1. حد مباشر لطاقة التصادمات الضربية على مستطيلات Vaughan الديادية؛ أو
2. إعادة تنظيم البرهان بحيث تدخل التصادمات مع طبقة خارج القطر في تقدير موحد لا يفقد الرتبة المستهدفة.

لا نعتمد في هذه الوحدة حدًا من نوع

\[
\sum_n|c_n|^2
\ll
(\log x)^A\|\alpha\|_2^2\|\beta\|_2^2
\]

من دون اشتقاق صريح، لأن مثل هذا الحد ليس حقيقة شكلية لكل معاملات عامة.

## 7. التفاعل مع الغربال الكبير

الحد

\[
R\log\frac{2Q}{R}
\|\alpha\|_2^2\|\beta\|_2^2
\]

هو بالضبط الجزء الموافق للحد \(R\) في عامل الغربال الكبير الموزون

\[
\left(\frac NR+R\right)
\log\frac{2Q}{R}.
\]

أما حد \(N/R\) فيمثل التداخل بين القيم المختلفة، ولذلك سيظهر في طبقة خارج القطر أو في التقدير الموحّد اللاحق.

## 8. عدم الدور

هذا البرهان يستعمل فقط:

1. حدود وزن الموصل من `MV-01` و`MV-02`؛
2. العدد التافه \(\varphi^*(r)\le\varphi(r)\)؛
3. توسيع مربع القيمة المطلقة؛
4. حدود معاملات Type II من `MV-03`.

لا يستعمل مبرهنة باربان أو BDH أو نتيجة مكافئة لهما.

## 9. حدود الادعاء

- القطر الصارم فقط مغلق.
- تصادمات حاصل الضرب ما تزال مفتوحة.
- لا يجوز تسجيل `FULL-DIAGONAL = PROVED`.
- لا اختيار نهائيًا لـ\(U,V\) بعد.
- لا إذن بالتأليف.

## 10. الحكم

```text
MV-04 STRICT-DIAGONAL          = PROVED-HERE-DRAFT
MV-04 MULTIPLICATIVE-COLLISION = OPEN
MV-04 FULL-DIAGONAL            = OPEN
MV-04 NON-CIRCULARITY          = PASS-AT-DRAFT-LEVEL
MV-04                          = PARTIAL
NEXT                           = MV-04B / COLLISION-DIAGONAL
PASS-FOR-AUTHORING             = NO
```
