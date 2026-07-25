# سجل أدلة الفصل التاسع عشر

التاريخ: 2026-07-25  
تاريخ القطع الأدبي: 2026-07-25  
الحالة: PRIMARY SOURCES FROZEN / INTERNAL DEPENDENCIES CLOSED / INDEPENDENT REVIEW PENDING

## 1. سؤال الفصل

ندرس توزيع الأوليات في
\[
(x,x+h],\qquad h=o(x),
\]
مع فصل أربع طبقات لا يجوز الخلط بينها:

1. الصيغة التقاربية لكل \(x\).
2. حد سفلي من الرتبة الصحيحة لكل \(x\).
3. مجرد وجود أولي.
4. نتيجة صحيحة لتقريبًا كل \(x\).

## 2. السجل التاريخي والمصادر الأصلية

| المرحلة | الصيغة المسموح بها في الفصل | المصدر والموضع | الحكم |
|---|---|---|---|
| Hoheisel (1930) | أول إثبات لوجود ثابت \(\delta>0\) يجعل PNT صحيحًا في فترات طولها \(x^{1-\delta}\). لا يثبت الفصل قيمة عددية لـ\(\delta\). | G. Hoheisel, *Primzahlprobleme in der Analysis*, Sitzungsberichte der Preußischen Akademie der Wissenschaften (1930), 580--588؛ السجل الأصلي غير متاح رقميًا في فحص المشروع. | HISTORICAL / BIBLIOGRAPHY VERIFIED / NUMERICAL CONSTANT WITHHELD |
| Ingham (1937) | إذا \(\zeta(1/2+it)=O(t^c)\)، فالصيغة التقاربية تصح لكل \(\theta>(1+4c)/(2+4c)\)؛ وبالإدخال الكلاسيكي ينتج \(\theta>5/8\). | A. E. Ingham, *On the Difference Between Consecutive Primes*, QJM os-8 (1937), 255--266، Theorem 1؛ DOI: 10.1093/qmath/os-8.1.255. | PRIMARY PDF / THEOREM 1 VERIFIED |
| Huxley (1972) | تاريخيًا: \(\pi(x+y)-\pi(x)\sim y/\log x\) في نطاق \(y\ge x^{7/12+\varepsilon}\) بصيغة كل \(x\). | M. N. Huxley, *On the Difference between Consecutive Primes*, Invent. Math. 15 (1972), 164--170؛ DOI: 10.1007/BF01418933. أعيد تثبيت الصيغة من Guth--Maynard, Corollary 1.3، التي تسمي \(7/12\) الأس السابق. | PRIMARY RECORD + MODERN PRIMARY CROSS-CHECK |
| Guth--Maynard (2026) | إذا \(x^{17/30+\varepsilon}\le y\le x^{0.99}\)، فـ \(\pi(x+y)-\pi(x)=y/\log x+O_\varepsilon(y\exp(-\sqrt[4]{\log x}))\). | L. Guth and J. Maynard, *New large value estimates for Dirichlet polynomials*, Ann. of Math. 203 (2026), no. 2؛ arXiv:2405.20552v2، Corollary 1.3. | PEER-REVIEWED / PRIMARY / CURRENT ASYMPTOTIC RECORD |
| Baker--Harman--Pintz (2001) | لكل \(x\) كبير: \(\pi(x+x^{0.525})-\pi(x)>(9/100)x^{0.525}/\log x\). هذه رتبة صحيحة وحد سفلي، وليست صيغة تقاربية. | R. C. Baker, G. Harman, J. Pintz, *The Difference Between Consecutive Primes, II*, PLMS 83 (2001), 532--562، خاتمة ص. 561؛ DOI: 10.1112/plms/83.3.532. | PEER-REVIEWED / PRIMARY TEXT VERIFIED |
| Li | يدعي وجود أوليات عند \(0.52\). | R. Li, arXiv:2308.04458v8، آخر تعديل 16 أكتوبر 2025. | PREPRINT / QUARANTINED / NOT AN ADOPTED RECORD |

روابط التحقق:

- Ingham: https://academic.oup.com/qjmath/article-pdf/os-8/1/255/4457711/os-8-1-255.pdf
- Huxley: https://doi.org/10.1007/BF01418933
- Guth--Maynard: https://doi.org/10.4007/annals.2026.203.2.6
- Guth--Maynard open version: https://arxiv.org/abs/2405.20552
- Baker--Harman--Pintz: https://doi.org/10.1112/plms/83.3.532
- Li: https://arxiv.org/abs/2308.04458

## 3. تصحيح خط الجبهة

لا يجوز بعد تاريخ القطع وصف \(7/12\) بأنه أفضل أس تقاربي. التصنيف الصحيح هو:

~~~text
HUXLEY-7/12         = HISTORICAL ASYMPTOTIC RECORD
GUTH-MAYNARD-17/30  = CURRENT PEER-REVIEWED ASYMPTOTIC RECORD
BHP-21/40           = CURRENT ADOPTED CORRECT-ORDER LOWER-BOUND RECORD
LI-0.52             = QUARANTINED PREPRINT CLAIM
~~~

ولا توجد مفاضلة عددية بسيطة بين \(17/30\) و\(21/40\): الأولى صيغة تقاربية أقوى نوعيًا في فترة أطول، والثانية حد سفلي أضعف نوعيًا في فترة أقصر.

## 4. الاعتمادات الداخلية

### 4.1 الفصل التاسع

