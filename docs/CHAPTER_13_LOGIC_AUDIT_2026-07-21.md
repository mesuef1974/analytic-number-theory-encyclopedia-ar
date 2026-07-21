# التدقيق المنطقي النهائي قبل تأليف الفصل الثالث عشر

التاريخ: 2026-07-21

```text
CHAPTER                  = 13
AUDIT                    = FINAL-PRE-AUTHORING-LOGIC
RESULTS-CHECKED          = 11
DEPENDENCY-GRAPH         = PASS
SIGN-AND-SUPPORT         = PASS
PARAMETER-RANGES         = PASS
LOG-LOSS                 = PASS / A+3
EFFECTIVITY              = PASS / INEFFECTIVE-CONSTANT
NON-CIRCULARITY          = PASS
VERDICT                  = PASS-FOR-AUTHORING
RELEASE-READY            = NO
```

## 1. نطاق التدقيق

يراجع هذا التقرير سلسلة البرهان كاملة من المدخل المقتبس للغربال الكبير حتى
مبرهنة Bombieri--Vinogradov ونتائجها التابعة. لا يراجع أسلوب العرض النهائي
أو التنضيد؛ فذلك يأتي بعد إنشاء متن الفصل.

الملفات الحاكمة:

- `docs/CHAPTER_13_LARGE_SIEVE_MEAN_VALUE_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_VAUGHAN_IDENTITY_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_TYPE_I_TYPE_II_MEAN_VALUE_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_CONDUCTOR_PRINCIPAL_BV_AUDIT_2026-07-21.md`
- `research/literature-reviews/chapter-13-bombieri-vinogradov-proof-map.md`

## 2. النتائج المدققة

| المعرّف | النتيجة | المنشأ | الحكم المنطقي |
|---|---|---|---|
| `ANT-THM-13-01` | حزمة الغربال الكبير: التربيعية والثنائية العظمى | `CITED / COMPOSITE-INPUT` | `PASS` |
| `ANT-LEM-13-01` | هوية Vaughan | `PROVED-HERE` | `PASS` |
| `ANT-PROP-13-01` | الرد إلى أشكال Type I/II | `PROVED-HERE` | `PASS` |
| `ANT-LEM-13-02` | تقدير Type I | `PROVED-HERE` | `PASS` |
| `ANT-LEM-13-03` | تقدير Type II | `PROVED-HERE` | `PASS` |
| `ANT-LEM-13-04` | Pólya--Vinogradov للشخصيات البدائية | `PROVED-HERE` | `PASS` |
| `ANT-THM-13-02` | مبرهنة القيمة المتوسطة مع `sup_{y\le x}` | `PROVED-HERE` من المدخل المقتبس | `PASS` |
| `ANT-THM-13-03` | Bombieri--Vinogradov في صيغة `psi` | `PROVED-HERE / INEFFECTIVE` | `PASS` |
| `ANT-COR-13-01` | النسخة الموافقة لـ`theta` | `PROVED-HERE / INEFFECTIVE` | `PASS` |
| `ANT-COR-13-02` | النسخة الموافقة لـ`pi` | `PROVED-HERE / INEFFECTIVE` | `PASS` |
| `ANT-COR-13-03` | تقريبًا كل الترديدات | `PROVED-HERE / INEFFECTIVE` | `PASS` |

## 3. تدقيق هوية Vaughan

تكتب الحدود على مستوى التفاف ديريشليه:

\[
\Lambda_U,
\quad
-\mathbf1*\Lambda_U*\mu_V,
\quad
\log*\mu_V,
\quad
(\log-\mathbf1*\Lambda_U)*(\mu-\mu_V).
\]

بعد التوسع تلغى حدود القطع الزوجية، ثم تستعمل

\[
\log=\mathbf1*\Lambda,
\qquad
\mathbf1*\mu=\varepsilon,
\]

فتكون المحصلة \(\Lambda\). الإشارة السالبة في الحد الثاني، والإشارة الموجبة
في الحد الثالث، وشرطا الدعم \(m>U\) و\(k>V\) في الحد الرابع كلها صحيحة.
الحالة \(n=1\) والقطع الحقيقي \(U,V\ge1\) مغلقان كذلك.

```text
VAUGHAN-IDENTITY = PASS
```

## 4. تدقيق Pólya--Vinogradov

