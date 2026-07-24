# الفصل الخامس عشر — سجل الأدلة

التاريخ: 2026-07-24

```text
CHAPTER             = 15
VERSION             = 0.19.0-dev
STATE               = RESEARCH-INTAKE / EVIDENCE-BUILDING
AUTHORING           = BLOCKED
PASS-FOR-AUTHORING  = NO
```

## 1. نطاق الفصل

يدرس الفصل الإطار المجرد لمشكلة الغربال، وغربال سيلبرغ العلوي، والبعد الغربالي، واللمّة الأساسية للغربال، والحدود العليا والسفلى، وعائق التكافؤ. لا يخلط الفصل بين هذه الطبقات، ولا يجعل اللمّة الأساسية نتيجة تلقائية من غربال سيلبرغ.

## 2. الصياغة المرجعية الأولية

نبدأ بمتتالية منتهية أو أوزان غير سالبة \(\mathcal A\)، ومجموعة أوليات \(\mathcal P\). نضع

\[
P(z)=\prod_{\substack{p<z\\p\in\mathcal P}}p,
\qquad
S(\mathcal A,\mathcal P,z)
=\sum_{\substack{n\in\mathcal A\\(n,P(z))=1}}1.
\]

ولكل عدد مربع حر \(d\mid P(z)\) نفترض تفكيكًا من الشكل

\[
|\mathcal A_d|=Xg(d)+r_d,
\qquad
g(d)\ \text{ضربية},
\qquad 0\le g(p)<1.
\]

الحاصل المحلي المتوقع هو

\[
V(z)=\prod_{\substack{p<z\\p\in\mathcal P}}(1-g(p)).
\]

هذه الصياغة مرشح عمل وليست نتيجة معتمدة بعد. يجب تثبيت التطبيع النهائي مقابل Halberstam--Richert وGreaves وOpera de Cribro وIwaniec--Kowalski.

## 3. المصادر التي تم التحقق منها

### 3.1 Greaves

- George Greaves, *Sieves in Number Theory* (2001).
- أظهر مسح Consensus أن الكتاب يغطي غربال سيلبرغ العلوي، وغربال برون، وغربال Rosser--Iwaniec، والغربال الموزون، واستخراج حدود سفلى من أفكار سيلبرغ.
- الحالة: `BOOK-TREATMENT / VERIFIED-METADATA-PARTIAL`.
- الاستعمال المقترح: مرجع تعليمي مقارن، لا المصدر الوحيد للصياغة النهائية.

### 3.2 Richert 1969

- H.-E. Richert, “Selberg's sieve with weights”, *Mathematika* 16 (1969), 1--22.
- DOI: `10.1112/S0025579300004563`.
- صفحة Cambridge تؤكد المؤلف، المجلد، العدد، الصفحات، وموضوع دالة الغربلة.
- الحالة: `ORIGINAL-RESEARCH / VERIFIED-PUBLISHER`.
- الاستعمال المقترح: مرجع أصلي للغربال الموزون، لا مدخل أساسي للفصل قبل إغلاق الغربال غير الموزون.

### 3.3 Opera de Cribro

- John Friedlander and Henryk Iwaniec, *Opera de Cribro*, AMS Colloquium Publications 57.
- صفحة AMS تؤكد بنية الكتاب: أسئلة الغربال، مبادئه ومصطلحاته، غربال برون، غربال سيلبرغ، الغربال الكبير، beta-sieve، الغربال الخطي، الغربال التقاربي، مبدأ التكافؤ، والتطبيقات.
- الحالة: `BOOK-TREATMENT / VERIFIED-PUBLISHER`.
- الاستعمال المقترح: المرجع البنيوي الأعلى للفصل، وخاصة للفصل بين Selberg sieve وbeta/linear sieve وparity principle.

### 3.4 Polymath 2014 وعائق التكافؤ

