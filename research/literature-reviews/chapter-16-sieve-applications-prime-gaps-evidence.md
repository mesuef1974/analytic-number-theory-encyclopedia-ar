# سجل أدلة الفصل السادس عشر

آخر تحديث: 2026-07-24

```text
CHAPTER               = 16
VERSION               = 0.20.0-dev
BASE-MAIN             = 5ebe7fd5ade9e1c1c7c3edabf646bad90a9cff6a
BRANCH                = agent/chapter-16-sieve-applications-prime-gaps-v0.20.0
ISSUE                 = #29 / OPEN
RESEARCH-INTAKE       = OPEN
PRE-AUTHORING-GATE    = OPEN
AUTHORING             = BLOCKED
RESULTS               = 0 / NOT RESERVED
PASS-FOR-AUTHORING    = NO
RELEASE-READY         = NO
```

## السؤال المركزي

كيف تنتقل لغة الغربال من الحد العلوي الأحادي في الفصل الخامس عشر إلى تطبيقات حقيقية على الأنماط الأولية والأعداد شبه الأولية والفجوات بين الأوليات، من دون خلط بين:

- غربال سيلبرغ التقليدي؛
- غربال برون والأدوات التوافقية؛
- مبرهنة تشن وأدواتها الأعمق؛
- طريقة GPY؛
- إنجاز Zhang؛
- صياغة Maynard--Tao متعددة الأبعاد؟

## طبقات الأدلة المطلوبة

### A. الأساس الغربالي

- الفصل 15 من الموسوعة: الحد العلوي المنتهي، البعد الغربالي، وعائق التكافؤ.
- Halberstam--Richert: sieve methods and standard upper/lower-bound frameworks.
- Iwaniec--Kowalski: sieve methods, almost primes, and modern applications.
- Friedlander--Iwaniec: the parity phenomenon and limits of classical sieve information.

### B. تطبيقات برون والأعداد شبه الأولية

- Brun: upper-bound treatment of twin-prime patterns and convergence of the Brun sum.
- Chen: representation of sufficiently large even integers as a prime plus an integer with at most two prime factors; source and exact theorem statement must be verified before use.
- Distinguish clearly between a theorem about almost primes and the twin-prime conjecture.

### C. فجوات الأوليات

- Goldston--Pintz--Yıldırım: small gaps relative to the average spacing and the GPY weight.
- Zhang: bounded gaps using distribution beyond the classical Bombieri--Vinogradov range for suitable moduli.
- Maynard and Tao: multidimensional Selberg-sieve weights and bounded intervals containing several primes.
- Polymath developments: numerical improvement history is contextual only unless exact constants and dates are independently verified.

## مصفوفة التصنيف الأولية

| الموضوع | التصنيف المرشح | حالة التحقق |
|---|---|---|
| اشتقاق حد علوي بسيط لنمط ثنائي من الفصل 15 | `PROVED-HERE` محتمل | يحتاج خريطة اعتماد دقيقة |
| تقارب مجموع برون | `CITED` أو `PROVED-HERE` جزئي | يحتاج تحديد مستوى البرهان المناسب |
| مبرهنة تشن | `CITED` | يحتاج المصدر الأصلي والصياغة الدقيقة |
| نتيجة GPY عن الفجوات الصغيرة نسبيًا | `CITED` | يحتاج النص الأصلي وحدود النتيجة |
| مبرهنة Zhang عن الفجوات المحدودة | `CITED` | يحتاج المصدر الأصلي وسقف الادعاء |
| مبرهنة Maynard--Tao | `CITED / EXPLAINED` | يحتاج تثبيت النسخة التعليمية المختارة |
| أفضل ثابت عددي معروف للفجوات | `DEFERRED / TIME-SENSITIVE` | لا يثبت دون تدقيق حديث مستقل |

## مخاطر الخلط

1. لا تنسب الفجوات المحدودة إلى غربال سيلبرغ التقليدي وحده.
2. لا تستنتج حدًا سفليًا للأزواج الأولية من حد علوي غربالي.
3. لا تخلط بين `P_2` وبين عدد أولي.
4. لا تجعل Bombieri--Vinogradov وحدها كافية لإنجاز Zhang.
5. لا تعرض أوزان Maynard متعددة الأبعاد كإعادة تسمية مباشرة لأوزان الفصل 15.
6. لا تسجل ثابتًا عدديًا معاصرًا بوصفه نهائيًا دون تدقيق زمني.

## المهام المرجعية قبل التأليف

- [ ] تحديد النص الأصلي الدقيق لنتيجة برون المختارة.
- [ ] تثبيت الصياغة الأصلية لمبرهنة تشن والنسخة التعليمية المستخدمة.
- [ ] تثبيت نتائج GPY التي ستدخل الفصل، مع الفرضيات والصيغ الدقيقة.
- [ ] تثبيت مبرهنة Zhang من الورقة الأصلية.
- [ ] تثبيت مبرهنة Maynard والنسخة الموازية عند Tao.
- [ ] مراجعة تطور الثوابت العددية فقط إن كان سيذكر.
- [ ] إعداد تدقيق عدم الدور مع الفصلين 13 و15.
- [ ] إصدار حكم `PASS-FOR-AUTHORING` مستقل قبل إنشاء المتن.
