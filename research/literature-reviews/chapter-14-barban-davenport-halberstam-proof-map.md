# خريطة برهان الفصل الرابع عشر — Barban--Davenport--Halberstam

التاريخ: 2026-07-24

```text
STATUS             = PARTIALLY-VERIFIED / ROUTE-SELECTED
PRE-AUTHORING-GATE = OPEN
AUTHORING           = BLOCKED
```

## الهدف

بناء مسار برهاني دقيق لكمية التباين

\[
V_\psi(x,Q)=
\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2,
\]

مع الفصل بين الحد العلوي الكلاسيكي، والصيغة التقاربية ذات الحد الرئيسي، والنسخ الملساء أو القصيرة.

## سلسلة الاعتماد المعتمدة

```text
ORTHOGONALITY OF CHARACTERS
        |
        v
RESIDUE-CLASS VARIANCE <-> CHARACTER SECOND MOMENT
        |
        +--> PRINCIPAL CHARACTER / PRIME-DIVISOR CORRECTIONS
        |
        v
IMPRIMITIVE CHARACTER -> PRIMITIVE CONDUCTOR REDUCTION
        |
        +--> LOCAL CORRECTION = CONTROLLED
        +--> W_Q(r) = sum_{m<=Q/r} 1/phi(rm)
        |
        v
BARBAN GENERAL MEAN-SQUARE THEOREM
        |
        +--> LARGE SIEVE AS AN INTERNAL TOOL
        +--> DIAGONAL / OFF-DIAGONAL DECOMPOSITION
        +--> SPECIALIZATION TO VON MANGOLDT COEFFICIENTS
        |
        v
CLASSICAL BDH UPPER BOUND
        |
        +--> RANGE OF Q
        +--> EFFECTIVITY
        v
SEPARATE ASYMPTOTIC LAYER (MONTGOMERY--HOOLEY / DEFERRED)
```

## ما ثبت داخليًا

### التطبيع والتحويل بالشخصيات

\[
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}|\Psi^\circ(x,\chi)|^2.
\]

```text
GATE-2 NORMALIZATION       = CLOSED / PASS
GATE-3 CHARACTER-TRANSFORM = CLOSED / PASS
```

### الشخصية الرئيسية

\[
\Psi(x,\chi_0)-x
=
\psi(x)-x-
\sum_{\substack{p^k\le x\\p\mid q}}\log p.
\]

### رد الشخصيات غير البدائية

إذا كانت `chi mod q` مستحثة من `chi* mod r`، حيث `r|q`، فثبت

\[
\Psi^\circ(x,\chi)
=
\Psi^\circ(x,\chi^*)-C(x;q,r,\chi^*),
\qquad
|C(x;q,r,\chi^*)|\le \omega(q/r)\log x.
\]

وكلفة التصحيحات المجمعة من رتبة

\[
O\!\left(Q(\log Q)^2(\log x)^2\right).
\]

```text
GATE-4 IMPRIMITIVE-REDUCTION = CLOSED / PASS
```

## تدقيق مدخل القيمة المتوسطة

### ما لا يكفي

1. مبرهنة القيمة المتوسطة في الفصل الثالث عشر من الرتبة الأولى لـ`|psi(y,chi)|`، وليست متوسطًا تربيعيًا.
2. تطبيق الغربال الكبير مباشرة مع `c_n=Lambda(n)` يعطي

\[
(x+R^2)x\log x,
\]

وهو أكبر من رتبة `xR log x` المطلوبة.
3. لا يجوز استنتاج BDH عكسيًا من Bombieri--Vinogradov دون خسارة حادة.

### المسار المختار

اعتمدت مبرهنة باربان العامة للقيمة المتوسطة التربيعية، أو برهان مكافئ لها، بوصفها العقدة التحليلية المركزية التي يجب تدخيلها من المصدر الكامل.

المصدر التعليمي الحاكم المرشح:

- H. L. Montgomery, *Topics in Multiplicative Number Theory*, LNM 227 (1971)، الفصل «The mean value theorem of Barban»، الصفحات 145--154.

مصادر المقارنة:

- R. C. Vaughan, “Mean Value Theorems in Prime Number Theory”, JLMS (2) 10 (1975), 153--162.
- P. X. Gallagher, “Bombieri's mean value theorem”, Mathematika 15 (1968), 1--6.

```text
GATE-5 MEAN-VALUE-ROUTE   = CLOSED / ROUTE-SELECTED
GATE-6 MEAN-VALUE-THEOREM = OPEN / FULL-PROOF-PENDING
NON-CIRCULARITY            = PASS AT ROUTE LEVEL
```

## تصنيف المنشأ الحالي

| المكوّن | الحالة |
|---|---|
| تعامد الشخصيات | `PROVED-HERE` |
| تحويل التباين | `PROVED-HERE` |
| فصل الشخصية الرئيسية | `PROVED-HERE` |
| رد الموصلات | `PROVED-HERE` |
| الغربال الكبير | `CITED / FROM CHAPTER 13` |
| مبرهنة باربان العامة | `TARGET / SOURCE-PINNING-PARTIAL` |
| تطبيقها على `Lambda` | `OPEN` |
| حد BDH النهائي | `OPEN` |
| صيغة Montgomery--Hooley | `DEFERRED` |

## البوابات

```text
GATE-1 ORIGINAL-SOURCES        = PARTIAL / FULL-TEXT-PENDING
GATE-2 NORMALIZATION           = CLOSED / PASS
GATE-3 CHARACTER-TRANSFORM     = CLOSED / PASS
GATE-4 IMPRIMITIVE-REDUCTION   = CLOSED / PASS
GATE-5 MEAN-VALUE-ROUTE        = CLOSED / ROUTE-SELECTED
GATE-6 MEAN-VALUE-THEOREM      = OPEN
GATE-7 CLASSICAL-UPPER-BOUND   = OPEN
GATE-8 RANGE-AND-EFFECTIVITY   = OPEN
GATE-9 INDEPENDENT-PRE-AUDIT   = OPEN
```

## الخطوة التالية

1. استخراج الصيغة العامة الدقيقة لمبرهنة باربان وشروطها.
2. تدخيل البرهان أو اعتمادها كمدخل مقتبس بموضع دقيق.
3. تطبيقها على معاملات فون مانغولت وضبط الحد القطري والوزن `W_Q(r)`.
4. تثبيت مجال `Q` والفعالية.
5. إجراء تدقيق مستقل قبل السماح بالتأليف.

```text
PASS-FOR-AUTHORING = NO
```
