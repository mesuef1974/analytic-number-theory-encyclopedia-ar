# الفصل الثامن عشر — تجميد التطبيع وصياغات النتائج

التاريخ: 2026-07-25

## الحالة

```text
CHAPTER                = 18
VERSION                = 0.22.0-dev
NORMALIZATION          = FROZEN
THEOREM-STATEMENTS     = FROZEN-AS-AUTHORING-CANDIDATES
CITABILITY             = DRAFT / NON-CITABLE
AUTHORING               = BLOCKED
```

## 1. التطبيع المعتمد

نعتمد طوال الفصل

```text
e(t) = exp(2 pi i t)
||x|| = distance from x to the nearest integer
S(f;I) = sum_{n in I cap Z} e(f(n))
Delta_h f(x) = f(x+h)-f(x)
```

وعند استعمال مجال ديادي نكتب

```text
S(f;N) = sum_{N<n<=2N} e(f(n)).
```

لا يجوز الانتقال بين المجال العام والمجال الديادي داخل المبرهنة الواحدة بلا تصريح.

## 2. ANT-ID-18-01 — الحد التافه

لكل متتالية عقدية منتهية `(a_n)` ولكل طور حقيقي `f(n)`:

```text
|sum_n a_n e(f(n))| <= sum_n |a_n|.
```

```text
CLASSIFICATION = IDENTITY / PROVED-HERE
```

## 3. ANT-LEM-18-01 — الجمع الجزئي المنفصل

إذا كان

```text
A(x)=sum_{m<n<=x} a_n,
```

وكان `g` من الصنف `C^1` على `[m,M]`، فإن

```text
sum_{m<n<=M} a_n g(n)
= A(M)g(M) - integral_m^M A(t) g'(t) dt.
```

وتُصاغ النسخة ذات النهايتين بحسب اصطلاح المجال المستخدم.

```text
CLASSIFICATION = PROVED-HERE
```

## 4. ANT-LEM-18-02 — متباينة فرق فان دير كوربوت

لأعداد عقدية `z_1,...,z_N` ولمعلم صحيح `1<=H<=N` نعتمد الصيغة:

```text
|sum_{n=1}^N z_n|^2
<= (N+H-1)/H *
   (sum_{n=1}^N |z_n|^2
    + 2 sum_{h=1}^{H-1} (1-h/H)
        |sum_{n=1}^{N-h} z_{n+h} conjugate(z_n)|).
```

هذه الصيغة هي صيغة التأليف المرشحة؛ يجب أن يثبت البرهان الداخلي الحدود الطرفية بدقة، ويُختبر على `z_n=1`.

عند `z_n=e(f(n))` تصبح حدود الارتباط

```text
sum_{n=1}^{N-h} e(Delta_h f(n)).
```

```text
CLASSIFICATION = PROVED-HERE
```

## 5. ANT-THM-18-01 — اختبار المشتقة الأولى

لتكن `f in C^1([a,b])`، ولتكن `f'` رتيبة على `[a,b]`. إذا وجد `lambda` بحيث

```text
0 < lambda <= 1/2
```

و

```text
||f'(x)|| >= lambda
```

لكل `x in [a,b]`، فإن

```text
sum_{a<n<=b} e(f(n)) << lambda^(-1),
```

بثابت مطلق.

الملاحظة الحاكمة: الشرط هو البعد عن الأعداد الصحيحة، لا مجرد `|f'(x)|>=lambda`.

```text
CLASSIFICATION = PROVED-HERE
```

يجب أن يُبنى البرهان من المجموع الهندسي الخطي ثم مبدأ كوسمين/التجزئة الرتيبة، من دون الاستناد إلى اختبار المشتقة الثانية.

## 6. ANT-THM-18-02 — اختبار المشتقة الثانية

لتكن `f in C^2([a,b])`، وليكن `L=b-a`. نفترض أن `f''` لا تغير الإشارة وأنه توجد ثوابت `lambda>0` و`C>=1` بحيث

```text
lambda <= |f''(x)| <= C lambda
```

على `[a,b]`. عندئذ

```text
sum_{a<n<=b} e(f(n)) <<_C L lambda^(1/2) + lambda^(-1/2).
```

```text
CLASSIFICATION = CITED / EXPLAINED
```

سبب عدم رفعها الآن إلى `PROVED-HERE`: البرهان الكامل يحتاج تفصيلًا أطول في تقسيم مناطق اقتراب `f'` من الأعداد الصحيحة وتتبع الثوابت. يمكن إدراج مخطط برهان واضح، لكن التصنيف يبقى مقتبسًا ما لم يكتب برهان كامل مستقل لاحقًا.

## 7. ANT-DEF-18-01 — إطار الزوج الأسي

لا نعتمد تعريفًا عامًا مطلقًا. يُعرض الزوج الأسي فقط داخل فئة الأطوار القياسية التي يحددها المرجع المتخصص، مع طول مجال `N` ومعلمة اشتقاق `Y` وشروط منتظمة على المشتقات.

```text
CLASSIFICATION = DEFINITION / CITED-FRAMEWORK
```

الزوج الابتدائي `(0,1)` يعرض مثالًا تافهًا فقط.

## 8. ANT-PROP-18-01 — عملية A

تُشرح عملية `A` بوصفها تطبيقًا منهجيًا لمتباينة فرق فان دير كوربوت على فئة الأطوار المجمدة. يمكن إثبات نسخة محدودة داخل الفصل، لكن تحويل الأزواج العام لا ينسب إلى الفصل ما لم تُثبت جميع فروض الفئة.

```text
CLASSIFICATION = PROVED-HERE FOR LIMITED FORM / CITED FOR GENERAL PAIR TRANSFORM
```

## 9. ANT-PROP-18-02 — عملية B

تعرض عملية `B` بوصفها تحويلًا ثنائيًا يعتمد على بواسون/الطور الساكن أحادي البعد وعلى نقاط تحقق `f'(x)=m`، مع عامل سعة من رتبة `|f''(x)|^{-1/2}`.

```text
CLASSIFICATION = CITED / EXPLAINED
```

لا يجوز اشتقاقها من فرق فان دير كوربوت وحده.

## 10. الحدود النهائية للنطاق

```text
HIGHER-DERIVATIVE-TESTS      = DEFERRED
FULL-EXPONENT-PAIR-THEORY    = CITED / EXPLAINED
BEST-KNOWN-EXPONENT-PAIRS    = OUT OF SCOPE
TWO-DIMENSIONAL-SUMS         = DEFERRED
CHAPTER-17-MINOR-ARC-PACKAGE = NOT REPROVED
```

## 11. العوائق المتبقية

1. تدقيق مستقل لصيغة فرق فان دير كوربوت وحدودها الطرفية.
2. تدقيق مستقل لبرهان اختبار المشتقة الأولى.
3. تدقيق عدم الدور مع الفصل 17.
4. حجز معرفات النتائج في سجل مستقل.
5. قرار صريح بشأن `PASS-FOR-AUTHORING`.
