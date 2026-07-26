# خريطة برهان الفصل الثالث والعشرين

```text
PROOF-MAP   = REVIEW-CORRECTED / SECOND-NARROW-REVIEW-PENDING
CIRCULARITY = CLOSED
AUTHORING   = BLOCKED
```

## المدخلات السابقة

- الفصل 6: المعادلة الوظيفية، الأصفار غير البديهية، ودالة \(\xi\)، ويتضمن `ANT-THM-06-06` لصيغة ريمان--فون مانغولت.
- الفصل 9: الصيغ الصريحة وعلاقة الأصفار بتوزيع الأوليات.
- الفصل 21: لغة عائلات دوال \(L\) والموصل التحليلي.
- الفصل 22: فصل مفاهيمي بين إحصاء القيم وإحصاء الأصفار؛ لا تستورد منه نتيجة برهانية.

## النتائج ومساراتها

### P23.1 — `ANT-DEF-23-01`: عد الأصفار والتطبيع المحلي

يعاد عرض تعريف \(N(T)\) مع العد بالتعدد، وتحيل الصيغة مباشرة إلى `ANT-THM-06-06`:
\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T).
\]
يشتق الفصل 23 الكثافة المتوسطة ومتوسط التباعد المحلي من الحد الرئيس فقط. مصدر الحقيقة الداخلي الوحيد للصيغة هو الفصل 6.

التصنيف: `DEFINITION / INTERNAL-CROSS-REFERENCE`.

### P23.2 — `ANT-DEF-23-02`: الارتباط الثنائي

تعريف دالة Montgomery الموزونة وصيغة دالة الاختبار للأزواج غير القطرية بعد التطبيع المحلي.

التصنيف: `DEFINITION`.

### P23.3 — `ANT-THM-23-01`: مبرهنة Montgomery

تحت RH، وباتفاقية فورييه المثبتة، يعرض الجزء المثبت عندما
\[
\operatorname{supp}\widehat f\subset(-1,1),
\]
مع الصيغة الموزونة في مجال \(0\le\alpha<1\):
\[
F(\alpha,T)=T^{-2\alpha}(\log T+O(1))+\alpha+o(1).
\]

التصنيف: `CITED-CORE / CONDITIONAL-ON-RH`.

### P23.4 — `ANT-CONJ-23-01`: حدسية الارتباط الثنائي الكاملة

\[
R_2(u)=1-\left(\frac{\sin\pi u}{\pi u}\right)^2.
\]

التصنيف: `CONJECTURAL-GUE`.

### P23.5 — `ANT-THM-23-02`: حد GUE المحلي

في نموذج المصفوفات الهرميتية الوحدوية:
\[
K(u)=\frac{\sin\pi u}{\pi u},
\qquad
R_2(u)=1-K(u)^2.
\]

التصنيف: `RANDOM-MATRIX-THEOREM / CITED-CORE`، وليس مبرهنة عن أصفار زيتا.

### P23.6 — `ANT-EVID-23-01`: دليل Odlyzko

يسجل مصدر 1987 وأحجام العينات والدقة المعلنة.

التصنيف: `NUMERICAL-EVIDENCE / FINITE-VERIFIED`.

### P23.7 — `ANT-DEF-23-03`: الفواصل والتباين العددي

تعريف nearest-neighbor spacing وnumber variance وبيان اختلافهما عن الارتباط الثنائي.

التصنيف: `DEFINITION`.

### P23.8 — `ANT-PRIN-23-01`: أنواع التناظر

عرض مبدأ Katz--Sarnak مع حارس انتقال صريح.

التصنيف: `CITED-CORE / INTERPRETATION-GUARDED`.

### P23.9 — `ANT-OPEN-23-01`: GUE وn-level

الصيغة الكاملة لأصفار زيتا وإحصاءات المستويات الأعلى تبقى جبهة مفتوحة.

التصنيف: `OPEN / FRONTIER`.

### P23.10 — `ANT-PRIN-23-02`: حدود الاستدلال

يسجل هذا العنصر قاعدة منهجية لضبط القراءة: لا يعامل توافق pair correlation بوصفه برهانًا على RH، ولا يعامل الإحصاء الثنائي بوصفه محددًا تلقائيًا لقانون الفواصل المتتالية أو لكل إحصاءات \(n\)-level. لا يقدم العنصر مبرهنة جديدة ولا يحمل وسم `PROVED-HERE`، بل يحدد حدود ما تسمح به المدخلات المعروضة في الفصل.

التصنيف: `METHODOLOGICAL-PRINCIPLE / INFERENCE-GUARDED`.

## تدقيق عدم الدور

```text
CHAPTER-6  -> source of truth for Riemann--von Mangoldt via ANT-THM-06-06
CHAPTER-9  -> explicit-formula context only
CHAPTER-21 -> family/conductor vocabulary only
CHAPTER-22 -> conceptual contrast only; no theorem imported
CHAPTER-23 -> no duplicate zero-count theorem
FRONTIERS-MAP -> not a scientific source
```

الحراس:

- لا تستخدم حدسية GUE لإثبات مبرهنة Montgomery.
- لا تستخدم بيانات Odlyzko لإثبات صيغة تقاربية.
- لا تستخدم حد GUE المصفوفي لإثبات نتيجة زيتا.
- لا تسجل صيغة ريمان--فون مانغولت بمعرّف جديد مستقل.
- لا يوسم `ANT-PRIN-23-02` بـ`PROVED-HERE` ولا يعرض كمبرهنة.

الحكم: `CIRCULARITY = CLOSED / DUPLICATION = CLOSED / CLASSIFICATION = CORRECTED`.