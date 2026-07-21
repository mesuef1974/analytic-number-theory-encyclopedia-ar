# سجل أدلة الفصل الرابع عشر — Barban--Davenport--Halberstam

التاريخ: 2026-07-21

```text
VERSION              = 0.18.0-dev
CHAPTER               = 14
TOPIC                 = BARBAN--DAVENPORT--HALBERSTAM
BASE-MAIN             = d2588c893d8d07be1e961813628e1bb210e0eece
BRANCH                = agent/chapter-14-barban-davenport-halberstam-v0.18.0
ISSUE                 = #25 / OPEN
RESEARCH-INTAKE       = OPEN
PRE-AUTHORING-GATE    = OPEN
AUTHORING             = BLOCKED
RELEASE-READY         = NO
```

## الكمية المرشحة

نعتمد مؤقتًا تباين أخطاء توزيع دالة فون مانغولت في المتتاليات الحسابية:

\[
V_\psi(x,Q)=
\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|
\psi(x;q,a)-\frac{x}{\varphi(q)}
\right|^2.
\]

هذه الصيغة مرجعية لمسار الحد العلوي الكلاسيكي فقط. لا يزال اختيار `\psi` مقابل `\vartheta`، والتطبيع النهائي، ومجال `Q`، والفعالية بحاجة إلى تثبيت من النصوص الكاملة.

## خريطة المصادر المتحققة

### المصادر الأصلية والمبكرة

1. M. B. Barban, `On the distribution of primes in arithmetic progressions on average`, Dokl. Akad. Nauk UzSSR 5 (1964), 5--7، بالروسية. بيانات المصدر مثبتة من فهارس المراجع؛ النص الكامل لم يفحص بعد.
2. H. Davenport and H. Halberstam, `Primes in arithmetic progressions`, Michigan Mathematical Journal 13 (1966), 485--489، DOI `10.1307/mmj/1028999608`.
3. H. Davenport and H. Halberstam, corrigendum, Michigan Mathematical Journal 15 (1968), 505.
4. P. X. Gallagher, `The large sieve`, Mathematika 14 (1967), 14--20. مرشح لتثبيت نطاق الحد العلوي الحديث.
5. H. L. Montgomery, `Primes in arithmetic progressions`, Michigan Mathematical Journal 17 (1970), 33--39. مرجع للصيغة التقاربية المبكرة.
6. H. L. Montgomery, `Topics in Multiplicative Number Theory`, LNM 227 (1971)، الفصل `The mean value theorem of Barban`، الصفحات 145--154.

### تحسينات Hooley

بدأت السلسلة بـ:

- C. Hooley, `On the Barban-Davenport-Halberstam theorem. I`, J. Reine Angew. Math. 274/275 (1975), 206--223، DOI `10.1515/crll.1975.274-275.206`.

وتوجد أجزاء لاحقة متعددة في Journal/Proceedings of the London Mathematical Society وغيرها. لا يعتمد أي جزء منها حتى يحدد بدقة أي نتيجة وصفحات وصيغ يحتاجها الفصل.

## القرار البنيوي المعتمد

يفصل الفصل بين مستويين:

### A. الحد العلوي الكلاسيكي

الهدف المرشح:

\[
V_\psi(x,Q)\ll_M xQ\log x,
\qquad
x(\log x)^{-M}\le Q\le x.
\]

هذه هي النتيجة الأساسية المرشحة للفصل، مع بقاء صياغتها النهائية معلقة حتى فحص النص الكامل لمصدر الحد العلوي.

### B. الصيغة التقاربية

صيغة Montgomery--Hooley ذات الحد الرئيسي الأدق تعامل كطبقة مستقلة. لا تدمج في البرهان الأساسي ولا تحجز لها نتيجة قبل تثبيت:

- المجال الدقيق لـ`Q`؛
- الحد الرئيسي وثوابته؛
- الفرق بين `\psi` و`\vartheta`؛
- أثر الفئات غير المختزلة؛
- الخطأ المتبقي والفعالية.

## العلاقة مع Bombieri--Vinogradov

Bombieri--Vinogradov يضبط متوسطًا من الرتبة الأولى لأكبر خطأ على الفئات، بينما BDH يضبط مجموع مربعات الأخطاء على الترديدات والفئات معًا. لا يجوز تقديم BDH كتطبيق مباشر أو عكس مباشر لـBombieri--Vinogradov دون بيان الأداة والخسارة.

## أسئلة يجب إغلاقها قبل التأليف

1. فحص النص الكامل لـDavenport--Halberstam وتصحيحه.
2. فحص Gallagher لتثبيت الصيغة الحديثة للحد العلوي.
3. فحص Montgomery 1970 والفصل 18 من كتابه لفصل الحد العلوي عن التقارب.
4. تثبيت الجمع على الفئات المختزلة فقط أو الصيغة الموسعة.
5. إثبات هوية التحويل بالشخصيات مع جميع عوامل `\varphi(q)`.
6. تحديد المدخل المقتبس: الغربال الكبير أم مبرهنة BDH نفسها.
7. تحديد ما يمكن إثباته داخليًا دون تدوير منطقي مع الفصل الثالث عشر.
8. تدقيق الفعالية واعتماد الثوابت على `M`.

## حدود الادعاء الحالية

- لا يوجد متن فصل بعد.
- لا توجد نتيجة محجوزة في السجل بعد.
- لا يوجد حكم `PASS-FOR-AUTHORING`.
- لا يثبت هذا المسار Elliott--Halberstam.
- لا يعالج الفترات القصيرة إلا عبر بوابة مستقلة.
- لا يستنتج حدًا أعظميًا فرديًا من المتوسط التربيعي دون أداة إضافية.
- لا تعتمد الصيغة التقاربية أو ثابت حد رئيسي بعد.

## قرار الإدخال الحالي

```text
PASS-FOR-RESEARCH-INTAKE    = YES
PASS-FOR-CLASSICAL-STRUCTURE = YES
PASS-FOR-REFERENCE-PINNING  = PARTIAL
PASS-FOR-AUTHORING          = NO
```
