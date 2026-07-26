# جدول تطبيعات الفصل الثالث والعشرين

## عد الأصفار

نكتب
\[
N(T)=\#\{\rho=\beta+i\gamma:0<\gamma\le T\},
\]
مع العد بالتعدد. الصيغة المعتمدة:
\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T).
\]
ومنها تكون الكثافة المتوسطة قرب الارتفاع \(T\):
\[
\frac{1}{2\pi}\log\frac{T}{2\pi}+O(T^{-1}),
\]
ومتوسط التباعد:
\[
\frac{2\pi}{\log(T/2\pi)}.
\]

## التطبيع المحلي

للفروق حول الارتفاع \(T\) نستخدم
\[
u=(\gamma-\gamma')\frac{\log T}{2\pi}.
\]
استبدال \(\log T\) بـ\(\log(T/2\pi)\) لا يغير الحد النهائي، لكن يجب عدم الخلط بينهما داخل حساب ثابت دقيق. سيستعمل الفصل \(\log T\) في صيغة Montgomery التاريخية، و\(\log(T/2\pi)\) عند شرح الكثافة المحلية.

## اتفاقية التحويل الفوري الوحيدة

\[
\widehat f(\alpha)=\int_{\mathbb R}f(u)e^{-2\pi i\alpha u}\,du,
\qquad
f(u)=\int_{\mathbb R}\widehat f(\alpha)e^{2\pi i\alpha u}\,d\alpha.
\]
بموجب هذه الاتفاقية:
\[
\widehat{\left(\frac{\sin\pi u}{\pi u}\right)^2}(\alpha)
=(1-|\alpha|)_+.
\]

## نواة الجيب وحد GUE

\[
K(u)=\frac{\sin\pi u}{\pi u},
\qquad K(0)=1,
\]
والكثافة الثنائية غير القطرية في حد GUE هي
\[
R_2(u)=1-K(u)^2
=1-\left(\frac{\sin\pi u}{\pi u}\right)^2.
\]
هذه مبرهنة في نموذج المصفوفات العشوائية، وحدسية لأصفار زيتا بعد التطبيع.

## دالة Montgomery الموزونة

نفترض RH، ونضع
\[
w(u)=\frac{4}{4+u^2},
\]
و
\[
F(\alpha,T)=
\left(\frac{T}{2\pi}\log T\right)^{-1}
\sum_{0<\gamma,\gamma'\le T}
T^{i\alpha(\gamma-\gamma')}w(\gamma-\gamma').
\]

خصائص التعداد:

- الأزواج مرتبة.
- القطر \(\gamma=\gamma'\) داخل المجموع.
- الأصفار تعد بالتعدد.
- \(F\) حقيقية وزوجية وغير سالبة.

الصيغة المجمدة للجزء المثبت:
\[
F(\alpha,T)=T^{-2\alpha}(\log T+O(1))+\alpha+o(1)
\]
على المجالات المغلقة داخل \(0\le\alpha<1\)، تحت RH. لا يكتب هذا بوصفه إثباتًا للحدسية عند \(\alpha\ge1\).

## صيغة دوال الاختبار

للأزواج غير القطرية:
\[
\frac{1}{N(T)}
\sum_{\substack{0<\gamma,\gamma'\le T\\ \gamma\ne\gamma'}}
f\!\left((\gamma-\gamma')\frac{\log T}{2\pi}\right)
\to
\int_{\mathbb R}f(u)R_2(u)\,du.
\]
يقدم الجزء المثبت فقط عندما
\[
\operatorname{supp}\widehat f\subset(-1,1),
\]
أما الصيغة لكل دعم مناسب فهي `CONJECTURAL-GUE`.

## الفصل بين الإحصاءات

| الإحصاء | موضوعه | هل يستنتج من pair correlation وحده؟ |
|---|---|---|
| Pair correlation | جميع الأزواج بعد التطبيع | هو المدخل الأساسي |
| Nearest-neighbor spacing | الفواصل المتتالية | لا |
| Number variance | عدد النقاط في نافذة | يحتاج معلومات ارتباط متكاملة وشروطًا إضافية |
| n-level correlation | مجموعات من \(n\) نقاط | لا، عندما \(n>2\) |

## تصنيفات الحالة

```text
PROVED-UNCONDITIONALLY
CONDITIONAL-ON-RH
CONJECTURAL-GUE
RANDOM-MATRIX-THEOREM
NUMERICAL-EVIDENCE
FINITE-VERIFIED
DEFERRED
```

## حارس أساسي

كل صيغة إحصائية يجب أن تحدد: نافذة الارتفاع، التطبيع، هل الأزواج مرتبة، هل القطر مستبعد، فئة دوال الاختبار، اتفاقية التحويل الفوري، وموضع RH إن وجد.