الفصل 9 يثبت داخليًا
\[
\psi(x)\sim x
\]
فقط، ويصرح صراحة بأنه لا يثبت حد خطأ فعالًا. لذلك:

~~~text
CHAPTER-09-QUALITATIVE-PNT = AVAILABLE
CHAPTER-09-EFFECTIVE-ERROR = NOT AVAILABLE
SHORT-INTERVAL-INPUT       = MUST NOT BE ATTRIBUTED TO CHAPTER 09
~~~

### 4.2 الصيغة الصريحة وكثافة الأصفار

لا يعاد إثبات Corollary 1.3 لـGuth--Maynard داخل الفصل. تدخل الصيغة الصريحة وتقديرات الكثافة الجديدة بوصفها CITED-CORE، ويشرح الفصل سلسلة الأدوات من غير ادعاء إعادة بناء البرهان.

### 4.3 الفصول 11--13 و18

- الفصل 11 يشرح المناطق الخالية، لكنه ليس حامل تقدير Guth--Maynard.
- الفصلان 12 و13 لا يحولان نتائج الترديدات أو المتوسطات إلى حكم نقطي في \(x\).
- الفصل 18 يمدنا بلغة المجاميع الأسية فقط، ولا يثبت غربال BHP.

إذن لا توجد حافة اعتماد عائدة من الفصل 19 إلى نتيجة مساوية أو أقوى داخليًا.

## 5. نتائج داخلية مجمدة

### 5.1 هوية فرق فون مانغولت

\[
\Delta_h\psi(x)
=
\psi(x+h)-\psi(x)
=
\sum_{x<n\le x+h}\Lambda(n).
\]

هذه هوية، وإيجابيتها وحدها لا تكفي لوجود أولي بسبب القوى الأولية العليا.

### 5.2 مبدأ نقل حد الخطأ

إذا
\[
\psi(t)=t+O(E(t))
\]
عند \(t=x,x+h\)، فإن
\[
\Delta_h\psi(x)
=
h+O(E(x+h)+E(x)).
\]
هذا استنتاج جبري داخلي، لكنه لا ينتج نطاقًا عدديًا في الفصل إلا من مدخل مقتبس محدد.

### 5.3 القوى الأولية العليا

من ANT-LEM-09-02:
\[
0\le \psi(t)-\vartheta(t)\ll \sqrt t\log t.
\]
لذلك
\[
0\le
\Delta_h\psi(x)-\Delta_h\vartheta(x)
\le
\psi(x+h)-\vartheta(x+h)
\ll
\sqrt{x+h}\log(x+h).
\]
وعندما \(h\ge x^{1/2+\eta}\) لأي \(\eta>0\)، يكون هذا \(o(h)\). يغطي ذلك نطاقي Guth--Maynard وHuxley.

### 5.4 الانتقال من \(\vartheta\) إلى \(\pi\)

لأن \(\log x<\log p\le\log(x+h)\) لكل \(x<p\le x+h\):
\[
\frac{\Delta_h\vartheta(x)}{\log(x+h)}
\le
\Delta_h\pi(x)
\le
\frac{\Delta_h\vartheta(x)}{\log x}.
\]
إذا \(h=o(x)\) و\(\Delta_h\vartheta(x)\sim h\)، فإن
\[
\Delta_h\pi(x)\sim \frac{h}{\log x}.
\]
لا تحتاج هذه الخطوة إلى حد خطأ عالمي جديد ولا إلى جمع جزئي دوري.

### 5.5 من الفترة إلى فجوة أولية

إذا ثبت أن \((x,x+x^\theta]\) تحوي أوليًا لكل \(x\ge x_0\)، فإن بوضع \(x=p_n\):
\[
p_{n+1}-p_n\le p_n^\theta
\]
لجميع \(n\) الكبيرة. العكس يحتاج ضبط اتجاه الفترة ولا يستعمل تلقائيًا.

## 6. قرار نطاق التأليف

- PROVED-HERE: التعريفات، هوية \(\Delta_h\psi\)، مبدأ نقل الخطأ، حد القوى العليا المحلي، حصار \(\Delta_h\pi\)، والانتقال إلى فجوة.
- CITED / EXPLAINED: Ingham وHuxley تاريخيًا، وGuth--Maynard بوصفه السجل التقاربي الحديث.
- CITED ONLY: Baker--Harman--Pintz عند \(0.525\).
- HISTORICAL WITHOUT NUMERICAL CONSTANT: Hoheisel.
- QUARANTINED: ادعاء \(0.52\).
- OPTIONAL SEPARATE SECTION: نتائج تقريبًا كل فترة؛ لا تستخدم لإثبات حكم لكل \(x\).

## 7. ما يزال حاجزًا

المحتوى العلمي والاعتمادات الداخلية مجمدة، لكن المراجعة المستقلة المنفصلة لم تُنفذ بعد. لذلك لا تفتح بوابة التأليف في هذا الالتزام.

## الحكم

~~~text
PRIMARY-SOURCE-AUDIT       = PASS WITH HOHEISEL NUMERICAL CONSTANT WITHHELD
MODERN-FRONTIER-AUDIT      = PASS
INTERNAL-DEPENDENCY-AUDIT  = PASS
CIRCULARITY-AUDIT          = PASS
INDEPENDENT-REVIEW         = PENDING
PASS-FOR-AUTHORING         = NO
AUTHORING                  = BLOCKED
~~~
