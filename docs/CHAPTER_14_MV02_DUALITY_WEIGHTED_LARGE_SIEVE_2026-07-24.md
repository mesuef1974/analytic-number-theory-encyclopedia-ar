# MV-02 — الازدواجية والغربال الكبير الموزون

التاريخ: 2026-07-24

```text
VERSION                    = 0.18.0-dev
CHAPTER                    = 14
UNIT                       = MV-02
TOPIC                      = DUALITY / WEIGHTED-LARGE-SIEVE
STATUS                     = PROVED-HERE-DRAFT
DYADIC-WEIGHT-COMPARISON   = PROVED-HERE-DRAFT
WEIGHTED-PRIMAL-INEQUALITY = PROVED-HERE-DRAFT
WEIGHTED-DUAL-INEQUALITY   = PROVED-HERE-DRAFT
FORMAL-LOGIC-AUDIT         = PENDING
REFERENCE-AUDIT            = PENDING
INDEPENDENT-REVIEW         = PENDING
NEXT-UNIT                  = MV-03
PASS-FOR-AUTHORING         = NO
```

## 1. نقطة الانطلاق

من `MV-01` لدينا

\[
W_Q(r)=\sum_{m\le Q/r}\frac1{\varphi(rm)}
\ll \frac{\log(2Q/r)}{\varphi(r)}.
\]

والغربال الكبير للشخصيات البدائية، بوصفه أداة مثبتة في الفصل الثالث عشر، يعطي لكل متتالية مركبة \((c_n)\) مدعومة على فترة طولها \(N\):

\[
\sum_{r\le R}\frac r{\varphi(r)}
\sum_{\chi\bmod r}^{*}
\left|\sum_n c_n\chi(n)\right|^2
\le (N+R^2)\sum_n|c_n|^2.
\]

هدف هذه الوحدة هو تحويل وزن `MV-01` إلى وزن ينسجم مع الغربال الكبير على كتل ديادية، ثم استخراج الصيغة المزدوجة اللازمة للحدود الثنائية في `MV-03` وما بعدها.

## 2. المقارنة الديادية للأوزان

ثبّت \(R\ge1\)، وافترض

\[
R<r\le 2R,
\qquad r\le Q.
\]

عندئذ

\[
W_Q(r)
\ll \frac{\log(2Q/r)}{\varphi(r)}
\le \frac{\log(2Q/R)}{\varphi(r)}.
\]

وبما أن \(r>R\)، فإن

\[
\frac1{\varphi(r)}
=\frac1r\frac r{\varphi(r)}
\le \frac1R\frac r{\varphi(r)}.
\]

إذن

\[
\boxed{
W_Q(r)
\ll
\frac{\log(2Q/R)}{R}
\frac r{\varphi(r)}
}
\qquad (R<r\le2R).
\]

هذه هي المقارنة الحاكمة في هذه الوحدة.

## 3. المتراجحة الموزونة المباشرة

لتكن

\[
S(\chi)=\sum_{M<n\le M+N}c_n\chi(n).
\]

باستعمال المقارنة السابقة ثم الغربال الكبير حتى \(2R\):

\[
\begin{aligned}
&\sum_{R<r\le2R}W_Q(r)
\sum_{\chi\bmod r}^{*}|S(\chi)|^2\\
&\qquad\ll
\frac{\log(2Q/R)}{R}
\sum_{R<r\le2R}\frac r{\varphi(r)}
\sum_{\chi\bmod r}^{*}|S(\chi)|^2\\
&\qquad\le
\frac{\log(2Q/R)}{R}
(N+4R^2)
\sum_{M<n\le M+N}|c_n|^2.
\end{aligned}
\]

ومن ثم

\[
\boxed{
\sum_{R<r\le2R}W_Q(r)
\sum_{\chi\bmod r}^{*}
\left|\sum_{M<n\le M+N}c_n\chi(n)\right|^2
\ll
\left(\frac NR+R\right)
\log\frac{2Q}{R}
\sum_{M<n\le M+N}|c_n|^2
}.
\]

نسمي هذا **الغربال الكبير الموزون على كتلة موصلات ديادية**.

## 4. صياغة مؤثرية

عرّف المؤثر

