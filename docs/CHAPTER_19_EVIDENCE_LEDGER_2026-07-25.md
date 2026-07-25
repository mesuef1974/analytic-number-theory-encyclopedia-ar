# سجل أدلة الفصل التاسع عشر

التاريخ: 2026-07-25  
تاريخ القطع الأدبي: 2026-07-25  
الحالة: `INITIALIZED / VERIFICATION OPEN / AUTHORING-BLOCKED`

## 1. سؤال الفصل

نريد تحديد ما يمكن إثباته أو نقله بدقة عن وجود الأوليات وتوزعها في فترة
[
(x,x+h],
qquad h=o(x),
]
مع منع الخلط بين ثلاث طبقات مختلفة:

1. الصيغة التقاربية (psi(x+h)-psi(x)sim h) لكل (x).
2. مجرد وجود أولي واحد في الفترة.
3. نتيجة صحيحة لتقريبًا كل (x).

هذه الطبقات ليست متكافئة، وقد تختلف أسسها وأدواتها.

## 2. المصادر الأصلية التي تحقق سجلها الببليوغرافي

| المصدر | النتيجة ذات الصلة | وضع التحقق | الاستعمال المسموح |
|---|---|---|---|
| A. E. Ingham, *On the Difference Between Consecutive Primes*, QJM 8 (1937), 255–266, DOI: 10.1093/qmath/os-8.1.255 | مرحلة تاريخية في خفض طول الفترة | `BIBLIOGRAPHY VERIFIED / THEOREM TEXT PENDING` | لا تثبت الصيغة العددية في المتن قبل فحص النص |
| M. N. Huxley, *On the Difference between Consecutive Primes*, Invent. Math. 15 (1971/72), 164–170, DOI: 10.1007/BF01418933 | الصيغة التقاربية الكلاسيكية عند (hge x^{7/12+arepsilon}) | `PRIMARY RECORD VERIFIED / STATEMENT CROSS-CHECKED` | `CITED` بعد تثبيت صيغة المبرهنة وكمّياتها |
| R. C. Baker, G. Harman, J. Pintz, *The Difference Between Consecutive Primes, II*, PLMS 83 (2001), 532–562, DOI: 10.1112/plms/83.3.532 | وجود/حد سفلي من الرتبة الصحيحة عند الأس (0.525) | `PEER-REVIEWED RECORD VERIFIED / EXACT QUANTIFIERS PENDING` | `CITED` فقط؛ لا توصف بصيغة Huxley التقاربية |
| R. Li, *The number of primes in short intervals and numerical calculations for Harman's sieve*, arXiv:2308.04458 | يدعي وجود أوليات عند الأس (0.52) | `PREPRINT / NOT PEER-REVIEWED AS OF CUTOFF` | `QUARANTINED-PREPRINT`؛ لا يدخل النتائج المعتمدة |

روابط التحقق:

- Huxley: https://link.springer.com/article/10.1007/BF01418933
- Ingham: https://doi.org/10.1093/qmath/os-8.1.255
- Baker--Harman--Pintz: https://doi.org/10.1112/plms/83.3.532
- Li preprint: https://arxiv.org/abs/2308.04458

## 3. مراجع البناء النظري المرشحة

| المرجع | الوظيفة | الحالة |
|---|---|---|
| Montgomery--Vaughan, *Multiplicative Number Theory II* | الصيغة الصريحة وكثافة الأصفار والفترات القصيرة | `EXACT SECTION/PAGES PENDING` |
| Iwaniec--Kowalski, *Analytic Number Theory* | كثافة الأصفار وأدوات الغربال | `EXACT SECTION/PAGES PENDING` |
| Harman, *Prime-Detecting Sieves* | المسار الغربالي وراء الحدود الأقصر | `EXACT SECTION/PAGES PENDING` |
| Friedlander--Iwaniec, *Opera de Cribro*, Chapter 23 | كشف الأوليات في فترة قصيرة | `SCOPE/PAGES PENDING` |

