# خريطة برهان الفصل الثالث عشر — مبرهنة بومبييري--فينوغرادوف

```text
STATUS             = PRE-AUTHORING / DEPENDENCY-MAP
CENTRAL-THEOREM    = TARGET / NOT YET ADOPTED
LARGE-SIEVE        = CLOSED / CITED
LOG-LOSS           = CLOSED / B(A)=A+3
EFFECTIVITY        = INEFFECTIVE-IN-ADOPTED-ROUTE
AUTHORING          = BLOCKED
```

## 1. الهدف

إثبات أنه لكل \(A>0\):

\[
\sum_{q\le Q}\max_{(a,q)=1}\max_{y\le x}
\left|\psi(y;q,a)-\frac{y}{\varphi(q)}\right|
\ll_A \frac{x}{(\log x)^A},
\qquad
Q\le \frac{x^{1/2}}{(\log x)^{A+3}}.
\]

القوة \(A+3\) تأتي من مبرهنة القيمة المتوسطة ذات العامل
\((\log x)^3\). لا تُعتمد النتيجة نهائيًا قبل إغلاق البرهان الداخلي لهوية
Vaughan وتقديري Type I وType II وعدم الدور.

## 2. مخطط الاعتماد

```text
ANT-PROP-10-01  character filter
        |
        v
principal / nonprincipal separation
        |                          \
        |                           \
        v                            v
ANT-THM-12-01 effective PNT       primitive-character reduction
                                     |
                                     v
                 ANT-THM-13-01 large sieve / CITED
                                     |
                                     v
                    ANT-LEM-13-01 Vaughan identity
                                     |
                         +-----------+-----------+
                         |                       |
                         v                       v
                 ANT-LEM-13-02 Type I    ANT-LEM-13-03 Type II
                         |                       |
                         +-----------+-----------+
                                     |
                                     v
              ANT-THM-13-02 mean value with sup(y<=x)
                                     |
                                     v
                       conductor-to-modulus bookkeeping
                                     |
                                     v
                 ANT-THM-13-03 Bombieri--Vinogradov
                          /             |             \
                         v              v              v
                      theta           pi       almost-all moduli
```

## 3. العقد البرهانية

### العقدة A — مرشح الشخصيات

الهوية الدقيقة للفئة المختزلة متاحة من `ANT-PROP-10-01`. يجب إعادة كتابتها
للمتغير \(y\) ولجميع \(q\le Q\)، مع فصل الشخصية الرئيسية قبل أخذ القيم
المطلقة.

الحالة: `OPEN / INTERNALIZATION`.

### العقدة B — الشخصية الرئيسية

الحد

\[
\psi(y,\chi_0)-y
\]

يحتوي أثر حذف الحدود ذات \((n,q)>1\). يلزم ضبط العوامل المحلية بانتظام ثم
جمعها على الترديدات.

الحالة: `OPEN`.

### العقدة C — الرد إلى الشخصيات البدائية

تحقق المصدر من البنية التالية:

- رد الشخصية المستحثة إلى جدها البدائي ذي الموصل \(d\mid q\).
- خطأ محلي \(O((\log qy)^2)\).
- وزن تعدد الاستحثاثات

\[
\sum_{\substack{q\le Q\\d\mid q}}\frac1{\varphi(q)}
\ll \frac1{\varphi(d)}\log\frac{2Q}{d}.
\]

الحالة: `SOURCE-VERIFIED / INTERNAL-PROOF-OPEN`.

### العقدة D — الغربال الكبير

المبرهنة 19.16 في Montgomery--Vaughan II تثبت:

\[
\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\left|\sum_{M<n\le M+N}a_n\chi(n)\right|^2
\le (N+Q^2)\sum_{M<n\le M+N}|a_n|^2.
\]

تشمل الصيغة فترة منقولة عامة، والنجمة على الشخصيات البدائية، والوزن الدقيق
\(q/\varphi(q)\).

الحالة: `CLOSED / PASS / CITED`.

### العقدة E — هوية Vaughan

يُختار معاملا قطع \(U,V\)، وتفكك \(\Lambda\) إلى حدود مناسبة لـType I وType
II. يجب إثبات الهوية داخل المشروع مع اختبار الإشارات وحدود المجاميع
والالتفافات.

الحالة: `OPEN`.

### العقدة F — Type I

المطلوب تقدير المتوسط على الشخصيات لمجاميع ذات معامل ناعم في أحد المتغيرين،
باستعمال الجمع الجزئي والغِربال الكبير.

الحالة: `OPEN`.

### العقدة G — Type II

هذه العقدة الثنائية الأساسية. يجب ضبط أطوال المتغيرين، وتطبيق كوشي والغِربال
الكبير، ثم اختيار \(U,V\) لتحقيق التوازن.

الحالة: `OPEN`.

### العقدة H — القيمة العظمى في \(y\)

المبرهنة 20.1 في Montgomery--Vaughan II تحتوي أصلًا

\[
\sup_{y\le x}|\psi(y,\chi)|,
\]

وتعطي

\[
\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}\sup_{y\le x}|\psi(y,\chi)|
\ll
\left(x+x^{5/6}Q+x^{1/2}Q^2\right)(\log x)^3.
\]

إذن آلية `max` مغلقة على مستوى المصدر، لكنها تبقى مفتوحة داخل البرهان الذي
ستكتبه الموسوعة.

