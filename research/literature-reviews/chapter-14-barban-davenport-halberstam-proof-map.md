# خريطة برهان الفصل الرابع عشر — Barban--Davenport--Halberstam

التاريخ: 2026-07-24

```text
STATUS                     = PARTIALLY VERIFIED
PRE-AUTHORING-GATE         = OPEN
AUTHORING                   = BLOCKED
NORMALIZATION-GATE          = CLOSED / PASS
CHARACTER-TRANSFORM-GATE    = CLOSED / PASS
IMPRIMITIVE-REDUCTION       = OPEN
MEAN-VALUE-INPUT            = OPEN
CLASSICAL-UPPER-BOUND       = OPEN
ASYMPTOTIC-LAYER            = DEFERRED
```

## الهدف

بناء مسار برهاني دقيق لكمية التباين

\[
V_\psi(x,Q)=
\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2,
\]

مع الفصل الصريح بين ثلاثة أهداف لا يجوز خلطها:

1. الحد العلوي الكلاسيكي من نوع Barban--Davenport--Halberstam.
2. الصيغة التقاربية Montgomery--Hooley ذات الحد الرئيسي الأدق.
3. النسخ الملساء أو المدمجة أو المعدلة في التطبيع ومجال المتغيرات.

الطبقة الأساسية للفصل هي الهدف الأول فقط. أما الصيغة التقاربية فتبقى طبقة مستقلة مؤجلة حتى يثبت الحد الرئيسي والثابت ومجال `Q` من نص مصدر كامل.

## السلسلة البرهانية الحالية

```text
ORTHOGONALITY OF CHARACTERS
        |
        v
RESIDUE-CLASS VARIANCE <-> CHARACTER SECOND MOMENT
        |
        +--> PRINCIPAL CHARACTER / PRIME-DIVISOR CORRECTIONS
        |
        v
REDUCTION OF IMPRIMITIVE CHARACTERS TO CONDUCTORS
        |
        v
LARGE-SIEVE / ANALYTIC MEAN-VALUE INPUT
        |
        v
DYADIC OR SMOOTH DECOMPOSITION
        |
        v
SECOND-MOMENT ESTIMATE
        |
        +--> CLASSICAL UPPER BOUND
        |
        +--> MAIN-TERM ANALYSIS (SEPARATE DEFERRED GATE)
        v
FINAL BDH STATEMENT + Q-RANGE + EFFECTIVITY
```

## ما أُغلق

### 1. التطبيع

اعتمد نهائيًا:

\[
\psi(x;q,a)=\sum_{\substack{n\le x\\n\equiv a\pmod q}}\Lambda(n),
\qquad
E(x;q,a)=\psi(x;q,a)-\frac{x}{\varphi(q)},
\]

مع الجمع على الفئات المختزلة فقط. الشخصية الرئيسية لا تُسقط، وتصحيح الأوليات القاسمة لـ`q` يبقى ظاهرًا.

الحالة:

```text
REDUCED-RESIDUE-CLASSES = FINAL
MAIN-TERM               = x / phi(q)
PRINCIPAL-CHARACTER     = EXPLICITLY RETAINED
GATE-2 NORMALIZATION    = CLOSED / PASS
```

### 2. التحويل بالشخصيات

ثبتت داخليًا هوية بارسيفال الدقيقة:

\[
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2
=
\frac{1}{\varphi(q)}
\sum_{\chi\bmod q}
\left|\Psi^{\circ}(x,\chi)\right|^2,
\]

حيث

\[
\Psi^{\circ}(x,\chi)
=
\Psi(x,\chi)-\delta_{\chi=\chi_0}x.
\]

هذه هوية منتهية مستقلة عن أي تقدير تحليلي.

الحالة:

```text
CHARACTER-ORTHOGONALITY = PROVED-HERE
PARSEVAL-IDENTITY       = PROVED-HERE
PRINCIPAL-SEPARATION    = PROVED-HERE
GATE-3A TRANSFORM       = CLOSED / PASS
```

## الديون المفتوحة

### 3. رد الشخصيات غير البدائية

يجب اشتقاق صيغة دقيقة تقارن

\[
\Psi(x,\chi)
\]

بالشخصية البدائية المحفزة `\chi^*` ذات الموصل `r\mid q`، مع تسجيل كلفة العوامل الأولية عند `q/r` وعدم دفنها داخل رمز خطأ غير مضبوط.

المطلوب:

