# تدقيق ما بعد التأليف — الفصل الخامس عشر

التاريخ: 2026-07-24

## الحكم الأصلي

```text
POST-AUTHORING-AUDIT       = FAIL
REFERENCE-AUDIT            = FAIL
CHAPTER-15                  = NOT-READY-FOR-REVIEWED
PR-28                       = DRAFT / OPEN / UNMERGED
```

## أسباب الفشل

1. برهان الحد العلوي المنتهي كان صحيح النتيجة لكنه مختصرًا أكثر من اللازم؛ لم يعرض تحويل موبيوس والمتغيرات المحولة وصيغة معاملات سيلبرغ المثلى.
2. تقدير مقام سيلبرغ استخدم عبارة غامضة عن فروض البعد بدل شرط انتظام كمي صريح.
3. صياغة اللمّة الأساسية خلطت بينها وبين صيغ الغربال الخطي ذات الدالتين \(F_\kappa,f_\kappa\).
4. تطبيق الأزواج لم يصرح بأن المجال \(z\le x^{1/4}\) اختيار متحفظ، ولم يعالج القيم الصغيرة بحد تافه صريح.
5. استدعاءات `\citedresult` الثلاثة جاءت بلا وسيط، فكانت LaTeX تلتقط الحرف التالي بوصفه مرجعًا وتفسد أول كلمة بعد الشارة.

## الدفعة التصحيحية الأولى

نُفذت على الفرع عند الالتزام:

```text
b9d9f0ca8362dcb5f4baa4a8f7404fc5e1da823f
```

وشملت:

- إدراج التقطير الكامل للصورة التربيعية وعكس موبيوس.
- إثبات \(Q_{\min}=1/G(R,z)\) وكتابة معاملات سيلبرغ المثلى صراحة.
- بيان أن عدد الأزواج ذات المضاعف المشترك \(d\) يساوي \(3^{\omega(d)}\) بالضبط.
- إدراج شرط انتظام كمي من نوع \(\Omega_1\).
- إعادة صياغة اللمّة الأساسية بصورة أحادية، مع دالة خطأ \(\rho_{\kappa,A_1}(s)\to0\)، دون استعمال \(F_\kappa,f_\kappa\).
- إصلاح استدعاءات `\citedresult` الثلاثة بوسائط فعلية.
- توضيح أن \(x^{1/4}\) مجال تعليمي آمن غير أمثل.
- إضافة معالجة صريحة للقيم الصغيرة بواسطة \(S_h(x,z)\le x\).

## ما لم يُغلق بعد

```text
REFERENCE-TEXT-VERIFICATION = OPEN
EXACT-PAGE-CITATIONS        = OPEN
INDEPENDENT-RECHECK         = OPEN
PDF-VISUAL-REVIEW           = OPEN
```

الاستشهاد المؤقت الحالي يستخدم `IwaniecKowalski2004` لمنع خلل العرض. لا يُعد هذا وحده تدقيقًا مرجعيًا مكتملًا. يجب إضافة ومطابقة المصادر المتخصصة التالية قبل `REFERENCE-AUDIT = PASS`:

- Halberstam--Richert لتقدير مقام سيلبرغ.
- Diamond--Halberstam--Galway أو Opera de Cribro للّمة الأساسية.
- Opera de Cribro لعائق التكافؤ.
- Cojocaru--Murty أو مصدر عام مكافئ لعرض غربال سيلبرغ المنتهي.

## الحالة بعد التصحيح

```text
POST-AUTHORING-AUDIT       = CORRECTIONS-APPLIED / RECHECK-PENDING
REFERENCE-AUDIT            = FAIL / TEXT-VERIFICATION-OPEN
MATHEMATICAL-BLOCKERS      = 0 / AFTER-FIRST-CORRECTION
REFERENCE-BLOCKERS         = 1
TEXTUAL-BLOCKERS           = 0
CHAPTER-15                  = AUTHORED-DRAFT
REVIEWED                    = NO
RELEASE-READY               = NO
```
