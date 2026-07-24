# بوابة ما قبل التأليف — الفصل السابع عشر

التاريخ: 2026-07-25

```text
CHAPTER                    = 17
VERSION                    = 0.21.0-dev
TOPIC                      = CIRCLE METHOD / GOLDBACH / WARING
ISSUE                      = #32 / OPEN
BRANCH                     = agent/chapter-17-circle-method-goldbach-waring-v0.21.0
EVIDENCE-LEDGER            = UPDATED
PROOF-MAP                  = INITIALIZED
PRIMARY-SOURCE-AUDIT       = PASS
NONCIRCULARITY-AUDIT       = PASS
RESULT-IDS                 = 7 / PROVISIONALLY RESERVED
REFERENCE-BLOCKERS         = 0
SCOPE-BLOCKERS             = 0
TECHNICAL-BLOCKERS         = 0
PRE-AUTHORING-GATE         = OPEN / FINAL AUDIT PENDING
PASS-FOR-AUTHORING         = NO
AUTHORING                  = BLOCKED
MANUSCRIPT-LINK            = PROHIBITED
MERGE                      = NOT AUTHORIZED
RELEASE-READY              = NO
```

## 1. النطاق المعتمد

1. التعامد الفورييري وصيغة تكامل عدد التمثيلات.
2. الأقواس الكبرى والأقواس الصغرى.
3. التقريب المحلي، السلسلة المفردة، والتكامل المفرد.
4. الصيغة التقاربية الكلاسيكية في وارينغ بحالة `CITED / EXPLAINED`.
5. مبرهنة فينوغرادوف للأعداد الفردية الكبيرة بحالة `CITED`.
6. مبرهنة هلفغوت لكل عدد فردي أكبر من 5 بحالة `CITED`، مع فصل المكوّن الحاسوبي بوصفه `FINITE-VERIFIED`.
7. غولدباخ الثنائية بحالة `HYPOTHESIS / OPEN`.
8. إبقاء النظرية العامة للمجاميع الأسية وفان دير كوربوت للفصل الثامن عشر.

## 2. القرارات المغلقة

```text
WARING-TARGET            = CLASSICAL ASYMPTOTIC FORMULA / FROZEN
MINOR-ARC-INPUTS         = SOURCE-VERIFIED / CITED COMPOSITE INPUT
VINOGRADOV-ATTRIBUTION   = SOURCE-VERIFIED
HELFGOTT-SCOPE           = INCLUDE AS CITED MODERN COMPLETION
NORMALIZATION            = FROZEN
```

مرجع فينوغرادوف المعتمد:

I. M. Vinogradov, *Representation of an odd number as the sum of three primes*,
*Doklady Akademii Nauk SSSR* 15 (1937), 129--132.

مرجع وارينغ المؤسس:

G. H. Hardy and J. E. Littlewood, *Some problems of Partitio Numerorum IV: The singular series in Waring's Problem and the value of G(k)*,
*Mathematische Zeitschrift* 12 (1922), 161--188, DOI `10.1007/BF01482074`.

المسار التقني المفسر للأقواس ومسألة وارينغ:

R. C. Vaughan, *The Hardy--Littlewood Method*, 2nd ed., Cambridge University Press, 1997.

## 3. التطبيع المجمد

\[
e(t)=e^{2\pi i t},
\qquad
f_k(\alpha;P)=\sum_{1\le x\le P}e(\alpha x^k),
\qquad
P=N^{1/k}.
\]

\[
r_{s,k}(N)=\int_0^1 f_k(\alpha;P)^s e(-N\alpha)\,d\alpha.
\]

تُبنى الأقواس الكبرى حول الكسور المختزلة `a/q` وفق

\[
1\le q\le Q,
\qquad
\left|\alpha-\frac aq\right|\le \frac{Q}{qN},
\]

والأقواس الصغرى هي المتممة في `[0,1)`.

الرموز الحاكمة:

\[
\mathfrak S_{s,k}(N)
\quad\text{و}\quad
\mathfrak J_{s,k}(N).
\]

## 4. مدخل الأقواس الصغرى

يُقتبس، لمسار وارينغ فقط، وجود `\delta=\delta(k,s)>0` عندما يكون `s` كبيرًا بما يكفي بدلالة `k` بحيث

\[
\int_{\mathfrak m}|f_k(\alpha;P)|^s\,d\alpha
\ll P^{s-k-\delta}.
\]

هذه نتيجة `CITED / COMPOSITE INPUT`، ولا تُقدّم بوصفها برهانًا داخليًا أو أفضل حد حديث.

## 5. اختبارات الإغلاق

- [x] `WARING-TARGET = FROZEN`.
- [x] `MINOR-ARC-INPUTS = SOURCE-VERIFIED`.
- [x] `VINOGRADOV-ATTRIBUTION = SOURCE-VERIFIED`.
- [x] `HELFGOTT-SCOPE = DECIDED`.
- [x] `NORMALIZATION = FROZEN`.
- [x] كل نتيجة مرتبطة بتصنيف حاكم واضح.
- [x] لا اعتماد على فصل لاحق بوصفه نتيجة داخلية.
- [x] لا عائق مرجعي أو منطقي مفتوح.
- [ ] صدور تدقيق مستقل للبوابة بحكم `PASS`.
- [ ] إصدار وثيقة مستقلة لـ`PASS-FOR-AUTHORING`.

## 6. الحكم الحالي

```text
RESEARCH-INTAKE       = COMPLETE
SOURCE-MINING         = COMPLETE FOR FROZEN SCOPE
PROOF-DESIGN          = READY FOR AUDIT
RESULT-RESERVATION    = NON-CITABLE
AUTHORING             = BLOCKED PENDING INDEPENDENT GATE AUDIT
CHAPTER-TEX           = DO NOT CREATE
MANUSCRIPT-MAIN       = DO NOT EDIT
```

حزمة الإغلاق التقنية موجودة في:

`docs/CHAPTER_17_SOURCE_NORMALIZATION_AND_MINOR_ARC_CLOSURE_2026-07-25.md`.

هذه الوثيقة لا تمنح وحدها إذن التأليف؛ يلزم تدقيق مستقل وإيصال إغلاق منفصل.