البرهان يعتمد فقط على تحويل فورييه المنتهي وقيمة مجموع غاوس للشخصية
البدائية من الفصل السابع، ثم تقدير المتسلسلة الهندسية والمجموع التوافقي.
ينتج

\[
\sup_{M,N}\left|\sum_{M<n\le M+N}\chi(n)\right|
\ll\sqrt q\log(2q).
\]

لا يظهر اعتماد على Bombieri--Vinogradov أو على متوسطات الأوليات.

```text
POLYA--VINOGRADOV = PASS / NON-CIRCULAR
```

## 5. تدقيق Type I وType II

### Type I

- الجزء الصغير من \(S_2\) يضبط بواسطة Pólya--Vinogradov.
- عدد الشخصيات البدائية لا يتجاوز \(\varphi(q)\).
- مع الوزن \(q/\varphi(q)\) تظهر الكمية
  \(\sum_{q\le Q}q^{3/2}\ll Q^{5/2}\).
- النتيجة:

\[
\mathcal M(S_2')
\ll(x+Q^{5/2}U)(\log(2Qx))^2,
\]

وبالمثل

\[
\mathcal M(S_3)
\ll(x+Q^{5/2}V)(\log(2Qx))^2.
\]

### Type II

في كتلة \(M<m\le2M\)، تكون معياريات المعاملات

\[
\|a\|_2\ll M^{1/2}\log(2x),
\qquad
\|b\|_2\ll(x/M)^{1/2}.
\]

تطبيق المدخل الثنائي العظمى ثم جمع الكتل الديادية يعطي

\[
\mathcal M(S_4)
\ll
\left(x+QxU^{-1/2}+QxV^{-1/2}+Q^2x^{1/2}\right)(\log 2x)^3.
\]

الجزء الكبير من \(S_2\) يعطي الحد الإضافي الصحيح

\[
Qx^{1/2}(UV)^{1/2}.
\]

لا توجد خسارة خطية خفية في عدد الكتل؛ الحدود الهندسية ذات \(M^{\pm1/2}\)
تهيمن عليها الأطراف، بينما يستهلك عدد الكتل قوة لوغاريتم واحدة في الحدود
الثابتة.

```text
TYPE-I  = PASS
TYPE-II = PASS
```

## 6. تدقيق اختيار المعلمات

### عندما \(Q\le x^{1/3}\)

الاختيار

\[
U=V=x^{1/3}
\]

يضع كل الحدود داخل

\[
x+x^{5/6}Q+x^{1/2}Q^2.
\]

### عندما \(x^{1/3}\le Q\le x^{1/2}\)

الاختيار

\[
U=V=x^{2/3}/Q
\]

صحيح لأن \(U,V\ge1\)، ويحقق

\[
Q^{3/2}x^{2/3}\le x^{1/2}Q^2,
\qquad
x^{7/6}\le x^{5/6}Q.
\]

### عندما \(Q>x^{1/2}\)

التطبيق المباشر للمدخل الثنائي العظمى مع \(M=1\)، و\(a_1=1\)،
و\(b_n=\Lambda(n)\) هو المسار الصحيح. لا تستعمل هنا صيغة التفاف غير لازمة.

```text
PARAMETER-RANGES = PASS
```

## 7. تدقيق الشخصية الرئيسية والموصل

تعريف

\[
\psi'(y,\chi)=\psi(y,\chi)-\mathbf1_{\chi=\chi_0}y
\]

يجعل هوية الفئة دقيقة:

\[
E(y;q,a)
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}\overline{\chi(a)}\psi'(y,\chi).
\]

الرد إلى الجد البدائي لا يغير الحد الرئيسي لأن الشخصية الرئيسية لا تُستحث
إلا من الشخصية البدائية ذات الموصل \(1\). الفرق المحلي مدعوم على القوى
الأولية المحذوفة ويضبط بـ\(O((\log(2qy))^2)\).

الوزن

\[
\sum_{\substack{q\le Q\\d\mid q}}\frac1{\varphi(q)}
\ll\frac1{\varphi(d)}\log\frac{2Q}{d}
\]

صحيح لأن \(\varphi(dm)\ge\varphi(d)\varphi(m)\) و
\(\sum_{m\le X}1/\varphi(m)\ll\log(2X)\).

```text
PRINCIPAL-CHARACTER  = PASS
CONDUCTOR-TO-MODULUS = PASS
```

