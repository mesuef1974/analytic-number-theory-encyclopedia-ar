# خريطة برهان الفصل الرابع عشر — Barban--Davenport--Halberstam

التاريخ: 2026-07-21

```text
STATUS             = INITIAL / UNVERIFIED
PRE-AUTHORING-GATE = OPEN
AUTHORING           = BLOCKED
```

## الهدف

بناء مسار برهاني دقيق لكمية التباين

\[
V(x,Q)=
\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2,
\]

مع الفصل بين ثلاثة أهداف محتملة لا يجوز خلطها:

1. حد علوي من رتبة صحيحة في مجال مناسب لـ`Q`.
2. صيغة تقاربية ذات حد رئيسي.
3. نسخة مدمجة أو ملساء تختلف في التطبيع أو مجال المتغيرات.

## سلسلة الاعتماد المرشحة

```text
ORTHOGONALITY OF CHARACTERS
        |
        v
RESIDUE-CLASS VARIANCE <-> CHARACTER SECOND MOMENT
        |
        +--> PRINCIPAL CHARACTER / PRIME-POWER CORRECTIONS
        |
        v
LARGE-SIEVE OR MEAN-VALUE INPUT
        |
        v
DYADIC / SMOOTH DECOMPOSITION
        |
        v
SECOND-MOMENT ESTIMATE
        |
        +--> UPPER-BOUND FORM
        |
        +--> MAIN-TERM ANALYSIS (SEPARATE GATE)
        v
BDH STATEMENT + RANGE OF Q + ERROR TERM
```

## ديون البرهان المفتوحة

### 1. التطبيع

- تثبيت تعريف `psi(x;q,a)` المستخدم.
- تثبيت جمع الفئات المختزلة.
- ضبط مساهمة الشخصية الرئيسية بدقة.
- تحديد أثر `q=1` ونقاط النهاية.

### 2. التحويل بالشخصيات

- إعادة اشتقاق هوية التعامد التي تحول التباين إلى متوسط تربيعي على الشخصيات.
- التمييز بين جميع الشخصيات والبدائية.
- تسجيل كلفة رد الموصلات، إن استُخدم.

### 3. المدخل المتوسط

- تحديد هل تكفي حزمة الغربال الكبير من الفصل الثالث عشر.
- تحديد الحاجة إلى صيغة أقوى أو تفكيك إضافي.
- منع الاستدلال الدائري من BDH إلى مدخل مكافئ لها.

### 4. الحد الرئيسي

- لا يُذكر حد رئيسي قبل اشتقاقه من المصدر وفحص ثابته.
- يجب فصل الصيغة التقاربية عن الحد العلوي في سجل النتائج.
- يجب تثبيت مجال `Q` الذي يهيمن فيه الحد الرئيسي على الخطأ.

### 5. الفعالية

- فحص ما إذا كان المسار يحتاج Siegel--Walfisz.
- تحديد أثر ذلك في فعالية الثابت النهائي.
- عدم نقل عدم الفعالية من الفصل الثالث عشر آليًا دون تحقق.

## تصنيف المنشأ المتوقع

| المكوّن | الحالة الأولية |
|---|---|
| تعامد الشخصيات | `PROVED-HERE / EXPECTED` |
| تحويل التباين إلى متوسط شخصيات | `PROVED-HERE / EXPECTED` |
| مدخل الغربال الكبير | `CITED / FROM CHAPTER 13` |
| صيغة BDH النهائية | `UNCLASSIFIED` |
| الحد الرئيسي وثابته | `UNVERIFIED` |
| مجال `Q` | `UNVERIFIED` |

## بوابات الإغلاق

```text
GATE-1 ORIGINAL-SOURCES      = OPEN
GATE-2 NORMALIZATION         = OPEN
GATE-3 CHARACTER-REDUCTION   = OPEN
GATE-4 MEAN-VALUE-INPUT      = OPEN
GATE-5 MAIN-TERM             = OPEN
GATE-6 RANGE-AND-EFFECTIVITY = OPEN
```

لا يتحول هذا الملف إلى خريطة برهان معتمدة إلا بعد إغلاق البوابات الست وتسجيل تدقيق مستقل لما قبل التأليف.
