# سجل أدلة الفصل الثاني والعشرين

## حالة السجل

```text
EVIDENCE-LEDGER     = PARTIALLY FROZEN
AUTHORING           = BLOCKED
PRIMARY-SOURCES     = 5 CORE ITEMS VERIFIED
FRONTIER-MATERIAL   = QUARANTINED UNTIL REVIEW
```

## المصادر الأساسية المثبتة

| المحور | المصدر الأولي | الاستعمال | الحالة |
|---|---|---|---|
| العزم الثاني | Hardy--Littlewood, *The Approximate Functional Equation in the Theory of the Zeta-Function, with Applications to the Divisor-Problems of Dirichlet and Piltz*, Proc. LMS (1923), 39--74, DOI `10.1112/plms/s2-21.1.39` | المصدر التاريخي للمعادلة التقريبية ومسار العزم الثاني | PRIMARY-VERIFIED-METADATA / FORMULA-PENDING-EXACT-LOCATION |
| العزم الرابع | A. E. Ingham, *Mean-Value Theorems in the Theory of the Riemann Zeta-Function*, Proc. LMS (2) 27 (1928), 273--300, DOI `10.1112/plms/s2-27.1.273` | الصيغة التقاربية الكلاسيكية للعزم الرابع | PRIMARY-VERIFIED-METADATA / FORMULA-PENDING-EXACT-LOCATION |
| حد Soundararajan | K. Soundararajan, *Moments of the Riemann zeta function*, Ann. of Math. 170 (2009), 981--993, DOI `10.4007/annals.2009.170.981` | تحت RH: حد علوي قريب من الرتبة المتوقعة | PRIMARY-VERIFIED |
| حد Harper الحاد | A. J. Harper, *Sharp conditional bounds for moments of the Riemann zeta function*, arXiv:1305.4618، Theorem 1 | تحت RH ولكل \(k\ge0\) ثابت: حد من الرتبة الحدسية | PRIMARY-TEXT-VERIFIED |
| الحدود الدنيا المستمرة | M. Radziwiłł--K. Soundararajan, *Continuous lower bounds for moments of zeta and L-functions*, Mathematika 59 (2013), 119--128, DOI `10.1112/S0025579312001088` | حد أدنى من الرتبة الصحيحة للعزم \(2k\) ضمن المجال المعلن | PRIMARY-VERIFIED |
| نموذج المصفوفات العشوائية | J. P. Keating--N. C. Snaith, *Random matrix theory and \(\zeta(1/2+it)\)*, Comm. Math. Phys. 214 (2000), 57--89 | حدسية ثابت العزوم وبنية العامل الحسابي/المصفوفي | PRIMARY-METADATA-VERIFIED / CONSTANTS-PENDING |

## صيغ ثبتت مباشرة

### 1. حد Soundararajan المشروط

من المقالة الأصلية: بافتراض RH، لكل \(k>0\) ثابت ولكل \(\varepsilon>0\)،

\[
\int_T^{2T}\left|\zeta\!\left(\frac12+it\right)\right|^{2k}\,dt
\ll_{k,\varepsilon} T(\log T)^{k^2+\varepsilon}.
\]

التصنيف: `CITED-CORE / CONDITIONAL-ON-RH`.

### 2. حد Harper الحاد

من Theorem 1 في النص الأصلي:

\[
\int_T^{2T}\left|\zeta\!\left(\frac12+it\right)\right|^{2k}\,dt
\ll_k T(\log T)^{k^2},
\qquad k\ge0 \text{ ثابت},
\]

بافتراض RH ولـ\(T\) كبير. الثابت الضمني يعتمد على \(k\) فقط.

التصنيف: `CITED-CORE / CONDITIONAL-ON-RH`.

### 3. الحدود الدنيا المستمرة

Radziwiłł--Soundararajan يثبتان حدودًا دنيا من الرتبة الصحيحة للعزم \(2k\) لكل \(k\ge1\)، مع استمرارية الاعتماد على \(k\)، ويمتد المنهج إلى عائلات من دوال \(L\).

التصنيف: `CITED-CORE / UNCONDITIONAL-IN-STATED-RANGE`.

## فواصل حوكمية ثابتة

1. الصيغة العامة المتوقعة للعزوم ليست مبرهنة لكل \(k\).
2. العزمان الثاني والرابع هما الحالتان الكلاسيكيتان ذواتا صيغ تقاربية مثبتة.
3. حد Soundararajan وحد Harper كلاهما مشروطان بفرضية ريمان.
4. Harper يزيل خسارة \(\varepsilon\) من أسّ اللوغاريتم، لكنه لا يثبت الثابت الحدسي.
5. الحدود الدنيا المستمرة غير مشروطة ضمن مجالها المعلن، ولا تعني صيغة تقاربية كاملة.
6. نموذج Keating--Snaith `CONJECTURAL / HEURISTIC` لدالة زيتا.
7. الانتقال من رتبة العزوم إلى قانون القيم القصوى ليس آليًا.
8. أي مادة منشورة أو مودعة في 2025--2026 تبقى `FRONTIER / QUARANTINED` حتى مراجعة منفصلة.

## العوائق المتبقية قبل التجميد

- استخراج الموضع والصيغة الدقيقة للعزم الثاني، بما في ذلك ثابت الحد الرئيس وحد الخطأ المعتمد في الفصل.
- استخراج موضع Ingham الدقيق وثابت \(1/(2\pi^2)\) في الحد الرئيس للعزم الرابع، مع حد الخطأ الذي سيُذكر.
- قراءة نص Keating--Snaith الأصلي وتجميد \(a(k)\) و\(g(k)\) دون خلط بين تطبيع \([0,T]\) و\([T,2T]\).
- تحديد هل سيُثبت الفصل العزم الثاني داخليًا أم يقتبسه؛ لا يُحسم ذلك قبل خريطة برهان نهائية.
- تثبيت جسر عائلات دوال \(L\) دون تعميم غير مشروع من حالة زيتا.