لا تكفي أسماء الكتب وحدها لوسم نتيجة بأنها موثقة؛ يلزم رقم مبرهنة أو صفحات وصيغة مطابقة.

## 4. مدخلات داخلية مرشحة من الموسوعة

| المدخل | الفصل | السؤال التدقيقي |
|---|---|---|
| مبرهنة الأعداد الأولية وحد خطئها | 9 | هل الحد الفعال المطلوب مثبت داخليًا أم مقتبس؟ |
| المنطقة الخالية من الأصفار | 11 | هل ثوابتها وفعّاليتها كافيتان للطرح عند (x+h) و(x)؟ |
| Siegel--Walfisz | 12 | ليست المدخل الطبيعي للمجال غير الحسابي؛ يمنع الاستعمال الزائد |
| Bombieri--Vinogradov | 13 | نتيجة متوسطية في الترديدات؛ لا تتحول تلقائيًا إلى نتيجة نقطية في (x) |
| المجاميع الأسية | 18 | أداة محتملة للمسار الغربالي، وليست بمفردها برهان BHP |

## 5. هويات ونتائج أولية قابلة للإثبات الداخلي

### 5.1 الهوية الدقيقة

[
psi(x+h)-psi(x)=sum_{x<nle x+h}Lambda(n).
]

هذه هوية تعريفية، لكنها لا تضمن وجود أولي؛ فقد تأتي مساهمة من قوة أولية أعلى.

### 5.2 مبدأ نقل حد الخطأ

إذا كان
[
psi(t)=t+O(E(t))
]
بصورة موحدة على ([x,x+h])، فإن
[
psi(x+h)-psi(x)=h+O(E(x+h)+E(x)).
]
ومن ثم يلزم (E(x)=o(h)) للحصول على الصيغة التقاربية بهذه الطريقة المباشرة. هذا الاستنتاج مرشح `PROVED-HERE`.

### 5.3 القوى الأولية العليا

الانتقال من (psi) إلى (	heta) أو إلى عدد الأوليات يتطلب حدًا مستقلًا لمساهمة (p^k) مع (kge2). لا يجوز استنتاج وجود أولي من إيجابية فرق (psi) قبل ضبط هذه المساهمة بالنسبة إلى (h).

## 6. نقاط الحجر العلمي

1. لا يسمى الأس (0.52) «أفضل حد معروف معتمد» ما دام الدليل المتاح preprint غير محكّم ولم يخضع لمراجعة مستقلة في المشروع.
2. نتيجة Huxley التقاربية أقوى نوعيًا من مجرد الوجود، رغم أن أسها أطول.
3. نتيجة BHP الأقصر لا تنقل إلى صيغة (sim h) بلا نص صريح من المصدر.
4. نتائج «تقريبًا كل فترة» لا تجيب عن سؤال «كل (x)».
5. لا تستعمل فرضية ريمان داخل نتيجة غير مشروطة؛ أي مسار شرطي يوسم `CONDITIONAL / CITED`.

## 7. ما يزال مفتوحًا قبل التأليف

- استخراج نصوص المبرهنات الأصلية ومعاملاتها وكمّيات (arepsilon).
- تثبيت الصيغة التاريخية الدقيقة لـHoheisel وIngham.
- تدقيق الفرق بين الفترتين ((x,x+h]) و([x-x^	heta,x]).
- تدقيق التحويل بين (psi,	heta,pi) في النطاقات القصيرة.
- مراجعة مستقلة لوضع preprint (0.52).
- تدقيق عدم الدور الكامل.

## الحكم الحالي

```text
EVIDENCE-INTAKE       = PASS
PRIMARY-SOURCE-AUDIT  = PARTIAL
DEPENDENCY-AUDIT      = OPEN
PASS-FOR-AUTHORING    = NO
AUTHORING              = BLOCKED
```
