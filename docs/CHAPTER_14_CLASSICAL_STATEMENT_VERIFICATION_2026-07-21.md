# التحقق من الصيغة الكلاسيكية للفصل الرابع عشر

التاريخ: 2026-07-21

```text
VERSION                 = 0.18.0-dev
CHAPTER                 = 14
TOPIC                   = BARBAN--DAVENPORT--HALBERSTAM
VERIFICATION-SCOPE      = CLASSICAL-UPPER-BOUND / HISTORICAL-SOURCE-MAP
PRE-AUTHORING-GATE      = OPEN
AUTHORING               = BLOCKED
RELEASE-READY           = NO
```

## الكمية المرجعية

نعتمد مؤقتًا، بوصفها كمية التباين الأساسية، الصيغة

\[
V_\psi(x,Q)=
\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|
\psi(x;q,a)-\frac{x}{\varphi(q)}
\right|^2.
\]

هذه هي الصيغة التي سيبنى عليها مسار الحد العلوي الكلاسيكي. لا يعني اعتمادها المؤقت اعتماد صيغة تقاربية أو ثابت حد رئيسي.

## ما تم التحقق منه

1. الورقة الأصلية لـDavenport--Halberstam هي:
   `Primes in arithmetic progressions`, Michigan Mathematical Journal 13 (1966), 485--489، DOI `10.1307/mmj/1028999608`، ولها تصحيح في Michigan Mathematical Journal 15 (1968), 505.
2. مرجع Montgomery التعليمي الأساسي هو:
   `Topics in Multiplicative Number Theory`, Lecture Notes in Mathematics 227 (1971)، والفصل `The mean value theorem of Barban` يقع في الصفحات 145--154.
3. ورقة Montgomery المستقلة:
   `Primes in arithmetic progressions`, Michigan Mathematical Journal 17 (1970), 33--39، هي مرجع مبكر للصيغة التقاربية الدقيقة، لكنها ليست المصدر الذي سيعتمد وحده لإثبات الحد العلوي الأساسي.
4. سلسلة Hooley بدأت على الأقل بـ`On the Barban-Davenport-Halberstam theorem. I`, J. Reine Angew. Math. 274/275 (1975), 206--223، ثم تلتها أجزاء متعددة؛ هذه السلسلة تخص التحسينات والصيغ التقاربية الأدق، ولا تدمج في النتيجة الأساسية دون تحقق مستقل لكل جزء مستعمل.
5. الصيغة الحديثة الشائعة للحد العلوي، في نطاق من الشكل
   \[
   x(\log x)^{-M}\le Q\le x,
   \]
   هي
   \[
   V_\psi(x,Q)\ll_M xQ\log x.
   \]
   يظل تحديد الاعتماد الدقيق للثابت، واختيار `\psi` مقابل `\vartheta`، وصيغة المجال النهائية، خاضعًا لفحص النص الكامل للمصدر المعتمد.

## قرار بنية الفصل

يفصل الفصل بين مستويين:

### المستوى A — النتيجة الأساسية

حد علوي كلاسيكي من نوع Barban--Davenport--Halberstam:

\[
V_\psi(x,Q)\ll_M xQ\log x
\]

في نطاق كبير لـ`Q` يبدأ من `x/(\log x)^M` حتى `x`، بعد تثبيت الصياغة النهائية من النص الكامل.

### المستوى B — طبقة مستقلة

صيغة Montgomery--Hooley التقاربية وحدودها الرئيسية الأدق. هذه الطبقة لا تدخل البرهان الأساسي ولا تسجل كنتيجة معتمدة قبل:

- فحص نص Montgomery 1970؛
- فحص الفصل 18 من Montgomery 1971؛
- فحص الجزء أو الأجزاء المحددة من سلسلة Hooley؛
- تثبيت الحد الرئيسي والثابت ومجال `Q` بدقة.

## العلاقة مع الفصل الثالث عشر

Bombieri--Vinogradov يضبط متوسطًا من الرتبة الأولى لأكبر خطأ على الفئات المختزلة، بينما BDH يضبط متوسطًا تربيعيًا على الترديدات والفئات معًا. لا تستنتج إحدى الصيغتين من الأخرى بصورة عكسية مباشرة دون خسارة أو أداة إضافية.

## البوابات المتبقية

```text
SOURCE-TEXT-DH-1966        = METADATA-VERIFIED / FULL-TEXT-PENDING
SOURCE-TEXT-MONTGOMERY-1970 = METADATA-VERIFIED / FULL-TEXT-PENDING
SOURCE-TEXT-MONTGOMERY-1971 = CHAPTER-LOCATION-VERIFIED / FULL-TEXT-PENDING
SOURCE-TEXT-HOOLEY          = SERIES-MAP-PARTIAL / FULL-TEXT-PENDING
NORMALIZATION               = PROVISIONAL
Q-RANGE                     = PROVISIONAL
ASYMPTOTIC-LAYER            = DEFERRED
PASS-FOR-AUTHORING          = NO
```

## الحكم

```text
PASS-FOR-CLASSICAL-STRUCTURE = YES
PASS-FOR-REFERENCE-PINNING   = PARTIAL
PASS-FOR-AUTHORING           = NO
```
