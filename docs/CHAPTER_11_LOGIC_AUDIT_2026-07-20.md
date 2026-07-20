# التدقيق المنطقي الشامل للفصل الحادي عشر

## بيانات التدقيق

```text
DATE                 = 2026-07-20
CHAPTER              = 11 — المناطق الخالية والأصفار الاستثنائية
VERSION              = 0.15.0-dev
SCOPE                = PRE-AUTHORING LOGIC / REFERENCES / CIRCULARITY
AUDIT-VERDICT        = PASS
BLOCKING-CORRECTIONS = NONE
PRE-AUTHORING-GATE   = MAY-CLOSE
```

## 1. المواد المدققة

- `research/literature-reviews/chapter-11-zero-free-regions-exceptional-zeros-evidence.md`
- `research/literature-reviews/chapter-11-zero-free-regions-exceptional-zeros-proof-map.md`
- `docs/CHAPTER_11_REFERENCE_VERIFICATION_2026-07-20.md`
- `docs/CHAPTER_11_LOG_DERIVATIVE_SIGN_AUDIT_2026-07-20.md`
- `docs/CHAPTER_11_QUANTITATIVE_INEQUALITY_AUDIT_2026-07-20.md`
- `docs/CHAPTER_11_UNIFORM_REMAINDER_AUDIT_2026-07-20.md`
- `docs/CHAPTER_11_STANDARD_ZERO_FREE_REGION_LOGIC_AUDIT_2026-07-20.md`
- `docs/CHAPTER_11_LANDAU_PAGE_LOGIC_AUDIT_2026-07-20.md`
- `docs/CHAPTER_11_SIEGEL_INEFFECTIVITY_AUDIT_2026-07-20.md`
- `docs/CHAPTER_11_DEURING_HEILBRONN_VERIFICATION_2026-07-20.md`

## 2. الحكم على النتائج المحجوزة

| المعرّف | النتيجة | الحكم المنطقي | المنشأ المقرر عند التأليف |
|---|---|---|---|
| `ANT-PROP-11-01` | الرد إلى الجد البدائي وضبط العوامل المحلية | `PASS` | `PROVED-HERE` |
| `ANT-LEM-11-01` | صيغة المشتقة اللوغاريتمية بمجموع الأصفار وغاما | `PASS` | `PROVED-HERE` مع هادامار العام `CITED` |
| `ANT-THM-11-01` | المنطقة القياسية الفردية والاستثناء الحقيقي البسيط الوحيد داخل الدالة | `PASS` | `PROVED-HERE` |
| `ANT-THM-11-02` | مبرهنة Landau--Page النوعية | `PASS` | `PROVED-HERE` |
| `ANT-THM-11-03` | مبرهنة Siegel | `PASS-FOR-CITATION` | `CITED / INEFFECTIVE` |
| `ANT-COR-11-01` | الإبعاد غير الفعال للصفر الاستثنائي | `PASS` | `PROVED-HERE` اعتمادًا على `ANT-THM-11-03` |
| `ANT-THM-11-04` | ظاهرة Deuring--Heilbronn النوعية | `PASS-FOR-CITATION` | `CITED` |
| `ANT-PROP-11-02` | الأثر في الصيغة الصريحة لـ\(\psi(x,\chi)\) | `NONBLOCKING-DEFERRED` | `DIAGNOSTIC / DEFERRED` |

لا تُرفع الحالات في سجل النتائج فعليًا قبل كتابة النص واجتياز تدقيق ما بعد التأليف.

## 3. المنطقة القياسية الفردية

أُغلق المسار التالي:

1. الدالة المكتملة والمعادلة الوظيفية من الفصل السابع.
2. هادامار العام والنمو من الرتبة الأولى بوصفهما مدخلين قياسيين مقتبسين.
3. اشتقاق صيغة المشتقة اللوغاريتمية:
   \[
   -\Re\frac{L'}{L}(s,\chi)
   =
   \frac12\log\frac q\pi
   +\frac12\Re\frac{\Gamma'}{\Gamma}
   \!\left(\frac{s+a_\chi}{2}\right)
   -\sum_\rho^*\Re\frac1{s-\rho}.
   \]
4. ضبط غاما والموصل والعوامل المحلية بحد
   \(O(\log(q(|t|+2)))\).
5. استعمال المتراجحة الموزونة ذات المعاملات \(3,4,1\).
6. فصل الشخصية غير الحقيقية عن الشخصية الحقيقية.
7. في الحالة الحقيقية غير الواقعية: الاحتفاظ بقطب \(\chi^2\) والصفر المرافق معًا.
8. إثبات أن الاستثناء الممكن حقيقي وبسيط ووحيد داخل الدالة.

الصيغة المعتمدة عند التأليف:

\[
\Re(s)>
1-
\frac{c_0}{\log(q(|\Im(s)|+2))},
\]

لثابت مطلق موجب غير محسن.

```text
STANDARD-ZERO-FREE-REGION = PASS
BEST-EXPLICIT-CONSTANT    = OUT-OF-SCOPE
```

## 4. الفصل بين طبقات الفرادة

ثبتت ثلاث عبارات مختلفة ولا يجوز دمجها:

1. **داخل دالة بدائية واحدة:** الصفر الحقيقي الممكن واحد وبسيط.
2. **عند ترديد ثابت:** حاصل ضرب جميع دوال الشخصيات يملك على الأكثر صفرًا استثنائيًا واحدًا في المنطقة الصريحة المناسبة.
3. **عبر الموصلات حتى \(Q\):** مبرهنة Landau--Page تمنح على الأكثر جدًا بدائيًا استثنائيًا واحدًا.

```text
UNIQUENESS-SEMANTICS = PASS
```

## 5. مبرهنة Landau--Page

أُغلق البرهان النوعي باستعمال

\[
F(s)=
\zeta(s)L(s,\chi_1)L(s,\chi_2)L(s,\chi_1\chi_2).
\]

النقاط المدققة:

- شخصية حاصل الضرب غير رئيسية إذا كانت الشخصيتان البدائيتان متميزتين.
- تُبقى شخصية حاصل الضرب غير البدائية في تعريف \(F\) للمحافظة على
  \[
  (1+\chi_1(n))(1+\chi_2(n))\ge0.
  \]
- يجري الرد إلى الجد البدائي فقط عند تقدير المشتقة.
- موصل الجد لا يتجاوز \(Q^2\)، فتظل الكلفة \(O(\log Q)\).
- صفران قريبان ينتجان تناقضًا مع القطب الوحيد لزيتا.

```text
LANDAU-PAGE = PASS
```

## 6. مبرهنة Siegel وعدم الفعالية

اعتمدت الصيغة المقتبسة:

\[
|L(1,\chi)|\gg_\varepsilon q^{-\varepsilon}
\]

للشخصية الحقيقية البدائية غير الرئيسية، مع ثابت غير فعال.

وأُثبت داخل حزمة التدقيق:

\[
|L'(\sigma,\chi)|\ll\log^2(2q)
\]

قرب الواحد باستعمال دورية الشخصية والجمع الجزئي فقط. ومن ثم إذا كان \(\beta\) صفرًا استثنائيًا:

\[
1-\beta\gg_\varepsilon q^{-\varepsilon},
\]

بثابت غير فعال.

```text
SIEGEL-CITATION       = PASS
INEFFECTIVITY-LABEL   = PASS
DERIVED-ZERO-BOUND    = PASS
```

## 7. Deuring--Heilbronn

اعتمدت صيغة نوعية مقتبسة ثابتة الترديد:

إذا كان

\[
\lambda_1=(1-\beta_1)\log(q(T+2))
\]

صغيرًا بما يكفي، فإن كل صفر آخر \(\rho=\beta+i\gamma\)، \(|\gamma|\le T\)، يحقق حدًا من الشكل

\[
1-\beta
\gg
\frac1{\log(q(T+2))}
\log\frac1{\lambda_1}.
\]

تُذكر في المتن بصيغة ثوابت وجودية أو بإحالة مباشرة إلى النسخة الصريحة، من دون نسخ الثوابت المحسنة ما لم تخضع لتدقيق عددي مستقل.

النسخة الفعالة والنسخة غير الفعالة مفصولتان بوضوح.

```text
DEURING-HEILBRONN = PASS-FOR-CITATION
FULL-PROOF         = DEFERRED
```

## 8. عدم الدور

لم تستعمل براهين النتائج الداخلية:

- Siegel--Walfisz.
- Bombieri--Vinogradov.
- Linnik.
- حد خطأ موحد لـPNT-AP.
- Deuring--Heilbronn لإثبات المنطقة القياسية.
- مبرهنة Siegel لإثبات Landau--Page.
- GRH.

ترتيب الاعتماد هو:

```text
Chapter 7 structure
  -> logarithmic derivative
  -> standard individual zero-free region
  -> Landau--Page
  -> Siegel citation and ineffective corollary
  -> Deuring--Heilbronn citation
  -> later quantitative prime-distribution chapters
```

```text
CIRCULARITY = PASS
```

## 9. سلامة الإشارات والحالات الخاصة

- مساهمة الصفر في \(-\Re L'/L\) سالبة.
- قطب الشخصية الرئيسية موجب في الحد العلوي.
- إذا كانت \(\chi\) غير حقيقية، فـ\(\chi^2\) غير رئيسية.
- إذا كانت \(\chi\) حقيقية وصفرها غير حقيقي، فالصفر المرافق وقطب \(\chi^2\) ضروريان معًا.
- عند \(t=0\)، تسمح المتراجحة بصفر حقيقي بسيط واحد فقط.
- العوامل المحلية لا تخلق أصفارًا في \(\Re(s)>0\).

```text
SIGN-AUDIT = PASS
EDGE-CASES = PASS
```

## 10. الحدود التحريرية الملزمة

يجب أن يصرح المتن بما يأتي:

- الثابت في المنطقة القياسية غير محسن، لكنه فعال من حيث المبدأ.
- ثابت Siegel غير فعال.
- Deuring--Heilbronn مقتبسة، وبرهانها الكامل مؤجل.
- لا Siegel--Walfisz ولا Bombieri--Vinogradov ولا Linnik في هذا الفصل.
- لا GRH.
- النتائج العددية الحديثة تُعرض تاريخيًا ولا تستبدل النواة النوعية.

## 11. الديون غير الحاجزة

- رقم الصفحة المباشر لصيغة هادامار/الكسور الجزئية في نسخة محلية من الكتب القياسية.
- الثوابت الصريحة الأفضل لـMcCurley وKadiri وBenli--Goel--Twiss--Zaman.
- بيان Tatuzawa الدقيق.
- الصيغة الصريحة الكاملة لـ\(\psi(x,\chi)\).
- التطبيقات إلى Linnik وSiegel--Walfisz.

هذه الديون لا تمنع تأليف النواة المحددة أعلاه، لكنها تمنع ادعاء `RELEASE-READY`.

## 12. الحكم النهائي

```text
EVIDENCE-FIRST       = PASS
REFERENCE-COVERAGE   = PASS-FOR-ADOPTED-SCOPE
LOGIC                = PASS
SIGNS                 = PASS
CIRCULARITY           = PASS
EFFECTIVITY-LABELS    = PASS
BLOCKING-CORRECTIONS  = NONE
PRE-AUTHORING-GATE    = CLOSE-AUTHORIZED
AUTHORING             = AUTHORIZED
```

## 13. الإجراء التالي

1. إغلاق حالة تدقيق ما قبل التأليف رسميًا.
2. إنشاء ملف الفصل الحادي عشر وربطه بالكتاب.
3. كتابة النواة وفق ترتيب الاعتماد المدقق.
4. إبقاء نتائج سجل المشروع `DRAFT` حتى تدقيق ما بعد التأليف والبناء.