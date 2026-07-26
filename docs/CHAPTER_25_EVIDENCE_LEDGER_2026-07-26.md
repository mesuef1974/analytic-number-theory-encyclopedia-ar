# سجل أدلة الفصل الخامس والعشرين

```text
CHAPTER      = 25
VERSION      = 0.29.0-dev
TOPIC        = DECOUPLING / EFFICIENT CONGRUENCING / VINOGRADOV MEAN VALUE
STATUS       = PRE-AUTHORING
AUTHORING    = BLOCKED
RESULTS      = RESERVED / NON-CITABLE
```

## المصادر الأولية

| الرمز | المصدر | الدور | الحالة |
|---|---|---|---|
| S1 | T. D. Wooley, *Vinogradov's mean value theorem via efficient congruencing*, Annals of Mathematics 175 (2012), 1575--1627, DOI: 10.4007/annals.2012.175.3.12 | نشأة التوافق الفعّال وحدود تقترب لأول مرة من الصورة المتوقعة؛ ليست إثبات الحالة التكعيبية الكاملة | PRIMARY / VERIFIED |
| S2 | J. Bourgain and C. Demeter, *The proof of the \(\ell^2\) Decoupling Conjecture*, Annals of Mathematics 182 (2015), 351--389 | مبرهنة فك الاقتران الحادة وسياقها التحليلي | PRIMARY / VERIFIED |
| S3 | J. Bourgain, C. Demeter, L. Guth, *Proof of the main conjecture in Vinogradov's Mean Value Theorem for degrees higher than three*, Annals of Mathematics 184 (2016), 633--682, DOI: 10.4007/annals.2016.184.2.7 | إثبات الحد الرئيسي عبر فك الاقتران للدرجات \(k\ge 4\) | PRIMARY / VERIFIED |
| S4 | T. D. Wooley, *Nested efficient congruencing and relatives of Vinogradov's mean value theorem*, Proceedings of the London Mathematical Society 118 (2019), no. 4, 942--1016, DOI: 10.1112/plms.12204 | صيغة التوافق الفعّال المتداخل وإثبات الحد الرئيسي لجميع الدرجات | PRIMARY / VERIFIED |
| S5 | T. D. Wooley, *The cubic case of the main conjecture in Vinogradov's mean value theorem*, Advances in Mathematics 294 (2016), 532--561, DOI: 10.1016/j.aim.2016.02.033 | الإثبات الكامل للحالة التكعيبية \(k=3\) | PRIMARY / VERIFIED |

## الصياغات المراد تثبيتها

### 1. مجموع القيمة المتوسطة

نستعمل التطبيع

\[
J_{s,k}(X)=\int_{[0,1)^k}
\left|\sum_{1\le n\le X}e(\alpha_1n+\cdots+\alpha_kn^k)\right|^{2s}
\,d\boldsymbol\alpha,
\qquad e(z)=e^{2\pi iz}.
\]

### 2. التفسير العددي

بالتعامد، يساوي \(J_{s,k}(X)\) عدد الحلول الصحيحة للنظام

\[
\sum_{i=1}^{s}x_i^j=\sum_{i=1}^{s}y_i^j
\qquad (1\le j\le k),
\]

مع \(1\le x_i,y_i\le X\).

### 3. الحد الرئيسي

الصيغة المحورية المنقولة هي: لكل \(\varepsilon>0\)،

\[
J_{s,k}(X)\ll_{s,k,\varepsilon}
X^{\varepsilon}\left(X^s+X^{2s-k(k+1)/2}\right).
\]

يجب عدم حذف حد \(X^s\)، وعدم إسقاط عامل \(X^\varepsilon\)، وعدم تقديم الثابت على أنه مطلق.

## حدود الادعاء

- لا يعاد بناء برهان التوافق الفعّال كاملًا.
- لا تعاد بناء نظرية فك الاقتران العامة.
- يعرض الفصل هندسة المسارين وموقعهما البرهاني مع نتائج منقولة بدقة.
- تطبيق وارينغ سيكون جسرًا تفسيريًا منضبطًا، لا برهانًا كاملًا للصيغة التقاربية.
- يجب الفصل بين مبرهنة فك الاقتران للأسطح ذات الانحناء وبين فك الاقتران للمنحنى اللحظي المستعمل في VMVT.
- التسلسل التاريخي المجمد: Wooley 2012 تأسيس وتقدم قوي؛ Wooley 2016 للحالة \(k=3\)؛ Bourgain--Demeter--Guth 2016 للحالات \(k\ge4\)؛ Wooley 2019 لجميع الدرجات بمسار التوافق المتداخل.

## فجوات يجب أن تفحصها المراجعة المستقلة

1. صحة التطبيع \(e(z)=e^{2\pi iz}\).
2. صحة أسّ الكتلة الحرجة \(k(k+1)/2\).
3. صحة نطاقات \(k\) التاريخية لكل مصدر، وعدم نسبة إثبات جميع الدرجات إلى BDG وحدهم.
4. عدم الخلط بين نتيجة 2015 العامة للأسطح المحدبة ونتيجة 2016 للمنحنى اللحظي.
5. عدم الدور مع الفصل 17 في وارينغ والفصل 18 في المجاميع الأسية.