- DHJ Polymath, “Variants of the Selberg sieve, and bounded intervals containing many primes”, *Research in the Mathematical Sciences* 1, Article 12 (2014).
- DOI: `10.1186/s40687-014-0012-7`.
- يوجد Erratum منشور سنة 2015، DOI: `10.1186/s40687-015-0033-x`.
- صفحة الناشر تؤكد أن الورقة تعدّل حجة سيلبرغ لعائق التكافؤ وتربطها بحدود الفجوات، وأن المناخل المستعملة من نوع سيلبرغ.
- الحالة: `PEER-REVIEWED / VERIFIED-PUBLISHER / ERRATUM-ATTACHED`.
- الاستعمال المقترح: مثال حديث على حدود ما يمكن تحصيله من الاعتبارات الغربالية البحتة، لا مصدر التعريف التاريخي للعائق.

## 4. مصادر مرشحة لم تُغلق بعد

- Halberstam--Richert, *Sieve Methods*.
- Iwaniec--Kowalski, *Analytic Number Theory*.
- Montgomery--Vaughan, *Multiplicative Number Theory II*.
- Cojocaru--Murty, *An Introduction to Sieve Methods and Their Applications*.
- النصوص الأصلية لسيلبرغ وبرون وروسر حسب مواضع النتائج النهائية.

لا يعتمد أي منها قبل تثبيت بيانات النشر وموضع النظرية أو الفصل المستخدم.

## 5. فصل المفاهيم الحاكم

### 5.1 الإطار المجرد

المعطيات \(\mathcal A,\mathcal P,z,g(d),r_d\) وكمية الغربلة \(S(\mathcal A,\mathcal P,z)\).

### 5.2 غربال سيلبرغ العلوي

يبنى من لا سلبية مربع مجموع قواسم، ثم اختيار معاملات \(\lambda_d\) وحل مسألة تربيعية تصغيرية. هذه طبقة حد علوي.

### 5.3 اللمّة الأساسية

تحتاج فرضيات كمية على البواقي ومستوى غربلة ومعامل بعد غربالي. لا تتبع آليًا من مجرد كتابة أوزان سيلبرغ.

### 5.4 الحدود السفلى

ليست انعكاسًا مباشرًا للحد العلوي، وقد تتطلب beta-sieve أو linear sieve أو أوزانًا إضافية.

### 5.5 عائق التكافؤ

هو قيد بنيوي على قدرة المناخل التقليدية على التمييز بين الأعداد ذات عدد زوجي أو فردي من العوامل الأولية. لا يصاغ بوصفه استحالة مطلقة لكل طريقة تستعمل غربالًا.

## 6. وحدات الأدلة المفتوحة

1. تثبيت التطبيع النهائي لـ\(S(\mathcal A,\mathcal P,z)\).
2. تثبيت العلاقة \(|\mathcal A_d|=Xg(d)+r_d\) وشروط \(g\).
3. إثبات المتراجحة التربيعية الأولية داخل الموسوعة.
4. تحديد صيغة الحد العلوي لسيلبرغ المناسبة وموضع اقتباس حل المسألة التربيعية.
5. تثبيت تعريف البعد الغربالي من حاصل الضرب المحلي أو مجموع \(g(p)\log p\).
6. اختيار نسخة واحدة من اللمّة الأساسية وتحديد نطاق \(z,D,s\).
7. فصل upper-bound sieve عن lower-bound/linear sieve.
8. صياغة عائق التكافؤ مع مثال تشخيصي موثق.
9. تدقيق اعتماد أي تطبيق على Bombieri--Vinogradov أو BDH لمنع الدور.

## 7. حدود الادعاء

- لا إثبات لحدسية الأوليات التوأم.
- لا إثبات للفجوات المحدودة.
- لا اعتبار Polymath 2014 مصدرًا وحيدًا لعائق التكافؤ.
- لا نقل لصيغة لها Erratum دون فحص التصحيح.
- لا حجز لمعرفات النتائج قبل إغلاق خريطة البرهان.
- لا تأليف قبل حكم صريح `PASS-FOR-AUTHORING`.

```text
PASS-FOR-RESEARCH-INTAKE = YES
PASS-FOR-AUTHORING       = NO
PRE-AUTHORING-GATE       = OPEN
```