\[
(Tc)_{r,\chi}
=
\sqrt{W_Q(r)}
\sum_{M<n\le M+N}c_n\chi(n),
\]

حيث \(R<r\le2R\) و\(\chi\) بدائية modulo \(r\).

المتراجحة السابقة تقول إن

\[
\|Tc\|_2^2
\ll B(R,N,Q)\,\|c\|_2^2,
\]

حيث

\[
B(R,N,Q)
=
\left(\frac NR+R\right)
\log\frac{2Q}{R}.
\]

إذن

\[
\|T\|^2\ll B(R,N,Q).
\]

## 5. صيغة الازدواجية

المؤثر المرافق هو

\[
(T^*b)_n
=
\sum_{R<r\le2R}
\sqrt{W_Q(r)}
\sum_{\chi\bmod r}^{*}
b_{r,\chi}\,\overline{\chi(n)}.
\]

وبما أن \(\|T^*\|=\|T\|\)، نحصل على

\[
\boxed{
\sum_{M<n\le M+N}
\left|
\sum_{R<r\le2R}
\sqrt{W_Q(r)}
\sum_{\chi\bmod r}^{*}
 b_{r,\chi}\,\overline{\chi(n)}
\right|^2
\ll
B(R,N,Q)
\sum_{R<r\le2R}
\sum_{\chi\bmod r}^{*}|b_{r,\chi}|^2
}.
\]

وهذه الصيغة ليست نتيجة جديدة مستقلة عن الغربال الكبير، بل هي صورته الموزونة المزدوجة بعد إدخال وزن الموصل الدقيق من `MV-01`.

## 6. نسخة ثنائية الفترات

إذا كان \(c_n\) مدعومًا على فترة منقولة عامة \(M<n\le M+N\)، فلا يتغير شيء في البرهان؛ لأن مدخل الغربال الكبير في الفصل الثالث عشر صالح للفترات المنقولة. لذلك النسخة الموزونة والنسخة المزدوجة صالحتان على كل كتلة عددية منقولة، وهو ما يلزم عند تقسيم معاملات الالتفاف في `MV-03` إلى مستطيلات ديادية.

## 7. جمع كتل الموصلات

تقسيم \(1\le r\le Q\) إلى كتل

\[
R<r\le2R
\]

يعطي عددًا من الكتل من رتبة \(O(\log(2Q))\). لكن لا يجوز في الوحدات اللاحقة جمع الحدود الديادية آليًا باستعمال أكبر حد فقط؛ يجب الاحتفاظ بالعامل

\[
\left(\frac NR+R\right)\log\frac{2Q}{R}
\]

لأن التوازن بين \(N/R\) و\(R\) هو الذي سيحدد اختيار المقاييس في الحدود الثنائية.

## 8. ما تثبته الوحدة وما لا تثبته

تثبت الوحدة:

1. المقارنة الدقيقة بين \(W_Q(r)\) ووزن الغربال الكبير على كتلة ديادية.
2. متراجحة غربال كبير موزونة مناسبة لمتوسط `MV-01`.
3. الصيغة المزدوجة المناظرة بالازدواجية الهيلبرتية.
4. صلاحية الصيغ للفترات المنقولة والكتل الديادية.

ولا تثبت بعد:

1. تفكيك معاملات فون مانغولت أو المعاملات العامة إلى حدود خطية وثنائية.
2. تقدير الحد القطري أو خارج القطري.
3. مبرهنة باربان العامة.
4. حد BDH النهائي.

## 9. الحكم

```text
MV-02 DYADIC-WEIGHT-COMPARISON = PROVED-HERE-DRAFT
MV-02 WEIGHTED-PRIMAL           = PROVED-HERE-DRAFT
MV-02 WEIGHTED-DUAL             = PROVED-HERE-DRAFT
MV-02 TRANSLATED-INTERVALS      = PROVED-HERE-DRAFT
MV-02 LOGIC-AUDIT               = PENDING
MV-02 REFERENCE-AUDIT           = PENDING
MV-02 INDEPENDENT-REVIEW        = PENDING
MV-02                           = COMPLETE-AS-DRAFT
NEXT                            = MV-03
PASS-FOR-AUTHORING              = NO
```
