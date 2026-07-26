# خريطة برهان الفصل الثالث والعشرين

```text
PROOF-MAP   = REVIEW-CORRECTED / NARROW-REVIEW-PENDING
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

يعاد عرض تعريف \(N(T)\) مع العد بالتعدد، ثم **تحيل الصيغة مباشرة إلى** `ANT-THM-06-06` بدل تسجيل مبرهنة جديدة:
\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T).
\]
يشتق الفصل 23 فقط الكثافة المتوسطة
\[
\frac{1}{2\pi}\log\frac{T}{2\pi}
\]
ومتوسط التباعد المحلي من الحد الرئيس. إعادة العرض بيداغوجية ذاتية الاكتفاء، لكن مصدر الحقيقة الداخلي الوحيد هو الفصل 6.

التصنيف: `DEFINITION / INTERNAL-CROSS-REFERENCE`.

### P23.2 — `ANT-DEF-23-02`: الارتباط الثنائي

تعريفان متكاملان:

1. دالة Montgomery الموزونة \(F(\alpha,T)\)، وفيها الأزواج مرتبة والقطر داخل المجموع.
2. صيغة دالة الاختبار للأزواج غير القطرية بعد التطبيع المحلي.

التصنيف: `DEFINITION`.

### P23.3 — `ANT-THM-23-01`: مبرهنة Montgomery

تحت RH، وبالاتفاقية
\[
\widehat f(\alpha)=\int f(u)e^{-2\pi i\alpha u}\,du,
\]
يعرض الجزء المثبت ضمن
\[
\operatorname{supp}\widehat f\subset(-1,1),
\]
وتعرض الصيغة الموزونة في مجال \(0\le\alpha<1\):
\[
F(\alpha,T)=T^{-2\alpha}(\log T+O(1))+\alpha+o(1).
\]

التصنيف: `CITED-CORE / CONDITIONAL-ON-RH`.

### P23.4 — `ANT-CONJ-23-01`: حدسية الارتباط الثنائي الكاملة

للأزواج غير القطرية:
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

يسجل مصدر 1987 فقط:

- أول \(10^5\) أصفار.
- \(10^5\) أصفار من الفهرس \(10^{12}+1\) إلى \(10^{12}+10^5\).
- دقة معلنة تقارب \(10^{-8}\).

التصنيف: `NUMERICAL-EVIDENCE / FINITE-VERIFIED`.

### P23.7 — `ANT-DEF-23-03`: الفواصل والتباين العددي

تعريف nearest-neighbor spacing وnumber variance مع بيان أنهما ليسا مرادفين للارتباط الثنائي.

التصنيف: `DEFINITION`.

### P23.8 — `ANT-PRIN-23-01`: أنواع التناظر

عرض مبدأ Katz--Sarnak: وحدوي، تعامدي، سمبلكتي، مع تحديد العائلة ومقياس الموصل قبل المقارنة.

التصنيف: `CITED-CORE / INTERPRETATION-GUARDED`.

### P23.9 — `ANT-OPEN-23-01`: GUE وn-level

الصيغة الكاملة لأصفار زيتا وإحصاءات المستويات الأعلى تبقى جبهة مفتوحة.

التصنيف: `OPEN / FRONTIER`.

### P23.10 — `ANT-PRIN-23-02`: حدود الاستدلال

تسجيل المبدأ المنطقي الآتي: توافق pair correlation لا يثبت RH، والإحصاء الثنائي لا يستعيد تلقائيًا spacing أو كل إحصاءات \(n\)-level.

التصنيف: `PROVED-HERE / LOGICAL-SEPARATION`.

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
- لا تستنتج RH من pair correlation.

الحكم: `CIRCULARITY = CLOSED / DUPLICATION = CLOSED`.
