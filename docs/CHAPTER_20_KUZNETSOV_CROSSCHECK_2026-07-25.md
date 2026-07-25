# مطابقة Kuznetsov للفصل العشرين — 2026-07-25

## الحكم

```text
CHAPTER                         = 20
SCOPE                           = SL2(Z) / WEIGHT 0 / TRIVIAL CHARACTER
SAME-SIGN-CORE                  = CROSS-CHECK PASS
CONTINUOUS-SPECTRUM             = INCLUDED / CROSS-CHECK PASS
J-BESSEL-TRANSFORM              = FROZEN FOR SAME-SIGN CORE
K-BESSEL-TRANSFORM              = SOURCE-MATCHED / OPPOSITE-SIGN CONTEXT ONLY
GENERAL LEVEL AND CHARACTERS    = DEFERRED
AUTHORING                       = BLOCKED
```

هذه المطابقة تجمد الصيغة الأساسية ذات الإشارة المتساوية عند المستوى 1 فقط. ولا تزعم صيغة موحدة للمستوى العام، ولا تجعل صيغة الإشارة المتعاكسة نتيجة مركزية في الفصل.

## 1. التطبيع المختار

نأخذ أساسًا متعامدًا معياريًا \(\{u_j\}\) من أشكال Hecke--Maass الحدبية للزمرة \(SL_2(\mathbb Z)\)، مع

\[
\Delta u_j=\left(\frac14+t_j^2\right)u_j,
\qquad
u_j(z)=\sqrt y\sum_{n\ne0}\rho_j(n)K_{it_j}(2\pi |n|y)e(nx),
\]

حيث \(e(x)=e^{2\pi i x}\)، و

\[
\rho_j(n)=\rho_j(1)\lambda_j(n),
\qquad
\rho_j(-n)=\varepsilon_j\rho_j(n),
\quad n>0.
\]

لا يجوز الجمع بين التطبيع \(\|u_j\|_2=1\) وفرض \(\rho_j(1)=1\) من دون إدخال الوزن الناتج.

نكتب توسع Eisenstein بالشكل

\[
E\!\left(z,\frac12+it\right)
 = \text{constant term}
 +\sqrt y\sum_{n\ne0}\tau(n,t)K_{it}(2\pi |n|y)e(nx).
\]

هذه الصياغة بمعامل \(\tau(n,t)\) هي الصيغة الحاكمة داخل الفصل؛ والاختزال إلى دوال القواسم وزيتا يذكر بعد تعريف تطبيع \(E(z,s)\) صراحة.

## 2. الصيغة الأساسية ذات الإشارة المتساوية

إذا كانت \(h\) زوجية، هولومورفية في شريط أعرض من \(|\Im t|\le 1/2\)، وذات اضمحلال كاف، فإن \(m,n>0\) يحققان

\[
\begin{aligned}
&\sum_j
 \frac{\rho_j(n)\overline{\rho_j(m)}}{\cosh(\pi t_j)}h(t_j)
 +\frac1{4\pi}\int_{-\infty}^{\infty}
 \frac{\tau(n,t)\overline{\tau(m,t)}}{\cosh(\pi t)}h(t)\,dt \\
&\qquad=
 \frac{\delta_{m,n}}{\pi^2}
 \int_{-\infty}^{\infty}t h(t)\tanh(\pi t)\,dt
 +\sum_{c\ge1}\frac{S(n,m;c)}{c}
 H^+\!\left(\frac{4\pi\sqrt{mn}}{c}\right),
\end{aligned}
\]

حيث

\[
\mathcal J(x,t)=\frac{J_{2it}(x)-J_{-2it}(x)}{\sinh(\pi t)},
\qquad
H^+(x)=\frac{i}{\pi}\int_{-\infty}^{\infty}
 \mathcal J(x,t)h(t)t\tanh(\pi t)\,dt.
\]

وبزوجية \(h\) وهوية تغيير \(t\mapsto -t\)، تكافئ هذه الصيغة التعريف الشائع

\[
H^+(x)=\frac{2i}{\pi}\int_{-\infty}^{\infty}
 J_{2it}(x)\frac{t h(t)}{\cosh(\pi t)}\,dt.
\]

## 3. الطيف المستمر عند المستوى 1

إذا عرّفنا

\[
E(z,s)=\frac12\sum_{\Gamma_\infty\backslash\Gamma}\Im(\gamma z)^s,
\]

فإن معامل فورييه غير الصفري يساوي، وفق هذا التطبيع،

\[
\tau(n,t)=
 \frac{2\pi^{1/2+it}}{\Gamma(1/2+it)\zeta(1+2it)}
 |n|^{it}\sigma_{-2it}(|n|).
\]

