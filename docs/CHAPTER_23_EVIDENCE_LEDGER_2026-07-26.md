# سجل أدلة الفصل الثالث والعشرين

```text
EVIDENCE-LEDGER   = CORE STATEMENTS FROZEN
PRIMARY-SOURCES   = VERIFIED FOR PRE-AUTHORING REVIEW
AUTHORING         = BLOCKED PENDING INDEPENDENT REVIEW
FRONTIER-MATERIAL = QUARANTINED
```

## المصادر الأساسية المثبتة

| المحور | المصدر | الصيغة المجمدة للاستعمال | الحالة |
|---|---|---|---|
| عد الأصفار | Riemann--von Mangoldt؛ Titchmarsh--Heath-Brown | \(N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T)\)، مع العد بالتعدد | STANDARD-CORE / PROVED-HERE CANDIDATE |
| الارتباط الثنائي | H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math. 24 (1973), 181--193، DOI: 10.1090/pspum/024/9944 | تحت RH، للدالة الموزونة \(F(\alpha,T)\) المعرفة أدناه: \(F(\alpha,T)=T^{-2\alpha}(\log T+O(1))+\alpha+o(1)\) بصورة منتظمة على المجالات المغلقة داخل \(0\le\alpha<1\)؛ لا تمدد إلى \(|\alpha|\ge1\) بلا حدسية | PRIMARY-VERIFIED / CONDITIONAL-ON-RH |
| إعادة صياغة حديثة | Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh, arXiv:2306.04799 | مرجع تدقيقي حديث لتعريف الوزن والتطبيع والصيغة المنتظمة؛ لا يحل محل إسناد النتيجة التاريخية إلى Montgomery | SUPPORT / PREPRINT |
| الحساب العددي | A. M. Odlyzko, *On the distribution of spacings between zeros of the zeta function*, Math. Comp. 48 (1987), 273--308، DOI: 10.1090/S0025-5718-1987-0866115-0 | أول \(10^5\) أصفار، وكتلة من \(10^5\) أصفار تبدأ عند الفهرس \(10^{12}+1\)، بدقة معلنة تقارب \(10^{-8}\)؛ توافق عددي يتحسن عند الارتفاع الأكبر | PRIMARY-VERIFIED / NUMERICAL-EVIDENCE ONLY |
| المصفوفات العشوائية | Dyson--Mehta؛ حد GUE المحلي | بعد جعل متوسط التباعد واحدًا: \(K(u)=\sin(\pi u)/(\pi u)\)، و\(R_2(u)=1-K(u)^2\) للأزواج غير القطرية | STANDARD-CORE / RANDOM-MATRIX-THEOREM |
| عائلات دوال L | N. Katz and P. Sarnak, *Random Matrices, Frobenius Eigenvalues, and Monodromy*, AMS Colloquium Publications 45 (1999) | أنواع التناظر الوحدوي والتعامدي والسمبلكتي في عائلات مضبوطة؛ النتائج المثبتة فوق الحقول المنتهية لا تنقل آليًا إلى دالة زيتا الكلاسيكية | PRIMARY-VERIFIED / TRANSFER-GUARDED |
| دعم متعدد المستويات | Rudnick--Sarnak، إحصاءات أصفار دوال L الرئيسية | يذكر بوصفه امتدادًا خارج النواة، ولا يستعمل لإثبات مبرهنة Montgomery الثنائية | DEFERRED / CITED-CONTEXT |

## التعريف المجمد لدالة Montgomery

نفترض RH، ونكتب الأصفار \(\rho=1/2+i\gamma\)، مع العد بالتعدد، ونضع
\[
w(u)=\frac{4}{4+u^2},
\]
ثم
\[
F(\alpha,T)
=
\left(\frac{T}{2\pi}\log T\right)^{-1}
\sum_{0<\gamma,\gamma'\le T}
T^{i\alpha(\gamma-\gamma')}w(\gamma-\gamma').
\]
الأزواج مرتبة، والقطر داخل المجموع. الدالة حقيقية وزوجية وغير سالبة.

## حدسية الارتباط الثنائي بصيغة دوال الاختبار

نعتمد اتفاقية فورييه
\[
\widehat f(\alpha)=\int_{\mathbb R}f(u)e^{-2\pi i\alpha u}\,du.
\]
بعد حذف القطر وتطبيع الفروق محليًا، تتنبأ الحدسية بأنه لكل دالة اختبار مناسبة:
\[
\frac{1}{N(T)}
\sum_{\substack{0<\gamma,\gamma'\le T\\ \gamma\ne\gamma'}}
f\!\left((\gamma-\gamma')\frac{\log T}{2\pi}\right)
\longrightarrow
\int_{\mathbb R}f(u)
\left[1-\left(\frac{\sin\pi u}{\pi u}\right)^2\right]du.
\]
الجزء الذي تثبته طريقة Montgomery يطابق هذه الصيغة فقط عندما يكون دعم \(\widehat f\) داخل \((-1,1)\)، وتحت RH في الصياغة التاريخية المعتمدة هنا.

## الحدود الفاصلة بين الإحصاءات

- `PAIR CORRELATION`: متوسط على جميع الأزواج بدالة اختبار؛ لا يساوي قانون الفاصل المتتالي.
- `NEAREST-NEIGHBOR SPACING`: توزيع \(\gamma_{n+1}-\gamma_n\) بعد التطبيع؛ يحتاج معلومات ترتيبية أقوى.
- `NUMBER VARIANCE`: تباين عدد النقاط في نافذة بطول \(L\)؛ تابع لتكاملات الارتباط، لكنه ليس مرادفًا لقيمة واحدة من pair correlation.
- `n-LEVEL CORRELATION`: بنية أعلى لا تستعاد تلقائيًا من الإحصاء الثنائي وحده.

## حراس الأدلة

1. لا تساوى مبرهنة Montgomery بحدسية الارتباط الثنائي الكاملة.
2. اتفاقية فورييه ذات \(2\pi\) هي الوحيدة المعتمدة في الفصل.
3. بيانات Odlyzko دليل عددي منتهٍ وليست برهانًا على RH أو GUE.
4. توافق GUE لا يثبت أن كل الأصفار على الخط الحرج.
5. نتائج Katz--Sarnak فوق الحقول المنتهية لا تنقل آليًا إلى عائلات دوال L الكلاسيكية.
6. لا تستعمل نتائج n-level لإثبات النتيجة الثنائية السابقة عليها منطقيًا.

## حالة العوائق

```text
BLOCKER-1 RIEMANN-VON-MANGOLDT = CLOSED
BLOCKER-2 MONTGOMERY-STATEMENT = CLOSED
BLOCKER-3 FOURIER-GUE-NORMALIZATION = CLOSED
BLOCKER-4 ODLYZKO-SOURCE = CLOSED
BLOCKER-5 STATISTICS-BOUNDARIES-AND-CIRCULARITY = CLOSED
```
