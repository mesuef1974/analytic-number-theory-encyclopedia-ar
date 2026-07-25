# خريطة برهان الفصل التاسع عشر

التاريخ: 2026-07-25  
الحالة: SCIENTIFIC SCOPE FROZEN / INDEPENDENT REVIEW PENDING

## الطبقات الحاكمة

\[
\text{صيغة مقتبسة في }\pi
\quad\text{أو}\quad
\text{مدخل مقتبس في }\psi
\Longrightarrow
\Delta_h\theta
\Longrightarrow
\Delta_h\pi
\Longrightarrow
\text{وجود أولي وفجوة}.
\]

لا يعامل الفصل هذه الأسهم كتكافؤات.

## المسار A — المبادئ الداخلية

1. الهوية
   \[
   \Delta_h\psi(x)=\sum_{x<n\le x+h}\Lambda(n).
   \]
2. مبدأ نقل أي حد خطأ معطى:
   \[
   \psi(t)=t+O(E(t))
   \Longrightarrow
   \Delta_h\psi(x)=h+O(E(x+h)+E(x)).
   \]
3. حد القوى الأولية العليا من الفصل 9:
   \[
   0\le\Delta_h\psi-\Delta_h\theta
   \ll\sqrt{x+h}\log(x+h).
   \]
4. إذا \(h\ge x^{1/2+\eta}\)، ففرق القوتين \(o(h)\).
5. الحصار
   \[
   \frac{\Delta_h\theta}{\log(x+h)}
   \le\Delta_h\pi
   \le\frac{\Delta_h\theta}{\log x}.
   \]
6. إذا \(h=o(x)\) و\(\Delta_h\theta\sim h\)، ينتج
   \[
   \Delta_h\pi\sim h/\log x.
   \]

الحالة: PROVED-HERE TARGETS / DEPENDENCIES CLOSED.

## المسار B — التاريخ الكلاسيكي

- Hoheisel: يسجل نوعيًا وجود \(\delta>0\)، بلا قيمة عددية في المتن.
- Ingham: Theorem 1 وصيغة الأس الناتجة؛ \(5/8\) مرحلة تاريخية.
- Huxley: \(7/12\) سجل تقاربي تاريخي، لا الجبهة الحالية.

الحالة: CITED / EXPLAINED / NO INTERNAL REPROOF.

## المسار C — الجبهة التقاربية الحديثة

Guth--Maynard, Corollary 1.3:
\[
x^{17/30+\varepsilon}\le y\le x^{0.99}
\Longrightarrow
\pi(x+y)-\pi(x)
=
\frac{y}{\log x}
+
O_\varepsilon\!\left(
y e^{-\sqrt[4]{\log x}}
\right).
\]

وتعتمد الورقة على:

1. تقدير قيم كبيرة جديد لمتعددات حدود ديريشليه.
2. تقدير كثافة
   \[
   N(\sigma,T)
   \le
   T^{15(1-\sigma)/(3+5\sigma)+o(1)},
   \]
   ومع تقدير Ingham في النطاق المكمل:
   \[
   N(\sigma,T)
   \le
   T^{30(1-\sigma)/13+o(1)}.
   \]
3. صيغة صريحة وVinogradov--Korobov zero-free region.
4. اختيار \(T\) وموازنة الحدود كما في القسم 13 من الورقة.

الحالة: CITED-CORE / EXPLANATION ONLY.  
لا تعاد تسمية هذه السلسلة PROVED-HERE.

## المسار D — Baker--Harman--Pintz

النص الأصلي يختم، لكل \(x\) كبير، بـ
\[
\pi(x+x^{0.525})-\pi(x)
>
\frac{9}{100}\frac{x^{0.525}}{\log x}.
\]

هذا يثبت حدًا سفليًا من الرتبة الصحيحة ووجود أولي، لكنه لا يثبت ثابتًا رئيسيًا 1 ولا صيغة تقاربية.

الحالة: CITED ONLY / EXACT PRIMARY STATEMENT FROZEN.

## المسار E — الادعاء عند 0.52

arXiv:2308.04458v8 يدعي الوجود عند \(0.52\)، لكنه لا يحمل سجل نشر محكّم مثبتًا في تاريخ القطع.

الحالة: QUARANTINED PREPRINT / NO RESULT ID.

## المسار F — تقريبًا كل فترة

تذكر Guth--Maynard, Corollary 1.4، نطاقًا أقصر لتقريبًا كل \(x\). إذا أدرج، فيوضع في قسم مستقل ولا يدخل في أي استنتاج لكل \(x\).

الحالة: OPTIONAL CITED SECTION.

## تدقيق عدم الدور

| الحافة | الحكم |
|---|---|
| الفصل 9 \(\to\) الفصل 19 | يسمح فقط بـPNT النوعية وحد القوى العليا؛ لا ينسب إليه حد خطأ فعال |
| الفصل 11 \(\to\) Guth--Maynard | تمهيد مفهومي فقط؛ التقدير الحديث مقتبس من ورقته الأصلية |
| الفصل 13 \(\to\) حكم لكل \(x\) | ممنوع؛ نتيجة متوسطية في الترديدات لا تكفي |
| الفصل 18 \(\to\) BHP | تمهيد لغوي فقط؛ لا يعاد بناء الغربال |
| الفصل 19 \(\to\) الفصل 9 | لا توجد حافة عكسية |
| نتيجة تقريبًا كل \(x\) \(\to\) كل \(x\) | ممنوع |

النتيجة: CIRCULARITY-AUDIT = PASS.

## النتائج المحجوزة بعد تجميد النطاق

1. تعريف أنظمة الفترات القصيرة.
2. هوية \(\Delta_h\psi\).
3. مبدأ نقل حد الخطأ.
4. حد القوى العليا والتحويل \(\psi\to\theta\).
5. حصار \(\theta\to\pi\).
6. Guth--Maynard عند \(17/30+\varepsilon\) بوصفه CITED.
7. BHP عند \(0.525\) بوصفه CITED.
8. الوجود \(\to\) حد فجوة.

Huxley وIngham يدخلان في السرد التاريخي ولا يحتاجان معرف مبرهنة مستقلاً في هذه النسخة. Hoheisel يبقى تاريخيًا بلا ثابت عددي.

## الحكم

~~~text
PROOF-MAP             = FROZEN
CORE-CITED-INPUTS     = FROZEN
INTERNAL-LEMMA-SCOPE  = FROZEN
CIRCULARITY-AUDIT     = PASS
INDEPENDENT-REVIEW    = PENDING
PASS-FOR-AUTHORING    = NO
~~~
