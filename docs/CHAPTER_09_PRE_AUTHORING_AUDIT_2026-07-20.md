# تدقيق ما قبل تأليف الفصل التاسع

## مبرهنة الأعداد الأولية

التاريخ: 2026-07-20  
الإصدار: `0.13.0-dev`  
الفرع: `agent/chapter-09-prime-number-theorem-v0.13.0`  
الحالة: `PRE-AUTHORING-GATE-CLOSED`

## 1. الغرض

تغلق هذه الوثيقة الفجوات التي منعت بدء متن الفصل التاسع. ولا ترفع الفصل إلى
`VERIFIED` أو `REVIEWED`؛ فهي تمنح الإذن ببدء مسودة الفصل فقط.

المسار النوعي المعتمد هو:

\[
-\frac{\zeta'}{\zeta}(s)
\longrightarrow
\zeta(1+it)\ne0
\longrightarrow
\text{Wiener--Ikehara}
\longrightarrow
\psi(x)\sim x
\longrightarrow
\vartheta(x)\sim x
\longrightarrow
\pi(x)\sim\frac{x}{\log x}.
\]

لا يستعمل هذا المسار صيغة بيرون، ولا تحويل المسار، ولا الصيغة الصريحة، ولا
المنطقة الكمية الخالية من الأصفار.

## 2. صيغة Wiener--Ikehara المعتمدة

اعتمدت صيغة المتسلسلات الديريشلية الخاصة في:

- Jaap Korevaar, *The Wiener--Ikehara theorem by complex analysis*,
  `Proceedings of the American Mathematical Society` 134 (2006), 1107--1116،
  DOI `10.1090/S0002-9939-05-08060-3`.
- نص المبرهنة: Theorem 1.1، الصفحتان 1107--1108.
- تطبيقها على دالة فون مانغولت ومبرهنة الأعداد الأولية: القسم 2، الصفحتان
  1108--1109.

الصيغة المستعملة هي:

> لتكن
> \[
> f(s)=\sum_{n\ge1}\frac{a_n}{n^s},\qquad a_n\ge0,
> \]
> متقاربة في \(\Re(s)>1\). ولتكن
> \(S(x)=\sum_{n\le x}a_n\). إذا كان \(S(n)=O(n)\)، وكان
> \[
> f(s)-\frac{A}{s-1}
> \]
> يمتد تحليليًا أو باستمرار إلى نصف المستوى المغلق \(\Re(s)\ge1\)، فإن
> \[
> S(n)\sim An.
> \]

حالة النتيجة في الموسوعة:

```text
ANT-THM-09-02 = CITED
```

لم تعتمد صيغة أضعف ذات سلوك حدّي توزيعي، ولم تخلط فروض نسخ مختلفة من
Wiener--Ikehara.

## 3. التحقق التاريخي والمرجعي

- سجل Ikehara الأصلي مثبت: Shikao Ikehara, *An Extension of Landau's
  Theorem in the Analytical Theory of Numbers*, `Journal of Mathematics and
  Physics` 10 (1931), 1--12، DOI `10.1002/sapm19311011`.
- سجل Hadamard الأصلي مثبت: `Bulletin de la Société Mathématique de France`
  24 (1896), 199--220، DOI `10.24033/bsmf.545`.
- سجل de la Vallée Poussin يثبت الأجزاء الثلاثة في المجلد 20 (1896)،
  الصفحات 183--256، 281--362، 363--397. ولا تنقل الموسوعة منه إحالة داخلية
  إلى خطوة محددة قبل فحص النسخة الأصلية نفسها.
- Apostol: فصل *Analytic Proof of the Prime Number Theorem*، الصفحات
  278--303.
- Davenport: فصل *The Prime Number Theorem*، الصفحات 111--114.
- Montgomery--Vaughan: الفصل 6، الصفحات 168--198.
- Iwaniec--Kowalski: الفصل 3 يبدأ في الصفحة 31 للنظرية الأولية للأعداد
  الأولية، والفصل 5 يبدأ في الصفحة 93 للنظرية التحليلية الكلاسيكية لدوال
  \(L\).
- Tenenbaum: القسمان II.4 وII.7، وفق فهرس الطبعة الثالثة.
- Titchmarsh: فصل Hadamard--de la Vallée Poussin في الفصول المبكرة؛ يستعمل
  بوصفه مرجعًا للمسار الكلاسيكي الكمي، لا بوصفه مصدر صيغة
  Wiener--Ikehara المعتمدة هنا.

المرجع الحاكم لصياغة المبرهنة التاوبيرية وتطبيقها في هذه النسخة هو Korevaar
2006، ولذلك لا تتوقف بوابة التأليف على استكمال كل إحالة صفحة لمسار بيرون
المؤجل.

## 4. حد تشيبيشيف المطلوب

### 4.1 حد \(\vartheta(x)\)

لكل عدد صحيح \(n\ge1\)، كل أولي \(p\) يحقق \(n<p\le2n\) يقسم
\(\binom{2n}{n}\). ومن ثم

\[
\vartheta(2n)-\vartheta(n)
\le
\log\binom{2n}{n}
\le
2n\log2.
\]

إذا كان \(2^k\le x<2^{k+1}\)، فإن الجمع على الفترات الثنائية يعطي

\[
\vartheta(x)
\le
\vartheta(2^{k+1})
\le
\sum_{j=0}^{k}2^{j+1}\log2
<4x\log2.
\]

إذن

\[
\vartheta(x)\ll x.
\]

### 4.2 حد \(\psi(x)\) والقوى الأولية العليا

لدينا الهوية الدقيقة

\[
\psi(x)=\sum_{m\ge1}\vartheta\!\left(x^{1/m}\right),
\]

حيث لا تظهر إلا الحدود \(m\le\log_2x\). لذلك

\[
0\le
\psi(x)-\vartheta(x)
=
\sum_{2\le m\le\log_2x}
\vartheta\!\left(x^{1/m}\right)
\ll
\sqrt{x}\log x.
\]

وبخاصة

\[
\psi(x)\ll x,
\qquad
\psi(x)-\vartheta(x)=o(x).
\]

هذا البرهان ابتدائي ولا يستعمل \(\pi(x)\sim x/\log x\)، ولذلك لا يحمل
دورًا منطقيًا.

## 5. المتراجحة الموزونة وعدم انعدام زيتا على الخط

من `ANT-THM-05-05`، عندما \(\sigma>1\):

\[
-\frac{\zeta'}{\zeta}(s)
=
\sum_{n\ge1}\frac{\Lambda(n)}{n^s}.
\]

وباستخدام `ANT-LEM-07-01`:

\[
3+4\cos u+\cos2u=2(1+\cos u)^2\ge0,
\]

نحصل، لكل \(t\in\mathbb R\)، على

\[
-3\frac{\zeta'}{\zeta}(\sigma)
-4\Re\frac{\zeta'}{\zeta}(\sigma+it)
-\Re\frac{\zeta'}{\zeta}(\sigma+2it)
\ge0.
\]

افترض أن \(t\ne0\) وأن \(1+it\) صفر من الرتبة \(m\ge1\). إذا كانت رتبة
الصفر عند \(1+2it\) هي \(m_2\ge0\)، فإن التوسعات المحلية عندما
\(\sigma\downarrow1\) تعطي

\[
\frac{\zeta'}{\zeta}(\sigma)
=-\frac1{\sigma-1}+O(1),
\]

\[
\Re\frac{\zeta'}{\zeta}(\sigma+it)
=\frac{m}{\sigma-1}+O(1),
\]

\[
\Re\frac{\zeta'}{\zeta}(\sigma+2it)
=\frac{m_2}{\sigma-1}+O(1).
\]

وبالتالي يساوي معامل \((\sigma-1)^{-1}\) في الطرف الأيسر

\[
3-4m-m_2\le-1,
\]

وهو يناقض عدم سلبية الطرف الأيسر قرب \(1\). إذن

\[
\zeta(1+it)\ne0\qquad(t\ne0).
\]

وعند \(t=0\) توجد لزيتا قطب بسيط لا صفر. ومن ثم لا تنعدم زيتا على الخط
\(\Re(s)=1\).

هذا البرهان لا يستعمل PNT، ولا الصيغة الصريحة، ولا منطقة خالية كمية.

## 6. إزالة القطب ومطابقة فروض Korevaar

ضع

\[
f(s)=-\frac{\zeta'}{\zeta}(s)
=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},
\qquad \Re(s)>1.
\]

- المعاملات \(\Lambda(n)\ge0\).
- المجاميع الجزئية هي \(S(n)=\psi(n)\ll n\) من القسم 4.
- عند كل نقطة \(1+it\)، \(t\ne0\)، تكون زيتا هولومورفية وغير منعدمة،
  ولذلك \(-\zeta'/\zeta\) هولومورفية في جوارها.
- قرب \(s=1\)، اكتب
  \[
  \zeta(s)=\frac{h(s)}{s-1},
  \qquad h(1)=1,
  \]
  حيث \(h\) هولومورفية وغير منعدمة قرب \(1\). عندئذ
  \[
  -\frac{\zeta'}{\zeta}(s)
  =
  \frac1{s-1}-\frac{h'}{h}(s),
  \]
  ومن ثم
  \[
  -\frac{\zeta'}{\zeta}(s)-\frac1{s-1}
  \]
  هولومورفية قرب \(1\).

إذن جميع فروض Theorem 1.1 في Korevaar متحققة مع \(A=1\)، فنحصل على

\[
\psi(n)\sim n.
\]

ولكل \(x\ge1\):

\[
\psi(x)=\psi(\lfloor x\rfloor),
\qquad
\lfloor x\rfloor\sim x,
\]

فتنتج الصيغة الحقيقية

\[
\psi(x)\sim x.
\]

ثم يعطي القسم 4

\[
\vartheta(x)=\psi(x)+o(x)\sim x,
\]

ويعطي `ANT-THM-02-04`

\[
\pi(x)\sim\frac{x}{\log x}.
\]

## 7. فحص عدم الدور

| الاعتماد | هل يستعمل النتيجة المركزية؟ | الحكم |
|---|---:|---|
| المشتقة اللوغاريتمية في \(\Re(s)>1\) | لا | `PASS` |
| قطب زيتا عند \(1\) | لا | `PASS` |
| المتراجحة المثلثية | لا | `PASS` |
| حد تشيبيشيف \(\vartheta(x)\ll x\) | لا | `PASS` |
| \(\psi(x)\ll x\) | لا | `PASS` |
| عدم الانعدام على الخط | لا | `PASS` |
| Wiener--Ikehara | مبرهنة خارجية مستقلة | `CITED` |
| الانتقال \(\psi\to\vartheta\) | لا يستعمل PNT | `PASS` |
| الانتقال \(\vartheta\to\pi\) | يفترض \(\vartheta\sim x\) فقط | `PASS` |

لا يوجد مسار يعود من \(\pi(x)\sim x/\log x\) إلى فرض سابق في البرهان.

## 8. قرار البوابة

```text
WIENER-IKEHARA-EXACT-STATEMENT = CLOSED
WIENER-IKEHARA-STATUS = CITED
CHEBYSHEV-LINEAR-BOUND = PROVED-IN-AUDIT
ZETA-LINE-NONVANISHING = PROVED-IN-AUDIT
REMOVABLE-POLE-CHECK = PASS
PSI-TO-THETA-LEMMA = PROVED-IN-AUDIT
PAGE-LEVEL-SOURCE-VERIFICATION = CLOSED-FOR-ADOPTED-ROUTE
NO-CIRCULARITY = PASS
PRE-AUTHORING-GATE = CLOSED
AUTHORING = AUTHORIZED
```

لا يعني هذا القرار أن الفصل صار `VERIFIED`، ولا أنه جاهز للدمج. الخطوة
التالية هي كتابة المسودة البرهانية، ثم البناء والتدقيق المنطقي والتحقق
المرجعي والمراجعة المستقلة.