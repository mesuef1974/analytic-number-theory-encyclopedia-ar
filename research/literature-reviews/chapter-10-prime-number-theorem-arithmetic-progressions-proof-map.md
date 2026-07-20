# خريطة برهان الفصل العاشر — مبرهنة الأعداد الأولية في المتتاليات الحسابية

## الهدف

لـ\(q\ge2\) ثابت و\((a,q)=1\):

\[
\psi(x;q,a)\sim\frac{x}{\varphi(q)},
\qquad
\vartheta(x;q,a)\sim\frac{x}{\varphi(q)},
\qquad
\pi(x;q,a)\sim\frac{x}{\varphi(q)\log x}.
\]

## الكائنات

\[
\psi(x;q,a)=\sum_{\substack{n\le x\\n\equiv a\pmod q}}\Lambda(n),
\]

\[
\vartheta(x;q,a)=\sum_{\substack{p\le x\\p\equiv a\pmod q}}\log p,
\qquad
\pi(x;q,a)=\sum_{\substack{p\le x\\p\equiv a\pmod q}}1.
\]

ونعرّف، عندما \(\Re(s)>1\):

\[
F_{q,a}(s)
=
\sum_{\substack{n\ge1\\n\equiv a\pmod q}}
\frac{\Lambda(n)}{n^s}.
\]

## العقد البرهانية

### P10-01 — مرشح الفئة

من تعامد الشخصيات:

\[
\mathbf 1_{n\equiv a\,(q)}
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}\overline{\chi(a)}\chi(n)
\]

لكل \((a,q)=1\). إذا كان \(n\equiv a\pmod q\)، فهو أولي مع \(q\)، ولذلك لا تظهر مشكلة قيم الشخصيات الصفرية.

### P10-02 — سلسلة الفئة

بالتقارب المطلق في \(\Re(s)>1\):