- هوية الرد إلى الموصل.
- حد موحد لتصحيح الأوليات القاسمة لـ`q` وغير القاسمة للموصل.
- عدّ عدد الشخصيات modulo `q` المحفزة من موصل ثابت.
- التحقق من أن الجمع الموزون بـ`1/\varphi(q)` لا يخلق خسارة أكبر من المسموح.

### 4. المدخل التحليلي المتوسط

لم يثبت بعد أن حزمة الغربال الكبير المستعملة في الفصل الثالث عشر تكفي وحدها لإنتاج رتبة

\[
V_\psi(x,Q)\ll xQ\log x.
\]

يجب تحديد أحد المسارين بوضوح:

1. استدعاء مبرهنة قيمة متوسطة مقتبسة بصياغة مطابقة تمامًا؛ أو
2. بناء البرهان داخل الفصل من الغربال الكبير مع تفكيك دالة فون مانغولت وضبط الحدود القطرية وغير القطرية.

يمنع استعمال نتيجة مكافئة لـBDH بوصفها مدخلًا، لأن ذلك سيكون استدلالًا دائريًا.

### 5. الصيغة الكلاسيكية النهائية

الصيغة المرشحة حاليًا هي

\[
V_\psi(x,Q)\ll_M xQ\log x
\]

في مجال من الشكل

\[
\frac{x}{(\log x)^M}\le Q\le x.
\]

لكن المجال واعتماد الثابت على `M` لا يزالان `PROVISIONAL` حتى فحص نص كامل للمصدر البرهاني المعتمد.

### 6. الفعالية

لا تنقل عدم الفعالية من فصل Bombieri--Vinogradov آليًا. يجب تحديد ما إذا كان مسار BDH المختار يستعمل:

- Siegel--Walfisz؛
- منطقة خالية من الأصفار؛
- تقديرًا فعالًا محضًا من الغربال الكبير؛
- أو مزيجًا منها.

ولا يثبت وصف الثابت النهائي قبل حسم هذا الاعتماد.

## طبقة الصيغة التقاربية

صيغة Montgomery--Hooley والحد الرئيسي الأدق خارج نتيجة الفصل الأساسية حاليًا.

```text
ASYMPTOTIC-MAIN-TERM = UNVERIFIED
ARITHMETIC-CONSTANT  = UNVERIFIED
ASYMPTOTIC-Q-RANGE   = UNVERIFIED
STATUS               = DEFERRED / SEPARATE RESULT FAMILY
```

لا تسجل هذه الطبقة في سجل النتائج قبل فحص Montgomery 1970، والفصل 18 من Montgomery 1971، والجزء المحدد من سلسلة Hooley الذي سيُستعمل.

## تصنيف المنشأ الحالي

| المكوّن | الحالة |
|---|---|
| تعامد الشخصيات | `PROVED-HERE` |
| تحويل التباين إلى متوسط شخصيات | `PROVED-HERE` |
| فصل الشخصية الرئيسية | `PROVED-HERE` |
| رد الشخصيات غير البدائية | `OPEN` |
| الغربال الكبير | `CITED / CHAPTER 13 CANDIDATE INPUT` |
| مبرهنة القيمة المتوسطة اللازمة | `UNCLASSIFIED / OPEN` |
| حد BDH العلوي | `UNPROVED / TARGET` |
| الصيغة التقاربية | `DEFERRED` |
| مجال `Q` النهائي | `PROVISIONAL` |
| الفعالية | `OPEN` |

## بوابات الإغلاق

```text
GATE-1 ORIGINAL-SOURCES          = PARTIAL / FULL-TEXT PINNING OPEN
GATE-2 NORMALIZATION             = CLOSED / PASS
GATE-3 CHARACTER-TRANSFORM       = CLOSED / PASS
GATE-3B IMPRIMITIVE-REDUCTION    = OPEN
GATE-4 MEAN-VALUE-INPUT          = OPEN
GATE-5 CLASSICAL-UPPER-BOUND     = OPEN
GATE-5B ASYMPTOTIC-MAIN-TERM     = DEFERRED
GATE-6 RANGE-AND-EFFECTIVITY     = OPEN
PASS-FOR-AUTHORING               = NO
```

## الإجراء التالي

الإجراء العلمي التالي هو إغلاق رد الشخصيات غير البدائية إلى الموصلات، ثم مطابقة الناتج مع مدخل متوسط غير دائري. لا يبدأ متن LaTeX قبل اكتمال ذلك وتثبيت صيغة الحد العلوي ومجال `Q` من مصدر كامل.