## 8. تدقيق الترديدات الصغيرة والكبيرة

يوضع

\[
D=(\log x)^{A+4}.
\]

- للموصلات \(d\le D\)، تعطي Siegel--Walfisz تقديرًا أسيًا موحدًا؛ معالجة
  \(y<e^{\sqrt{\log x}}\) بالتقدير التافه صحيحة.
- للموصلات \(d>D\)، يؤدي التقسيم الديادي ومبرهنة القيمة المتوسطة إلى

\[
xD^{-1}(\log x)^4
+x^{5/6}(\log x)^5
+x^{1/2}Q(\log x)^3.
\]

مع

\[
Q=x^{1/2}(\log x)^{-(A+3)}
\]

تكون الحدود الأول والثالث بالضبط من رتبة \(x/(\log x)^A\)، والحد الأوسط
أصغر منها لكل \(A\) ثابت عندما يكبر \(x\). الخطأ المحلي المجموع على
الترديدات أصغر أيضًا.

```text
SMALL-CONDUCTORS = PASS
LARGE-CONDUCTORS = PASS
LOG-LOSS         = PASS / A+3
```

## 9. تدقيق النتائج التابعة

### الانتقال إلى \(\vartheta\)

\[
|\psi(y;q,a)-\vartheta(y;q,a)|
\le\psi(y)-\vartheta(y)
\ll y^{1/2}\log(2y).
\]

جمع هذا الخطأ حتى \(Q\le x^{1/2}(\log x)^{-(A+3)}\) يعطي
\(O(x/(\log x)^{A+2})\)، فيمتص.

### الانتقال إلى \(\pi\)

الجمع الجزئي يضبط الخطأ بنسخة \(\vartheta\) مع أس ادخار \(A+1\). لذلك المجال
الصريح الصحيح هو

\[
Q\le x^{1/2}(\log x)^{-(A+4)}.
\]

### تقريبًا كل الترديدات

متراجحة ماركوف على مجموع الأخطاء تعطي، عند تطبيق المبرهنة بالأس \(B+C\)،
أن عدد الترديدات التي تتجاوز
\(x/(Q(\log x)^B)\) هو

\[
O\left(Q/(\log x)^C\right).
\]

```text
THETA-COROLLARY      = PASS
PI-COROLLARY         = PASS
ALMOST-ALL-COROLLARY = PASS
```

## 10. الفعالية وحدود الادعاء

المسار المعتمد يستعمل Siegel--Walfisz للموصلات الصغيرة؛ ولذلك تكون الثوابت
العامة غير فعالة. هذا لا يغير صحة المبرهنة، لكنه يجب أن يظهر في صياغتها.

لا يثبت الفصل:

- Elliott--Halberstam؛
- مستوى توزيع أكبر من \(1/2\) في الصيغة العامة؛
- Barban--Davenport--Halberstam؛
- نسخة الفترات القصيرة؛
- نتائج الأوزان well-factorable بعد حاجز \(1/2\).

```text
EFFECTIVITY  = INEFFECTIVE-CONSTANT
SCOPE-AUDIT  = PASS
```

## 11. فحص عدم الدور

ترتيب الاعتماد هو:

```text
chapters 2,4,7,9,12
        +
large-sieve package (CITED)
        -> Vaughan identity
        -> Pólya--Vinogradov
        -> Type I / Type II
        -> mean-value theorem
        -> conductor reduction
        -> Bombieri--Vinogradov
        -> theta / pi / almost-all
```

لا تستعمل أي نتيجة لاحقة في إثبات سابقتها. وبخاصة، لا تدخل
Bombieri--Vinogradov في Type I أو Type II أو مبرهنة القيمة المتوسطة.

```text
NON-CIRCULARITY = PASS
```

## 12. الحكم

```text
MATHEMATICAL-BLOCKERS = 0
LOGICAL-BLOCKERS      = 0
DEPENDENCY-BLOCKERS   = 0
VERDICT               = PASS-FOR-AUTHORING
```

يجوز إغلاق بوابة ما قبل التأليف بعد نجاح التحقق المرجعي النهائي ومزامنة
حجز المعرفات. لا يعني هذا الحكم أن الفصل `VERIFIED` أو `REVIEWED`، ولا يعني
`RELEASE-READY`.