\[
F_{q,a}(s)
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}
\overline{\chi(a)}
\left(-\frac{L'}{L}(s,\chi)\right).
\]

### P10-03 — موجبية \(3-4-1\) لدوال \(L\)

لكل شخصية \(\chi\)، ولكل \(\sigma>1\)، و\(t\in\mathbb R\):

\[
-3\frac{\zeta'}{\zeta}(\sigma)
-4\Re\frac{L'}{L}(\sigma+it,\chi)
-\Re\frac{L'}{L}(\sigma+2it,\chi^2)
\ge0.
\]

والسبب أن الحد عند \(n\) يساوي

\[
\frac{\Lambda(n)}{n^\sigma}
\left(3+4\Re z_n+\Re z_n^2\right),
\qquad
z_n=\chi(n)n^{-it},\quad |z_n|\le1.
\]

إذا كتبنا \(z=re^{i\theta}\)، فإن

\[
3+4r\cos\theta+r^2\cos2\theta
\ge
3-4r+r^2
=(1-r)(3-r)\ge0.
\]

### P10-04 — عدم الانعدام على الخط

#### الحالة \(t=0\)

- إذا كانت \(\chi\) غير رئيسية: `ANT-THM-07-09` يعطي \(L(1,\chi)\ne0\).
- إذا كانت رئيسية: \(L(s,\chi_0)\) لها قطب بسيط عند \(1\).

#### الحالة \(t\ne0\)

افترض أن \(L(1+it,\chi)\) له صفر رتبته \(m\ge1\). عند \(\sigma\downarrow1\):

\[
-3\frac{\zeta'}{\zeta}(\sigma)
=
\frac{3}{\sigma-1}+O(1),
\]

\[
-4\Re\frac{L'}{L}(\sigma+it,\chi)
=
-\frac{4m}{\sigma-1}+O(1).
\]

أما الحد الثالث فلا يملك قطبًا موجبًا عند \(1+2it\)، لأن \(t\ne0\). فإذا كانت النقطة صفرًا زادت المعامل سلبية. يصبح المعامل الكلي لا يزيد على \(3-4m\le-1\)، ويناقض الموجبية.

#### الشخصيات غير البدائية

إذا كانت \(\chi\) مستحثة من \(\chi^*\):

\[
L(s,\chi)
=
L(s,\chi^*)
\prod_{p\mid q,\,p\nmid q^*}
\left(1-\chi^*(p)p^{-s}\right).
\]

العوامل المحدودة لا تنعدم على \(\Re(s)=1\)، لأن \(|p^{-s}|=p^{-1}<1\).

### P10-05 — تحليل القطب

للشخصية الرئيسية:

\[
L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s}).
\]

إذن

\[
-\frac{L'}{L}(s,\chi_0)
=
\frac1{s-1}+H_q(s),
\]

حيث \(H_q\) هولومورفية قرب \(s=1\). وبما أن \(\overline{\chi_0(a)}=1\):

\[
F_{q,a}(s)
-
\frac1{\varphi(q)(s-1)}
\]

يمتد تحليليًا عبر كل نقطة من \(\Re(s)=1\).

### P10-06 — مطابقة Wiener--Ikehara

نأخذ

\[
a_n=\Lambda(n)\mathbf 1_{n\equiv a\,(q)}\ge0.
\]

ومجاميعها الجزئية هي \(\psi(x;q,a)\). كما أن

\[
0\le\psi(x;q,a)\le\psi(x)\ll x
\]

من الفصل التاسع. القطب له الباقي \(1/\varphi(q)\)، ولذلك:

\[
\psi(x;q,a)\sim\frac{x}{\varphi(q)}.
\]

### P10-07 — إزالة القوى الأولية العليا

لدينا حد مباشر من الحالة العالمية:

\[
0\le
\psi(x;q,a)-\vartheta(x;q,a)
\le
\psi(x)-\vartheta(x)
\ll\sqrt{x}\log x=o(x).
\]

ومن ثم:

\[
\vartheta(x;q,a)\sim\frac{x}{\varphi(q)}.
\]

### P10-08 — الجمع الجزئي

من

\[
\vartheta(x;q,a)=\sum_{\substack{p\le x\\p\equiv a\,(q)}}\log p
\]

نطبق الجمع الجزئي كما في `ANT-THM-02-04`، فنحصل على:

\[
\pi(x;q,a)\sim\frac{x}{\varphi(q)\log x}.
\]

## مخطط الاعتماد

```text
ANT-COR-07-01 + ANT-PROP-07-06
        |
        v
P10-01 / P10-02: character-filtered Dirichlet series
        |
        +------------------------------+
        |                              |
        v                              v
ANT-LEM-07-01 + ANT-THM-09-01      ANT-THM-07-09
        |                              |
        +--------------+---------------+
                       v
          P10-03 / P10-04: L nonvanishing on Re(s)=1
                       |
                       v
          P10-05: only principal pole remains
                       |
                       v
ANT-THM-09-02 + psi(x;q,a) <= psi(x) << x
                       |
                       v
          P10-06: psi(x;q,a) ~ x/phi(q)
                       |
          +------------+-------------+
          |                          |
          v                          v
ANT-LEM-09-02                ANT-THM-02-04
          |                          |
          v                          v
 theta(x;q,a) asymptotic      pi(x;q,a) asymptotic
```

## فحص عدم الدور

يحظر في العقد P10-03 إلى P10-05 استعمال أي من:

- \(\psi(x;q,a)\sim x/\varphi(q)\).
- \(\pi(x;q,a)\sim x/(\varphi(q)\log x)\).
- منطقة خالية كمية لدوال \(L\) مشتقة من PNT-AP.
- صيغة صريحة في الفئات تعتمد على عدم الانعدام المراد إثباته.

المسموح فقط:

- المنتجات الأويلرية في \(\Re(s)>1\).
- قطب زيتا البسيط.
- عدم انعدام زيتا على الخط من الفصل التاسع.
- عدم انعدام \(L(1,\chi)\) من الفصل السابع.
- التحليل المحلي للمشتقة اللوغاريتمية.
- موجبية الحدود.

## نقاط تحتاج تدقيقًا قبل فتح التأليف

- [ ] فحص إشارة كل حد في P10-03 وP10-04.
- [ ] تثبيت أن الحد الثالث لا يضيف قطبًا عند \(t\ne0\).
- [ ] فحص الانتقال من الشخصيات البدائية إلى غير البدائية.
- [ ] مطابقة الباقي \(1/\varphi(q)\) بدقة.
- [ ] مطابقة جميع فروض Wiener--Ikehara.
- [ ] تثبيت أن جميع العبارات تخص \(q\) ثابتًا.
- [ ] فحص عدم الدور كاملًا.

## حالة الخريطة

```text
PROOF-MAP = COMPLETE-CANDIDATE
LOGIC-AUDIT = NOT YET PASSED
PRE-AUTHORING-GATE = OPEN
AUTHORING = BLOCKED
```
