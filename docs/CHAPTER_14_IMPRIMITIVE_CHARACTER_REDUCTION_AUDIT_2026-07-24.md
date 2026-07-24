# تدقيق رد الشخصيات غير البدائية — الفصل الرابع عشر

التاريخ: 2026-07-24

```text
VERSION                 = 0.18.0-dev
CHAPTER                 = 14
OBJECT                  = IMPRIMITIVE CHARACTER REDUCTION
STATUS                  = PROVED-HERE
PRE-AUTHORING-GATE      = OPEN
PASS-FOR-AUTHORING      = NO
```

## 1. الإعداد

لتكن `chi mod q` شخصية ديريشليه موصلها `r | q`، ولتكن `chi* mod r` الشخصية البدائية التي تستحثها. نكتب

\[
\Psi(x,\chi)=\sum_{n\le x}\Lambda(n)\chi(n),
\qquad
\Psi^{\circ}(x,\chi)=\Psi(x,\chi)-\delta_{\chi=\chi_0}x.
\]

## 2. هوية الرد الدقيقة

لأن `chi(n)=chi*(n)` عندما `(n,q)=1`، وتساوي صفرًا عندما يشترك `n` مع `q` بعامل أولي لا يفرضه الموصل، فإن

\[
\Psi(x,\chi)
=
\Psi(x,\chi^*)
-
\sum_{\substack{p^k\le x\\p\mid q,\ p\nmid r}}
\chi^*(p^k)\log p.
\]

وتبقى الهوية صحيحة للنسخة المتمركزة:

\[
\boxed{
\Psi^{\circ}(x,\chi)
=
\Psi^{\circ}(x,\chi^*)-C(x;q,r,\chi^*)
}
\]

حيث

\[
C(x;q,r,\chi^*)
=
\sum_{\substack{p^k\le x\\p\mid q,\ p\nmid r}}
\chi^*(p^k)\log p.
\]

لا يوجد حد `x` إضافي في الحالة الرئيسية، لأن الشخصية الرئيسية modulo `q` والشخصية البدائية الرئيسية ذات الموصل `1` تُركّزان بالطرح نفسه.

## 3. ضبط التصحيح المحلي

لدينا

\[
|C(x;q,r,\chi^*)|
\le
\sum_{\substack{p^k\le x\\p\mid q,\ p\nmid r}}\log p
\le
\omega(q/r)\log x
\le
\frac{\log(q/r)}{\log 2}\log x.
\]

ومن ثم

\[
|\Psi^{\circ}(x,\chi)|^2
\le
2|\Psi^{\circ}(x,\chi^*)|^2
+
\frac{2}{(\log 2)^2}(\log(q/r))^2(\log x)^2.
\]

## 4. تفكيك جميع الشخصيات بحسب الموصل

كل شخصية modulo `q` تُستحث بصورة وحيدة من شخصية بدائية modulo موصل `r | q`. لذلك

\[
\sum_{\chi\bmod q}|\Psi^{\circ}(x,\chi)|^2
\le
2\sum_{r\mid q}\sum_{\chi^*\bmod r}^{*}
|\Psi^{\circ}(x,\chi^*)|^2
+
O\!\left(\varphi(q)(\log q)^2(\log x)^2\right).
\]

بعد الضرب بـ`1/phi(q)` والجمع على `q <= Q` نحصل على

\[
V_\psi(x,Q)
\le
2\sum_{q\le Q}\frac1{\varphi(q)}
\sum_{r\mid q}\sum_{\chi^*\bmod r}^{*}
|\Psi^{\circ}(x,\chi^*)|^2
+
O\!\left(Q(\log Q)^2(\log x)^2\right).
\]

وبكتابة `q=rm` يصبح الجزء التحليلي

\[
2\sum_{r\le Q}
\left(
\sum_{m\le Q/r}\frac1{\varphi(rm)}
\right)
\sum_{\chi^*\bmod r}^{*}
|\Psi^{\circ}(x,\chi^*)|^2.
\]

هذه هي الصيغة التي يجب أن يطبّق عليها مدخل القيمة المتوسطة. وزن المضاعفات

\[
W_Q(r)=\sum_{m\le Q/r}\frac1{\varphi(rm)}
\]

لا يجوز إسقاطه أو استبداله بـ`1/phi(r)` بلا برهان.

## 5. حجم الخطأ المحلي

عندما `Q <= x` فإن

\[
Q(\log Q)^2(\log x)^2
\ll Q(\log x)^4.
\]

وهذا أصغر من المقياس المستهدف `xQ log x` لكل `x` كبير. إذن تصحيحات الاستحثاث ليست العقبة الرئيسية في BDH؛ العقبة هي تقدير المتوسط البدائي الموزون بالكمية `W_Q(r)`.

## 6. حكم البوابة

```text
UNIQUE-CONDUCTOR-DECOMPOSITION = PROVED-HERE
CENTERED-REDUCTION-IDENTITY    = PROVED-HERE
LOCAL-PRIME-CORRECTION         = PROVED-HERE
AGGREGATE-CORRECTION-BOUND     = PROVED-HERE
IMPRIMITIVE-REDUCTION-GATE     = CLOSED / PASS
MEAN-VALUE-INPUT               = OPEN
CLASSICAL-UPPER-BOUND          = OPEN
PASS-FOR-AUTHORING             = NO
```

## 7. القرار بشأن الفصل الثالث عشر

الغربال الكبير المجرد من الفصل الثالث عشر يضبط متوسطات مربعات مجاميع معاملات عامة على الشخصيات البدائية. لكنه لا يعطي وحده حد BDH النهائي مباشرة؛ لا بد من:

1. اختيار تفكيك لمعاملات `Lambda` أو استعمال مبرهنة قيمة متوسطة مخصصة؛
2. التعامل مع الوزن `W_Q(r)`؛
3. فصل الشخصية الرئيسية؛
4. استعادة رتبة `xQ log x` بدل حدود أكثر خشونة.

لذلك يسجل مدخل الفصل الثالث عشر بوصفه `AVAILABLE COMPONENT` لا بوصفه برهانًا كاملًا لـBDH.
