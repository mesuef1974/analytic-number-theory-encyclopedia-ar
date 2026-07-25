# تقرير مطابقة Selberg للفصل العشرين — 2026-07-25

## الحكم

\`\`\`text
SCOPE                       = COMPACT TORSION-FREE HYPERBOLIC SURFACE
SELBERG-COMPACT-PROTOTYPE   = CROSS-CHECK PASS
FOURIER-PAIR                = FROZEN FOR THIS PROTOTYPE
NONCOMPACT-MODULAR-CASE     = DEFERRED
INDEPENDENT-REVIEW          = PENDING
AUTHORING                   = BLOCKED
RESULTS                     = RESERVED / NON-CITABLE
\`\`\`

هذا التقرير يثبت نموذج Selberg المدمج المطلوب للمدخل البنيوي في الفصل العشرين. لا يمنح حكمًا للصيغة غير المدمجة، ولا يحذف حدود Eisenstein أو المبعثرات من حالة المجموعة المعيارية.

## الفرضيات والنطاق

ليكن \(M=\Gamma\backslash\mathbb H\) سطحًا زائدًا مدمجًا، حيث \(\Gamma\) زمرة متقطعة خالية من الالتواء. يكون طيف \(-\Delta\) منفصلًا، ونكتب

\[
\lambda_j=\frac14+r_j^2.
\]

تُختار \(h\) زوجية، تحليلية في شريط حول المحور الحقيقي، وذات تناقص كافٍ يضمن تقارب الطرفين.

## زوج التحويل المعتمد

نعتمد اصطلاح Marklof، وهو الاصطلاح المطابق للعرض المنسوب إلى Hejhal:

\[
g(u)=\frac1{2\pi}\int_{\mathbb R}h(r)e^{-iru}\,dr,
\qquad
h(r)=\int_{\mathbb R}g(u)e^{iru}\,du.
\]

إذن عامل \(2\pi\) يقع في التحويل الأمامي وحده. لا يجوز نقل هذا الزوج إلى اصطلاح متناظر بعوامل \(1/\sqrt{2\pi}\) من دون إعادة حساب الطرف الهندسي.

## الصيغة المدمجة المثبتة

إذا جرى الجمع على الجيوديسيات البدائية \(\gamma\) وأطوالها \(\ell_\gamma\)، فإن النموذج المعتمد هو

\[
\sum_{j\ge0} h(r_j)
=
\frac{\operatorname{Area}(M)}{4\pi}
\int_{\mathbb R} h(r)\,r\tanh(\pi r)\,dr
+
\sum_{\gamma\ {\rm primitive}}\sum_{n\ge1}
\frac{\ell_\gamma\,g(n\ell_\gamma)}
     {2\sinh(n\ell_\gamma/2)}.
\]

المطابقة الحدية:

| المكوّن | الثابت/الاصطلاح | الحكم |
|---|---|---|
| المعلمة الطيفية | \(\lambda_j=1/4+r_j^2\) | PASS |
| حد الهوية | \(\operatorname{Area}(M)/(4\pi)\) | PASS |
| كثافة Plancherel | \(r\tanh(\pi r)\,dr\) | PASS |
| التحويل الأمامي | \(1/(2\pi)\) وإشارة \(-iru\) | PASS |
| التحويل العكسي | بلا عامل إضافي وإشارة \(+iru\) | PASS |
| التكرار الجيوديسي | \(\ell_\gamma/[2\sinh(n\ell_\gamma/2)]\) | PASS |

## سلسلة الأدلة

1. J. Marklof، *Selberg's Trace Formula: An Introduction*:
   - شروط دالة الاختبار في §3؛
   - تعريف التحويل في (69)؛
   - صيغة الأثر المدمجة في Theorem 4، المعادلة (182).
2. D. A. Hejhal، *The Selberg Trace Formula for PSL(2,R)*، Vol. I:
   - الفصل الأول، *The trace formula for compact Riemann surfaces*، ص 1--38؛
   - بيانات الفصل والموضع مثبتة من Springer.
3. A. Selberg، ورقة 1956 الأصلية:
   - تثبت الأصل التاريخي والببليوغرافي؛
   - لا تُستخدم وحدها لنقل اصطلاح التحويل إلى الفصل.

روابط التحقق:

- https://people.maths.bris.ac.uk/~majm/bib/selberg.pdf
- https://link.springer.com/chapter/10.1007/BFb0079609
- https://doi.org/10.1007/BFb0079608
- https://doi.org/10.1090/S0002-9904-1956-10063-3

## ما لا يثبته هذا التقرير

- لا يثبت صيغة Selberg الكاملة للسطوح غير المدمجة.
- لا يثبت حدود القطع المكافئ أو الإهليلجي.
- لا يثبت حد الطيف المستمر أو مصفوفة المبعثرات.
- لا يجيز عرض النموذج المدمج بوصفه صيغة \(PSL_2(\mathbb Z)\).
- لا يفتح بوابة التأليف قبل المراجعة المستقلة.

## نتيجة البوابة

أُغلق العائق العلمي الخاص بزوج تحويل Selberg وعوامل \(2\pi\) ضمن النطاق المدمج وحده. بقيت المراجعة المستقلة للحزمة كاملة شرطًا مانعًا وحيدًا قبل PASS-FOR-AUTHORING.