ومن

\[
|\Gamma(1/2+it)|^2=\frac{\pi}{\cosh(\pi t)}
\]

ينتقل الحد المستمر السابق إلى صيغة Kuznetsov الأصلية بدوال القواسم وعامل \(|\zeta(1+2it)|^{-2}\). هذه الخطوة هي موضع عامل \(1/\pi\)؛ لذلك لا يجوز نسخه من مرجع يستعمل Eisenstein مطبعًا بطريقة مختلفة.

## 4. قاموس المطابقة

| المكوّن | Kuznetsov 1981 | الصيغة الحديثة المختارة | الحكم |
|---|---|---|---|
| القياس | \(dx\,dy/y^2\)، قبل (2.6) | القياس نفسه | `PASS` |
| لابلاس | اصطلاح المصدر يترجم إلى \(1/4+t^2\) | \(-y^2(\partial_x^2+\partial_y^2)\) | `PASS WITH SIGN TRANSLATION` |
| توسع مااس | (2.10)، معاملات \(p_j(n)\) | معاملات \(\rho_j(n)\) في أساس \(L^2\) | `PASS WITH NOTATION MAP` |
| Hecke | (2.11)--(2.12) | \(\rho_j(n)=\rho_j(1)\lambda_j(n)\) | `PASS` |
| Kloosterman | (2.13) | \(S(n,m;c)=\sum_d^*e((nd+m\bar d)/c)\) | `PASS` |
| الطيف المستمر | ظاهر في (2.14) بدوال القواسم وزيتا | ظاهر بمعاملات \(\tau(n,t)\) | `PASS` |
| الحد القطري | حد \(\delta_{m,n}\) في (2.14) | كثافة \(t\tanh(\pi t)/\pi^2\) | `PASS` |
| تحول \(J\) | (2.14)--(2.15) | \(H^+\) أعلاه | `PASS` |
| الاتجاه العكسي | Theorem 2، (2.22)--(2.23) | لا يستعمل نتيجة مركزية | `SOURCE-LOCATED` |
| تحول \(K\) | ينشأ في فرع الإشارة المتعاكسة في الصيغ الحديثة | \(K_{2it}\) مع وزن \(\sinh(\pi t)t\) | `CONTEXT ONLY / NOT CORE` |

## 5. فحوص الثوابت

- حجة Bessel الحسابية هي دائمًا \(4\pi\sqrt{mn}/c\).
- عامل \(1/c\) يبقى خارج مجموع Kloosterman.
- الحد القطري لا يظهر في حالة الإشارة المتعاكسة.
- الطيف المستمر لا يحذف للزمرة المعيارية غير المدمجة.
- تحويل \(J\) يخص النواة الأساسية ذات \(mn>0\).
- تحويل \(K\) لا يدمج في الرمز \(H^+\)؛ يذكر منفصلًا عند \(mn<0\).
- إدخال معاملات Hecke يستلزم إبقاء \(|\rho_j(1)|^2\) أو وزن مكافئ.

## 6. المصادر التي تمت المطابقة عليها

1. N. V. Kuznetsov، النص الإنجليزي الأصلي، §2: (2.10)، (2.13)، Theorems 1--2، (2.14)، (2.22)--(2.23).
2. Iwaniec--Kowalski، §16.4، وبخاصة الصيغة الحديثة المشار إليها في المراجع اللاحقة بوصفها Theorem 16.3.
3. Khan--Young، Lemma 2.1: صيغة حديثة صريحة تجمع الطيف المنفصل والمستمر والقطري وتحول \(J\).
4. Blomer--Assing، *Relative Trace Formulae in Analytic Number Theory*, Set 2، ص 1--3: تطبيع \(L^2\)، علاقة Hecke، Eisenstein، والاتجاهان الأمامي والخلفي.
5. Li--Knightly، *Kuznetsov's Trace Formula and the Hecke Eigenvalues of Maass Forms*، مرجع حديث بنيوي اكتشف عبر Consensus ثم استرجع سجله الكامل.

## 7. القرار

```text
KUZNETSOV-LEVEL-1 = CROSS-CHECK PASS
CORE-FORMULA       = SAME-SIGN / CONTINUOUS SPECTRUM INCLUDED
OPTIONAL-BRANCH    = OPPOSITE-SIGN / K-TRANSFORM CONTEXT ONLY
NORMALIZATION-TABLE = NOT YET FROZEN
```

لا يجمد هذا التقرير جدول الفصل كله؛ يبقى زوج تحويل Selberg والمراجعة المستقلة عائقين مانعين.
