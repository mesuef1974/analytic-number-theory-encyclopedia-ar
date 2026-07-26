# سجل أدلة الفصل الثاني والعشرين

## حالة السجل

```text
EVIDENCE-LEDGER     = CORE SOURCES VERIFIED / FRONTIER LIMITED
AUTHORING           = BLOCKED
PRIMARY-SOURCES     = VERIFIED FOR CORE STATEMENTS
FRONTIER-MATERIAL   = QUARANTINED UNTIL REVIEW
```

## المصادر الأساسية المثبتة

| المحور | المصدر | الصيغة المثبتة للاستعمال | الحالة |
|---|---|---|---|
| العزم الثاني | Hardy--Littlewood؛ وصياغة معيارية لاحقة في Titchmarsh--Heath-Brown | \(\int_0^T|\zeta(1/2+it)|^2dt=T\log(T/2\pi)+(2\gamma-1)T+E_1(T)\)، ويكفي للنواة حد كلاسيكي من رتبة \(E_1(T)=O(T^{1/2}\log T)\) | CORE-VERIFIED |
| العزم الرابع | A. E. Ingham, *Mean-Value Theorems in the Theory of the Riemann Zeta-Function*, Proc. LMS (2) 27, 273--300 | \(\int_0^T|\zeta(1/2+it)|^4dt=\frac{1}{2\pi^2}T\log^4T+O(T\log^3T)\)؛ النسخة الحديثة الأدق تكتب \(TP_4(\log T)+E_2(T)\) ومعامل الحد الأعلى \(1/(2\pi^2)\) | CORE-VERIFIED |
| الحدود العليا | K. Soundararajan, *Moments of the Riemann zeta function*, Annals of Mathematics 170 (2009), 981--993 | تحت RH: لكل \(k>0\) ثابت و\(\varepsilon>0\)، \(J_k(T)\ll_{k,\varepsilon}T(\log T)^{k^2+\varepsilon}\) | PRIMARY-VERIFIED |
| تحسين الحدود العليا | A. J. Harper, *Sharp conditional bounds for moments of the Riemann zeta function* | تحت RH: لكل \(k\ge0\) ثابت، \(J_k(T)\ll_k T(\log T)^{k^2}\) | PRIMARY-VERIFIED |
| الحدود الدنيا | Radziwiłł--Soundararajan, *Continuous lower bounds for moments of zeta and L-functions*, Mathematika 59 (2013), 119--128 | لكل \(k\ge1\) ثابت، حد أدنى غير مشروط من الرتبة \(T(\log T)^{k^2}\)؛ لا يُصاغ كتكافؤ تقاربي | PRIMARY-VERIFIED |
| حدود دنيا حديثة | Heap--Soundararajan, *Lower bounds for moments of zeta and L-functions revisited*, Mathematika 68 (2022) | تبسيط وتوسيع منهج الحدود الدنيا؛ يبقى CITED-SUPPORT لا بديلًا عن المصدر الأصلي | PRIMARY-VERIFIED / SUPPORT |
| نموذج المصفوفات العشوائية | Keating--Snaith, *Random matrix theory and \(\zeta(1/2+it)\)*, CMP 214 (2000), 57--89 | حدسية العزوم العامة بعامل حسابي وعامل Barnes \(G\) | PRIMARY-VERIFIED / CONJECTURAL |
| العزوم المزاحة | Ng--Shen--Wong, *Shifted moments of the Riemann zeta function*, CJM 76 (2024), 1556--1586 | سياق حديث خارج النواة الأساسية | VERIFIED-METADATA / DEFERRED |
| مسح 2026 | Alexandra Florea, *A survey of moment bounds for \(\zeta(s)\)* | اكتشاف ومقارنة فقط، لا مصدر تأسيسي للنواة | QUARANTINED-SURVEY |

## الصيغ المجمدة

### العزم الثاني

\[
I_1(T)=\int_0^T\left|\zeta\!\left(\frac12+it\right)\right|^2dt
=T\log\frac{T}{2\pi}+(2\gamma-1)T+E_1(T).
\]

لأغراض الفصل يكفي تسجيل الحد الكلاسيكي
\[
E_1(T)=O(T^{1/2}\log T),
\]
من دون الادعاء أنه أفضل حد معروف.

### العزم الرابع

\[
I_2(T)=\int_0^T\left|\zeta\!\left(\frac12+it\right)\right|^4dt
=\frac{1}{2\pi^2}T\log^4T+O(T\log^3T).
\]

والصياغة الحديثة الأدق هي
\[
I_2(T)=TP_4(\log T)+E_2(T),
\]
حيث \(P_4\) كثيرة حدود من الدرجة الرابعة ومعامل \(x^4\) فيها \(1/(2\pi^2)\).

### حدسية Keating--Snaith

لكل \(k\) ثابت مع \(\Re k>-1/2\):
\[
I_k(T)\sim a(k)\,\frac{G(k+1)^2}{G(2k+1)}\,T\left(\log\frac{T}{2\pi}\right)^{k^2}.
\]

ويُجمّد العامل الحسابي على الصورة
\[
a(k)=\prod_p\left(1-\frac1p\right)^{k^2}
\sum_{m=0}^{\infty}
\left(\frac{\Gamma(m+k)}{m!\,\Gamma(k)}\right)^2p^{-m}.
\]

وعند \(k\in\mathbb N\):
\[
\frac{G(k+1)^2}{G(2k+1)}
=\prod_{j=0}^{k-1}\frac{j!}{(j+k)!}.
\]

هذه صيغة `CONJECTURAL` لدالة زيتا، مع أن متوسط كثير الحدود المميز على \(U(N)\) نتيجة مثبتة في نموذج المصفوفات العشوائية.

## حقائق الحوكمة المجمدة

1. الصيغة العامة المتوقعة للعزوم ليست مبرهنة لكل \(k\).
2. العزمان الثاني والرابع هما الحالتان الكلاسيكيتان ذواتا صيغ تقاربية مثبتة.
3. حد Soundararajan لعام 2009 وحد Harper مشروطان بفرضية ريمان.
4. الحدود الدنيا المستمرة غير مشروطة ضمن مجالها المعلن.
5. نموذج Keating--Snaith حدسي لدالة زيتا، لا نتيجة مثبتة فيها.
6. الانتقال من رتبة العزوم إلى قانون القيم القصوى يحتاج مدخلًا إضافيًا.
7. لا تُستعمل أفضل حدود الخطأ الحديثة إذا لم تكن لازمة لبنية الفصل.

## المتبقي قبل التجميد النهائي

- حسم مستوى البرهان الداخلي للعزم الثاني.
- تثبيت أن العزم الرابع `CITED-CORE` لا `PROVED-HERE`.
- إغلاق خريطة عدم الدور بعد تثبيت هذين القرارين.
- مراجعة مستقلة فعلية لبوابة التأليف.