الحالة: `SOURCE-CLOSED / INTERNALIZATION-OPEN`.

### العقدة I — الخسارة اللوغاريتمية

المبرهنة 20.2 تعطي

\[
\sum_{q\le Q}E^*(x,q)
\ll x^{1/2}Q(\log x)^3.
\]

بوضع \(Q_0=x^{1/2}(\log x)^{-(A+3)}\)، ينتج

\[
x^{1/2}Q_0(\log x)^3=\frac{x}{(\log x)^A}.
\]

وبالرتابة تمتد النتيجة إلى كل \(Q\le Q_0\).

الحالة: `CLOSED / PASS / B(A)=A+3`.

### العقدة J — الفعالية

المسار المصدر يستعمل Siegel--Walfisz للترديدات الصغيرة. لذلك يرث عدم فعالية
الثوابت في الفصل الثاني عشر.

الحالة: `RESOLVED / INEFFECTIVE-IN-ADOPTED-ROUTE`.

## 4. تدقيق عدم الدور

يحظر استعمال أي من الآتي داخل المدخلات السابقة للمبرهنة المركزية:

- Bombieri--Vinogradov نفسها.
- نتيجة «تقريبًا كل الترديدات» المشتقة منها.
- مستوى توزيع يتجاوز \(1/2\).
- تطبيقات غربالية تفترض مسبقًا توزيع الأوليات حتى \(x^{1/2}\).

يمكن استعمال:

- تعامد الشخصيات ومرشح الفئة.
- PNT الفعال للشخصية الرئيسية.
- Siegel--Walfisz للترديدات الصغيرة، مع التصريح بعدم الفعالية.
- الرد المحلي للشخصيات المستحثة.
- الغربال الكبير بوصفه مدخلًا مقتبسًا.
- حدود الدوال الحسابية والالتفافات من الفصول السابقة.

## 5. خطة النتائج

| الترتيب | المعرّف المؤقت | المحتوى | منشأ البرهان المتوقع |
|---:|---|---|---|
| 1 | `ANT-THM-13-01` | الغربال الكبير للشخصيات البدائية | `CITED` |
| 2 | `ANT-LEM-13-01` | هوية Vaughan | `PROVED-HERE` |
| 3 | `ANT-PROP-13-01` | تفكيك Type I/II | `PROVED-HERE` |
| 4 | `ANT-LEM-13-02` | تقدير Type I | `PROVED-HERE` |
| 5 | `ANT-LEM-13-03` | تقدير Type II | `PROVED-HERE` |
| 6 | `ANT-THM-13-02` | مبرهنة القيمة المتوسطة للشخصيات | `PROVED-HERE` اعتمادًا على الغربال الكبير المقتبس |
| 7 | `ANT-THM-13-03` | Bombieri--Vinogradov لـ`psi` | `PROVED-HERE / INEFFECTIVE-CONSTANT` |
| 8 | `ANT-COR-13-01` | النسخة لـ`theta` | `PROVED-HERE / INEFFECTIVE-CONSTANT` |
| 9 | `ANT-COR-13-02` | النسخة لـ`pi` | `PROVED-HERE / INEFFECTIVE-CONSTANT` |
| 10 | `ANT-COR-13-03` | تقريبًا كل الترديدات | `PROVED-HERE / INEFFECTIVE-CONSTANT` |

هذه معرفات تخطيطية غير قابلة للاستشهاد حتى إنشاء سجل حجز رسمي.

## 6. القرارات المحسومة والمؤجلة

### محسوم

- الغربال الكبير: `CITED`.
- المسار التعليمي: Vaughan + large sieve.
- النتيجة المركزية: صيغة `psi`.
- الخسارة: \(B=A+3\).
- الفعالية في المسار الحالي: غير فعالة.
- Elliott--Halberstam وما بعد حاجز \(1/2\): خارج النطاق المركزي.

### مؤجل

- الصياغة الدقيقة لهوية Vaughan وحدود \(U,V\).
- تفاصيل Type I وType II.
- البرهان الداخلي للموصل والترديد والحد الرئيسي.
- الحجز الرسمي للمعرفات.

## 7. شروط إغلاق بوابة ما قبل التأليف

- [x] مطابقة نص الغربال الكبير مع مرجع وصفحة محددة.
- [ ] إثبات هوية Vaughan والتحقق من جميع حدود القطع.
- [ ] إغلاق حساب Type I.
- [ ] إغلاق حساب Type II.
- [x] تثبيت آلية `max_{y\le x}` على مستوى المصدر.
- [ ] تدخيل آلية `max_{y\le x}` في البرهان الداخلي.
- [x] التحقق من بنية الموصلات والشخصيات المستحثة في المصدر.
- [ ] كتابة تدقيق الموصلات الداخلي.
- [ ] تدقيق الشخصية الرئيسية والعوامل المحلية.
- [x] حساب الخسارة اللوغاريتمية وتحديد \(B(A)=A+3\).
- [x] إصدار حكم الفعالية: `INEFFECTIVE-IN-ADOPTED-ROUTE`.
- [ ] فحص عدم الدور.
- [ ] حجز معرفات النتائج.

```text
PRE-AUTHORING-GATE = OPEN
AUTHORING           = BLOCKED
```
